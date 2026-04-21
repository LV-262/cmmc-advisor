# System and Information Integrity (SI)

> Source: NIST SP 800-171 Rev 2, Section 3.14; CMMC Assessment Guide Level 2

## Overview

System and Information Integrity is the domain that keeps the organization's
systems in a known-good state against software flaws, malicious code, and
unauthorized activity. The domain has 7 practices: 4 at CMMC Level 1
(inherited from FAR 52.204-21 basic safeguarding) and 3 at Level 2. Every
contractor handling Federal Contract Information carries the 4 L1 SI
practices; contractors handling CUI add the 3 L2 practices on top.

NIST SP 800-171 Rev 2 separately organizes the 7 as 3 Basic Security
Requirements (3.14.1–3.14.3) plus 4 Derived Security Requirements
(3.14.4–3.14.7). The Basic/Derived split is a 171 classification and is
orthogonal to the CMMC L1/L2 split. L1 contains two Basic (3.14.1, 3.14.2)
and two Derived (3.14.4, 3.14.5); L2 contains one Basic (3.14.3) and two
Derived (3.14.6, 3.14.7). Do not conflate the two classifications.

Three practice clusters carry distinct operational loads. Flaw
remediation (SI.L1-3.14.1) is the patching-and-correction backbone, the
practice most visible on a POA&M (Plan of Action and Milestones) and the
execution counterpart to RA.L2-3.11.3 vulnerability remediation.
Malicious-code capability and execution (SI.L1-3.14.2 capability,
SI.L1-3.14.4 currency, SI.L1-3.14.5 scanning execution) function as a
capability-hub cluster where SI.L1-3.14.2 defines the anti-malware
protection and the other two maintain and exercise it. System monitoring
and unauthorized-use detection (SI.L2-3.14.6, SI.L2-3.14.7) are the
detective controls that produce telemetry incident response consumes.
Advisory intake (SI.L2-3.14.3) threads across all three clusters. It
is the channel that converts bulletins from
CISA (Cybersecurity and Infrastructure Security Agency), industry
ISAC (Information Sharing and Analysis Center) feeds,
KEV (Known Exploited Vulnerabilities) catalog entries, and vendor
advisories into findings the other practices then act on.

Cross-domain relationships cluster tightly because SI is a consumer
practice by design. CUI (Controlled Unclassified Information) context
shapes every one: the systems SI monitors are the systems where CUI
flows. Risk Assessment (RA) shares a single remediation record with
SI.L1-3.14.1; Configuration Management (CM) is the change-control gate
for patches and engine updates; Security Assessment (CA) owns the
monitoring cadence SI executes within; Maintenance (MA), Audit and
Accountability (AU), Access Control (AC), System and Communications
Protection (SC), and Incident Response (IR) each reciprocate at
specific practice boundaries called out in the practice bodies below.

---

## Level 1 Practices

### SI.L1-3.14.1 — Flaw Remediation

**Requirement:** Identify, report, and correct system flaws in a timely
manner.

**Why it matters:** Flaw remediation is the practice with the largest
operational surface in SI and the most frequent POA&M presence. Every
unpatched system is a standing exposure, and the "timely" qualifier
means an assessor evaluates not just whether patching happens but
whether the organization has a defensible definition of timely
keyed to risk. Without a documented remediation cadence, the organization
is one high-severity vulnerability away from discovering its patch
process does not exist in any reviewable form.

**Implementation guidance:**
- Patch management program covering operating systems, applications,
  firmware, container images, and cloud workloads. Scope matches the
  CUI boundary documented in the SSP (System Security Plan)
- Remediation SLA (service-level agreement) keyed to exposure and
  CVSS (Common Vulnerability Scoring System). Critical findings on
  CUI-handling or internet-facing assets in days; high in weeks;
  medium in the monthly patch cycle; low at the next opportunity
- KEV (Known Exploited Vulnerabilities) catalog entries warrant
  accelerated treatment: when a vulnerability appears on the CISA KEV
  catalog and is present on an in-scope asset, treat it as critical
  regardless of CVSS score. Active-exploitation signal outranks raw
  severity
- Coordination with RA.L2-3.11.3 vulnerability remediation: the two
  practices overlap where flaw correction takes the form of a patched
  vulnerability. RA prioritizes per risk; SI executes the correction.
  Agree on a single authoritative record per remediation item so the
  assessor sees one evidence trail rather than two parallel ones
- Coordination with CM.L2-3.4.3 system change tracking: a patch is a
  configuration change. It flows through the change-control process
  with test, approve, deploy, verify stages. Emergency patches follow
  a compressed but documented path, not a bypass
- POA&M eligibility: gaps in SI.L1-3.14.1 become POA&M entries only
  under weight-1 practices plus the SC.L2-3.13.11 encryption carve-out
  per references/poam-management.md. NIST SP 800-171A scores practices
  MET or NOT MET; partial implementations score NOT MET
- Verification scan to close: a remediation ticket closes only when a
  follow-up scan confirms the flaw is no longer detected. Ticket
  closure on patch deployment without verification is the most common
  finding in this practice

**Evidence to collect:**
- Patch management policy with defined SLAs per CVSS tier and asset
  exposure class
- Patch deployment records tied to CM change tickets for a
  representative sample
- Vulnerability scanner output showing findings closed after
  remediation (verification scan)
- KEV-catalog-triggered out-of-cycle remediation evidence
- POA&M entries for deferred items with compensating-control
  documentation and target dates

**Common mistakes:**
- Patches deployed outside CM change control because "it's just a
  patch"; configuration drift follows
- Tickets closed on patch deployment without verification scan
- SLAs in policy but no internal tracking of SLA compliance
- KEV catalog entries treated the same as any other CVSS-matching
  finding; active-exploitation signal not acted on

---

### SI.L1-3.14.2 — Malicious Code Protection

**Requirement:** Provide protection from malicious code at designated
locations within organizational systems.

**Why it matters:** This practice defines the anti-malware capability
that the other two malicious-code practices in this domain keep current
and exercise. NIST names designated locations specifically: system
entry and exit points
(firewalls, remote-access servers, electronic mail servers, web
servers, proxy servers) plus workstations, notebook computers, and
mobile devices. The capability is the technology investment; the
other two practices are the operational discipline that makes it
effective.

**Implementation guidance:**
- Endpoint protection on every in-scope workstation, laptop, and
  server. Modern platforms (EDR (Endpoint Detection and Response)
  class tools, platform-native protection such as Microsoft Defender
  for Endpoint, CrowdStrike Falcon, SentinelOne) provide signature-
  based detection plus behavioral analytics
- Gateway protection at system entry and exit: email security
  gateway (inbound attachment scanning, URL rewriting), web gateway
  (egress traffic scanning), plus firewall/IPS inline inspection
  where architecture supports it
- Server-side protection sized to the server role. File servers get
  on-access scanning; web servers get application-layer protection;
  email servers get message-layer scanning. One-size-fits-all desktop
  anti-malware on a server is under-protection
- Coordination with MA.L2-3.7.4 check diagnostic media for malicious
  code: SI owns the anti-malware capability on systems; MA owns the
  pre-connection discipline at the maintenance boundary. Coordinate
  so scan signatures and capability come from the same source of truth
- Cross-reference: SI.L1-3.14.4 keeps the capability current;
  SI.L1-3.14.5 covers scan execution (periodic plus real-time on
  file events). This practice does not restate those execution
  surfaces; each subsequent practice builds on the capability
  defined here

**Evidence to collect:**
- Endpoint protection coverage report (installed and active on every
  in-scope system)
- Email and web gateway configuration showing malicious-code
  inspection enabled
- Server-side protection configuration per server class
- Detection and block logs covering a representative time period
- Coordination record with MA.L2-3.7.4 on shared signature source

**Common mistakes:**
- Endpoint protection installed but disabled on a subset of systems
  (developer workstations, build servers, "performance" exclusions)
- Email gateway exists but attachment scanning is off or signature-only
- No server-side anti-malware; desktop policy assumed sufficient
- Coverage report stale; new systems onboarded without enrollment

---

### SI.L1-3.14.4 — Update Malicious Code Protection Mechanisms

**Requirement:** Update malicious code protection mechanisms when new
releases are available.

**Why it matters:** The SI.L1-3.14.2 anti-malware capability degrades
rapidly without currency. Signature feeds are hours-stale within a
day; engine versions accumulate vulnerabilities; ML models on newer
platforms require periodic retraining. This practice is the currency
discipline that keeps the capability effective.

**Implementation guidance:**
- Signature and definition updates: automated and near-continuous
  (every 1-4 hours is standard). Automated updates flow without
  per-update change tickets because the cadence would make change
  control unworkable; the policy documents this as a standing
  exception
- Engine and major version updates: these are configuration changes.
  They flow through CM.L2-3.4.3 change control with test, approve,
  deploy, verify stages. Engine rollouts coordinate with endpoint
  performance baselines so a failed rollout does not break
  production workloads
- Coverage verification: daily report of endpoints that failed to
  pull signatures in the last 24 hours, quarantining or remediating
  stragglers. A definition feed that stops silently on 5% of
  endpoints is the common failure mode
- Back-reference to SI.L1-3.14.2: this practice keeps the capability
  defined there current. It does not add new capability surface

**Evidence to collect:**
- Update configuration showing automated signature cadence
- CM change tickets for engine or major version rollouts
- Signature-currency dashboard or report (endpoints with stale
  signatures)
- Remediation records for endpoints that fell behind

**Common mistakes:**
- Signature updates set to "manual" for a subset of systems and
  forgotten
- Engine upgrades deployed without change control because "it's just
  an update"; incompatibility breaks production
- Signature-currency dashboard exists but nobody reviews the failure
  list; ML-model and reputation-service updates treated as
  out-of-scope because they are not "signatures"

---

### SI.L1-3.14.5 — Periodic and Real-Time Scanning

**Requirement:** Perform periodic scans of organizational systems and
real-time scans of files from external sources as files are
downloaded, opened, or executed.

**Why it matters:** Scanning is the execution surface of the
SI.L1-3.14.2 capability. The NIST text explicitly names two modes:
periodic scans of systems and real-time scans of files on external-
source events (download, open, execute). Both are required. A
configuration with only one is a practice gap.

**Implementation guidance:**
- On-access scanning triggers on every download, open, and execute
  event. Endpoint protection is configured with on-access scanning
  enabled by default; performance-sensitive exclusions are documented
  and bounded to specific paths
- Periodic full-system scans on a documented cadence (weekly is
  typical for workstations; monthly or quarterly for servers where
  load allows). Scheduled to minimize user impact but not so
  infrequent that dormant infections survive indefinitely
- Removable-media scan-on-insert: USB mass storage devices scanned
  automatically when connected; the user cannot dismiss the scan.
  Ties to CM.L2-3.4.7 nonessential-functionality restrictions where
  removable media is blocked entirely, in which case this requirement
  is satisfied by prevention rather than scanning
- Back-reference to SI.L1-3.14.2: this practice exercises the
  capability defined there. Also a specialized case at the
  maintenance boundary: MA.L2-3.7.4 pre-connection scanning of
  diagnostic media invokes the same capability with stricter
  pre-use discipline
- Scan-result handling: detections generate tickets routed to
  incident response per IR.L2-3.6.1, not silently quarantined and
  forgotten

**Evidence to collect:**
- Endpoint protection configuration showing on-access scanning
  enabled
- Scheduled scan records covering the documented cadence
- Removable-media scan configuration and sample records
- Detection-to-ticket routing evidence

**Common mistakes:**
- On-access scanning disabled or narrowly scoped ("performance")
- Scheduled scans configured but last-run dates show months of
  missed scans
- Removable-media policy silent on scanning; devices mount without
  inspection, and detections logged but not routed to IR

---

## Level 2 Practices

### SI.L2-3.14.3 — Security Alerts and Advisories

**Requirement:** Monitor system security alerts and advisories and take
action in response.

**Why it matters:** Advisory intake is how the organization learns
about threats the other SI practices then act on. NIST identifies the
primary public source explicitly: CISA generates security alerts and
advisories to maintain situational awareness across federal and
nonfederal organizations. Software vendors, subscription services,
and ISACs supplement that channel. Without a defined intake program,
advisories arrive through whichever inbox a staff member happens to
watch, and action depends on whether that person is at work that week.

**Implementation guidance:**
- Advisory sources subscribed and routed to an identified role:
  CISA alerts and advisories; vendor security advisories for every
  platform in use (operating systems, hypervisors, network devices,
  major applications); industry ISAC feeds where membership applies
  (IT-ISAC, Defense Industrial Base ISAC); the CISA KEV catalog as
  an accelerated-priority feed
- Intake discipline: advisories arrive at a central distribution,
  are triaged against the asset inventory, and produce action items
  routed to SI.L1-3.14.1 flaw remediation, SI.L1-3.14.4 malicious-
  code mechanism updates, or other relevant practices. The triage
  is documented, not memorialized in someone's head
- Action cadence: critical advisories trigger same-day review;
  high-severity advisories trigger review within the business week;
  medium and low on a weekly cadence. Action includes explicit
  "no action required" determinations with rationale, not silent
  closure
- Coordination with CA.L2-3.12.3 continuous monitoring: CA.L2-3.12.3
  owns the assessment and monitoring cadence (are controls still
  operating, are findings still being produced). SI.L1-3.14.1 owns
  flaw-correction execution (are findings being closed). SI.L2-3.14.3
  provides the advisory-intake channel that surfaces new findings
  from external sources into the monitoring program. All three
  practices draw from the same findings inventory
- IoC (Indicator of Compromise) handling: advisories that include
  IoCs feed into SI.L2-3.14.6 detection rules and SI.L2-3.14.7
  unauthorized-use baselines. The IoC-to-detection-rule pipeline is
  an integration surface, not a separate program

**Evidence to collect:**
- Advisory source subscription list with distribution configuration
- Advisory triage records showing intake, asset-inventory mapping,
  action-item routing, and closure
- Sample advisories with evidence of action taken within the
  documented cadence
- KEV-catalog handling evidence (out-of-cycle remediation triggered)
- IoC-to-detection-rule records demonstrating the integration

**Common mistakes:**
- Advisories subscribed to an individual's mailbox; when that person
  leaves or goes on leave, the channel dies silently
- Advisories logged but no action-item routing; the log is a file,
  not a program
- KEV-catalog entries treated at CVSS-score speed rather than
  active-exploitation speed
- IoCs in advisories never converted to detection rules; the
  information lives in a PDF and never reaches monitoring tools

---

### SI.L2-3.14.6 — System Monitoring

**Requirement:** Monitor organizational systems, including inbound
and outbound communications traffic, to detect attacks and indicators
of potential attacks.

**Why it matters:** System monitoring is the primary detective
control for attacks that get past prevention. NIST frames this as
external monitoring (at the system boundary) plus internal
monitoring (within the system), with capabilities achieved through
IDS/IPS (Intrusion Detection System / Intrusion Prevention System),
malicious-code protection software, scanning tools, audit-record
monitoring, and network monitoring. The "inbound and outbound
traffic" phrase is deliberate: outbound matters because exfiltration
and command-and-control traffic are leaving-the-network events.

**Implementation guidance:**
- Boundary monitoring: IDS/IPS or network detection and response
  (NDR) capability inline or in span at the perimeter. Inspects
  inbound traffic for attack signatures and outbound traffic for
  data-exfiltration patterns and command-and-control indicators
- Internal monitoring: host-based detection, flow monitoring
  between network segments, and east-west traffic inspection where
  architecture supports it. Lateral movement between segments is
  the detection-of-potential-attacks surface this requirement
  references
- SIEM (Security Information and Event Management) aggregation
  platform with correlation rules for common attack patterns. Raw
  telemetry that nobody reads is not monitoring
- Coordination with AU (Audit and Accountability): AU.L2-3.3.1
  audit logs and AU.L2-3.3.5 audit correlation provide the log
  data SI.L2-3.14.6 correlates; the two practices share the same
  log pipeline
- Coordination with SC (System and Communications Protection): SC
  enforces the boundary (firewalls, DMZ design, network
  segmentation); SI monitors at and inside the boundary. Boundary
  enforcement without monitoring is half the control; monitoring
  without enforced boundary definition has no stable inspection
  point
- IoC-driven rules: IoCs from SI.L2-3.14.3 advisory intake feed
  detection rules here on a documented cadence

**Evidence to collect:**
- IDS/IPS or NDR configuration and rule inventory
- SIEM correlation-rule documentation and sample alerts
- Sample investigation records showing detection through triage
  through response
- Log-source inventory demonstrating both inbound and outbound
  traffic coverage
- IoC-to-detection-rule pipeline records

**Common mistakes:**
- Inbound monitoring only; outbound traffic not inspected for
  exfiltration or C2 beacons
- IDS/IPS deployed but rules never tuned past vendor defaults;
  false-positive fatigue leads to alert suppression
- SIEM collects logs but no correlation rules; alerts come from
  individual tools and nobody sees the attack chain
- Detection-to-response path undefined; alerts accumulate until an
  incident forces triage

---

### SI.L2-3.14.7 — Unauthorized Use Detection

**Requirement:** Identify unauthorized use of organizational systems.

**Why it matters:** Unauthorized use is distinct from external
attack. It includes compromised credentials being used by an
outsider, insider misuse of legitimate access, and misconfigured
automation performing actions it was not intended to. Detection
here closes the gap between "the user is authenticated" and "the
user is doing what they were authorized to do."

**Implementation guidance:**
- Lightweight-tier baseline (every DIB organization can achieve
  this): log-based behavioral monitoring on authentication, privilege
  use, and sensitive-resource access. Specific checks include
  off-hours authentication, impossible-travel login pairs, privilege
  escalation followed by atypical resource access, and bulk
  download or export events. All achievable with AU.L2-3.3.1 log
  data and SIEM correlation rules
- Privilege inventory as detection baseline: AC.L2-3.1.5 least-
  privilege and AC.L2-3.1.7 privileged-function controls define
  what each account is authorized to do. Detection here flags
  departures from that authorized envelope. Without a current
  privilege inventory, "unauthorized use" has no reference point
- Mature-tier option: UEBA (User and Entity Behavior Analytics)
  platforms apply machine-learning anomaly detection across the
  same telemetry. UEBA is an investment for larger organizations
  with mature telemetry; it is one option among several, not the
  headline capability this practice requires
- Coordination with AU: log data from AU.L2-3.3.1 feeds detection;
  AU.L2-3.3.8 log protection prevents attackers from covering their
  tracks by modifying or deleting records this practice depends on
- Coordination with AC: the privilege inventory AC maintains is the
  baseline this practice measures against
- Coordination with IR (Incident Response): detection signals from
  this practice activate IR.L2-3.6.1 incident-handling procedures.
  SI detects; IR responds

**Evidence to collect:**
- Correlation-rule inventory for off-hours, impossible-travel,
  privilege-escalation, and bulk-download detection
- Sample detection alerts with investigation outcomes
- Privilege inventory referenced as the baseline
- Handoff records from detection to IR activation

**Common mistakes:**
- "Unauthorized use" treated as equivalent to "failed authentication";
  the practice covers authenticated-but-abnormal use, not just
  unsuccessful login attempts
- Detection rules written once at SIEM deployment and never tuned
  against the current privilege inventory
- Shared service accounts make attribution impossible; unauthorized
  use on a shared account cannot be traced to a human actor
- UEBA purchased as the check-the-box solution without the
  foundational log coverage that makes it useful

**Modern IT note:** See
`modern-it/ai-services/fedramp-ai-services.md` and
`modern-it/ai-services/self-hosted-ai.md` for AI-service content-
safety and guardrail monitoring posture. Bedrock Guardrails,
Azure AI Content Safety, and Vertex AI Safety provide managed
unauthorized-use detection on AI outputs (jailbreak attempts,
policy-violating prompts, PII-leak detection). Self-hosted
deployments author equivalent guardrails via NeMo Guardrails,
Llama Guard, or contractor-authored filters. Guardrail events
feed the same SI.L2-3.14.7 detection pipeline as other
unauthorized-use signals.

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 4 | 3 | 7 |

**Assessment priority:** Start with SI.L1-3.14.1. Flaw remediation is
the largest operational surface in the domain and the practice most
visible on a POA&M, and a documented patch cadence with verification
scans is the foundation other SI practices build reporting and
detection on. Next, establish the malicious-code cluster: SI.L1-3.14.2
as capability baseline, SI.L1-3.14.4 as the currency discipline,
SI.L1-3.14.5 as the scanning execution surface. Then the monitoring
practices: SI.L2-3.14.6 for system and traffic monitoring, SI.L2-3.14.7
for unauthorized-use detection. SI.L2-3.14.3 advisory intake threads
across the entire sequence; stand it up early because every other
practice's timely response depends on advisories arriving at a
defined channel. The most common finding gap in this domain is
SI.L1-3.14.1 without a verification-scan-to-close step, followed by
SI.L2-3.14.6 without outbound-traffic inspection.

**Key relationships:**

- Risk Assessment (RA) shares flaw-remediation scope; coordination
  defined in the SI.L1-3.14.1 body
- Security Assessment (CA) owns continuous-monitoring cadence under
  CA.L2-3.12.3; coordination defined in the SI.L2-3.14.3 body
- Configuration Management (CM) is the change-control gate for
  patches and engine-version updates; coordination defined in the
  SI.L1-3.14.1 and SI.L1-3.14.4 bodies
- Maintenance (MA) pre-connection scanning at MA.L2-3.7.4 is a
  specialized application of the SI.L1-3.14.2 capability; shared
  signature source of truth, coordination defined in SI.L1-3.14.2
- Audit and Accountability (AU) log data feeds SI.L2-3.14.6 and
  SI.L2-3.14.7; AU is the shared telemetry surface
- System and Communications Protection (SC) enforces the boundary
  SI.L2-3.14.6 monitors
- Access Control (AC) privilege inventory is the baseline
  SI.L2-3.14.7 measures departures against
- Incident Response (IR) is the primary consumer of SI detection
  signals from SI.L1-3.14.5, SI.L2-3.14.6, and SI.L2-3.14.7
