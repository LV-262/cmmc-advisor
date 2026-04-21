# Configuration Management (CM)

> Source: NIST SP 800-171 Rev 2, Section 3.4; CMMC Assessment Guide Level 2

## Overview

Configuration Management ensures that systems are configured securely,
changes are controlled, and unnecessary functionality is eliminated. This
domain has 9 practices, all at Level 2.

CM is about knowing what your systems look like, keeping them in a known
good state, and controlling how that state changes. Unmanaged
configurations drift toward insecurity — CM prevents that drift.

---

## Level 2 Practices

### CM.L2-3.4.1 — System Baselining

**Requirement:** Establish and maintain baseline configurations and
inventories of organizational systems (including hardware, software,
firmware, and documentation) throughout the respective system development
life cycles.

**Why it matters:** You cannot secure what you do not know exists. A
baseline configuration defines the known-good state. An inventory tells
you what you have. Together, they enable you to detect unauthorized changes
and ensure all systems are configured to your standards.

**Implementation guidance:**
- Create baseline configurations for each system type (workstations,
  servers, network devices, mobile devices)
- Use industry baselines as a starting point: CIS Benchmarks, DISA STIGs,
  or vendor security guides
- Maintain a hardware and software inventory of all in-scope assets
- Version-control baseline configurations so changes are tracked
- Review and update baselines when new threats emerge, software updates
  are released, or system roles change

**Evidence to collect:**
- Documented baseline configurations per system type
- CIS Benchmark or STIG adoption records
- Hardware inventory (make, model, serial, location, classification)
- Software inventory (application, version, license, classification)
- Baseline change history

**Common mistakes:**
- No documented baseline — systems configured ad hoc
- Baseline created once and never updated
- Inventory incomplete (missing mobile devices, cloud resources, or
  network equipment)
- Baseline exists but systems have drifted from it without detection

---

### CM.L2-3.4.2 — Security Configuration Enforcement

**Requirement:** Establish and enforce security configuration settings
for information technology products employed in organizational systems.

**Why it matters:** Default configurations of operating systems,
applications, and network devices are optimized for ease of use, not
security. Security configuration settings harden these defaults to
reduce attack surface.

**Implementation guidance:**
- Apply CIS Benchmarks or DISA STIGs to all in-scope systems
- Enforce configurations through Group Policy (Windows), MDM profiles
  (macOS/mobile), or configuration management tools (Ansible, Chef, etc.)
- Automate configuration compliance checking to detect drift
- Document any deviations from the baseline with justification

**Evidence to collect:**
- Security configuration standard (CIS, STIG, or custom)
- Configuration enforcement mechanism (GPO, MDM, config management tool)
- Compliance scan results showing systems match the baseline
- Deviation documentation with justification for any exceptions

**Common mistakes:**
- Using default configurations without hardening
- Configurations hardened manually but not enforced through automation
- No compliance scanning to detect configuration drift
- Exceptions granted without documentation

---

### CM.L2-3.4.3 — System Change Tracking

**Requirement:** Track, review, approve or disapprove, and log changes
to organizational systems.

**Why it matters:** Uncontrolled changes are the leading cause of security
incidents and system outages. Change management ensures that changes are
reviewed, approved, tested, and documented before implementation.

**Implementation guidance:**
- Implement a change management process covering all in-scope systems
- Require change requests with description, justification, and risk
  assessment
- Require approval from an appropriate authority before implementation
- Log all changes including who made them, when, and what was changed
- Test changes in a non-production environment when feasible

**Evidence to collect:**
- Change management policy and procedures
- Recent change request records with approvals
- Change implementation logs
- Evidence of testing before production changes

**Common mistakes:**
- No change management process — changes made ad hoc
- Process exists but is bypassed for "emergency" changes routinely
- Changes logged but not reviewed or approved before implementation
- No testing before production changes

**Modern IT note:** See
`modern-it/productivity/microsoft-365-gcc.md` and
`modern-it/productivity/google-workspace.md` for feature-rollout
governance on government productivity suites. Tier-level FedRAMP
authorization is stable; feature-level claims (new services, new
Purview modules, new Workspace controls) drift faster and are
tracked via vendor release notes and staged rollouts. The
productivity files' versioning sections flag which claims are
anchor-stable versus feature-date-sensitive.

---

### CM.L2-3.4.4 — Impact Analysis

**Requirement:** Analyze the security impact of changes prior to
implementation.

**Why it matters:** Every change to an in-scope system could affect your
security posture. Impact analysis ensures that security implications are
considered before a change is made, not discovered after.

**Implementation guidance:**
- Include security impact analysis as a required step in the change
  management process
- Evaluate whether the change affects CUI protection, access controls,
  audit logging, or network boundaries
- Determine if the change requires an SSP update
- Involve security personnel in review of significant changes

**Evidence to collect:**
- Security impact analysis in change request records
- Evidence of security review for significant changes
- SSP updates triggered by changes

**Common mistakes:**
- Change management process does not include security impact analysis
- Security team not involved in reviewing changes
- Changes made without considering SSP update requirements

---

### CM.L2-3.4.5 — Access Restrictions for Change

**Requirement:** Define, document, approve, and enforce physical and
logical access restrictions associated with changes to organizational
systems.

**Why it matters:** Not everyone should be able to make changes to
in-scope systems. Restricting change access prevents unauthorized
modifications and ensures only qualified, authorized personnel make
changes.

**Implementation guidance:**
- Restrict system administrator access to authorized personnel only
- Implement separate accounts for change management (admin accounts)
  vs. daily work (standard accounts)
- Restrict physical access to infrastructure where changes are made
  (server rooms, network closets)
- Log all administrative access and changes

**Evidence to collect:**
- Administrative access policy
- Administrative account inventory
- Physical access controls on infrastructure areas
- Administrative access logs

**Common mistakes:**
- Too many people with administrator access
- No separation of admin and regular accounts
- Physical infrastructure accessible without access controls

---

### CM.L2-3.4.6 — Least Functionality

**Requirement:** Employ the principle of least functionality by
configuring organizational systems to provide only essential capabilities.

**Why it matters:** Every unnecessary service, port, protocol, and
application is potential attack surface. Least functionality reduces that
surface to only what is needed for the system's mission.

**Implementation guidance:**
- Disable unnecessary services on all in-scope systems
- Remove or disable unnecessary software and features
- Restrict open network ports to only those required
- Disable unnecessary protocols
- Document the functionality required for each system type and remove
  everything else

**Evidence to collect:**
- Approved services/ports/protocols list per system type
- Configuration showing disabled unnecessary services
- Firewall rules showing restricted ports
- Software removal or disabling records

**Common mistakes:**
- Default services left running (web server on a workstation, FTP on
  a file server that does not use FTP)
- Unnecessary ports open in firewalls
- Software installed "just in case" but not needed

---

### CM.L2-3.4.7 — Nonessential Functionality Restrictions

**Requirement:** Restrict, disable, or prevent the use of nonessential
programs, functions, ports, protocols, and services.

**Why it matters:** This practice reinforces least functionality with
active prevention. It is not enough to not install unnecessary software —
you must actively prevent its use.

**Implementation guidance:**
- Implement application allowlisting or denylisting
- Block unauthorized applications through endpoint protection
- Restrict USB mass storage where not operationally required
- Block unnecessary outbound network connections
- Disable scripting engines not required for operations

**Evidence to collect:**
- Application control policy configuration
- Blocked application or service lists
- USB restriction configuration
- Outbound firewall rules
- Endpoint protection configurations

**Common mistakes:**
- No application control — users can install and run anything
- USB drives unrestricted on all endpoints
- Outbound traffic completely open

---

### CM.L2-3.4.8 — Application Execution Policy

**Requirement:** Apply deny-by-exception (blocklist) policy to prevent
the use of unauthorized software or deny-all, permit-by-exception
(allowlist) policy to allow the execution of authorized software.

**Why it matters:** Controlling which software can execute prevents
malware, unauthorized tools, and unapproved applications from running
on your systems.

**Implementation guidance:**
- Choose an approach:
  - **Allowlist (stronger):** Only explicitly approved software can run.
    Best for tightly controlled environments.
  - **Blocklist (more practical):** All software can run except explicitly
    blocked items. Easier to implement but less secure.
- Implement through OS controls (Windows AppLocker, macOS Gatekeeper),
  endpoint protection, or application control tools
- Maintain the approved/blocked software list
- Review and update the list regularly

**Evidence to collect:**
- Application execution policy document
- Technical implementation (AppLocker, Gatekeeper, or tool configuration)
- Approved/blocked software list
- Review and update records

**Common mistakes:**
- No application control mechanism at all
- Allowlist created but not maintained (new approved software cannot run)
- Blocklist that only covers a few known-bad applications

---

### CM.L2-3.4.9 — User-Installed Software

**Requirement:** Control and monitor user-installed software.

**Why it matters:** Users installing unauthorized software can introduce
vulnerabilities, malware, and unlicensed applications. Controlling
user-installed software maintains the integrity of your baseline
configuration.

**Implementation guidance:**
- Remove local administrator rights from standard users (prevents
  software installation on Windows)
- Use MDM to control software installation on macOS and mobile devices
- Monitor for unauthorized software installation through endpoint
  protection or inventory scanning
- Define a process for users to request software installation

**Evidence to collect:**
- Policy restricting user software installation
- Removal of local admin rights configuration
- MDM software restriction configuration
- Software request and approval process
- Monitoring tool configuration for unauthorized software detection

**Common mistakes:**
- All users have local admin rights (can install anything)
- Policy exists but no technical enforcement
- No monitoring for unauthorized software

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 9 | 9 |

**Assessment priority:** Start with CM.L2-3.4.1 (baselining) — without
a known baseline and asset inventory, all other CM practices lack a
foundation. Then focus on CM.L2-3.4.6 and CM.L2-3.4.7 (least functionality)
because reducing attack surface has immediate security impact.

**Key relationships:**
- CM baselines (CM.L2-3.4.1) inform Security Assessment (CA)
  evaluations, specifically CA.L2-3.12.1 (periodic security
  assessment) which uses the baseline as the evaluation reference
- CM change management (CM.L2-3.4.3) generates Audit (AU) log
  entries captured under AU.L2-3.3.1 (audit log creation)
- CM software restrictions (CM.L2-3.4.8, CM.L2-3.4.9) relate to
  System and Information Integrity (SI) malicious code protection
  at SI.L1-3.14.2 (malicious code protection) and SI.L1-3.14.5
  (periodic and real-time scanning)
- CM configuration enforcement (CM.L2-3.4.2) supports all other
  domains by ensuring systems are in a known-good state
