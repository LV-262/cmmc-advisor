# Personnel Security (PS)

> Source: NIST SP 800-171 Rev 2, Section 3.9; CMMC Assessment Guide Level 2

## Overview

Personnel Security gates who gets trusted with CUI and what happens
when that trust ends or shifts. The domain has 2 practices: PS.L2-3.9.1
(screening individuals before authorizing access) and PS.L2-3.9.2
(protecting systems during and after personnel actions such as
transfers and terminations). Both are at Level 2. No Level 1 PS
practices exist, so contractors handling only FCI have no
personnel-security requirement under this domain. PS.L2-3.9.2 is the
locus of separation, transfer, and termination content that other
domains (especially Physical Protection) cross-reference.

Key cross-domain relationships: Access Control (AC) governs how
authorized personnel use systems and revokes logical access when
PS.L2-3.9.2 fires; Identification and Authentication (IA) issues and
revokes credentials on the PS schedule; Physical Protection (PE)
revokes badges under PE.L1-3.10.5, triggered by PS.L2-3.9.2 events;
Awareness and Training (AT) assigns role-based training that keys off
PS screening tier and role; Incident Response (IR) handles
insider-threat cases that reference PS screening baselines and
personnel-action timing; Media Protection (MP) governs CUI media
return during separation as part of the PS.L2-3.9.2 exit workflow. PS
is a hub practice: doing it well makes the other six easier; doing it
poorly produces findings in all of them.

---

## Level 2 Practices

### PS.L2-3.9.1 — Screen Individuals Before Access

**Requirement:** Screen individuals prior to authorizing access to
organizational systems containing CUI.

**Why it matters:** Pre-access screening is the mechanism the contract
recognizes for trusting a person with CUI. Screening completed after
access has already been granted is not screening, it is notification.

**Implementation guidance:**
- Screening scope is the set of roles with CUI access, not the full
  employee population. Screening everyone equally wastes budget on
  low-risk staff and under-screens the high-risk ones
- Screening depth is risk-matched: criminal history check and
  employment verification as a baseline, education verification for
  technical roles claiming specialized credentials, credit history
  check for roles with financial or fraud exposure, reference checks
  for senior or high-access roles
- For contracts that require federal investigations, the typical
  pattern is the Tier 1 investigation (which replaced the NACI,
  National Agency Check with Inquiries, under the 2012 Federal
  Investigative Standards). Higher-risk public-trust CUI roles may
  require MBI (Moderate Background Investigation), which is the
  Tier 2 investigation under the 2012 FIS. Tier 3 and above are
  generally national-security or otherwise higher-sensitivity
  investigations and are out of scope for most CUI-only roles;
  include Tier 3 only when the contract explicitly requires that
  higher investigation level. Investigation submissions today route
  through NBIS (National Background Investigation Services,
  which replaced e-QIP around 2023) and are tracked in
  DISS (Defense Information System for Security)
- Clearance mechanics are out of scope for Level 2 CUI work; the
  investigation tier references are included here only because
  contracts sometimes require them for CUI-handling roles even without
  a classified component
- Periodic reinvestigation cadence where contracts require it
  (commonly 5 to 10 years depending on tier). Screening valid at hire
  does not stay valid forever
- Contractor and subcontractor screening flow-down is prime-contract
  driven. Primes pass the screening requirement down through subcontract
  clauses; subs who claim screening compliance must be able to
  demonstrate it
- Pre-access evidence timing matters. Screening complete and documented
  before access authorization, before first login, and before entry
  on duty (EOD). Access granted first with screening results returned
  later
  fails the practice as written

**Evidence to collect:**
- Screening policy defining scope, depth, and cadence by role category
- Sample background check results (redacted) correlated to personnel
  records
- Completion records for NACI, Tier 1, MBI, or Tier 3 investigations
  where contracts require them
- NBIS submission confirmations and DISS tracking records for
  federal-investigation subjects
- Onboarding checklist showing the screening-complete gate preceding
  access authorization
- Subcontract agreements with screening flow-down clauses and evidence
  that subs execute the requirement

**Common mistakes:**
- Screening all employees at the same depth regardless of role risk
- Post-hoc screening: access granted day one, results returned week
  four; the practice assesses pre-access timing
- Contract investigation requirements ignored until an assessor asks
- Subcontractor screening assumed but never verified by the prime
- Periodic reinvestigation cadence lapsed; long-tenured staff still
  operating on a ten-year-old background check
- Credit checks absent for financial or fraud-exposed roles where the
  risk analysis would have called for them

---

### PS.L2-3.9.2 — Protect CUI During Personnel Actions

**Requirement:** Ensure that organizational systems containing CUI are
protected during and after personnel actions such as terminations and
transfers.

**Why it matters:** Separation and transfer are the two highest-risk
transitions in the personnel lifecycle. PE.L1-3.10.5 badge revocation
timing depends on this practice firing correctly; without it, former
employees retain logical access, physical access, or both for days
after they should have been cut off.

**Implementation guidance:**
- Separation workflow: HR initiates a personnel action ticket that
  triggers parallel revocation actions. Access Control disables logical
  accounts, Physical Protection (PE.L1-3.10.5) deactivates badges
  within the defined SLA (same-day for hostile terminations, one
  business day for routine separations). Media Protection handles
  credential and CUI artifact return: issued laptops, tokens, hardcopy
  CUI documents, personal devices containing any CUI residue. Exit
  interview includes a security briefing covering the departing
  employee's ongoing CUI confidentiality obligations after employment
  ends
- Transfer workflow: role change triggers re-authorization, not access
  retention. Need-to-know decisions made for the previous role do not
  automatically apply to the new role. Access review against the new
  role's need-to-know. Awareness and Training re-assignment when the
  new role requires different role-based training. Badge re-encoding
  when the new role requires different facility access. A transfer is
  a fresh authorization event, not a shortcut around one
- Termination timing: same-day revocation for hostile terminations,
  with access cut off before the termination meeting begins and the
  employee escorted off the premises with badge already deactivated.
  Within-SLA (typically one business day) for routine separations.
  The SLA is documented in policy and verifiable from HR-to-security
  timing records
- Staged revocation is a risk-based deviation from immediate
  revocation. For example, retain email access for 30 days for
  knowledge handoff while revoking CUI-system access immediately.
  Staging must be explicit, approved at the right authority level,
  time-bound, and documented. A "temporary" retention with no
  expiration date is a finding waiting to happen
- CUI debrief for long-tenured or high-access personnel on departure.
  The debrief covers ongoing obligations under the contract,
  non-disclosure terms that survive employment, specific CUI artifacts
  to return, and how to report any future unauthorized disclosures
- HR-to-security audit trail: every personnel action generates a
  traceable record linking the HR system ticket (termination,
  transfer, role change) to the specific revocation actions executed
  in access control, badge, and credential systems. Assessors look for
  end-to-end traceability; gaps suggest revocations were missed

**Evidence to collect:**
- Personnel action workflow documentation covering separation,
  transfer, and termination paths
- Sample separation records showing HR trigger timestamp and
  downstream revocation timestamps in AC and PE.L1-3.10.5 systems
- Exit interview records with security briefing attestation signed by
  the departing employee
- Transfer records showing access review against the new role and
  explicit re-authorization decisions
- CUI debrief records for long-tenured or high-access departures
- HR-to-security audit trail samples demonstrating end-to-end
  traceability from personnel action to access revocation

**Common mistakes:**
- Access Control account left active past termination date; the IT
  tickets existed but no one closed them on schedule
- Badge revocation delayed past the same-day SLA; the same miss shows
  up as a PE.L1-3.10.5 finding because the two practices share the
  same failure mode
- Transfer treated as "same person, more access" rather than "same
  person, new role, fresh authorization required"
- No exit interview security briefing; departing employee leaves with
  unclear understanding of ongoing confidentiality obligations
- Staged revocation applied without approval or time-bound expiration;
  the "temporary" arrangement quietly becomes permanent
- HR system and access control systems not linked; audit trail
  requires manual reconstruction after the fact and has gaps
- Hostile-termination workflow absent; access revoked only after the
  employee has already left the building with equipment and knowledge

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 2 | 2 |

**Assessment priority:** Start with PS.L2-3.9.1 because pre-access
screening is the authorization gate for every other control. Without
documented screening complete before access authorization, PS.L2-3.9.2
is operating on incomplete context. Then focus on PS.L2-3.9.2 evidence
timing; the practice commonly passes on policy existence and fails on
timing (the gap between HR personnel action and downstream revocation
actions).

**Key relationships:**
- Access Control (AC) revokes logical access in response to
  PS.L2-3.9.2 personnel actions; AC account disable is the logical
  counterpart to PE.L1-3.10.5 badge revocation
- Identification and Authentication (IA) issues and revokes
  credentials on the PS schedule. Pre-access screening under
  PS.L2-3.9.1 is the gate for IA account issuance
- Physical Protection (PE) revokes badges under PE.L1-3.10.5 triggered
  by PS.L2-3.9.2 events. The same-day hostile-termination SLA lives
  across both domains and either side's failure is visible in the
  other
- Awareness and Training (AT) assigns role-based training keyed to PS
  screening tier and role at hire, and re-assigns on transfer under
  PS.L2-3.9.2
- Incident Response (IR) insider-threat cases reference PS screening
  baselines and personnel-action timing. IR.L2-3.6.2 case records
  capture personnel-action-adjacent incidents
- Media Protection (MP) governs CUI media return during separation as
  part of the PS.L2-3.9.2 exit workflow. Issued devices, hardcopy
  documents, and tokens move from personnel to property custody on
  separation
