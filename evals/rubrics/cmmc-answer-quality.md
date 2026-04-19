# CMMC Advisor Answer-Quality Rubric

Scores the cmmc-advisor skill's response to a scenario on five categories. Each category is scored 0, 1, 2, or 3 against the anchors below. Weighted mean must be at least 2.0 to pass. Category A (Accuracy) hard-fails the whole response at score 0 regardless of the other scores.

The evaluator is a second Claude call that receives the scenario, the full subject response, and this rubric.

## Category A: Accuracy (weight 2.0, hard-fail at 0)

Factual correctness on CMMC level requirements, assessment rules, control text, and regulatory citations.

| Score | Anchor |
|-------|--------|
| 3 | All factual claims trace to public CMMC/NIST/DoD sources. Level recommendation is correct for the scenario. Assessment path (self, C3PAO, DIBCAC) is correct. No invented control IDs or misattributed practices. |
| 2 | Level recommendation is correct. Minor factual slips on supporting details (e.g., off-by-one practice count, wrong specific paragraph of DFARS 252.204-7012) but nothing load-bearing. |
| 1 | Level recommendation directionally correct but based on flawed reasoning. Or level correct but assessment-path recommendation wrong. |
| 0 | Level recommendation wrong. Invented controls or assessments. Hallucinated citations. Hard-fail. |

## Category B: CUI Scoping (weight 1.5)

Clarity on what is in scope, what is out of scope, how to define the boundary.

| Score | Anchor |
|-------|--------|
| 3 | Explicit in-scope and out-of-scope call-outs. Enclave model addressed if relevant. Points to SSP boundary documentation as the mechanism. Addresses shared-responsibility split with the CSP. |
| 2 | Scope addressed generally. Misses at least one of: enclave model, shared responsibility, SSP boundary doc. |
| 1 | Only addresses scope at a surface level ("include systems processing CUI"). No actionable boundary guidance. |
| 0 | Scope not addressed or addressed incorrectly (e.g., says corporate email is always in scope when it need not be). |

## Category C: Citation Hygiene (weight 1.0)

Factual claims are traceable. Inference is distinguished from fact.

| Score | Anchor |
|-------|--------|
| 3 | Every factual claim is a link to a public source or an explicit paraphrase with attribution. Interpretive guidance is flagged ("in practice", "my read", "the pattern most C3PAOs accept"). No unsourced dates or deadlines. |
| 2 | Most factual claims are cited or attributed. One or two bare factual assertions without attribution. |
| 1 | Factual claims mixed with interpretation without a clear line. Citations partial. |
| 0 | No citations. Fact and opinion indistinguishable. |

## Category D: Enabler Posture (weight 1.5)

The skill's purpose: say how, not no. When a compliant path exists, map it. When it does not, describe the gap and the state of the art.

| Score | Anchor |
|-------|--------|
| 3 | Every blocker has a path forward. The answer ends with actionable next steps (which vendor to evaluate, what to draft next, who to talk to, rough timeline). If a gap exists, the gap is named and the industry state is described. |
| 2 | Path forward present but not actionable. Ends with generalities ("work with a qualified assessor") rather than specifics. |
| 1 | The answer is informational only. States the rules. Does not recommend next action. |
| 0 | The answer blocks ("you cannot do this"), refuses to help, or recommends the user hire a lawyer before continuing. |

## Category E: Voice Discipline (weight 1.0)

Practitioner register. No slop, no teacher voice, no hedging filler.

| Score | Anchor |
|-------|--------|
| 3 | Zero anti-tells. Practitioner-to-practitioner register throughout. Sentence variety. Parentheticals used for vulnerability or qualification, never for restating. |
| 2 | One or two anti-tells (a stray slop word, one hedging opener, etc.). Register otherwise correct. |
| 1 | Multiple anti-tells. Drifts into teacher voice or bullet-point consulting-speak. |
| 0 | Slop-word-heavy, em-dash-bearing, teacher-voice answer. Fails voice discipline. |

## Weighting and pass threshold

Weighted mean = (A * 2.0 + B * 1.5 + C * 1.0 + D * 1.5 + E * 1.0) / 7.0

Pass threshold: weighted mean >= 2.0 AND Category A > 0.

## Output format

The evaluator returns JSON:

```json
{
  "scenario": "<scenario id>",
  "scores": {
    "A_accuracy": {"score": 0, "rationale": "..."},
    "B_cui_scoping": {"score": 0, "rationale": "..."},
    "C_citation": {"score": 0, "rationale": "..."},
    "D_enabler": {"score": 0, "rationale": "..."},
    "E_voice": {"score": 0, "rationale": "..."}
  },
  "weighted": 0.0,
  "passed": false,
  "hard_fail_flag": null,
  "notes": "optional overall observation"
}
```

Set `hard_fail_flag` to `"category_A_zero"` when A is 0 regardless of the other scores.
