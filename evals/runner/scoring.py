"""Evaluator-as-judge scoring for cmmc-advisor responses.

Takes the scenario, the subject response, the rubric markdown, and the
precheck findings. Constructs a grader prompt, invokes Claude as the
evaluator, and parses a JSON score object back.

Kept intentionally thin. The rubric itself carries the domain judgment;
this file just orchestrates the evaluator call and parses the result.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from typing import Any

try:
    from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock
    SDK_AVAILABLE = True
except ImportError:
    SDK_AVAILABLE = False


EVALUATOR_MODEL = "claude-sonnet-4-6"


@dataclass(frozen=True)
class ScoreResult:
    scenario_id: str
    scores: dict[str, dict[str, Any]]
    weighted: float
    passed: bool
    hard_fail_flag: str | None
    notes: str
    raw: str


def _build_prompt(scenario: dict, response: str, rubric: str, precheck: dict) -> str:
    return f"""You are a strict but fair evaluator grading a cmmc-advisor skill response.

# RUBRIC

{rubric}

# SCENARIO

id: {scenario.get("id", "(unknown)")}
prompt the subject received:
<<<
{scenario.get("prompt", "")}
>>>

evaluator_notes:
{scenario.get("evaluator_notes", "(none)")}

expected_recommendation:
{scenario.get("expected_recommendation", "(none)")}

# PRECHECK (regex-based, deterministic)

These were pre-computed before you. Use as evidence, not as a hard
constraint. If a finding is a false positive on inspection (e.g., a
slop word inside a quoted example), do not deduct for it.

{json.dumps(precheck, indent=2)}

# SUBJECT RESPONSE

<<<
{response}
>>>

# INSTRUCTIONS

Grade per the rubric. Return JSON matching the rubric's output format
exactly. Include "scenario": "{scenario.get("id", "")}" as a top-level
field. Scores are integers 0-3. Set hard_fail_flag to "category_A_zero"
when Category A scores 0. Respond ONLY with the JSON object, no prose
before or after.
"""


def _extract_json(text: str) -> dict | None:
    stripped = text.strip()
    candidates = []
    depth = 0
    start = -1
    for i, ch in enumerate(stripped):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start >= 0:
                candidates.append(stripped[start : i + 1])
                start = -1
    for c in candidates:
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            continue
    sys.stderr.write(
        f"[scoring] _extract_json: could not parse JSON from "
        f"{len(candidates)} candidate block(s); "
        f"raw first 200 chars: {stripped[:200]!r}\n"
    )
    return None


async def _call_evaluator(prompt: str) -> str:
    if not SDK_AVAILABLE:
        raise RuntimeError(
            "claude-agent-sdk not installed. Run pip install -r requirements.txt"
        )
    options = ClaudeAgentOptions(model=EVALUATOR_MODEL, system_prompt="")
    chunks: list[str] = []
    async for msg in query(prompt=prompt, options=options):
        if isinstance(msg, AssistantMessage):
            for block in msg.content:
                if isinstance(block, TextBlock):
                    chunks.append(block.text)
    return "".join(chunks)


def _compute_weighted(scores: dict[str, dict[str, Any]]) -> float:
    weights = {
        "A_accuracy": 2.0,
        "B_cui_scoping": 1.5,
        "C_citation": 1.0,
        "D_enabler": 1.5,
        "E_voice": 1.0,
    }
    total = sum(weights.values())
    acc = 0.0
    for key, w in weights.items():
        entry = scores.get(key) or {}
        score = entry.get("score")
        if isinstance(score, (int, float)):
            acc += float(score) * w
    return acc / total if total else 0.0


async def score_response(
    scenario: dict,
    response: str,
    rubric_text: str,
    precheck: dict,
) -> ScoreResult:
    prompt = _build_prompt(scenario, response, rubric_text, precheck)
    raw = await _call_evaluator(prompt)
    parsed = _extract_json(raw) or {}
    scores = parsed.get("scores", {})
    hard_fail = parsed.get("hard_fail_flag")
    # Always recompute weighted locally from the parsed category scores.
    # The evaluator is given the rubric and may compute its own, but the
    # rubric formula is canonical and we trust the category scores more
    # than a derived field the model could miscompute.
    weighted = _compute_weighted(scores)
    a_score = (scores.get("A_accuracy") or {}).get("score")
    passed = (
        isinstance(a_score, (int, float))
        and a_score > 0
        and weighted >= 2.0
    )
    return ScoreResult(
        scenario_id=scenario.get("id", ""),
        scores=scores,
        weighted=float(weighted) if isinstance(weighted, (int, float)) else 0.0,
        passed=bool(passed),
        hard_fail_flag=hard_fail,
        notes=parsed.get("notes", ""),
        raw=raw,
    )
