# Risk Assessment (RA)

> Source: NIST SP 800-171 Rev 2, Section 3.11; CMMC Assessment Guide Level 2

## Overview

Risk Assessment is the domain that produces the organization's picture
of what could go wrong and how bad it would be. The domain has 3
practices: RA.L2-3.11.1 (periodic risk assessment), RA.L2-3.11.2
(vulnerability scanning), and RA.L2-3.11.3 (vulnerability remediation
per risk). All three are at Level 2. No Level 1 RA practices exist, so
contractors handling only FCI have no risk-assessment requirement
under this domain. RA is the risk-visibility layer for the rest of
the skill; Phase 6 anti-pattern content will cite RA.L2-3.11.1 as the
correct pattern against which risk-assessment theater is the
anti-pattern, and Phase 5 FedRAMP gap analysis cites RA methodology
for identifying coverage gaps between contractor and cloud-provider
responsibility.

Cross-domain relationships cluster around how risk data moves:
Security Assessment (CA) consumes RA output; risk assessments and
vulnerability-scan findings populate SSP (System Security Plan) and
POA&M (Plan of Action and Milestones) content under CA.L2-3.12.2.
System and Information Integrity (SI) overlaps RA.L2-3.11.3 with
SI.L1-3.14.1 flaw remediation; coordination is required so both
practices reference the same remediation artifact rather than
tracking duplicates. Configuration Management (CM) is the control
gate through which patches land as configuration changes.
Incident Response (IR) both feeds RA and consumes RA output:
post-incident lessons-learned drive RA re-assessment, and RA findings
drive IR playbook priority.
Audit and Accountability (AU) log data informs the risk picture and
supports vulnerability-scan validation.
Access Control (AC) surfaces excessive-privilege risk through the
periodic assessment loop.
Personnel Security (PS) contributes insider-threat risk as a
first-class input; PS.L2-3.9.1 screening tier and PS.L2-3.9.2
personnel-action triggers inform risk re-assessment on separation and
transfer events.

---

## Level 2 Practices

### RA.L2-3.11.1 — Periodic Risk Assessment

**Requirement:** Periodically assess the risk to organizational
operations (including mission, functions, image, or reputation),
organizational assets, and individuals, resulting from the operation
of organizational systems and the associated processing, storage, or
transmission of CUI.

**Why it matters:** Every other control in this skill depends on a
sensible picture of what is at risk and how bad the consequences
would be. Without a real risk assessment, control-selection decisions
are defensive posturing rather than informed prioritization, and an
assessor will find evidence of controls but no rationale for why
those controls rather than others.

**Implementation guidance:**
- Methodology: document the risk-assessment process end to end.
  Common frameworks include NIST SP 800-30 (Risk Assessment guidance)
  and the NIST Cybersecurity Framework's Identify function. The
  specific framework matters less than having one and applying it
  consistently
- Cadence: at least annual for the organizational baseline; more
  frequently on material change (new system, new threat category,
  incident post-mortem finding, significant personnel turnover at
  high-access levels)
- Threat-source catalog: include adversarial threats (nation-state,
  criminal, insider), accidental threats (human error, misconfiguration),
  environmental threats (power, weather, hardware failure), and
  structural threats (dependency failures, supply-chain compromise)
- Asset scope: every system, application, and data store that
  processes, stores, or transmits CUI, plus the supporting
  infrastructure. Scope the assessment to the CUI boundary defined
  in the SSP
- Risk register: the tangible output. Each entry names the threat,
  the vulnerability, the affected asset, likelihood, impact, composite
  risk rating, current treatment, and residual risk. Without the
  register, the assessment has no durable artifact
- Tie to business context: risk ratings are expressed in terms an
  executive can act on (financial exposure, contract impact,
  reputational harm), not purely in CVSS or technical language
- Feeds downstream: the risk register is the primary input to
  CA.L2-3.12.2 POA&M development; items that cannot be immediately
  remediated become POA&M entries with target dates

**Evidence to collect:**
- Risk assessment policy and methodology documentation
- Most recent completed risk assessment report with all threat-source
  categories covered
- Risk register with dated entries, composite ratings, and residual
  risk after treatment
- Change log showing re-assessment events triggered by material
  changes
- Business-context translation artifacts (executive-briefing risk
  summaries, quarterly risk-posture reports)

**Common mistakes:**
- Risk assessment completed once at program launch and never refreshed
- Methodology exists but the risk register does not; the assessment
  produces a narrative without a trackable artifact
- All risks rated the same (usually "medium") because the
  likelihood-and-impact scoring is unanchored to actual data
- Insider-threat risk omitted because PS-related risks are assumed
  to be HR's concern
- Risk register disconnected from POA&M; items identified as risks
  never become tracked remediation work
- Ratings in CVSS only, with no translation to business impact that
  leadership can act on

---

### RA.L2-3.11.2 — Vulnerability Scanning

**Requirement:** Scan for vulnerabilities in organizational systems
and applications periodically and when new vulnerabilities affecting
those systems and applications are identified.

**Why it matters:** Vulnerability scanning is the operational feed
for RA.L2-3.11.1. Without scans, the risk assessment operates on
assumptions rather than current system state. Scans also validate
that CM patching and SI flaw remediation are actually closing
exposures, not just producing tickets.

**Implementation guidance:**
- Asset scope: endpoints (workstations, laptops), servers, network
  devices, web applications, container images, cloud workloads, and
  infrastructure-as-code definitions where they describe deployed
  state. The scope matches the CUI boundary at minimum, with
  pre-production systems scanned at the same cadence as production
- Authenticated scanning: credentialed scans into systems find issues
  unauthenticated scans cannot see (missing patches on non-listening
  services, local configuration weaknesses, installed-but-unused
  software). Authenticated scanning is the practitioner standard for
  internal assets (NIST SP 800-115 Section 4.3.1 recommends
  credentialed testing for complete results); unauthenticated
  scanning supplements it for external-perimeter views
- Frequency: a periodic baseline (monthly for production, more
  frequently for internet-facing assets) plus event-driven scans on
  new-vulnerability disclosure. The new-vulnerability trigger is the
  "when new vulnerabilities affecting those systems and applications
  are identified" portion of the requirement and must be operational,
  not just policy
- Tooling uses CVE (Common Vulnerabilities and Exposures) as the
  identifier namespace and CVSS (Common Vulnerability Scoring System)
  for severity scoring.
  Automated tools consume SCAP (Security Content Automation Protocol)
  content and check against NVD (National Vulnerability Database)
  entries
- Prioritization signals beyond raw CVSS: KEV (Known Exploited Vulnerabilities)
  catalog entries indicate active exploitation in
  the wild and warrant faster treatment than the CVSS score alone
  suggests. Asset exposure (internet-facing, CUI-handling, privileged)
  also elevates priority
- Web application scanning: distinct tooling (DAST, SAST where
  applicable) covers application-layer issues that infrastructure
  scanners miss. Required when the organization runs custom web
  applications in scope for CUI processing
- Cloud-workload scanning: cloud-native tools (Amazon Inspector,
  Microsoft Defender for Cloud, GCP Security Command Center)
  supplement traditional scanners for cloud assets and integrate
  with the overall scan record

**Evidence to collect:**
- Vulnerability scanning policy with defined asset scope and
  frequency
- Scanner configuration showing authenticated scans on in-scope
  systems
- Sample scan reports covering a representative cross-section of
  asset types
- Event-driven scan records triggered by specific new-vulnerability
  disclosures
- KEV-catalog-aligned priority handling evidence
- Integration between scanner output and the risk register or
  vulnerability management platform

**Common mistakes:**
- Unauthenticated scanning only, which misses the majority of
  installed-software findings
- Scan cadence in policy but missed in practice; monthly-scheduled
  scans that actually run quarterly
- No event-driven scan on new-vulnerability disclosure; the "when
  new vulnerabilities are identified" trigger is treated as
  aspirational
- Web applications excluded from scanning scope; infrastructure
  scanner run against the web tier catches none of the application
  logic issues
- Cloud assets scanned only when they happen to be reachable from
  the on-premise scanner; cloud-native scanning not integrated
- Credentialed scans failing silently because scanner credentials
  expired or lost privilege; scan output looks complete but covers
  only a fraction of intended assets

---

### RA.L2-3.11.3 — Vulnerability Remediation

**Requirement:** Remediate vulnerabilities in accordance with risk
assessments.

**Why it matters:** Finding vulnerabilities without remediating them
produces a growing inventory of known exposure. The practice requires
remediation keyed to risk, which means a prioritization model that
routes finite remediation capacity to the highest-risk findings
first, not to whichever team complains loudest.

**Implementation guidance:**
- Remediation SLA (service-level agreement) keyed to CVSS and
  exposure: critical findings on internet-facing or CUI-handling
  assets resolved in days; high findings in weeks; medium in the
  monthly patch cycle; low at the next opportunity. KEV-catalog
  entries warrant accelerated treatment with priority elevated to
  critical when the vulnerability is present on an in-scope asset,
  regardless of CVSS score
- Coordination with SI.L1-3.14.1 flaw remediation: the two practices
  overlap where vulnerability remediation takes the form of patches,
  firmware updates, or configuration corrections. SI.L1-3.14.1 is
  broader (includes flaw correction beyond CVE-tracked vulnerabilities);
  RA.L2-3.11.3 is risk-prioritized within that overlap. Agree on a
  single tracking system and single authoritative record per
  remediation item so the assessor sees one evidence trail rather
  than two parallel ones
- Patch application flows through Configuration Management (CM). A
  patch is a configuration change; it goes through the change-control
  process with test, approve, deploy, verify stages. The patch being
  fast does not exempt it from CM
- Compensating controls when patches are unavailable or deferred:
  network segmentation, access restrictions, monitoring rule
  additions. The compensating control has an expiration date tied to
  the patch-available date, not an indefinite acceptance
- POA&M (Plan of Action and Milestones) as the tracking artifact for
  items that cannot be immediately remediated. Each POA&M entry has
  a target completion date, an interim compensating control if one
  exists, and a named owner. POA&M feeds CA.L2-3.12.2 deliverables
- Verification scan to close: remediation is not complete until a
  follow-up scan confirms the vulnerability is no longer detected.
  Ticket closure without verification is the most common assessment
  finding in this practice

**Evidence to collect:**
- Remediation policy defining SLAs by CVSS and exposure
- Ticketing or vulnerability-management platform records showing
  findings moved from detection to closure with timestamps
- POA&M entries for deferred items with compensating-control
  documentation
- CM change records for patch deployments
- Verification-scan records pairing each closed finding with a
  follow-up confirmation
- Evidence of KEV-catalog-triggered out-of-cycle remediation

**Common mistakes:**
- Tickets closed on patch deployment without verification scan; the
  patch may have failed to install or reverted
- SLAs in policy but missed in practice; no internal tracking of SLA
  compliance
- POA&M and the ticketing system tracking different items; assessors
  cannot reconcile
- Patches deployed outside CM change control because "it's just a
  patch"; configuration drift follows
- Compensating controls applied without expiration; "temporary"
  network isolation becomes permanent architectural complexity
- KEV catalog entries treated the same as any other CVSS-matching
  finding; active-exploitation signal not acted on

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 3 | 3 |

**Assessment priority:** Start with RA.L2-3.11.1. Methodology is the
foundation; without a documented risk-assessment process producing a
risk register, RA.L2-3.11.2 vulnerability scans have no destination
and RA.L2-3.11.3 remediation has no prioritization input. Then
RA.L2-3.11.2 (scanning feeds the register with current-state data)
and finally RA.L2-3.11.3 (remediation closes the loop). RA.L2-3.11.2
authenticated-scanning coverage is the most common finding gap
because unauthenticated scans miss the majority of real issues.

**Key relationships:**
- Security Assessment (CA) consumes RA output; risk-assessment
  findings and vulnerability data populate SSP content and
  CA.L2-3.12.2 POA&M entries
- System and Information Integrity (SI) shares flaw-remediation
  scope with RA.L2-3.11.3; SI.L1-3.14.1 and RA.L2-3.11.3 require
  coordination so evidence is not duplicated or split
- Configuration Management (CM) is the change-control gate through
  which patches and other remediations land as configuration changes
- Incident Response (IR) both feeds RA (post-incident lessons
  trigger re-assessment) and consumes RA (risk findings drive
  playbook priority)
- Audit and Accountability (AU) provides log data that informs the
  risk picture and validates vulnerability-scan findings
- Access Control (AC) surfaces excessive-privilege risk through
  periodic assessment of account and entitlement inventories
- Personnel Security (PS) contributes insider-threat risk; PS.L2-3.9.1
  screening tier and PS.L2-3.9.2 personnel-action events feed RA
  re-assessment on separation and transfer
