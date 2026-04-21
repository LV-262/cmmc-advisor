# Security Assessment (CA)

> Source: NIST SP 800-171 Rev 2, Section 3.12; CMMC Assessment Guide Level 2

## Overview

Security Assessment is where "we implemented the controls" becomes
"we can show the controls work." The domain has 4 practices, all at
Level 2: CA.L2-3.12.1 (periodic control assessment), CA.L2-3.12.2
(plans of action for deficiencies), CA.L2-3.12.3 (continuous
monitoring), and CA.L2-3.12.4 (system security plan development and
periodic update). No Level 1 practices exist in this domain, so
contractors handling only FCI have no CA obligation. Two of the four
practices overlap with dedicated skill references.
SSP (System Security Plan) structure, section content, and
maintenance cadence live in references/ssp-guidance.md.
POA&M (Plan of Action and Milestones) mechanics live in
references/poam-management.md, which covers Conditional Certification
scoring, the 180-day closeout clock, and the SC.L2-3.13.11 encryption
carve-out. This file keeps CA.L2-3.12.4 and CA.L2-3.12.2 in
practice-assessment framing: what the requirement demands, what an
assessor verifies, where the evidence comes from.

Cross-domain relationships cluster around the assessment evidence
flow. CUI (Controlled Unclassified Information) shapes every
relationship in this domain: the SSP documents where CUI lives,
POA&Ms track gaps in CUI-protecting controls, and monitoring watches
the systems where CUI flows. Risk Assessment (RA) feeds CA.L2-3.12.1
with current-state risk data and CA.L2-3.12.2 POA&M entries with
vulnerability-scan findings; among prior Phase 4 domain files, RA is
the only one that cites CA practice identifiers directly. System and
Information Integrity (SI) shares the findings inventory with
CA.L2-3.12.3 continuous monitoring. CA owns the assessment cadence;
SI owns flaw-correction execution. Configuration Management (CM)
provides the baselines that controls are assessed against. Incident
Response (IR) produces post-incident lessons that become POA&M
entries. Audit and Accountability (AU) log data supports ongoing
monitoring. System and Communications Protection (SC) carries the
single SC.L2-3.13.11 POA&M carve-out and supplies much of what
CA.L2-3.12.3 monitors.

---

## Level 2 Practices

### CA.L2-3.12.1 — Security Assessment

**Requirement:** Periodically assess the security controls in
organizational systems to determine if the controls are effective
in their application.

**Why it matters:** Implementation without assessment is claims
without evidence. The assessment is how an organization learns
whether documented controls are actually operating as intended and
producing the intended security outcome. During CMMC certification,
a C3PAO (CMMC Third-Party Assessment Organization) conducts an
equivalent external assessment and issues the certification
decision. Without periodic self-assessment, control effectiveness
degrades silently and nobody notices until a finding or an incident
surfaces it.

**Implementation guidance:**

- Assessment methodology: document the process and scoring against
  NIST SP 800-171A assessment objectives for each of the 110 Level 2
  practices. Each objective decomposes a practice into testable
  determinations (interview, examine, test activities). Without a
  written methodology, assessment results are not reproducible
  across assessors or cycles
- Cadence: at least annual for the full control set, with off-cycle
  assessment on material change (new system, new CUI category, SSP
  revision). Annual is practitioner baseline, not a NIST mandate;
  match the cadence to system volatility
- Assessor independence: self-assessment is performed by personnel
  who did not implement the specific controls under assessment.
  Full organizational independence is not required at Level 2, but
  an implementer reviewing their own control is not an assessment
- Scoping: assessment covers the system boundary documented in the
  CA.L2-3.12.4 SSP. In-scope asset categories (CUI Assets, Security
  Protection Assets, Contractor Risk Managed Assets, Specialized
  Assets) all receive assessment; out-of-scope assets remain out of
  scope with the scoping decision documented in the SSP
- Assessment output: a written report documenting which practices
  are MET, NOT MET, or NOT APPLICABLE, with evidence references and
  rationale. Findings feed directly into CA.L2-3.12.2 POA&M entries
  when the gap cannot be closed before the assessment concludes
- Relationship to CA.L2-3.12.3: continuous monitoring provides
  ongoing data between periodic assessments. The two practices
  complement each other: periodic assessment is the deep pass,
  continuous monitoring is the between-pass signal

**Evidence to collect:**

- Assessment methodology document with scoring approach and mapping
  to NIST SP 800-171A objectives
- Most recent completed self-assessment report against all 110
  Level 2 practices
- Objective-by-objective results traceable to the assessment report
- Assessor independence documentation naming who assessed which
  controls and who implemented them
- Change-triggered assessment records for the past 12 months
- Finding-to-POA&M-entry traceability records

**Common mistakes:**

- Self-assessment performed by the same individuals who implemented
  the controls; findings biased toward confirming existing
  implementation
- Assessment methodology exists but does not align to NIST SP
  800-171A objectives; practices scored without decomposition into
  testable determinations
- Annual cadence claimed in policy but actual intervals run 18 to
  24 months; change-triggered re-assessment treated as optional
- MET/NOT MET determinations recorded without supporting evidence
  references; an assessor cannot reconstruct the determination on
  review
- Out-of-scope assets included in the assessment because scoping
  decisions were never documented; assessment scope exceeds the
  SSP boundary
- Findings identified but never moved to CA.L2-3.12.2 POA&M
  entries; the finding lives in the assessment report and dies
  there

---

### CA.L2-3.12.2 — Plan of Action

**Requirement:** Develop and implement plans of action designed
to correct deficiencies and reduce or eliminate vulnerabilities
in organizational systems.

**Why it matters:** Every assessment produces findings and not every
finding can be closed before the next milestone. The POA&M is the
tracking artifact that converts "we found this" into "we committed
to close it by this date." For CMMC, the POA&M also gates
Conditional Certification: organizations with limited gaps can
achieve certification by committing to close remaining items under
defined rules. An organization without a structured POA&M has no way
to show an assessor (or itself) that deficiencies are being worked
rather than forgotten.

**Implementation guidance:**

- POA&M as tracking artifact: practices scored NOT MET in
  CA.L2-3.12.1 become POA&M entries when the gap cannot be closed
  before the assessment concludes AND the practice qualifies for
  Conditional Certification deferral (weight-1 practices plus the
  SC.L2-3.13.11 encryption carve-out per references/poam-management.md).
  NIST SP 800-171A scores practices MET or NOT MET; partially
  implemented practices score NOT MET
- Entry content per item: practice ID, weakness description, named
  point of contact, planned remediation steps, target completion
  date, resources required, current status. Specificity beats
  volume
- Integration with RA.L2-3.11.1 risk register: the register and
  the POA&M are distinct artifacts, but the same remediation items
  should appear on both when a finding carries significant risk.
  Reconcile on a documented schedule so an assessor sees one
  consistent inventory
- Ownership: each POA&M entry names an individual, not a role or
  team alias. Anonymous ownership is a common assessment finding
- Closure discipline: an entry closes only when remediation is
  verified, not when the action is scheduled or taken. Verification
  evidence attaches to the closure record
- See references/poam-management.md for Conditional Certification
  scoring rules, the 180-day closeout clock, the SC.L2-3.13.11
  encryption carve-out, and worked examples of effective POA&M
  entries versus ineffective ones

**Evidence to collect:**

- POA&M document or system export showing active and closed entries
- Traceability from CA.L2-3.12.1 assessment findings to POA&M
  entries
- Closure records with verification evidence for recently closed
  items
- Named ownership per entry with current contact information
- Integration records with the RA.L2-3.11.1 risk register or the
  ticketing system of record

**Common mistakes:**

- POA&M used as a dumping ground for every unresolved item,
  regardless of whether it is a control deficiency or routine
  operational work
- Entries without named owners, or with stale ownership after
  personnel turnover
- Target completion dates missed without replan; entries slip
  indefinitely without a change record
- Items marked closed based on remediation action taken rather than
  on remediation verification; no evidence attached to closure
- POA&M maintained by the compliance team in isolation from the
  engineering team responsible for remediation; entries describe
  fixes that will not actually happen
- Organization treats the POA&M as something to produce at
  assessment time rather than as the ongoing record of gap to
  closure

---

### CA.L2-3.12.3 — Continuous Monitoring

**Requirement:** Monitor security controls on an ongoing basis to
ensure the continued effectiveness of the controls.

**Why it matters:** CA.L2-3.12.1 produces a point-in-time picture.
Between assessments, system state changes: patches land, users
join and leave, new services come online, attackers discover new
vulnerabilities. Continuous monitoring is the mechanism for
detecting drift between assessment cycles. Without it, the picture
from last year's assessment becomes increasingly unreliable as time
passes, and a finding closed during the assessment may quietly
reappear a month later.

**Implementation guidance:**

- ISCM (Information Security Continuous Monitoring) strategy per
  NIST SP 800-137: document what gets monitored, how often, by
  what mechanism, and who reviews the output. Without a documented
  strategy, monitoring is a collection of tools rather than a
  program
- Monitoring targets: account provisioning and deprovisioning,
  configuration drift, patch and vulnerability state, access log
  anomalies, privileged-user activity, security-tool health.
  Automated monitoring covers what humans cannot watch in
  real-time; human review covers signals automation cannot
  summarize
- Cadence by target class: real-time for high-signal events
  (authentication failures, privilege escalation, EDR alerts);
  daily for configuration drift and scan results; weekly for
  patch-status rollups; monthly for privileged-account reviews
- Reporting and review: monitoring data flows to dashboards that
  an identified role reviews on a documented schedule. Raw
  telemetry that nobody reads is not monitoring
- Coordination with SI.L1-3.14.1 (flaw remediation) and
  SI.L2-3.14.3 (security alerts and advisories): CA.L2-3.12.3
  owns the assessment and monitoring cadence (are controls still
  operating, are findings still being produced). SI.L1-3.14.1
  owns flaw-correction execution (are findings being closed).
  SI.L2-3.14.3 provides the advisory-intake channel that surfaces
  new findings from external sources into the monitoring program.
  All three practices draw from the same findings inventory.
  Agree on a single authoritative record per finding so the
  assessor sees one evidence trail rather than three parallel
  ones
- Feedback to CA.L2-3.12.1: monitoring data updates assessment
  scope and priority for the next periodic pass. Practices where
  monitoring shows drift get deeper attention in the next
  assessment cycle

**Evidence to collect:**

- ISCM strategy document naming targets, cadence, and review roles
- Sample monitoring dashboards or report outputs covering a
  representative cross-section of targets
- Review records showing identified personnel examined monitoring
  output on the documented schedule
- Cross-reference between monitoring-detected issues and
  SI.L1-3.14.1 remediation records demonstrating the coordinated
  tracking artifact
- Change log showing ISCM strategy revisions tied to scope or
  technology changes

**Common mistakes:**

- Tools deployed without a strategy; telemetry collected but no
  review cadence assigned
- Monitoring dashboards exist but no identified role reviews them;
  alerts accumulate until an incident forces manual triage
- ISCM cadence documented but SI.L1-3.14.1 remediation tracking
  uses a different ticketing system; the assessor cannot
  reconcile findings to closure
- Real-time alerts in tooling but no real-time response path; an
  alert that fires on Friday at 5 PM is still open Monday morning
- Privileged-account reviews treated as an IA responsibility and
  not wired into CA.L2-3.12.3 monitoring; two parallel programs,
  two tracking systems
- Monitoring scope limited to what is easy to automate (log
  volume, endpoint count); control-effectiveness signals like
  configuration drift skipped because they are harder to
  quantify

---

### CA.L2-3.12.4 — System Security Plan

**Requirement:** Develop, document, and periodically update system
security plans that describe system boundaries, system environments
of operation, how security requirements are implemented, and the
relationships with or connections to other systems.

**Why it matters:** The SSP is the document an assessor reads to
understand the system under assessment. Without it, the assessor
does not know what is in scope, how controls are implemented, or
how one system connects to another. Practices can be perfectly
implemented and still score NOT MET because the SSP does not
describe them. The SSP is also a living operational artifact: the
version that describes how things used to be rather than how they
are now is a finding waiting to happen.

**Implementation guidance:**

- Required elements from the NIST text: system boundaries, system
  environments of operation, how security requirements are
  implemented, and relationships with or connections to other
  systems. Missing any one of the four is a practice defect, not
  a documentation defect
- Periodic update cadence: at least annual at the NIST practice
  requirement floor, with off-cycle updates triggered by material
  change (new system, new interconnection, significant personnel
  turnover in named SSP roles, significant control implementation
  change). References/ssp-guidance.md establishes quarterly full
  review as the operational cadence
- Ownership: a named individual (typically the System Security
  Officer) accountable for SSP currency. Anonymous or distributed
  ownership is the most common cause of stale SSPs
- Currency verification: quarterly spot-check of SSP contents
  against actual system state (asset inventory, network
  architecture, user population, interconnection list). Drift
  surfaced during spot-checks becomes input to the next update
- See references/ssp-guidance.md for SSP section structure,
  required content per section, assessor expectations, common
  gaps, and maintenance cadence detail. CA.L2-3.12.4 is the
  practice requirement; ssp-guidance.md is the authoring
  reference

**Evidence to collect:**

- Current SSP with date of last update clearly recorded
- SSP revision history showing periodic and change-triggered
  updates over the past 12 months
- Named ownership documented in the SSP and in role assignments
- Quarterly currency-verification records
- Interconnection documentation integrated into the SSP rather
  than maintained as a separate artifact that may drift out of
  sync

**Common mistakes:**

- SSP written once at program launch and never updated; the
  document reflects the environment that existed 18 months ago
- One of the four required elements (typically interconnections)
  missing or superficial; the SSP covers boundaries and controls
  but not system relationships
- Ownership assigned to a role title rather than a named
  individual; no one is accountable when the SSP drifts out of
  date
- SSP describes intended state rather than current state; an
  assessor comparing the SSP against production finds inconsistent
  implementation
- Change-triggered updates deferred because routine work takes
  priority; the next material-change update compresses six months
  of drift into a single rushed revision
- SSP maintained separately from the systems it describes; the
  system team and the SSP team do not coordinate, so SSP currency
  lags operational reality

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 4 | 4 |

**Assessment priority:** Start with CA.L2-3.12.4 (SSP), even though
it is numerically last. The SSP is the document an assessor reads to
understand what is in scope, and no other CA practice has meaning
without it: CA.L2-3.12.1 assesses controls documented in the SSP,
CA.L2-3.12.3 monitors the system the SSP describes, and
CA.L2-3.12.2 POA&M tracks gaps against the SSP baseline. Once the
SSP is stable, move to CA.L2-3.12.1 (periodic self-assessment
against NIST SP 800-171A objectives), then CA.L2-3.12.3 (continuous
monitoring between assessment cycles), and finally CA.L2-3.12.2
(POA&M for findings that cannot be immediately closed). CA.L2-3.12.4
currency and CA.L2-3.12.1 assessor independence are the two most
common assessment gaps in this domain.

**Key relationships:**

- Risk Assessment (RA) feeds CA.L2-3.12.1 with current-state risk
  data and CA.L2-3.12.2 POA&M entries with vulnerability-scan
  findings. Reciprocal: RA already cites CA.L2-3.12.2 across
  multiple practices as the POA&M tracking artifact for items
  that cannot be immediately remediated
- System and Information Integrity (SI) shares the findings
  inventory with CA.L2-3.12.3 continuous monitoring. CA owns the
  assessment cadence; SI.L1-3.14.1 and SI.L2-3.14.3 own
  flaw-correction execution. A single authoritative record per
  finding is the coordination target
- Audit and Accountability (AU) log data is assessment evidence
  under CA.L2-3.12.1 and ongoing-monitoring input under
  CA.L2-3.12.3; AU log-review cadence feeds monitoring-output
  review
- Configuration Management (CM) baselines are what controls are
  assessed against under CA.L2-3.12.1 and monitored against under
  CA.L2-3.12.3; CM change records feed SSP currency under
  CA.L2-3.12.4
- Incident Response (IR) post-incident lessons become POA&M
  entries under CA.L2-3.12.2; incident-response effectiveness is
  itself assessed under CA.L2-3.12.1
- System and Communications Protection (SC) carries the single
  FIPS (Federal Information Processing Standards) validated
  crypto POA&M carve-out under SC.L2-3.13.11; SC boundary
  protection is a primary subject of CA.L2-3.12.3 monitoring
- FedRAMP inheritance: CA.L2-3.12.3 (continuous monitoring) sits
  against a FedRAMP Moderate ConMon program that runs on a
  monthly/annual cycle, substantially more frequent than the
  CMMC triennial assessment cycle. CA.L2-3.12.4 (SSP) sits
  against a FedRAMP SSP template with roughly seventeen
  appendices and per-control Requirement/Summary/Implementation
  structure. See `references/fedramp-gap.md` "Continuous
  monitoring cadence" and "System Security Plan depth"
