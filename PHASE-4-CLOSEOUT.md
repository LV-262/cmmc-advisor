# Phase 4 Close-Out Review — cmmc-advisor

**Date:** 2026-04-20
**Branch:** `phase-4-closeout-review`
**Reviewer:** Igris (automated corpus audit)
**Scope:** 14 domain practice files at `references/domains/*.md`, 5549 lines total

---

## Verdict

**No-Go at audit time → Go after inline hotfix.** One CRITICAL finding in the SI slice: a factual regulatory error that misstated whether FCI-only contractors carry SI obligations under CMMC. Remediated inline on this branch (commit `245a7c4`); see the Remediation addendum at the bottom of this report. This close-out report intentionally preserves both the audit-time snapshot and the post-hotfix state.

The rest of the corpus is in good shape. Format parity is clean, per-practice structure is uniform, and practice totals sum to 110 across all 14 domains, matching the canonical `levels-and-assessment.md` table. Three MEDIUM findings (scope-boundary leaks in CA and MP, gloss-hygiene drift in MP/PS/SI) and several LOW/informational findings should be filed as follow-ups but do not block.

---

## Check 1 — Domain count and practice totals

Canonical totals from `references/levels-and-assessment.md`: 17 L1 + 93 L2 = 110 practices.

The table below is the **audit-time snapshot before** commit `245a7c4`. Post-hotfix SI counts are 4/3/7 and post-hotfix corpus totals are 17/93/110.

| File | L1 declared | L2 declared | Total declared | Canonical (L1/L2/Total) | Match |
|------|-------------|-------------|----------------|-------------------------|-------|
| ac-access-control | 4 | 18 | 22 | 4/18/22 | ✓ |
| at-awareness-training | 0 | 3 | 3 | 0/3/3 | ✓ |
| au-audit | 0 | 9 | 9 | 0/9/9 | ✓ |
| ca-security-assessment | 0 | 4 | 4 | 0/4/4 | ✓ |
| cm-configuration-mgmt | 0 | 9 | 9 | 0/9/9 | ✓ |
| ia-identification-auth | 2 | 9 | 11 | 2/9/11 | ✓ |
| ir-incident-response | 0 | 3 | 3 | 0/3/3 | ✓ |
| ma-maintenance | 0 | 6 | 6 | 0/6/6 | ✓ |
| mp-media-protection | 1 | 8 | 9 | 1/8/9 | ✓ |
| pe-physical-protection | 4 | 2 | 6 | 4/2/6 | ✓ |
| ps-personnel-security | 0 | 2 | 2 | 0/2/2 | ✓ |
| ra-risk-assessment | 0 | 3 | 3 | 0/3/3 | ✓ |
| sc-system-comms | 2 | 14 | 16 | 2/14/16 | ✓ |
| **si-system-information-integrity** | **0** | **7** | **7** | **4/3/7** | **✗** |
| **Totals** | **13** | **93** | **106** | **17/93/110** | ✗ (4 L1 missing) |

**CRITICAL at audit time — SI Domain Summary count.** SI declared 0 L1 + 7 L2 + 7 total. Canonical is 4 L1 + 3 L2 + 7 total. The total was right; the split was wrong. This cascaded from the labeling error below.

---

## Check 2 — Reciprocal citation matrix

Forward citations by source file (practice-ID references to other domains):

| Source | AC | AT | AU | CA | CM | IA | IR | MA | MP | PE | PS | RA | SC | SI |
|--------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| AC     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| AT     |    |    |    |    |    |    | 9  |    |    | 5  | 8  |    |    |    |
| AU     |    |    |    |    |    | 1  |    |    |    |    |    |    |    |    |
| CA     |    |    |    |    |    |    |    |    |    |    |    | 2  | 5  | 8  |
| CM     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| IA     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| IR     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| MA     |    |    |    |    |    | 3  |    |    | 1  | 1  | 4  |    |    | 3  |
| MP     |    |    |    |    |    |    | 1  | 6  |    | 3  | 1  |    | 1  |    |
| PE     |    |    |    |    |    |    |    |    |    |    | 2  |    |    |    |
| PS     |    |    |    |    |    |    | 1  |    |    | 7  |    |    |    |    |
| RA     |    |    |    | 4  |    |    |    |    |    |    | 4  |    |    | 4  |
| SC     |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| SI     | 2  |    | 5  | 3  | 3  |    | 2  | 4  |    |    |    | 2  | 1  |    |

**Structural observation (HIGH, informational).** Five files carry zero outbound practice-ID citations: AC, CM, IA, IR, SC. These are the earliest Phase 4 slices (PR #2 in the commit log: "feat: add top 5 domain practice files (AC, IA, AU, CM, SC)") plus IR (PR #3). Practice-level coordination pointers were adopted only in later slices (CA, SI, MA, MP, PE, PS, RA, AT). These older files still carry prose-level "Key relationships" sections but do not cite specific practice IDs.

Most asymmetries trace to this gap:
- SI → AC (2), AU (5), CM (3), IR (2), SC (1): none reciprocate because those domains predate the pattern
- CA → SC (5): SC has no outbound citations
- MA → IA (3), PE (1), PS (4): asymmetric; PE cites PS but not MA
- RA → PS (4): asymmetric; PS cites PE and IR but not RA
- AT → IR (9), PE (5), PS (8): one-way by design (AT is a consumer of cross-domain inputs for training content) — legitimate asymmetry per the prompt's caveat

**Symmetric pairs (working as intended):** CA↔RA, CA↔SI, RA↔SI, MA↔MP, MA↔SI, PE↔PS.

**Recommendation for Phase 5 or a hotfix slice:** backfill practice-ID coordination into AC, CM, IA, IR, SC. Not a Phase 4 blocker.

---

## Check 3 — Scope-boundary leak scan

Rule: each of the listed phrases should appear 0 or 1 times per domain file (pointer only). 2+ occurrences means substantive content has leaked in from a dedicated references file.

| File | Phrase | Count | Verdict |
|------|--------|-------|---------|
| ca-security-assessment | Conditional Certification | 4 | **MEDIUM leak.** 2 are substantive content expansion (lines 136, 147); 2 are pointers. Belongs in `references/poam-management.md`. |
| ca-security-assessment | ISCM strategy | 2 | LOW. Both occurrences are inside Evidence-to-collect bullet lists, not scope expansion. Accept. |
| mp-media-protection | CUI Registry | 4 | **MEDIUM leak.** Dissemination controls content (FEDCON/NOCON/RELTO) duplicates `references/scoping-and-cui.md`. Belongs there; MP should point. |

All other phrases scanned ("180 days", "NIST SP 800-137", "32 CFR Part 170", "FAR 52.204-21") produced 0 or 1 hits per file — clean.

---

## Check 4 — 800-171A vocabulary audit

Full corpus-wide grep across 14 files:

| Check | Finding |
|-------|---------|
| `PARTIALLY MET` (banned) | **0 hits.** Clean. |
| `largely implemented` | 0 |
| `mostly compliant` | 0 |
| `substantially implemented` | 0 |
| `\bIOC\b` standalone | 0 |
| `SCAP [0-9]+\.` versioned | 0 |

Clean. The SI gate rule landing was retroactively safe — the ex-ante regrep of the other 13 files surfaces no drift.

---

## Check 5 — Rule 2 retrospective spot-check

**Method:** 42 practices sampled (3 per file; PS family exhausted at 2 practices, 4th AC practice added to reach 42). Each `**Requirement:**` line WebFetched against `csf.tools/reference/nist-sp-800-171/r2/3-X-Y/` canonical page and diffed. HIGH for semantic change, MEDIUM for scope drift, LOW stylistic skipped.

**Results:** 37 clean, 4 MEDIUM, 1 HIGH.

### HIGH findings

**AU.L2-3.3.5 — HIGH (semantic narrowing).**
- File: "Correlate audit record review, analysis, and reporting processes to support after-the-fact investigations of incidents."
- Canonical: "Correlate audit record review, analysis, and reporting processes for investigation and response to indications of unlawful, unauthorized, suspicious, or unusual activity."
- Deltas:
  - Drops "and response" — narrows investigate+respond to investigate only.
  - Replaces "indications of unlawful, unauthorized, suspicious, or unusual activity" with "incidents" — narrows the trigger surface from pre-incident indications to post-incident only.
  - Adds "after-the-fact," which is not in canonical and contradicts the pre-incident indications language.
- Impact: a contractor following the paraphrase would under-implement audit correlation (skip pre-incident indication work expected by the canonical).

### MEDIUM findings

**AC.L1-3.1.20 — MEDIUM (Rev 1/Rev 2 language drift).**
- File: "Verify and control/limit connections to and use of external information systems."
- Canonical: "Verify and control/limit connections to and use of external systems."
- Delta: inserts "information" before "systems." Rev 1 phrasing on a Rev 2 practice.

**IA.L1-3.5.1 — MEDIUM (Rev 1/Rev 2 language drift).**
- File: "Identify information system users, processes acting on behalf of users, or devices."
- Canonical: "Identify system users, processes acting on behalf of users, or devices."
- Delta: inserts "information" before "system users." Same class as AC.L1-3.1.20 and the already-known PE "organizational information systems" finding.

**IR.L2-3.6.2 — MEDIUM (scope drift + added clause).**
- File: "Track and document incidents and report them to designated internal officials and external authorities per contractual and regulatory obligations."
- Canonical: "Track, document, and report incidents to designated officials and/or authorities both internal and external to the organization."
- Deltas: maps "officials" to internal-only and "authorities" to external-only (canonical allows either to be either); adds "per contractual and regulatory obligations" not in canonical.

**IR.L2-3.6.3 — MEDIUM (800-53 language in 800-171 slot).**
- File: "Test the organizational incident response capability using appropriate tests and exercises, and use the results to improve the capability."
- Canonical: "Test the organizational incident response capability."
- Delta: adds 800-53 IR-3 language (assessment-objective text) to the 800-171 Rev 2 requirement line. If the skill convention is "800-171 text in requirement, 800-53A in assessment objectives elsewhere," this is drift; inconsistent with the other IR practices that use 171 text.

### Pattern observations

1. **Rev 1/Rev 2 "information system" drift is a family bug — corpus-wide scan complete.** Two of the four Rule 2 MEDIUMs (AC.L1-3.1.20, IA.L1-3.5.1) are the same class as the already-flagged PE case. The follow-up corpus-wide grep over all `**Requirement:**` blocks surfaces 5 total drift instances across 2 files (AC: 3.1.20, 3.1.21, 3.1.22; IA: 3.5.1, 3.5.2). PE is clean on this pattern. The IR `information system` match is DFARS 252.204-7012 defined terminology ("covered contractor information system"), not drift. One scoped follow-up slice can fix all 5 in one pass.

2. **IR practices carry added-clause drift.** Both sampled IR requirement lines extend canonical with external material. The underlying rule (Rule 2) did not exist when IR was drafted (Phase 4c), so this is pre-rule drift. File as follow-ups, not reverts.

3. **Slices drafted after Rule 2 landed are clean.** SI, CA, MP, MA, PS, RA, AT, and the later PE pass are 100% clean on their sampled requirements. The Rule 2 gate works; earlier slices need backfill.

### Files with Rule 2 findings

- `references/domains/ac-access-control.md` (1 MEDIUM)
- `references/domains/au-audit.md` (1 HIGH)
- `references/domains/ia-identification-auth.md` (1 MEDIUM)
- `references/domains/ir-incident-response.md` (2 MEDIUM)

---

## Check 6 — Format parity

Required per file: H1 with code, `> Source` line, `## Overview`, `## Level 2 Practices`, `## Domain Summary`.
Required per practice: `**Requirement:**`, `**Why it matters:**`, `**Implementation guidance:**`, `**Evidence to collect:**`, `**Common mistakes:**`.

All 14 files carry all 5 required sections. Per-practice block counts match practice counts exactly across every file:

| File | Practices | Req | Why | Impl | Evidence | Mistakes |
|------|-----------|-----|-----|------|----------|----------|
| AC | 22 | 22 | 22 | 22 | 22 | 22 |
| AT | 3 | 3 | 3 | 3 | 3 | 3 |
| AU | 9 | 9 | 9 | 9 | 9 | 9 |
| CA | 4 | 4 | 4 | 4 | 4 | 4 |
| CM | 9 | 9 | 9 | 9 | 9 | 9 |
| IA | 11 | 11 | 11 | 11 | 11 | 11 |
| IR | 3 | 3 | 3 | 3 | 3 | 3 |
| MA | 6 | 6 | 6 | 6 | 6 | 6 |
| MP | 9 | 9 | 9 | 9 | 9 | 9 |
| PE | 6 | 6 | 6 | 6 | 6 | 6 |
| PS | 2 | 2 | 2 | 2 | 2 | 2 |
| RA | 3 | 3 | 3 | 3 | 3 | 3 |
| SC | 16 | 16 | 16 | 16 | 16 | 16 |
| SI | 7 | 7 | 7 | 7 | 7 | 7 |

Density spread (line count): AC 668, SC 553, MP 494, SI 493, PE 379, MA 373, IA 364, IR 361, AU 322, RA 302, CA 405, CM 323, AT 285, PS 227. AC and SC are the pre-density-discipline files; note as "pre-rule drift, accepted" per the prompt.

---

## Check 7 — First-use gloss hygiene (Rule 1)

Scan: open paren immediately after an uppercase acronym with no closing paren on the same line (proximity-grep failure mode).

True gloss violations (acronym expansion crosses a hard-wrap break):

| File | Line | Acronym | Defect |
|------|------|---------|--------|
| mp-media-protection | 203 | FEDCON | `FEDCON (Federal\n  Government and contractors only)` |
| ps-personnel-security | 63 | NBIS | `NBIS\n  (National Background Investigation Services, ...)` |
| ps-personnel-security | 64 | DISS | `DISS\n  (Defense Information System for Security)` |
| si-system-information-integrity | 10 | FCI | `FCI (Federal Contract\n  Information)` |

Non-gloss list continuations (false positives, accepted): `(Azure AD, Okta, Google Workspace` style line-wraps where the parenthetical is an inline list, not an acronym expansion. 20+ such false positives across the corpus; not flagged as findings.

---

## CRITICAL finding detail — SI mislabeling and factual error

**File:** `references/domains/si-system-information-integrity.md`
**Severity:** CRITICAL (regulatory misstatement)

### What is wrong

1. **Practice labels wrong on 4 of 7 practices.** File uses `SI.L2-3.14.1`, `SI.L2-3.14.2`, `SI.L2-3.14.4`, `SI.L2-3.14.5` (21 times combined in headings and prose). Canonical CMMC labels are `SI.L1-` because these 4 practices come from FAR 52.204-21 basic safeguarding.

2. **Domain Summary count wrong.** File shows `| Count | 0 | 7 | 7 |`. Canonical per `levels-and-assessment.md` is `| SI | 4 | 3 | 7 |`.

3. **Overview prose makes a factually incorrect regulatory claim.** Lines 9–11 read:

   > "The domain has 7 practices, all at Level 2. No Level 1 SI practices exist, so contractors handling only FCI (Federal Contract Information) have no SI obligation under CMMC."

   This is **false**. FCI-only contractors subject to FAR 52.204-21 DO carry SI obligations — specifically the 4 L1 SI practices. A contractor reading the advisor and acting on this claim could skip flaw-remediation, malicious-code protection, malicious-code currency, and periodic scanning controls that FAR already requires them to perform.

### Root cause

The author conflated two orthogonal classifications:

- **NIST SP 800-171 Rev 2 Basic vs Derived.** Lines 12–13: "3 Basic Security Requirements (SI.L2-3.14.1–3.14.3) plus 4 Derived Security Requirements (SI.L2-3.14.4–3.14.7)." This split is correct: 3 Basic + 4 Derived.
- **CMMC L1 vs L2.** A different split: 4 L1 (3.14.1, 3.14.2, 3.14.4, 3.14.5) + 3 L2 (3.14.3, 3.14.6, 3.14.7).

The file carries the correct 800-171 Basic/Derived labels in the taxonomy sentence but then uses `SI.L2-` prefixes throughout, which are wrong under the CMMC L1/L2 classification. The Overview sentence "No Level 1 SI practices exist" reads as a direct corollary of the mislabeling.

### Why upstream gates did not catch this

- Planner and quartet do not load canonical CMMC L1/L2 mappings.
- Rule 2 (primary-source verification) was codified for the SI slice but checks requirement paraphrase text against csf.tools, not the CMMC level assignment. The csf.tools page is 800-171-centric; CMMC level classification lives in CMMC Assessment Guide Level 1 and Level 2, not on csf.tools per practice.
- Format-parity check passed because it verifies structural sections, not label-to-canonical mapping.

### Remediation

One file, targeted changes:

1. Change `### SI.L2-3.14.1` → `### SI.L1-3.14.1` (and .2, .4, .5) in all 4 practice headings (8 locations across headings + cross-references).
2. Update all prose references to `SI.L2-3.14.1`, `SI.L2-3.14.2`, `SI.L2-3.14.4`, `SI.L2-3.14.5` to `SI.L1-`. Grep shows 21 such references across the file.
3. Fix Domain Summary row to `| Count | 4 | 3 | 7 |`.
4. Rewrite Overview lines 8–13 to state correctly:
   - 7 total practices: 4 at L1 (FAR 52.204-21 basic safeguarding), 3 at L2.
   - FCI-only contractors under FAR 52.204-21 carry obligations for the 4 L1 SI practices.
   - 800-171 Rev 2 Basic/Derived split is a separate classification from CMMC L1/L2 and does not map 1:1.
5. Audit all other files for any inbound citations to SI practice IDs and correct them (RA cites SI 4 times, SI cites CA/CM/AC/AU/IR/MA/SC/RA — most SI self-references are in prose about relationships which reference the correct semantic practice regardless of label).
6. Update cross-references in `references/levels-and-assessment.md` if any exist (none found in scan, but verify before merge).

### Recommendation

Hotfix on this branch as a standalone commit before the close-out report PR, per the prompt's "1-line regulatory-citation fix" provision — though this one is larger than 1 line. Alternative: separate hotfix PR targeting main, then re-run close-out on the corrected corpus. I defer the choice to the commander.

### Process learning

Add to the SI/practice-file gate (and to `rules/common/content-skill-authoring.md` as Rule 5 candidate): **"Verify CMMC level classification against `levels-and-assessment.md` canonical table before drafting practice labels, not only after."** The L1/L2 split is a CMMC-specific overlay on top of NIST 800-171 numbering and is easy to conflate with the 800-171 Basic/Derived split.

---

## HIGH/MEDIUM findings summary (for bd follow-ups)

| ID seed | Severity | File | Finding |
|---------|----------|------|---------|
| F-1 | CRITICAL | si-system-information-integrity.md | Mislabels 4 L1 practices as L2; incorrect FCI regulatory claim in Overview |
| F-2 | HIGH | ac/cm/ia/ir/sc *.md | No practice-ID cross-citations — structural inconsistency with later Phase 4 files |
| F-3 | MEDIUM | ca-security-assessment.md | Conditional Certification content (lines 136, 147) duplicates poam-management.md |
| F-4 | MEDIUM | mp-media-protection.md | CUI Registry dissemination-controls content duplicates scoping-and-cui.md |
| F-5 | LOW | mp-media-protection.md:203 | FEDCON gloss splits across hard-wrap (Rule 1) |
| F-6 | LOW | ps-personnel-security.md:63 | NBIS gloss splits across hard-wrap (Rule 1) |
| F-7 | LOW | ps-personnel-security.md:64 | DISS gloss splits across hard-wrap (Rule 1) |
| F-8 | LOW | si-system-information-integrity.md:10 | FCI gloss splits across hard-wrap (Rule 1) — subsumed by F-1 remediation |
| F-9 | HIGH | au-audit.md (AU.L2-3.3.5) | Requirement paraphrase narrows canonical scope — drops "response," drops "indications of unlawful/unauthorized/suspicious/unusual," adds "after-the-fact" |
| F-10 | MEDIUM | ac-access-control.md | Rev 1 "information system(s)" language on Rev 2 practices: AC.L1-3.1.20, AC.L1-3.1.22, AC.L2-3.1.21 |
| F-11 | MEDIUM | ia-identification-auth.md | Rev 1 "information system(s)" language on Rev 2 practices: IA.L1-3.5.1, IA.L1-3.5.2 |
| F-12 | MEDIUM | ir-incident-response.md (IR.L2-3.6.2) | Requirement paraphrase maps officials/authorities to internal/external 1:1; adds contractual-obligations clause not in canonical |
| F-13 | MEDIUM | ir-incident-response.md (IR.L2-3.6.3) | Requirement paraphrase incorporates 800-53 IR-3 language into the 800-171 slot |
| F-14 | — | — | Absorbed into F-10/F-11; corpus-wide scan already complete (5 drift instances across AC + IA) |

---

## Phase 5 scoping

Per the prompt, a bd issue will be created for the Phase 5 scoping session (FedRAMP gap + modern-it/endpoints content), dependent on the close-out PR landing. No Phase 5 work in this session.

---

## Pre-rule drift (accepted, not findings)

- AC 668 lines with 22 practices; SC 553 lines with 16 practices. Both pre-date the density-discipline rule codified in later slices. Accepted as-is.
- AC, CM, IA, IR, SC carry zero practice-ID coordination pointers. Filed as F-2 for follow-up but not a Phase 4 blocker; the pattern emerged mid-Phase 4 and retrofitting is a scoped Phase 5 slice.

---

## Remediation addendum — SI CRITICAL resolved inline

Commit `245a7c4` on this branch resolves F-1 (the SI CRITICAL). Changes:

- 4 practice headings relabeled `SI.L2-3.14.x` → `SI.L1-3.14.x` for 3.14.1, 3.14.2, 3.14.4, 3.14.5
- File restructured into `## Level 1 Practices` and `## Level 2 Practices` sections, following PE/MP/AC/IA/SC convention. `SI.L2-3.14.3` moved from between .2 and .4 into the L2 section (numerical order preserved within each level)
- Domain Summary count row fixed: `0/7/7` → `4/3/7` (matches canonical `levels-and-assessment.md`)
- Overview prose rewritten to remove the false FCI claim and call out the NIST 800-171 Basic/Derived vs CMMC L1/L2 distinction explicitly
- All intra-file prose references updated to correct labels (21 occurrences)
- Inbound references updated: `ca-security-assessment.md` (5 refs), `ma-maintenance.md` (3 refs), `ra-risk-assessment.md` (4 refs)
- FCI split-line gloss (F-8) resolved implicitly by the Overview rewrite

Post-hotfix verification:
- Zero `SI.L2-3.14.[1245]` remaining anywhere in `references/`
- Format parity clean: all required sections present, 7 practices matched by 7 of each block type
- 59 total SI cross-references across the corpus, all correctly labeled

### Side-discovery during hotfix

AC, IA, and SC section headers use `## Level 1 Practices (Basic)` and `## Level 2 Practices (Derived)`. This conflates CMMC L1/L2 with NIST 800-171 Basic/Derived — the same conflation that broke SI, with inverted effect. In AC, the "Level 1 Practices (Basic)" heading labels 4 practices that span both Basic (3.1.1, 3.1.2) and Derived (3.1.20, 3.1.22) Security Requirements. The per-practice identifiers are correct; the section label prose is misleading. Filed as a separate MEDIUM bd issue, not included in this hotfix to keep scope minimal. PE, MP, SI (post-hotfix) use the unambiguous `## Level 1 Practices` / `## Level 2 Practices` style and are the convention to standardize on.

### Verdict flip

With commit `245a7c4` on the branch, Phase 4 clears the CRITICAL blocker. Residual findings (HIGH AU.L2-3.3.5 paraphrase, MEDIUM scope/drift/header issues, LOW gloss hygiene) are filed as bd follow-ups and do not block Phase 5 scoping. Phase 4 is **Go** on this branch as of the hotfix commit.
