# Project Instructions for AI Agents

This repository distributes the `cmmc-advisor` Claude Code skill. It ships a full SKILL.md plus a `references/` knowledge base, and carries its own eval runner under `evals/` so the skill's answer quality is measurable against curated scenarios and a rubric.

## Scope

Do not treat this repo as a general code project. It is a content-first artifact:

- `SKILL.md` defines the advisor persona, routing table, and anti-patterns.
- `references/` holds every factual claim the skill cites, organized by CMMC domain, level, assessment process, SSP/POA&M guidance, Rev 3 transition notes, and modern IT mapping.
- `evals/` tests the skill's answers against real CMMC scenarios.
- `SOURCES.md` lists the public DoD and NIST sources behind every factual claim. Any new factual assertion must cite a source in `SOURCES.md` before it lands.

## Philosophy

From `README.md`: this skill is an enabler, not a gatekeeper. When a compliant path exists, map it clearly. When no compliant option exists today, identify the gap honestly, describe who is working on closing it, estimate when options may become available, and suggest interim measures.

Every change must preserve that posture. Answers that block, hedge, or refuse without offering a path forward are failures regardless of factual accuracy.

## Evals

The eval runner at `evals/runner/` invokes Claude as the subject (using the skill), captures the answer, runs a deterministic precheck for required CMMC vocabulary and voice discipline, then scores the answer against a rubric via a second Claude call.

Usage (run from repo root):
```bash
pip install -r evals/runner/requirements.txt
python -m evals.runner.runner evals/scenarios/level-2-scoping-basic.yaml
```

Add scenarios under `evals/scenarios/` as YAML. Add rubrics under `evals/rubrics/` as Markdown. The format is intentionally small so contributors can extend coverage without harness work.

## Source discipline

Every factual claim in the skill (control text, assessment procedures, CMMC level definitions, acronyms, deadlines) must trace to a source in `SOURCES.md`. Interpretive guidance (when to choose which cloud, how to draft an SSP narrative) does not require citation but must not contradict cited sources.

When an AI agent edits any file under `references/` or `SKILL.md`, it must:
1. Verify the factual claim is already in `SOURCES.md` or add the source there.
2. Prefer linking to the authoritative URL over paraphrasing memory.
3. Flag any claim it cannot source rather than guessing.

## Voice

Same voice discipline as the wider Igris-family content: no em dashes, no slop words (delve, utilize, tapestry, paradigm, leverage as verb, etc.), no hedging filler ("It's worth noting", "Importantly"), no teacher voice ("Let me explain"). The skill speaks practitioner-to-practitioner to compliance officers, security engineers, and contracting officers.

## When to use which agent

- Content work on `SKILL.md` or `references/`: edit directly; run the eval runner to confirm no regression on existing scenarios.
- New domain practice files (there are 14 domains, only 5 have files so far): author one domain at a time, add at least one eval scenario per new domain.
- Eval runner changes: small repo, direct edits are fine; tests are the scenario runs themselves.

## What this repo does NOT carry

- No hooks, no agents dir, no settings.json, no soul.md. This is a skill distribution, not a Claude Code harness host. Harness-level governance (hooks, agents, settings) lives in the author's separate Claude Code harness repo and is out of scope here.
