# Audit and Accountability (AU)

> Source: NIST SP 800-171 Rev 2, Section 3.3; CMMC Assessment Guide Level 2

## Overview

Audit and Accountability ensures that system activities are logged,
protected, reviewed, and retained. This domain has 9 practices, all at
Level 2. No Level 1 audit practices exist — meaning organizations that
only handle FCI (Level 1) have no audit logging requirements, but any
organization handling CUI must implement comprehensive audit capabilities.

Without effective audit logging, you cannot detect unauthorized access,
investigate incidents, or prove to assessors that your other controls
are working.

---

## Level 2 Practices

### AU.L2-3.3.1 — System Audit

**Requirement:** Create and retain system audit logs and records to the
extent needed to enable the monitoring, analysis, investigation, and
reporting of unlawful or unauthorized system activity.

**Why it matters:** Audit logs are your forensic record. Without them,
you cannot detect a breach, investigate how it happened, or prove to
assessors that your controls are operational.

**Implementation guidance:**
- Enable audit logging on all in-scope systems (servers, workstations,
  network devices, cloud services, applications)
- Log at minimum: authentication events, access control decisions,
  account management actions, configuration changes, privileged function
  execution, system events
- Centralize logs in a SIEM or log management platform
- Define retention periods (DFARS 7012 does not specify, but 1 year is
  a common standard; some organizations retain for 3 years)

**Evidence to collect:**
- Audit policy defining what events are logged
- Log source inventory (all systems sending logs)
- SIEM or log management platform configuration
- Sample logs from multiple system types
- Log retention configuration

**Common mistakes:**
- Only logging some systems (workstations log but servers do not)
- No centralized log collection — logs only on individual systems
- Insufficient event types logged (only login events, missing admin actions)

---

### AU.L2-3.3.2 — User Accountability

**Requirement:** Ensure that the actions of individual system users can
be uniquely traced to those users so they can be held accountable for
their actions.

**Why it matters:** If you cannot attribute an action to a specific person,
you cannot hold anyone accountable. This requires unique user IDs (ties
to IA.L1-3.5.1) and audit logs that capture the user identity with each
event.

**Implementation guidance:**
- Ensure all audit log entries include the user identity (unique user ID)
- Prohibit shared accounts — actions under shared accounts cannot be
  attributed to individuals
- Correlate logs across systems using a common user identifier
- Implement user activity monitoring for CUI access

**Evidence to collect:**
- Sample audit logs showing user identification in each entry
- Policy prohibiting shared accounts
- Log correlation configuration in SIEM
- Evidence linking log user IDs to real individuals

**Common mistakes:**
- Shared service accounts used for interactive work
- Logs that record actions but not who performed them
- User IDs in logs that cannot be traced back to named individuals

---

### AU.L2-3.3.3 — Event Review

**Requirement:** Review and update logged events.

**Why it matters:** Logs that exist but are never reviewed provide no
security value. Regular review detects anomalies, policy violations, and
potential incidents. Updating logged events means adjusting what you log
based on experience and changing threats.

**Implementation guidance:**
- Establish a log review schedule (daily for critical systems, weekly
  for others)
- Define what constitutes a reviewable event (failed logins, privilege
  escalation, after-hours access, large data transfers)
- Assign responsibility for log review to specific personnel
- Document review findings and any actions taken
- Periodically assess whether the right events are being logged — add
  new event types as threats evolve

**Evidence to collect:**
- Log review procedures
- Review schedule and assigned reviewers
- Sample review reports with findings and actions
- Records of logging configuration updates

**Common mistakes:**
- Logs collected but never reviewed
- Review assigned but no documented process or findings
- Same logging configuration since initial setup with no updates

---

### AU.L2-3.3.4 — Audit Failure Alerting

**Requirement:** Alert in the event of an audit logging process failure.

**Why it matters:** If logging stops, you lose visibility. An attacker
who can disable logging can operate undetected. Alerting on logging
failures ensures you know immediately when your audit trail is broken.

**Implementation guidance:**
- Configure alerts for: logging service stops, disk space exhaustion
  on log storage, log forwarding failures, SIEM connectivity loss
- Send alerts to security personnel (email, SMS, ticket system)
- Test alerting periodically to verify it works
- Define response procedures for logging failures

**Evidence to collect:**
- Alert configuration for logging failures
- Alert recipient list
- Sample alert notifications
- Test records showing alerts fire correctly
- Response procedures for logging failures

**Common mistakes:**
- No alerting configured — log failures go unnoticed
- Alerts configured but sent to an unmonitored mailbox
- Log storage fills up silently, overwriting oldest logs

---

### AU.L2-3.3.5 — Audit Correlation

**Requirement:** Correlate audit record review, analysis, and reporting
processes for investigation and response to indications of unlawful,
unauthorized, suspicious, or unusual activity.

**Why it matters:** A single log source rarely tells the full story.
Correlating logs across systems (network + endpoint + authentication +
application) reveals attack chains and incident scope that individual
logs cannot.

**Implementation guidance:**
- Use a SIEM platform to correlate logs across sources
- Synchronize time across all systems (NTP) — logs with different
  timestamps cannot be correlated accurately
- Create correlation rules for common attack patterns
- Maintain the ability to query historical logs for investigations

**Evidence to collect:**
- SIEM configuration showing multiple log sources
- NTP configuration across all systems
- Correlation rules documentation
- Sample correlated event investigation

**Common mistakes:**
- Logs collected centrally but no correlation rules defined
- Time not synchronized — logs are seconds or minutes apart, making
  correlation unreliable
- Historical logs not searchable (archived to cold storage without
  query capability)

---

### AU.L2-3.3.6 — Audit Reduction and Reporting

**Requirement:** Provide audit record reduction and report generation to
support on-demand analysis and reporting.

**Why it matters:** Raw logs are too voluminous for manual review. Audit
reduction (filtering, summarizing, aggregating) and reporting tools make
logs actionable for both routine review and incident investigation.

**Implementation guidance:**
- Configure SIEM dashboards for routine monitoring
- Create reports for common review needs (daily login summary, weekly
  admin action report, monthly access review)
- Enable ad-hoc query capability for investigations
- Define standard reports for management and compliance reporting

**Evidence to collect:**
- SIEM dashboard screenshots
- Sample standard reports
- Evidence of ad-hoc query capability
- Report distribution records

**Common mistakes:**
- Raw logs only — no dashboards, reports, or summarization
- Reports generated but never reviewed
- No ability to perform ad-hoc queries when an incident occurs

---

### AU.L2-3.3.7 — Authoritative Time Source

**Requirement:** Provide a system capability that compares and
synchronizes internal system clocks with an authoritative source to
generate time stamps for audit records.

**Why it matters:** Accurate timestamps are essential for log correlation,
incident investigation, and legal admissibility. If system clocks are not
synchronized, logs from different systems cannot be correlated.

**Implementation guidance:**
- Configure all in-scope systems to synchronize with an authoritative
  NTP source (e.g., time.nist.gov, pool.ntp.org, or organizational
  NTP server)
- Verify time synchronization is active on all system types (servers,
  workstations, network devices, cloud services)
- Monitor for time drift and alert on synchronization failures
- Document the authoritative time source

**Evidence to collect:**
- NTP configuration per system type
- Time synchronization status showing current sync
- Authoritative time source documentation
- Time drift monitoring configuration

**Common mistakes:**
- Not all systems configured for NTP (common with network devices)
- Using inconsistent time sources across different system types
- No monitoring for time synchronization failures
- Virtual machines drifting from host time

---

### AU.L2-3.3.8 — Audit Protection

**Requirement:** Protect audit information and audit logging tools from
unauthorized access, modification, and deletion.

**Why it matters:** If an attacker can modify or delete logs, they can
cover their tracks. Audit logs must be protected with the same rigor as
the CUI they document.

**Implementation guidance:**
- Restrict access to log repositories to authorized security personnel only
- Implement write-once or append-only storage for audit logs where possible
- Encrypt logs in transit (to SIEM) and at rest (in storage)
- Separate log storage from the systems being monitored — a compromised
  server should not have access to its own log repository
- Back up audit logs

**Evidence to collect:**
- Access control configuration on log repositories
- Log storage architecture showing separation from monitored systems
- Encryption configuration for logs in transit and at rest
- Backup configuration for audit logs
- Access logs showing who accessed the log repository

**Common mistakes:**
- Logs stored on the same system they monitor (attacker compromises
  system, deletes local logs)
- All IT staff can access and modify logs
- No encryption on log storage or transmission
- Logs not backed up

---

### AU.L2-3.3.9 — Audit Management

**Requirement:** Limit management of audit logging functionality to a
subset of privileged users.

**Why it matters:** The ability to configure, disable, or modify audit
logging should be restricted to a small group of trusted personnel.
If any administrator can disable logging, the audit trail is only as
trustworthy as your least trustworthy administrator.

**Implementation guidance:**
- Define which roles can manage audit logging (typically security team
  only, not general IT administrators)
- Restrict access to SIEM administrative functions
- Restrict access to logging configurations on endpoints and servers
- Log all changes to audit logging configuration (audit the auditors)

**Evidence to collect:**
- Audit logging management role assignments
- SIEM administrative access configuration
- Evidence that logging configuration changes are logged
- Access control list for audit management functions

**Common mistakes:**
- All IT administrators can disable logging
- No logging of changes to logging configuration
- SIEM admin access shared broadly across IT staff

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 9 | 9 |

**Assessment priority:** Start with AU.L2-3.3.1 (system audit) and
AU.L2-3.3.7 (time source). If logs do not exist or timestamps are
inconsistent, every other audit practice is undermined. Then focus on
AU.L2-3.3.8 (audit protection) — logs that can be tampered with are
not trustworthy.

**Key relationships:**
- AU depends on Identification and Authentication (IA) for user
  attribution in log entries
- AU supports Access Control (AC) by logging access decisions
- AU supports Incident Response (IR) by providing investigation data
- AU log protection relates to System and Communications Protection (SC)
  encryption
- FedRAMP inheritance: the FedRAMP Moderate AU baseline covers NIST
  SP 800-53 controls AU-2, AU-3, AU-6, AU-11, and AU-12, and the
  cloud service provider (CSP) runs a continuous monitoring program
  with monthly vuln scanning, monthly Plan of Action and Milestones
  (POA&M) upload, and annual Third-Party Assessment Organization
  (3PAO) subset assessment. See `references/fedramp-gap.md`
  "Audit and accountability" family deep-dive and "Continuous
  monitoring cadence"
