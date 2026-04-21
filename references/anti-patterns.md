# Compliance Anti-Patterns

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2
> (DoD CIO); DFARS 252.204-7012; 32 CFR Part 170 CMMC Program
> Final Rule (effective 2024-12-16); NIST SP 800-171A
> assessment objectives; CMMC Phase 2 enforcement observations
> (48 CFR acquisition rule effective 2025-11-10); DoD CMMC
> Program cost-benefit analysis
> (federalregister.gov/documents/2023/12/26/2023-27280); C3PAO
> assessment guidance; practitioner-reported patterns from the
> DIB compliance community.

## Overview

Compliance theater is the pattern of appearing compliant
without being operationally secure. It takes effort,
investment, and organizational attention — all without
producing the control outcomes CMMC requires. Assessors see
through it. Peers see through it. Adversaries do not care.

This file catalogs sixteen named anti-patterns organized into
four theater categories: documentation theater (policy
without practice), tool theater (tools without outcomes),
scope theater (narrowing the boundary via semantic games),
and assessment theater (passing the assessment without being
ready). Each pattern covers four elements: what it looks like,
why it fails, which CMMC practices it breaks, and what to do
instead.

The patterns are not theoretical. They are observed
practitioner-level failure modes from DIB contractor
assessments and operational postures. Names and descriptions
stay at the product-category or behavior level; specific
vendor or contractor examples are not named.

Read alongside `references/ssp-guidance.md` (where the SSP
fails if documentation theater succeeds),
`references/poam-management.md` (where POA&M discipline
detects assessment theater), and
`references/evidence-collection.md` (where evidence-quality
standards prevent the theater categories below).

---

## Scope of this file

Covered:

- Sixteen named anti-patterns across four categories
  (documentation, tool, scope, assessment theater). Each
  pattern traceable to specific CMMC practices where the
  failure surfaces.
- Cross-cutting observations about why theater persists and
  what organizational dynamics reinforce it.
- Recovery paths when a contractor discovers they have been
  running one of these patterns.

Not covered:

- Specific vendor or product anti-patterns. Vendor-level
  failures belong in vendor-specific trust-center reporting,
  not in a CMMC-alignment file.
- Named contractor case studies. Public assessment outcomes
  are rare and privacy-sensitive; the file works at the
  pattern level.
- Fraud-specific categories (false attestation, forged
  evidence) beyond brief mention. Deliberate misrepresentation
  carries civil liability under the False Claims Act (31 USC
  3729-3733), with criminal exposure under 18 USC 1001 for
  knowingly false statements to the federal government. This
  file treats failure modes attributable to ignorance, time
  pressure, and organizational incentives rather than willful
  deception.
- Non-CMMC compliance frameworks (SOC 2, ISO 27001, HIPAA).
  The patterns overlap, but this file stays on CMMC / NIST
  800-171 framing.
- Anti-patterns specific to classified (IL6 and above)
  systems. Out of CMMC L2 contractor scope.

---

## How to read this file

Each anti-pattern section follows the same four-element
structure:

1. **What it looks like.** The observable symptoms — what an
   assessor or auditor would see when inspecting the
   environment, policies, or staff behavior.
2. **Why it fails.** The underlying reason the pattern does
   not satisfy the practice's intent, typically because the
   practice assesses operational behavior rather than policy
   existence.
3. **CMMC practices broken.** The specific practice
   identifiers where the pattern produces findings. Each
   identifier links back to the domain practice file at
   `references/domains/`.
4. **What to do instead.** The corrective pattern that
   produces both assessment-ready state and operational
   security outcomes.

Patterns are ordered within each category from most common
(first) to most subtle (last). A contractor running multiple
patterns typically accumulates them; the recovery path
threads them in the order given.

---

## Documentation theater

Patterns where documentation substitutes for practice.
Assessors catch these via the gap between what the SSP claims
and what systems actually do.

### Pattern 1: Policy pyramid without procedures

**What it looks like.** Organization has a comprehensive
policy library: an information-security policy, an
acceptable-use policy, an access-control policy, an
incident-response policy, a configuration-management policy.
Each policy references procedures that either do not exist,
exist as outdated drafts from a previous compliance effort,
or exist as generic templates with no organization-specific
content.

**Why it fails.** NIST 800-171A assessment objectives test
whether the practice is implemented, not whether a policy
claims it will be. Policies without procedures cannot
demonstrate implementation; assessors ask "show me the
procedure" and the gap becomes visible in the first
interview.

**CMMC practices broken.** CA.L2-3.12.4 (SSP maintenance),
CM.L2-3.4.1 (baseline configuration), IR.L2-3.6.1 (incident
handling), AU.L2-3.3.1 (system audit), plus most domain
practices that assume procedural implementation.

**What to do instead.** Pair every policy with a procedure
that names the operator, the tooling, the cadence, and the
evidence produced. The procedure is shorter than the policy
in most cases; it names who does what by when. Stop drafting
policies until the existing policies have procedures.

### Pattern 2: SSP that documents the intended state

**What it looks like.** The SSP describes controls as
designed or as planned. Implementation status reads
"implemented" across most practices even when the tooling or
process is in procurement or partial deployment. Date stamps
on the SSP are current; the content reflects a future state
the contractor intends to reach.

**Why it fails.** NIST SP 800-171A scores controls MET or NOT
MET based on operational state at assessment time, not
intended state. An SSP that overstates implementation
produces assessment findings when the assessor tests the
control and finds gaps. The contractor then faces two
problems: the finding itself and the credibility loss from
the SSP-reality mismatch.

**CMMC practices broken.** CA.L2-3.12.4 (SSP accuracy);
indirectly, every practice the SSP misrepresents.

**What to do instead.** SSP reflects current operational
state. NOT MET practices appear in the SSP as NOT MET and
flow to the POA&M per CA.L2-3.12.2. Honest NOT MET reporting
plus a credible POA&M beats overstated implementation every
time.

### Pattern 3: POA&M graveyard

**What it looks like.** POA&M document exists and appears
substantial: dozens of entries, some with target dates,
some with resource estimates. Entries have been in the POA&M
for years. New entries get added; few get closed. The POA&M
is a parking lot for everything the organization has not
decided how to handle.

**Why it fails.** Conditional Certification deferral rules
(see `references/poam-management.md`) scope POA&M use to
specific practice-weight categories with a 180-day closeout
clock. A POA&M graveyard violates the closeout discipline and
creates audit exposure when the assessor samples entries and
finds multi-year-old items with no active remediation.

**CMMC practices broken.** CA.L2-3.12.2 (plans of action);
RA.L2-3.11.1 (risk register) where POA&M items should
reconcile against risk register entries.

**What to do instead.** Entries enter the POA&M with a
specific closure date, a named owner, and a remediation plan.
Monthly POA&M review closes items that remediated, updates
items making progress, and escalates items past their
target. A POA&M entry with no closure activity in 90 days is
a finding against the contractor's process maturity.

### Pattern 4: Training completion without behavior change

**What it looks like.** Learning Management System reports
100% annual training completion. Completion records are
current. Phishing-simulation click rates are unmeasured or
measured but high (> 10% click-through). Incident reports
show users fell for basic phishing or social engineering
scenarios the training explicitly covered.

**Why it fails.** AT.L2-3.2.1 assesses that users are "made
aware" of security risks; NIST 800-171A's examine and test
objectives look at training content quality and effectiveness
measurement, not just completion. High completion with high
phishing-simulation click-through is evidence the training
is not producing awareness.

**CMMC practices broken.** AT.L2-3.2.1 (awareness),
AT.L2-3.2.2 (role-based training), AT.L2-3.2.3 (insider
threat awareness).

**What to do instead.** Pair completion tracking with
effectiveness measurement. Phishing-simulation click-through
rates < 5% is a practitioner target. Role-based content that
references the actual SSP, real contractor procedures, and
specific incidents relevant to the team. Refresh trigger on
material change (new policy, new threat vector, incident
lessons-learned) rather than calendar-only annual refresh.

---

## Tool theater

Patterns where tooling investment substitutes for outcomes.
Common at medium and large contractors; small contractors
less often because budget constrains the pattern.

### Pattern 5: Tool proliferation without integration

**What it looks like.** Three DLP products, two SIEM
platforms, two vulnerability scanners, separate endpoint
protection per business unit. Each tool was purchased to
address a specific gap; none were retired when the next was
purchased. Operators log into ten consoles to assemble a
single incident picture.

**Why it fails.** Fragmented tooling produces fragmented
signal. Assessors see the tool count and ask for integration
evidence (consolidated audit, single-pane alerting); the
contractor produces per-tool exports that do not correlate.
Findings accumulate against multiple practices because
nothing is operationally working end-to-end.

**CMMC practices broken.** AU.L2-3.3.5 (audit correlation),
SI.L2-3.14.6 (monitoring), IR.L2-3.6.1 (incident handling),
CM.L2-3.4.2 (security configuration enforcement) where tool
sprawl means inconsistent baseline enforcement.

**What to do instead.** Tool rationalization before tool
acquisition. A single SIEM with feeds from endpoint, network,
and cloud tooling; a single DLP policy surface (often the
primary productivity suite's native DLP); consolidated
vulnerability management. When a new tool is proposed, ask
what retires.

### Pattern 6: SIEM with no review cadence

**What it looks like.** SIEM platform deployed, logs flowing
in from endpoints, network devices, cloud services, and
applications. Correlation rules exist — sometimes
vendor-default, sometimes tuned at deployment and never
revisited. No named analyst is responsible for alert
triage. Alerts accumulate in a queue nobody reads.

**Why it fails.** AU.L2-3.3.3 (event review) requires that
logged events be reviewed on a defined cadence with
investigation of identified risks. A SIEM without review
cadence collects data that no one acts on; the assessor asks
for investigation records and none exist.

**CMMC practices broken.** AU.L2-3.3.3 (event review),
AU.L2-3.3.5 (audit correlation), SI.L2-3.14.6 (monitoring),
SI.L2-3.14.7 (unauthorized-use detection), IR.L2-3.6.1
(incident handling) — detection signals never flow to
response.

**What to do instead.** Named analyst role (security analyst,
SOC tier-1 operator, or managed-service equivalent) with
daily triage cadence, weekly correlation-rule review, and
monthly detection-quality metrics. Alerts have owners;
investigations produce written outcomes even if the outcome
is "confirmed benign."

### Pattern 7: Encryption-in-name-only

**What it looks like.** Encryption is claimed across the
environment: laptop full-disk encryption enabled, file
transfers use TLS, email carries TLS labels. FIPS 140
validation status for the cryptographic modules is unknown.
Some tooling uses TLS 1.0 or 1.1 for backwards compatibility;
some endpoint encryption uses non-validated modules bundled
with older operating-system images.

**Why it fails.** SC.L2-3.13.11 requires "FIPS-validated
cryptography" specifically; the control is not satisfied by
any encryption but by CMVP-validated modules per NIST FIPS
140-2 or 140-3 certificate listings. An assessor verifies
module certificate numbers against the CMVP registry
(csrc.nist.gov); "encryption enabled" without FIPS validation
produces a finding.

**CMMC practices broken.** SC.L2-3.13.11 (FIPS cryptography),
SC.L2-3.13.8 (data in transit), SC.L2-3.13.16 (data at
rest).

**What to do instead.** Inventory cryptographic modules by
CMVP certificate number. Decommission non-validated modules
from CUI systems. Disable TLS 1.0 and 1.1. Select endpoint
encryption that carries CMVP-validated modules (BitLocker
with validated modules, FileVault validated modules,
third-party FIPS-validated alternatives for Linux workloads).

### Pattern 8: Vulnerability scanner without remediation

**What it looks like.** Credentialed or authenticated
vulnerability scanning tool purchased and configured.
Scheduled scans run weekly or monthly. Reports pile up in
the scanner's web console; remediation tickets are opened
sporadically and close without verification. Critical and
high vulnerabilities identified three scan cycles ago are
still present in the next scan report.

**Why it fails.** SI.L1-3.14.1 (flaw remediation) requires
that flaws be identified, reported, and corrected in a
timely manner. Identification without correction satisfies
the first half and fails the second. NIST 800-171A examines
remediation evidence; unremediated persistent vulnerabilities
produce findings.

**CMMC practices broken.** SI.L1-3.14.1 (flaw remediation),
RA.L2-3.11.2 (vulnerability scanning), RA.L2-3.11.3
(vulnerability response).

**What to do instead.** Remediation SLA per severity
(practitioner-typical: critical 72 hours, high 14 days,
medium 30 days, low 90 days). Exception process for
vulnerabilities that cannot be patched (compensating control
documented, POA&M entry opened). Weekly vulnerability-
remediation review against the SLA; escalation when the
inventory of past-SLA items exceeds a defined threshold.

---

## Scope theater

Patterns where the contractor narrows the boundary through
semantic maneuvers rather than architectural changes. Assessors
often spot these in the first scoping conversation.

### Pattern 9: CUI scope drift

**What it looks like.** Original assessment scoped CUI to a
specific set of systems and users. Business operations have
evolved: a new program handles CUI in a BU outside the
original scope; email attachments containing CUI flow to
users not on the authorized list; a SaaS tool was adopted
that wasn't evaluated against the CUI boundary. The SSP has
not been updated.

**Why it fails.** The SSP becomes inaccurate against
operational reality. CA.L2-3.12.4 requires SSP maintenance
reflecting current state. Assessors discover the drift when
they sample CUI-touching systems and find ones not in the
SSP scope.

**CMMC practices broken.** CA.L2-3.12.4 (SSP), AC.L1-3.1.1
(authorized access control — access granted to CUI by users
not in the authorization boundary), MP.L2-3.8.2 (limit media
access), and every CUI-protecting practice on the out-of-
scope systems.

**What to do instead.** Quarterly scope review tied to
project intake and vendor onboarding. New systems touching
CUI flow through a gate that updates the SSP before go-live.
Named scope owner (typically CISO, deputy CISO, or compliance
lead) with authority to pause a CUI-adjacent project until
scope is documented.

### Pattern 10: Semantic scope-dodging

**What it looks like.** Contract clause review identifies
DFARS 252.204-7012. Contractor-level response: "we don't
store CUI; we only exchange it via email with the customer,
and we delete attachments after processing." SSP scope
excludes email and storage systems. CUI is everywhere the
customer-contractor email flow touches.

**Why it fails.** 32 CFR 2002 defines CUI based on
information content and handling requirements; "we don't
store it" does not remove CUI-status when the information
transits contractor systems. DFARS 7012 applies to CUI
processed, stored, or transmitted — all three.

**CMMC practices broken.** CA.L2-3.12.4 (SSP scoping),
AC.L1-3.1.1 (authorized access), SC.L2-3.13.8 (data in
transit — CUI email is in-scope), MP.L2-3.8.2 (media
access — email attachments are media).

**What to do instead.** CUI scope follows the information,
not the storage state. Transmitted CUI is in scope. See
`references/scoping-and-cui.md` for the scope-determination
framework. When the contract references DFARS 7012, assume
full CMMC L2 applies until scoping analysis proves a
narrower boundary with documented justification.

### Pattern 11: Commercial cloud with policy controls

**What it looks like.** Contractor runs CUI workflow on a
commercial-tenancy productivity suite. Configuration
tightened: advanced threat protection, conditional-access
policies, DLP rules, retention policies. Contractor argues
the policy configuration substitutes for a FedRAMP-authorized
tenancy.

**Why it fails.** DFARS 7012 requires FedRAMP Moderate
equivalence, which commercial M365 and Workspace meet for
federal use but not for CUI/DoD IL4+ under CSP SRG v1r1.
Commercial tenancies run on the commercial-cloud operator-
access boundary; US-person operator-access commitments and
sovereign-tenancy requirements do not apply. Policy controls
on a commercial tenancy do not substitute for the
authorization boundary.

**CMMC practices broken.** CA.L2-3.12.1 (security
assessment — inheritance from commercial cloud does not
cover the required IL4/IL5 scope), SC.L2-3.13.11 (FIPS
cryptography may not be enforced consistently), MP.L2-3.8.1
(media protection depends on tenancy-level operator access).

**What to do instead.** Migrate the CUI-handling surface to
GCC High (Microsoft), Workspace Assured Controls Plus
(Google), or an equivalent FedRAMP-authorized tenancy. See
`references/modern-it/productivity/README.md` for the
tenancy-selection framework. Policy controls layer on top of
the authorized tenancy, not in place of it.

### Pattern 12: Shared service accounts with no attribution

**What it looks like.** Operational teams share service
accounts ("admin," "ops," "cmmc-svc") for convenience across
multiple staff. Password rotation is infrequent. Audit logs
show "admin" performing actions without identifying the
human operator.

**Why it fails.** AU.L2-3.3.2 (user accountability) requires
that actions be traceable to unique users. Shared accounts
make forensic attribution impossible; SI.L2-3.14.7
(unauthorized-use detection) cannot detect individual
anomalies because the baseline is a shared identity. Both
assessment and incident-response fail on shared-account
patterns.

**CMMC practices broken.** AU.L2-3.3.2 (user accountability),
IA.L1-3.5.1 (identification), AC.L2-3.1.5 (least privilege —
shared accounts typically have broad privilege), AC.L2-3.1.7
(privileged-function auditing), SI.L2-3.14.7 (unauthorized
use detection).

**What to do instead.** Unique user accounts for every
human operator. Service-principal accounts for automation
with documented owners and purpose. Just-in-time privileged
access for administrative tasks (PIM in Entra ID Government;
Cloud Identity access elevation). Shared accounts retired or
replaced with role-based access tied to individual identity.

---

## Assessment theater

Patterns where the contractor optimizes for assessment
outcome rather than operational security. C3PAOs vary in
experience; sophisticated assessors catch these patterns,
less-experienced assessors sometimes let them pass — a gap
that surfaces on re-assessment when a different assessor
finds what the first one missed.

### Pattern 13: Point-in-time readiness

**What it looks like.** Three months before assessment, the
contractor surges resources: consultants engaged, tooling
configured, policies updated, evidence collected, staff
trained. Assessment passes. Six months later, the tooling
licenses lapsed, the consultants are gone, the staff moved to
other projects, and the compliance posture has degraded.

**Why it fails.** The CMMC rule anticipates continuous
compliance through annual affirmations (48 CFR 252.204-
7021). Point-in-time readiness fails the annual affirmation
when the contractor must re-attest under the same SSP to
the same control state.

**CMMC practices broken.** CA.L2-3.12.3 (continuous
monitoring), CA.L2-3.12.4 (SSP maintenance), CM.L2-3.4.3
(change tracking — continuous process required), and the
48 CFR 252.204-7021 annual affirmation obligation.

**What to do instead.** Continuous-compliance cycle
embedded in operations: monthly control spot-check, quarterly
internal assessment, annual internal assessment against the
full control set, triennial C3PAO assessment. Budget and
staffing treat compliance as an operational function, not a
project.

### Pattern 14: Inherited control fantasy

**What it looks like.** SSP claims inheritance from FedRAMP-
authorized cloud providers, primary-suite tenancies, or
managed-service providers. Specific inheritance claims are
not documented with traceability (which FedRAMP package,
which control, which package scope). Assessor asks for the
System Security Plan of the inherited provider; contractor
produces marketing material.

**Why it fails.** FedRAMP inheritance is legitimate per
NIST SP 800-171 Rev 2 control inheritance framing, but
requires documentation matching the inherited controls to
the provider's SSP and the contractor's usage configuration.
Claims without traceability produce findings.

**CMMC practices broken.** CA.L2-3.12.4 (SSP inheritance
documentation), CA.L2-3.12.1 (assessment — inherited
controls must be verifiable).

**What to do instead.** For each inherited control, document:
the provider, the FedRAMP package identifier (from
marketplace.fedramp.gov), the specific control in the
provider's SSP that the contractor inherits, and the
contractor-side configuration that activates the
inheritance. Store as an inheritance matrix alongside the
SSP.

### Pattern 15: C3PAO engagement without gap remediation

**What it looks like.** Contractor contracts with a C3PAO
for certification assessment without first conducting an
internal readiness assessment. The C3PAO arrives, finds
material gaps, and the assessment produces either a failed
certification or a POA&M-heavy Conditional Certification
that the contractor is not equipped to close in 180 days.

**Why it fails.** C3PAO assessment is for certification, not
for gap identification. A readiness assessment (internal,
consultant-led, or gap-assessment-specific C3PAO engagement)
identifies gaps the contractor closes before the
certification assessment.

**CMMC practices broken.** CA.L2-3.12.1 (pre-assessment
preparation), CA.L2-3.12.2 (POA&M discipline).

**What to do instead.** Internal readiness assessment six to
twelve months before the certification assessment.
Remediation sprint closes gaps before the C3PAO arrives.
Gap-assessment-only engagements (where the same or different
C3PAO provides non-attestation pre-assessment review) are
available and cost less than a full assessment.

### Pattern 16: Conditional Certification as default strategy

**What it looks like.** Contractor assumes Conditional
Certification will absorb remediation timeline slippage.
POA&M is planned at scale: thirty or forty practice gaps
expected to be open at assessment time, all queued for
180-day post-certification closure. Contractor underinvests
in remediation pre-assessment assuming Conditional
Certification carries the implementation cost to
post-certification.

**Why it fails.** Conditional Certification rules (see
`references/poam-management.md` and 32 CFR 170.21/170.23) limit
deferral to weight-1 practices (with SC.L2-3.13.11 included as
a specific carve-out despite its higher weight) and require a
minimum 80% assessment score for eligibility. Assumed-scale
POA&M strategies hit the 80% floor once enough weight-1
practices are NOT MET; non-weight-1 gaps fail the assessment
outright regardless of the POA&M volume.

**CMMC practices broken.** CA.L2-3.12.2 (POA&M rules),
CA.L2-3.12.1 (pre-assessment remediation), and whichever
practices the contractor intended to POA&M that fall
outside deferral eligibility.

**What to do instead.** Conditional Certification as a
discrete outcome for specific unavoidable gaps, not a
default strategy. Pre-assessment remediation closes most
weight-1 practices; POA&M carries only the gaps the
contractor genuinely cannot close before the assessment
date, documented with credible closure plans.

---

## Cross-cutting observations

Four reasons these patterns persist organizationally:

**Budget myopia.** Compliance is framed as cost rather than
operational investment. When compliance is a line item owed
to the contract vehicle, theater is rational: minimize the
cost, maximize the appearance of compliance. When compliance
is framed as risk management and part of operational
maturity, theater becomes expensive relative to the real
investment.

**Assessor variance.** Less-experienced C3PAO assessors
sometimes let theater pass. Contractors who pass through
theater sometimes conclude the theater works. On re-
assessment with a different assessor, the gap surfaces and
the contractor faces catch-up costs that exceed what proper
implementation would have required.

**Consulting incentives.** Consultants engaged for point-
in-time readiness optimize for the assessment outcome they
are measured on. Continuous-compliance consulting is a
different engagement with different incentives. Contractor
procurement that scopes consulting to the assessment produces
the point-in-time pattern; scoping to the compliance
posture produces the continuous pattern.

**Organizational entropy.** Compliance posture degrades
naturally as systems change, people move, tools get
deprecated, contracts add requirements. Without a
continuous-monitoring discipline, the degradation outpaces
the occasional compliance refresh. Theater is sometimes what
remains after the operational reality drifted away from the
documented state.

**Recovery path.** A contractor who recognizes they are
running one or more of these patterns has three months of
work minimum to recover, not three years. The recovery path
is: honest self-assessment (NOT MET is the honest answer for
most of these patterns), credible POA&M that actually
remediates rather than defers, continuous-compliance process
embedded in operations, and a C3PAO engagement timed for
readiness rather than urgency.

---

## Cross-domain anchors

Anti-pattern recognition composes with corpus cross-cutting
files and domain practice files:

- **SSP authoring.** `references/ssp-guidance.md` — the SSP
  is where documentation theater surfaces or is prevented.
- **POA&M management.** `references/poam-management.md` —
  the POA&M is where assessment theater meets operational
  reality.
- **Evidence collection.**
  `references/evidence-collection.md` — evidence quality
  standards prevent most documentation and tool theater.
- **CUI scoping.** `references/scoping-and-cui.md` — the
  upstream determination that scope theater operates against.
- **Levels and assessment.**
  `references/levels-and-assessment.md` — CMMC level
  determines assessment stakes.
- **Contractor profiles.**
  `references/contractor-profiles.md` — profile-specific
  theater risk (small contractors most vulnerable to
  documentation theater; large contractors most vulnerable
  to tool theater and scope sprawl).
- **FedRAMP Marketplace guide.**
  `references/fedramp-marketplace-guide.md` — inherited-
  control fantasy (Pattern 14) requires marketplace-verified
  inheritance claims.
- **Modern IT.** `references/modern-it/` — tenancy-selection
  framework prevents commercial-cloud-with-policy-controls
  (Pattern 11).

Domain practice files at `references/domains/` carry the
specific practice text each anti-pattern violates.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/scoping-and-cui.md`,
`references/levels-and-assessment.md`,
`references/ssp-guidance.md`,
`references/poam-management.md`,
`references/contractor-profiles.md`, or previous Phase 5
slices are not repeated here.

**Assessment objective.** A NIST SP 800-171A criterion that
decomposes a practice into testable determinations
(interview, examine, test activities). Assessors score the
practice MET or NOT MET by evaluating each objective.

**Assessor variance.** The observed variance in assessment
depth and rigor across different C3PAOs and individual
assessors within a C3PAO. A source of theater-persistence
risk.

**Conditional Certification.** Defined in
`references/poam-management.md`. The certification outcome
where specific eligible gaps are tracked on the POA&M for
180-day post-certification closure.

**Continuous compliance.** The operational discipline of
maintaining CMMC control state between assessments, versus
point-in-time readiness optimized for a specific assessment
date.

**False Claims Act.** 31 USC 3729-3733. US federal civil
statute imposing treble damages and civil penalties for
knowingly presenting false claims for payment to the federal
government. Knowingly false CMMC attestation may carry False
Claims Act civil exposure (see, for example, the Aerojet
Rocketdyne DOJ settlement, 2022-07-08); separate criminal
exposure under 18 USC 1001 may apply to knowingly false
statements to federal agencies. Consult counsel on specific
scenarios; this skill does not make FCA determinations.

**Inheritance matrix.** A traceability artifact mapping
inherited controls to the inheriting contractor's SSP, the
provider's FedRAMP package, and the specific inherited
control text. Distinguishes inherited-control fantasy
(Pattern 14) from documented inheritance.

**NIST SP 800-171A.** NIST Special Publication 800-171A,
the assessment methodology document for NIST SP 800-171
controls. Defines assessment objectives per practice.

**POA&M graveyard.** Pattern 3. A POA&M where entries
accumulate without closure, losing the tracking-artifact
function the POA&M is designed for.

**Remediation SLA.** The agreed time-to-remediation per
severity tier for identified vulnerabilities. Absent SLA or
SLA-without-enforcement is Pattern 8.

**Scope drift.** Pattern 9. The divergence between the
original assessment scope and the actual operational CUI
footprint over time.

**Tool rationalization.** The pre-acquisition discipline of
asking what retires when a new tool is adopted. The
alternative to tool proliferation (Pattern 5).

---

## Versioning and drift

Anti-pattern content drifts more slowly than vendor-specific
content, but the underlying CMMC enforcement context shifts:

- **Phase 2 enforcement observations.** Per the canonical
  phased-rollout taxonomy in
  `references/levels-and-assessment.md`, Phase 1 is the 2024-12-16
  32 CFR 170 program-rule effective date and Phase 2 is the
  2025-11-10 48 CFR acquisition-rule effective date. Patterns in
  this file reflect practitioner observations through Phase 2
  enforcement. Patterns 13 (point-in-time readiness) and 16
  (Conditional Certification default) are particularly likely to
  surface in Phase 3 enforcement (2026-11-10) when annual
  affirmations under 48 CFR 252.204-7021 become the continuous-
  compliance test.
- **Assessor experience maturation.** Assessor variance is
  expected to narrow as C3PAO experience accumulates across
  the industry. Patterns that currently pass with
  less-experienced assessors will be less likely to pass in
  2026-2027 assessment cycles.
- **Tooling market evolution.** Pattern 5 (tool
  proliferation) shifts with the market. Platform-
  consolidation trends (XDR replacing EDR+SIEM+NDR; SASE
  consolidating network tooling) reduce the surface area
  where proliferation is possible but introduce new
  single-vendor risk patterns not yet catalogued here.
- **Regulatory update cadence.** 32 CFR Part 170 and 48 CFR
  Parts 204/212/217/252 revisions change specific
  requirements; the anti-pattern framing largely survives
  specific control-text updates because the theater patterns
  attach to organizational dynamics rather than control
  specifics.

Content verified 2026-04-21 against corpus framework and
practitioner reporting through Phase 2 enforcement. Next
full re-verification at the corpus review cycle or when
CMMC enforcement phase changes materially (Phase 2 begins,
48 CFR annual affirmation cycle reaches steady state).
