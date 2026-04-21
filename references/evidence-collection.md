# Evidence Collection Patterns

> Source: NIST SP 800-171A (Assessment Procedures), CMMC Assessment Guide,
> publicly available C3PAO preparation guidance

## Overview

Evidence is what proves your controls are implemented, not just documented.
The SSP describes what you do. Evidence proves you actually do it.

Assessors evaluate three things per practice: Is it documented? Is it
implemented? Is it effective? Evidence addresses the second and third
questions. Without it, your SSP is a claim without proof.

---

## Evidence Types

### 1. Configuration Evidence

Screenshots or exports showing system settings match your SSP descriptions.

**Best practices:**
- Include the system name and date in every screenshot
- Capture the full context, not just the single setting. Assessors want
  to see surrounding configuration to verify nothing contradicts the claim
- Export configurations programmatically when possible (CLI output, JSON
  exports, policy exports). These are harder to fabricate and easier to
  version
- Refresh configuration evidence quarterly at minimum. Stale screenshots
  from 18 months ago do not prove current implementation.

### 2. Policy Documents

Written policies that establish the organization's intent and requirements
for each practice domain.

**Best practices:**
- Each CMMC domain should have at least one governing policy
- Policies should be signed or approved by leadership
- Include effective dates and review dates
- Policies without evidence of implementation are insufficient. The policy
  says "we will do X" and the evidence shows "we did X"

### 3. Procedure Documents

Step-by-step instructions for operational controls.

**Best practices:**
- Procedures should be specific enough that a new employee could follow them
- Reference specific tools, systems, and configurations
- Include responsible roles
- Version-control procedures and track changes

### 4. Log Samples

System logs demonstrating controls are active and monitored.

**Best practices:**
- Provide representative samples, not exhaustive dumps
- Include logs from different time periods to show consistency
- Annotate log entries to highlight the relevant evidence
- Show both normal operation (control working) and alert/response
  (control detecting an issue)

### 5. Training Records

Documentation that personnel completed required training.

**Best practices:**
- Include training topic, date, attendee names, and completion status
- Maintain training records for all personnel with CUI access
- Show both initial training (onboarding) and refresher training (annual)
- Include role-specific training where applicable

### 6. Scan Results

Output from vulnerability scans, configuration assessments, or compliance checks.

**Best practices:**
- Include scan date, scope, and tool used
- Show both the findings and the remediation actions taken
- Maintain scan history to demonstrate regular cadence
- Annotate results to show which findings are relevant to which practices

### 7. Process Records

Records showing operational processes are followed consistently.

**Examples:**
- Account provisioning and deprovisioning records
- Change management tickets
- Incident reports and response actions
- Maintenance logs
- Media sanitization records

---

## Evidence by Domain

### Access Control (AC)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| User access management | Account provisioning records, access request forms, periodic access reviews |
| Least privilege | Role-based access control configurations, service account permission audits |
| Remote access | VPN configuration, remote access policy, connection logs |
| Session management | Session timeout settings, screen lock configurations |
| Wireless access | Wireless network configuration, authentication settings, access point inventory |
| Mobile devices | MDM enrollment records, device policy configurations, remote wipe capability |
| External connections | Interconnection agreements, firewall rules for external connections |

### Awareness and Training (AT)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Security awareness | Training materials, completion records, annual refresher dates |
| Role-based training | Specialized training records for IT staff, system administrators, security personnel |
| Insider threat awareness | Insider threat training materials and completion records |

### Audit and Accountability (AU)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Audit logging | SIEM configuration, log source inventory, sample audit logs |
| Log review | Log review procedures, review schedules, sample review reports |
| Log protection | Log storage configuration, access controls on log repositories |
| Log retention | Retention policy, storage configuration showing retention period |
| Audit correlation | SIEM correlation rules, sample alerts, investigation procedures |

### Configuration Management (CM)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Baseline configurations | Documented baselines for each system type, CIS benchmark adoption records |
| Change management | Change management process, recent change tickets, approval records |
| Least functionality | Disabled services list, unnecessary software removal records, port/protocol restrictions |
| Software restrictions | Application allowlisting/denylisting configuration, unauthorized software detection |
| Configuration settings | Security configuration settings exports, GPO or MDM policy screenshots |

### Identification and Authentication (IA)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| User identification | Unique account policy, shared account prohibition evidence |
| Multi-factor authentication | MFA configuration for all remote and privileged access, MFA enrollment records |
| Password policy | Password complexity settings, password expiration configuration |
| Replay-resistant auth | Authentication protocol configuration (Kerberos, SAML, etc.) |
| Account management | Account lifecycle procedures, terminated user deprovisioning records |

### Incident Response (IR)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| IR capability | Incident response plan, POC list, communication procedures |
| IR testing | Test/exercise records, after-action reports, lessons learned |
| IR reporting | Reporting procedures, DoD 72-hour notification process documentation |

**Important:** DFARS 252.204-7012 requires reporting cyber incidents to
DoD within 72 hours. Evidence should show you have a process for this
and have tested it.

### Maintenance (MA)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Controlled maintenance | Maintenance schedules, maintenance logs, approved maintenance personnel list |
| Remote maintenance | Remote maintenance session logs, monitoring records, session termination evidence |
| Maintenance tools | Approved tools list, tool inspection procedures |
| Equipment sanitization | Sanitization procedures for equipment leaving CUI areas |

### Media Protection (MP)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Media protection | Media handling policy, storage location security |
| Media marking | CUI marking procedures, sample marked media |
| Media transport | Transport procedures, encryption of media in transit, courier logs |
| Media sanitization | Sanitization procedures, sanitization records, tool certifications |
| Media disposal | Disposal procedures, disposal records, destruction certificates |

### Personnel Security (PS)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Personnel screening | Background check policy, screening records (redacted as needed) |
| Termination procedures | Termination checklist, access revocation records, equipment return records |

### Physical Protection (PE)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Physical access | Access control systems (badge readers, key logs), visitor procedures |
| Visitor management | Visitor logs, escort procedures, visitor badge processes |
| Monitoring | Security camera placement, alarm system configuration |
| Physical access to equipment | Server room access controls, network closet security |

### Risk Assessment (RA)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Risk assessments | Risk assessment reports, risk register, assessment schedule |
| Vulnerability scanning | Scan schedules, recent scan results, remediation tracking |
| Vulnerability remediation | Remediation timelines, patching records, exception documentation |

### Security Assessment (CA)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Security assessments | Internal assessment schedule, assessment reports, findings tracking |
| SSP | Current SSP with all sections complete (see ssp-guidance.md) |
| POA&M | Current POA&M with milestones and progress (see poam-management.md) |
| Continuous monitoring | Monitoring strategy, automated tool configurations, review cadence |

### System and Communications Protection (SC)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Boundary protection | Firewall rules, network diagrams, DMZ configuration |
| Encryption in transit | TLS/HTTPS configuration, VPN configuration, certificate management |
| Encryption at rest | Disk encryption configuration (BitLocker, FileVault), database encryption settings |
| Network segmentation | VLAN configuration, subnet design, enclave boundary documentation |
| FIPS validation | FIPS 140-2/140-3 module certifications for encryption modules in use |

**Note on FIPS:** The encryption must use FIPS-validated cryptographic
modules. "We use AES-256" is insufficient. The specific implementation
must be validated. Check the NIST Cryptographic Module Validation Program
(CMVP) list at https://csrc.nist.gov/projects/cryptographic-module-validation-program

### System and Information Integrity (SI)

| Practice Area | Evidence to Collect |
|---------------|---------------------|
| Flaw remediation | Patching policy, patch management tool configuration, patching records |
| Malicious code protection | Antivirus/EDR configuration, update schedules, detection logs |
| Security alerts | Alert source subscriptions (CISA, vendor advisories), response procedures |
| System monitoring | Monitoring tool configuration, alert rules, sample alerts and responses |

---

## Evidence Organization

### Folder Structure

Organize evidence by domain for easy retrieval during assessment:

```
evidence/
├── AC-access-control/
│   ├── AC.L2-3.1.1-authorized-access/
│   │   ├── 2026-03-azure-ad-config.png
│   │   ├── 2026-03-access-request-form.pdf
│   │   └── 2026-03-quarterly-access-review.xlsx
│   ├── AC.L2-3.1.2-transaction-control/
│   └── ...
├── AT-awareness-training/
├── AU-audit/
├── ...
└── evidence-index.xlsx
```

### Evidence Index

Maintain a master index mapping each practice to its evidence:

| Practice ID | Evidence File | Type | Date Collected | Status |
|-------------|---------------|------|----------------|--------|
| AC.L2-3.1.1 | azure-ad-config.png | Configuration | 2026-03-15 | Current |
| AC.L2-3.1.1 | access-request-form.pdf | Process | 2026-01-10 | Current |
| AC.L2-3.1.1 | quarterly-access-review.xlsx | Process | 2026-03-30 | Current |

### Evidence Refresh Schedule

| Evidence Type | Refresh Frequency | Trigger |
|---------------|-------------------|---------|
| Configuration screenshots | Quarterly | Also after any configuration change |
| Policy documents | Annually | Also after any policy update |
| Log samples | Quarterly | Collect from different periods |
| Training records | After each training event | Annual training cycle |
| Scan results | Per scan schedule (monthly/quarterly) | After each scan |
| Process records | Ongoing | As processes are executed |

---

## Common Evidence Mistakes

### 1. Undated Screenshots

A screenshot without a date could be from any time. Assessors need to know
the evidence is current.

**Fix:** Include the system clock in screenshots, or add date annotations.
Better yet, use CLI exports with timestamps.

### 2. Evidence That Contradicts the SSP

The SSP says MFA is enabled for all remote access. The VPN configuration
screenshot shows MFA is optional. This is worse than having no evidence.
It actively demonstrates non-compliance.

**Fix:** Update either the SSP or the configuration so they match. Then
collect new evidence.

### 3. Policy Without Implementation Evidence

A beautiful access control policy exists but there is no evidence that
anyone follows it. Policies alone do not satisfy CMMC practices.

**Fix:** For every policy, collect corresponding implementation evidence.
The policy says "accounts are reviewed quarterly." The evidence shows the
last four quarterly reviews with results.

### 4. Stale Evidence

Scan results from 14 months ago. Training records from two years ago.
Configuration screenshots from a system version you no longer run.

**Fix:** Follow the refresh schedule. Evidence older than 12 months is
suspect. Evidence older than the current assessment period is insufficient.

### 5. Missing Periodicity Proof

Many practices require periodic execution (quarterly reviews, monthly
scans, annual training). Evidence from a single instance does not prove
ongoing compliance.

**Fix:** Collect evidence from multiple periods. Show three quarterly
reviews, not one. Show six months of monthly scan results, not one scan.

### 6. No Evidence Index

Evidence exists but is scattered across file shares, email attachments,
and individual machines. When the assessor asks for AC.L2-3.1.5 evidence,
no one can find it quickly.

**Fix:** Build and maintain the evidence index. The five minutes it takes
to log each piece of evidence saves hours during assessment week.
