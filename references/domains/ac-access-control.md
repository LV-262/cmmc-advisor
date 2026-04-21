# Access Control (AC)

> Source: NIST SP 800-171 Rev 2, Section 3.1; CMMC Assessment Guide Level 2

## Overview

Access Control is the largest CMMC domain with 22 practices — 4 at Level 1
and 18 additional at Level 2. This domain governs who and what can access
your systems and CUI, and under what conditions.

Access Control failures are among the most commonly cited findings in
assessments because the domain touches every system, every user, and every
connection in your environment.

---

## Level 1 Practices (Basic)

These 4 practices apply to all CMMC levels and represent fundamental
access control capabilities.

### AC.L1-3.1.1 — Authorized Access Control

**Requirement:** Limit system access to authorized users, processes acting
on behalf of authorized users, and devices (including other systems).

**Why it matters:** This is the foundational access control principle —
only authorized entities should access your systems. Without this, no
other control is meaningful.

**Implementation guidance:**
- Maintain an authoritative list of authorized users for each system
- Implement an account provisioning process tied to HR onboarding
- Use a centralized identity provider (Azure AD, Okta, Google Workspace
  identity) as the single source of truth for user authorization
- Enforce authentication on all system access — no anonymous or guest
  access to systems containing FCI or CUI

**Evidence to collect:**
- Account management policy
- Current user account list per system
- Account provisioning procedure
- Identity provider configuration showing authentication requirements

**Common mistakes:**
- Shared accounts (multiple users using one login)
- Orphaned accounts (former employees still active)
- Service accounts with no documented owner
- Systems accessible without authentication

---

### AC.L1-3.1.2 — Transaction and Function Control

**Requirement:** Limit system access to the types of transactions and
functions that authorized users are permitted to execute.

**Why it matters:** Even authorized users should only do what they need
to do. An HR employee should not have database admin access. A developer
should not approve their own code deployments.

**Implementation guidance:**
- Implement role-based access control (RBAC) with defined roles per system
- Document which roles can perform which functions
- Restrict administrative functions to designated administrator accounts
- Use separate accounts for administrative and regular work

**Evidence to collect:**
- RBAC role definitions per system
- User-to-role assignments
- Administrative access restrictions configuration
- Evidence of separation between admin and regular accounts

**Common mistakes:**
- All users having the same access level
- Roles that are too broad (one "admin" role for everything)
- No documentation of what each role can do

---

### AC.L1-3.1.20 — External System Connections

**Requirement:** Verify and control/limit connections to and use of
external systems.

**Why it matters:** Every connection to an external system is a potential
path for CUI to leave your boundary or for threats to enter it. You need
to know what external connections exist and control them.

**Implementation guidance:**
- Inventory all connections to external systems (SaaS tools, APIs,
  partner portals, cloud services)
- Establish terms and conditions for each external connection
- Implement technical controls limiting data transfer to external systems
- Review external connections periodically

**Evidence to collect:**
- External system connection inventory
- Terms of use or interconnection agreements
- Firewall rules controlling external connections
- Periodic review records

**Common mistakes:**
- Shadow IT — users connecting to unapproved external services
- No inventory of external connections
- Assuming cloud services are "internal" when they are external systems

---

### AC.L1-3.1.22 — Publicly Accessible Content

**Requirement:** Control CUI posted or processed on publicly
accessible systems.

**Why it matters:** CUI must never be posted on publicly accessible
systems. This practice ensures someone reviews content before it goes
public and that CUI is removed if accidentally posted.

**Implementation guidance:**
- Designate individuals authorized to post information publicly
- Review content before public posting for CUI or sensitive information
- Implement a process to identify and remove CUI from public systems
  if accidentally posted
- Train authorized individuals on CUI identification

**Evidence to collect:**
- Public posting authorization policy
- Content review procedures
- List of authorized individuals
- Records of content reviews

**Common mistakes:**
- No review process before posting to public websites
- CUI inadvertently included in public documentation
- No process to detect and remove CUI from public-facing systems

---

## Level 2 Practices (Derived)

These 18 practices apply at CMMC Level 2 and above.

### AC.L2-3.1.3 — CUI Flow Control

**Requirement:** Control the flow of CUI in accordance with approved
authorizations.

**Why it matters:** CUI must only flow through approved paths. This
prevents CUI from leaking outside your boundary through unapproved
channels (personal email, unapproved cloud storage, unauthorized file
transfers).

**Implementation guidance:**
- Document approved CUI flow paths (data flow diagram)
- Implement DLP (Data Loss Prevention) policies to detect CUI in
  unapproved channels
- Configure email rules to flag or block CUI sent to external addresses
- Restrict file sharing to approved collaboration tools within your
  CUI boundary

**Evidence to collect:**
- Data flow diagram showing approved CUI paths
- DLP policy configuration
- Email filtering rules
- File sharing restrictions

**Common mistakes:**
- No data flow diagram
- CUI flowing through personal email
- No DLP or technical controls — relying on policy alone

---

### AC.L2-3.1.4 — Separation of Duties

**Requirement:** Separate the duties of individuals to reduce the risk
of malevolent activity without collusion.

**Why it matters:** No single individual should have enough access to
compromise CUI without another person being involved. This prevents both
insider threats and accidental damage.

**Implementation guidance:**
- Identify critical functions that require separation (e.g., requesting
  access vs. approving access, writing code vs. deploying code)
- Ensure no single individual can both make a change and approve it
- Document separation of duties in your access control policy
- For small organizations: document compensating controls where true
  separation is not feasible (e.g., enhanced logging and review)

**Evidence to collect:**
- Separation of duties matrix
- Approval workflows showing different individuals
- Compensating control documentation (if applicable)

**Common mistakes:**
- One person approving their own access requests
- Small teams assuming separation doesn't apply to them — it does,
  but compensating controls are acceptable when documented

---

### AC.L2-3.1.5 — Least Privilege

**Requirement:** Employ the principle of least privilege, including for
specific security functions and privileged accounts.

**Why it matters:** Users should have only the minimum access necessary
to perform their job. Excessive privileges increase the blast radius of
any compromise.

**Implementation guidance:**
- Audit current user permissions against job requirements
- Remove unnecessary administrative access
- Use separate privileged accounts for administrative functions
- Implement just-in-time (JIT) access for elevated privileges when possible
- Review privileged access quarterly

**Evidence to collect:**
- Privileged account inventory
- Quarterly access reviews with results
- JIT access configuration (if used)
- Evidence of permission reduction actions

**Common mistakes:**
- Everyone is a local admin on their workstation
- Service accounts with domain admin privileges
- No regular review of privileged access

---

### AC.L2-3.1.6 — Non-Privileged Account Use

**Requirement:** Use non-privileged accounts or roles when accessing
nonsecurity functions.

**Why it matters:** Administrators should use regular accounts for email,
web browsing, and other daily activities — not their admin accounts. This
limits exposure if a daily-use account is compromised.

**Implementation guidance:**
- Require separate accounts for administrative and non-administrative work
- Enforce that admin accounts cannot access email or browse the internet
- Technical controls preventing admin accounts from non-admin functions

**Evidence to collect:**
- Admin account policy requiring separate accounts
- Configuration showing admin account restrictions
- Evidence of separate admin vs. regular accounts for IT staff

**Common mistakes:**
- IT staff using their admin account for everything
- Admin accounts with email access

---

### AC.L2-3.1.7 — Privileged Function Logging

**Requirement:** Prevent non-privileged users from executing privileged
functions and capture the execution of such functions in audit logs.

**Why it matters:** Privileged functions (installing software, changing
system configurations, managing accounts) must be restricted and logged.
This creates accountability and detects unauthorized elevation.

**Implementation guidance:**
- Configure OS and application permissions to prevent non-privileged
  execution of privileged functions
- Enable audit logging for all privileged function execution
- Forward privileged function logs to SIEM for monitoring
- Alert on unexpected privileged function execution

**Evidence to collect:**
- OS permission configurations (Group Policy, MDM profiles)
- Audit log configuration showing privileged function logging
- SIEM alert rules for unexpected privileged actions
- Sample audit logs showing captured privileged function execution

**Common mistakes:**
- Privileged functions not logged
- Logs generated but not monitored
- Users able to elevate privileges without authorization

---

### AC.L2-3.1.8 — Unsuccessful Logon Attempts

**Requirement:** Limit unsuccessful logon attempts.

**Why it matters:** Account lockout after repeated failed attempts
prevents brute-force password attacks.

**Implementation guidance:**
- Configure account lockout after a defined number of failed attempts
  (typically 3-5 attempts)
- Set a lockout duration or require administrator unlock
- Log all failed login attempts
- Consider implementing progressive delays between attempts

**Evidence to collect:**
- Account lockout policy configuration
- OS or identity provider lockout settings screenshot
- Sample failed login logs

**Common mistakes:**
- No lockout configured
- Lockout threshold too high (e.g., 100 attempts)
- Failed login attempts not logged

---

### AC.L2-3.1.9 — Privacy and Security Notices

**Requirement:** Provide privacy and security notices consistent with
applicable CUI rules.

**Why it matters:** Users must be informed about system monitoring, data
handling, and acceptable use before they access the system. This provides
legal standing for monitoring and sets user expectations.

**Implementation guidance:**
- Display login banners on all systems containing CUI
- Include notice of monitoring, acceptable use, and CUI handling
  requirements
- Obtain user acknowledgment of the notice (interactive consent)
- Update notices when CUI handling rules change

**Evidence to collect:**
- Login banner text
- Banner configuration screenshots per system type
- User acknowledgment records

**Common mistakes:**
- No login banner configured
- Banner text that does not address CUI-specific requirements
- Banner only on some systems, not all in-scope systems

---

### AC.L2-3.1.10 — Session Lock

**Requirement:** Use session lock with pattern-hiding displays to prevent
access and viewing of data after a period of inactivity.

**Why it matters:** Unattended workstations with CUI visible on screen
are a physical security risk. Session lock ensures the screen is protected
after inactivity.

**Implementation guidance:**
- Configure automatic screen lock after 15 minutes of inactivity
  (or less per organizational policy)
- Require password/PIN/biometric to unlock
- Ensure lock applies to all in-scope endpoints (workstations, laptops,
  VDI sessions)
- Pattern-hiding means the lock screen must not display CUI

**Evidence to collect:**
- Screen lock policy (Group Policy, MDM profile)
- Configuration screenshots showing timeout settings
- Evidence of enforcement across all endpoint types

**Common mistakes:**
- Timeout set too long (30+ minutes)
- Lock not configured on all device types
- Users disabling screen lock on their devices

---

### AC.L2-3.1.11 — Session Termination

**Requirement:** Terminate (automatically) a user session after a
defined condition.

**Why it matters:** Idle sessions represent risk. Automatic termination
ensures abandoned sessions do not remain active indefinitely.

**Implementation guidance:**
- Define session termination conditions (time-based, inactivity-based)
- Configure automatic session termination for remote access sessions
- Implement termination for VDI sessions, VPN sessions, and web
  application sessions
- Document exceptions and justification for longer session times

**Evidence to collect:**
- Session termination policy
- VPN timeout configuration
- Web application session timeout settings
- Remote desktop timeout configuration

**Common mistakes:**
- VPN sessions that never time out
- Web applications with indefinite sessions
- Inconsistent timeout policies across systems

---

### AC.L2-3.1.12 — Remote Access Monitoring

**Requirement:** Monitor and control remote access sessions.

**Why it matters:** Remote access is the most common entry point for
threats. Every remote session should be monitored, logged, and subject
to control.

**Implementation guidance:**
- Log all remote access connections (VPN, RDP, SSH, VDI)
- Monitor remote sessions for anomalies (unusual times, locations, durations)
- Implement ability to terminate remote sessions
- Review remote access logs regularly

**Evidence to collect:**
- Remote access logging configuration
- Sample remote access logs
- Monitoring procedures and review schedule
- Evidence of session termination capability

**Common mistakes:**
- Remote access not logged
- Logs exist but no one reviews them
- No ability to terminate suspicious sessions

---

### AC.L2-3.1.13 — Remote Access Encryption

**Requirement:** Employ cryptographic mechanisms to protect the
confidentiality of remote access sessions.

**Why it matters:** Remote access sessions traverse networks you do
not control. Encryption prevents interception of CUI during transit.

**Implementation guidance:**
- Require encrypted VPN for all remote access to CUI systems
- Use TLS 1.2 or higher for web-based remote access
- Ensure encryption uses FIPS-validated cryptographic modules
- Prohibit unencrypted remote access protocols

**Evidence to collect:**
- VPN encryption configuration (protocol, cipher suite)
- TLS configuration for web applications
- FIPS validation certificates for encryption modules
- Policy prohibiting unencrypted remote access

**Common mistakes:**
- VPN configured but using weak encryption
- TLS 1.0/1.1 still enabled
- Encryption not FIPS-validated

---

### AC.L2-3.1.14 — Remote Access Routing

**Requirement:** Route remote access via managed access control points.

**Why it matters:** All remote access should pass through a controlled
entry point where it can be authenticated, authorized, monitored, and
logged. Direct remote access to individual systems bypasses these controls.

**Implementation guidance:**
- Route all remote access through VPN concentrators or VDI gateways
- Prohibit direct RDP, SSH, or other remote access from the internet
- Configure firewall rules to enforce routing through access control points
- Document all approved remote access paths

**Evidence to collect:**
- Network diagram showing remote access flow through managed points
- Firewall rules blocking direct remote access
- VPN or VDI gateway configuration
- Policy requiring managed access points

**Common mistakes:**
- RDP exposed directly to the internet
- Multiple unapproved remote access paths
- No centralized remote access gateway

---

### AC.L2-3.1.15 — Privileged Remote Access

**Requirement:** Authorize remote execution of privileged commands and
remote access to security-relevant information.

**Why it matters:** Privileged commands executed remotely carry higher
risk. Authorization ensures only approved personnel perform administrative
actions remotely, and those actions are explicitly permitted.

**Implementation guidance:**
- Define which privileged commands may be executed remotely
- Require explicit authorization for remote privileged access
- Log all remote privileged command execution
- Implement MFA for all remote privileged access

**Evidence to collect:**
- Remote privileged access authorization policy
- List of approved remote privileged commands
- MFA configuration for privileged remote access
- Audit logs of remote privileged command execution

**Common mistakes:**
- No distinction between remote privileged and non-privileged access
- Privileged remote access without MFA
- No logging of remote privileged commands

---

### AC.L2-3.1.16 — Wireless Access Authorization

**Requirement:** Authorize wireless access prior to allowing such
connections.

**Why it matters:** Wireless networks extend your attack surface beyond
your physical boundary. Only authorized wireless connections should be
permitted within the CUI environment.

**Implementation guidance:**
- Require authorization before granting wireless network access
- Implement 802.1X or certificate-based wireless authentication
- Maintain a list of authorized wireless devices
- Separate guest wireless from CUI wireless networks

**Evidence to collect:**
- Wireless access authorization policy
- Wireless authentication configuration (802.1X, WPA3-Enterprise)
- Authorized wireless device inventory
- Network diagram showing wireless network separation

**Common mistakes:**
- Shared wireless passwords (PSK) for CUI network
- No separation between guest and CUI wireless
- No authorization process for wireless device enrollment

---

### AC.L2-3.1.17 — Wireless Access Protection

**Requirement:** Protect wireless access using authentication and
encryption.

**Why it matters:** Wireless traffic is inherently interceptable.
Authentication prevents unauthorized connections and encryption prevents
eavesdropping.

**Implementation guidance:**
- Use WPA3-Enterprise or WPA2-Enterprise (minimum)
- Implement 802.1X with certificate or RADIUS authentication
- Use AES encryption for all wireless traffic
- Disable WEP and WPA (legacy protocols)
- Monitor for rogue access points

**Evidence to collect:**
- Wireless encryption configuration (WPA3/WPA2-Enterprise)
- Authentication method configuration (802.1X)
- Rogue AP detection configuration
- Evidence that legacy protocols are disabled

**Common mistakes:**
- Using WPA2-Personal (shared passwords) instead of Enterprise
- Legacy protocols still enabled
- No rogue access point monitoring

---

### AC.L2-3.1.18 — Mobile Device Connection

**Requirement:** Control connection of mobile devices.

**Why it matters:** Mobile devices (phones, tablets) connecting to CUI
systems introduce risk — they can be lost, stolen, or compromised. Their
connections must be controlled.

**Implementation guidance:**
- Implement Mobile Device Management (MDM) for all devices accessing
  CUI systems
- Require device enrollment and compliance checks before granting access
- Enforce security policies on mobile devices (passcode, encryption,
  screen lock)
- Implement remote wipe capability for lost or stolen devices

**Evidence to collect:**
- MDM enrollment policy
- Device compliance policies (passcode, encryption requirements)
- MDM configuration screenshots
- Remote wipe capability demonstration
- Mobile device inventory

**Modern IT note:** See `modern-it/endpoints/macos-fleet.md` for
macOS-specific MDM guidance.

**Common mistakes:**
- Personal phones accessing CUI with no MDM
- No remote wipe capability
- No policy governing mobile device use with CUI

---

### AC.L2-3.1.19 — Mobile Device Encryption

**Requirement:** Encrypt CUI on mobile devices and mobile computing
platforms.

**Why it matters:** Mobile devices are easily lost or stolen. Encryption
ensures CUI remains protected even if the physical device is compromised.

**Implementation guidance:**
- Enable full-device encryption on all mobile devices accessing CUI
  (FileVault on macOS, BitLocker on Windows, device encryption on
  iOS/Android)
- Verify encryption uses FIPS-validated modules where required
- Enforce encryption through MDM policy
- Prohibit CUI storage on devices without encryption

**Evidence to collect:**
- MDM encryption policy configuration
- Device encryption status reports
- FIPS validation status of encryption modules
- Policy prohibiting CUI on unencrypted devices

**Common mistakes:**
- Assuming all devices are encrypted by default — verify
- Encryption enabled but not enforced through MDM
- No verification that encryption modules are FIPS-validated

---

### AC.L2-3.1.21 — Portable Storage on External Systems

**Requirement:** Limit use of portable storage devices on external
systems.

**Why it matters:** USB drives and other portable storage moving between
your CUI environment and external systems create data leakage and malware
introduction risks.

**Implementation guidance:**
- Restrict or prohibit use of organizational USB drives on non-CUI systems
- Implement USB device control policies through endpoint management
- Encrypt all portable storage devices
- Log USB device connections

**Evidence to collect:**
- Portable storage policy
- USB device control configuration (GPO, MDM)
- Encryption enforcement for portable storage
- USB connection logs

**Common mistakes:**
- No USB device control — anyone can plug in any drive
- Policy exists but no technical enforcement
- USB drives used freely between CUI and personal systems

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 4 | 18 | 22 |

**Assessment priority:** Access Control is the most practice-heavy domain
and touches every system in scope. Start your assessment preparation here
because findings in AC often cascade into other domains (Audit, IA, SC).

**Key relationships:**
- AC practices depend on Identification and Authentication (IA) for
  user verification; specifically IA.L1-3.5.1 (identify users) and
  IA.L1-3.5.2 (authenticate users) are prerequisites for AC.L1-3.1.1
  and AC.L1-3.1.2
- AC practices generate evidence relevant to Audit and Accountability
  (AU), notably AU.L2-3.3.1 (audit log creation) and AU.L2-3.3.2
  (user traceability), which depend on AC to know who is logged in
- Remote access AC practices (AC.L2-3.1.12 through AC.L2-3.1.15)
  relate to System and Communications Protection (SC) encryption
  requirements, specifically SC.L2-3.13.8 (transmission
  confidentiality) and SC.L2-3.13.11 (FIPS-validated cryptography)
- FedRAMP inheritance: AC.L1-3.1.1, AC.L1-3.1.2, and the L2 AC
  practices overlap with FedRAMP Moderate AC-2, AC-3, and AC-17.
  See `references/fedramp-gap.md` "Access control" family deep-dive
  under "Where the mapping is tightest" for the inheritance
  pattern and the break-glass-account gap
- AC.L1-3.1.20 (external system connections) is anchored in DFARS
  252.204-7012(b)(2)(ii)(D) when the external system is a cloud
  service holding CUI. See `references/fedramp-gap.md` "The CUI
  Baseline Decision"
