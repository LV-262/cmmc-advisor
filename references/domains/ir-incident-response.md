# Incident Response (IR)

> Source: NIST SP 800-171 Rev 2, Section 3.6; CMMC Assessment Guide
> Level 2; NIST SP 800-61 Rev 2

## Overview

Incident Response is the pipeline that turns detection into action. It
consumes the output of Audit and Accountability (AU) alerting,
coordinates with Configuration Management (CM) during containment and
recovery, relies on System and Communications Protection (SC) to
understand where the boundary is, and leans on Identification and
Authentication (IA) for account lockdown during triage. The domain has
3 practices, all at Level 2. No Level 1 IR practices exist, so
organizations handling only FCI have no incident response requirement.
Any organization handling CUI needs a working capability.

The domain covers the full incident lifecycle: preparation, detection
and analysis, containment, eradication and recovery, and post-incident
activity. Assessors look for the capability as a coherent whole, not
the plan document alone. Plans that have never been practiced fail the
first realistic test. Awareness and Training (AT) sets the baseline
for team and stakeholder readiness that makes exercises meaningful,
and Media Protection (MP) governs evidence handling and
chain-of-custody during investigation.

---

## Level 2 Practices

### IR.L2-3.6.1 — Incident Handling Capability

**Requirement:** Build and maintain an operational incident handling
capability for organizational systems covering preparation, detection
and analysis, containment, recovery, and user response.

**Why it matters:** Detection without response is surveillance. A plan
on the shelf is not a capability. The 72-hour reporting clock starts
when something goes wrong, not when the team finishes reading the
runbook for the first time.

**Implementation guidance:**
- Preparation: document an IR plan with named roles, severity
  definitions, communication tree, and decision authority. The plan
  should specify declaration criteria that separate a security event
  from a declared incident, a severity classification scheme (common
  schemes run Critical / High / Medium / Low with defined impact
  thresholds), and the authority each role has at each severity. Assign
  a primary IR lead and at least one backup, and keep both reachable
  outside business hours. Maintain runbooks for the incident types the
  organization is most likely to face: ransomware, credential
  compromise, insider misuse, malware outbreak, phishing campaign, data
  exfiltration, denial of service, and lost or stolen device scenarios
- Tooling: a SIEM for detection and correlation, EDR on endpoints for
  containment actions, a case management system or structured ticketing
  for tracking, and a runbook platform the team can actually open
  during an incident. For cloud workloads, add cloud-native detection
  (CloudTrail anomaly detection, Azure Sentinel, GCP Security Command
  Center) integrated into the same SIEM where possible
- Detection and analysis: define triage criteria that map alert signals
  to severity levels. Document the decision path from raw alert to
  declared incident so triage is repeatable across shifts and
  responders. Include on-call procedures, runbook entry points per
  alert category, and escalation thresholds. Detection sources extend
  beyond the SIEM: user reports, EDR alerts, managed detection and
  response partner notifications, cloud provider security alerts, and
  supplier or customer notifications all need defined intake paths
- Containment: short-term actions include network isolation, EDR host
  quarantine, account disable, and session termination. Cloud workloads
  add identity-based containment (revoke tokens, disable IAM users,
  remove role assignments). Coordinate with network, endpoint, and
  cloud operations teams before executing disruptive containment.
  Pre-approved containment actions speed response by removing the need
  for real-time approval on well-understood scenarios
- Eradication and recovery: remove attacker persistence including rogue
  accounts, scheduled tasks, malicious services, modified binaries,
  injected registry keys, and persistence mechanisms in cloud resources
  (unexpected IAM roles, lambda triggers, cron entries). Restore from
  known-good configuration baselines under CM control. Validate systems
  before returning them to production. Account resets and credential
  rotations belong in this phase. Confirm backups are themselves
  uncompromised before restoring from them, particularly for ransomware
  scenarios
- User response: help-desk scripts for affected users, credential reset
  procedures, and a low-friction path for users to report suspected
  incidents. Users are frequently the earliest detection source for
  phishing and social engineering; an intake path that is faster than
  the alternative of ignoring the message is worth the investment
- Post-incident: a lessons-learned review within two weeks of closure.
  Review should cover what the detection missed, what the containment
  got right, what the recovery revealed about the environment, and
  what external comms worked or failed. Translate findings into runbook
  updates, plan revisions, and SSP changes if the incident exposed
  scope drift or control gaps. Track metrics across incidents: time to
  detect, time to contain, time to recover, root-cause category
  distribution

**Evidence to collect:**
- Incident response policy and plan documents with version history and
  sign-off
- IR team roster with primary and backup contact information, including
  after-hours reach
- Runbooks or playbooks for the incident types the plan anticipates
- Tool inventory showing SIEM, EDR, case management platform, and
  cloud-native detection in use
- Integration evidence between detection tools and the case management
  system
- Sample incident case records showing plan execution end to end
- Post-incident reports and after-action summaries
- Change log tying runbook revisions to specific incidents or exercises
- Metrics dashboard or periodic report on detection, containment, and
  recovery times

**Common mistakes:**
- A plan document exists but the team has never executed it against a
  real or simulated incident, so the plan reads well and fails under
  pressure
- No named IR lead. Incidents are assumed to be the security team's job
  with no accountable owner, and decisions stall waiting for consensus
- Runbooks written once and never updated after use, so they drift from
  the current environment
- Strong detection tooling paired with weak response tooling. Alerts
  fire but no one can act on them quickly because containment requires
  tickets, approvals, or tools the team cannot reach
- Lessons-learned reviews happen but findings never get back into the
  plan or runbooks. The organization relearns the same lesson every
  year
- Containment authority ambiguous. Responders hesitate to isolate
  systems because no one has pre-approved the action, and the business
  impact of waiting is higher than the impact of the containment itself
- Cloud-native detection not integrated with on-premise SIEM, producing
  two separate investigation experiences and missing the hybrid attack
  paths between them
- Backups restored into a compromised environment because re-infection
  was not ruled out before recovery

---

### IR.L2-3.6.2 — Incident Tracking and Reporting

**Requirement:** Track and document incidents and report them to
designated internal officials and external authorities per contractual
and regulatory obligations.

**Why it matters:** Assessors require a documented record. Contractual
obligations require external reports on a clock. Missing the DIBNet
72-hour window after a cyber incident affecting CUI can breach the
contract independent of the incident's technical impact.

**Implementation guidance:**
- Tracking: every declared incident opens a case in a structured system
  (ITSM ticket with a dedicated incident template, a standalone IR
  platform, or a case-management tool). The record carries the incident
  from open to closure with timestamped actions, attribution, affected
  systems, and outcome. A numbering scheme that persists across the
  year makes audit review easier
- Internal reporting: an escalation matrix maps severity to recipients.
  On-call responder notifies IR lead, who notifies management, legal,
  and affected business units according to severity thresholds.
  Executive notification defined for material incidents. Information
  protection obligations apply to incident communications themselves
  (CUI leaked in an email to an unauthorized recipient becomes its own
  incident)
- External reporting to DIBNet: for cyber incidents affecting CUI on
  covered contractor systems, report within 72 hours of discovery via
  DIBNet (the DoD Defense Industrial Base Network cyber incident
  reporting portal at dibnet.dod.mil) per DFARS 252.204-7012 (the DFARS
  cyber incident reporting clause). The 72-hour clock is a contractual
  requirement, not a suggestion. Discovery starts when the organization
  has credible reason to suspect a cyber incident, not when root cause
  is confirmed, so conservative reporting is the default posture
- DIBNet pre-provisioning: DIBNet submission requires a medallion
  certificate for authentication. The certificate takes time to obtain
  from the DoD external certification authority; organizations that
  wait until an incident to start the process will miss the 72-hour
  window. Register the organization and obtain at least one medallion
  certificate before it is needed
- External reporting to law enforcement: FBI field office or local law
  enforcement for criminal activity, typically coordinated through
  legal counsel. Parallel paths may be required (DIBNet for contractual
  compliance, FBI for criminal referral)
- External reporting (other): customer notification clauses in specific
  contracts, partner notifications per information-sharing agreements,
  supplier or subcontractor notifications when the incident involves a
  supply-chain element, DoD CIO notifications for certain incident
  classes as directed by contracting officer
- Documentation quality: each case record includes initial detection
  timestamp, triage decisions, containment actions with timestamps,
  eradication and recovery steps, external reports filed with
  confirmation numbers, and final disposition. Assessors look for
  timelines that make sense when read end to end. Gaps in the timeline
  raise questions about what happened during the gap

**Evidence to collect:**
- Case management platform or structured incident ticketing system in
  operation
- Sample incident records showing open and close timestamps, actions
  log, and attribution
- DIBNet reporting account provisioning evidence (medallion
  certificate, account registration confirmation)
- Sample DFARS 252.204-7012 report submission or a tested submission
  path
- Written escalation matrix with severity thresholds and named
  recipients
- Customer and partner notification templates or clause-mapped
  notification procedures
- Retention schedule for incident records (commonly tied to contract
  retention requirements)

**Common mistakes:**
- No DIBNet account established before an incident occurs. Discovering
  the registration and medallion-certificate requirement mid-incident
  burns hours against the 72-hour clock
- Incident tracking via email threads rather than a case-management
  system, which produces no audit trail and no structured timeline
- Undefined escalation path. Each incident re-invents who to call and
  who decides
- No legal or executive loop-in path for incidents with material
  business impact, so the response team makes business-risk decisions
  it is not authorized to make
- DFARS 252.204-7012 reporting treated as optional or best-effort
  rather than a contractual obligation
- Reports filed to DIBNet but no copy or confirmation number preserved
  for assessor review
- Supply-chain notification obligations (to primes, to subs, to
  customers) missed because the external-reporting list was built for
  regulators only

---

### IR.L2-3.6.3 — Incident Response Testing

**Requirement:** Exercise the incident response capability periodically
to confirm the plan works under realistic conditions.

**Why it matters:** A plan that has never been tested will fail the
first time it matters. Tests surface missing contacts, broken
runbooks, tool gaps, and coordination failures while the stakes are
still low.

**Implementation guidance:**
- Test types, from low cost to high cost: tabletop exercises walk the
  team through a scenario in a conference room and exercise
  decision-making and role clarity. Functional tests have the team
  execute runbooks against a simulated incident and validate tools and
  procedures end to end. Full simulation exercises use red-team or
  purple-team engagement with live detection, containment, and
  response for the highest fidelity
- Red-team vs purple-team distinction: a red-team exercise runs
  offensive operations without direct cooperation from the defenders;
  success is measured by whether the attack was detected and stopped.
  A purple-team exercise pairs the red-team with the defenders
  collaboratively; success is measured by which detections fired, which
  did not, and what the team learns about tooling. Purple-team
  exercises deliver more learning per dollar for teams still maturing
  their detection stack
- Cadence: annual as a practical baseline minimum. Additional exercises
  after major plan changes, new tooling deployments, team turnover, or
  as a corrective action after a real incident exposed gaps.
  Organizations with mature programs run smaller tabletop exercises
  quarterly and functional tests semiannually
- Scope: a single exercise should cover detection, containment,
  external reporting, recovery, and user communications. External
  reporting is the most frequently skipped element, which defeats the
  purpose of the exercise because external reporting is the hardest
  part to get right under pressure. Explicitly include a simulated
  DIBNet or DFARS 252.204-7012 report step in at least one exercise
  per year
- Participants: the IR team plus cross-functional stakeholders.
  Network, endpoint, cloud, legal, communications, and executive
  representation should rotate through exercises. Tests that involve
  only the security team miss the coordination failures that matter in
  practice. Supplier or managed-service-provider representation is
  valuable when those parties hold material response responsibilities
- Scenario design: scenarios should vary year over year. Common
  rotation themes include ransomware with backup compromise, insider
  misuse with extended dwell time, supply-chain compromise via a
  shared tool, cloud account takeover via long-lived API keys, and
  phishing leading to business email compromise. Reuse of the same
  scenario converts the exercise from discovery into muscle memory
- After-action: findings tracked to closure in the same case-management
  system used for real incidents. The after-action report should
  capture detection gaps, containment friction, tooling failures,
  communication breakdowns, and recommended plan or runbook changes.
  Plan revisions, runbook updates, and tool configuration changes
  traceable to specific test exercises
- Metrics as test targets: time to detect, time to contain, time to
  recover. Testing against target times surfaces where the bottleneck
  actually is, rather than relying on post-incident impressions

**Evidence to collect:**
- Test schedule covering the current cycle
- Test plans and scenario documents for each exercise
- After-action reports from each exercise
- Participant rosters showing cross-functional participation
- Change log tying plan and runbook updates to specific tests
- Open-finding tracking with closure timestamps
- Metrics reports showing detection, containment, and recovery times
  achieved during exercises compared to targets

**Common mistakes:**
- Tabletop-only testing. Functional tests never attempted, so tool and
  runbook gaps go undetected until a real incident finds them
- Same scenario repeated year after year, converting exercises from
  discovery into muscle memory
- After-action findings documented but never closed
- The IR team exercises alone without network, legal, or executive
  participation
- Testing scheduled but repeatedly deferred. No enforced cadence with
  accountability
- Exercise scope excludes external reporting, leaving DIBNet submission
  untested even after years of tabletop work
- Metrics not measured during exercises, so the team has no
  quantitative baseline to improve against

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 3 | 3 |

**Assessment priority:** Start with IR.L2-3.6.1. Without the plan and
tooling in place, the other two practices are unprovable. Then focus
on IR.L2-3.6.3 (testing) because testing is the evidence that
IR.L2-3.6.1 is real rather than documented. IR.L2-3.6.2 (tracking and
reporting) is straightforward to demonstrate once the case-management
system and DIBNet account are in place, but DIBNet pre-provisioning
should start early because the medallion certificate has lead time.

**Key relationships:**
- IR consumes Audit and Accountability (AU) detection output as the
  primary alert source for incident declaration
- IR coordinates with Configuration Management (CM) during containment
  (pre-approved containment actions) and recovery (restore from
  known-good baselines under change control)
- IR relies on System and Communications Protection (SC) for boundary
  awareness during containment decisions
- IR depends on Identification and Authentication (IA) for account
  lockdown, credential rotation, and session termination during triage
- IR builds on Awareness and Training (AT) to prepare the IR team and
  cross-functional stakeholders for meaningful exercise participation
- IR intersects Media Protection (MP) for evidence handling,
  chain-of-custody, and forensic media management during investigation
