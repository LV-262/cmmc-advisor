"""Deterministic checks on a cmmc-advisor response before the evaluator scores it.

Precheck finds the cheap stuff: required CMMC vocabulary presence, voice
anti-tells (em dashes, slop words, teacher voice), citation shape when the
scenario declares factual_claims_expected. The evaluator uses these findings
as evidence for Category A (Accuracy) and Category E (Voice Discipline),
but precheck is NOT a hard constraint; the evaluator makes its own call.
"""

from __future__ import annotations

import re

EMDASH_RE = re.compile(r"\u2014|(?<=\w)--(?=\w)")

SLOP_WORDS = [
    "delve", "utilize", "tapestry", "landscape", "testament",
    "paradigm", "synergy", "multifaceted", "holistic", "myriad",
    "plethora", "realm", "foster", "showcase", "underscore",
    "leverage", "navigate",
]
SLOP_RE = re.compile(r"\b(" + "|".join(SLOP_WORDS) + r")\b", re.IGNORECASE)

HEDGE_PHRASES = [
    "it's worth noting", "it is worth noting",
    "importantly,", "notably,",
    "it bears mentioning", "it should be mentioned",
]
TEACHER_PHRASES = [
    "let's break this down", "let me break this down",
    "here's the kicker", "let me explain", "let me walk you through",
]

CITATION_MARKERS = [
    r"\bhttps?://",
    r"\bNIST SP\s?800-\d+",
    r"\bDFARS\s?252\.",
    r"\bCFR\s?\d+",
    r"\b32 CFR Part 170\b",
    r"\bCMMC (?:2\.0|Rev \d+)\b",
    r"\bper the (?:rule|final rule|DFARS)",
]
CITATION_RE = re.compile("|".join(CITATION_MARKERS), re.IGNORECASE)


def _strip_code_fences(text: str) -> str:
    lines = text.split("\n")
    out = []
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        out.append(line)
    return "\n".join(out)


def run_precheck(response: str, scenario: dict) -> dict:
    prose = _strip_code_fences(response)
    lower = prose.lower()

    em_dashes = len(EMDASH_RE.findall(prose))
    slop_hits = [m.group(0).lower() for m in SLOP_RE.finditer(prose)]
    slop_counts: dict[str, int] = {}
    for w in slop_hits:
        slop_counts[w] = slop_counts.get(w, 0) + 1
    hedges = [p for p in HEDGE_PHRASES if p in lower]
    teacher = [p for p in TEACHER_PHRASES if p in lower]

    required_terms = scenario.get("required_terms", []) or []
    missing_required = [t for t in required_terms if t.lower() not in lower]

    citation_ok = True
    if scenario.get("factual_claims_expected"):
        citation_ok = bool(CITATION_RE.search(prose))

    hard_fail_flags: list[str] = []
    if em_dashes > 0:
        hard_fail_flags.append(f"em_dashes={em_dashes}")
    if slop_counts:
        hard_fail_flags.append(f"slop_words={sorted(slop_counts.keys())}")
    if not citation_ok:
        hard_fail_flags.append("no_citation_for_factual_claims")

    return {
        "em_dashes": em_dashes,
        "slop_words": slop_counts,
        "hedge_phrases": hedges,
        "teacher_phrases": teacher,
        "missing_required_terms": missing_required,
        "citation_ok": citation_ok,
        "hard_fail_flags": hard_fail_flags,
    }
