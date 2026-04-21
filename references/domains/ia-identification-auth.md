# Identification and Authentication (IA)

> Source: NIST SP 800-171 Rev 2, Section 3.5; CMMC Assessment Guide Level 2

## Overview

Identification and Authentication ensures that users, processes, and
devices are who they claim to be before they are granted access. This
domain has 11 practices — 2 at Level 1 and 9 additional at Level 2.

IA is the gatekeeper that makes Access Control work. Without reliable
identification and authentication, access control policies cannot be
enforced because you cannot verify who is requesting access.

---

## Level 1 Practices (Basic)

### IA.L1-3.5.1 — Identification

**Requirement:** Identify system users, processes acting on behalf
of users, and devices.

**Why it matters:** Every entity accessing your system must have a unique
identity. Without unique identification, you cannot attribute actions to
individuals, which undermines accountability and audit.

**Implementation guidance:**
- Assign unique user IDs to every individual
- Prohibit shared accounts — each person gets their own credentials
- Identify service accounts and document their purpose and owner
- Identify devices through certificates, MAC addresses, or device
  management enrollment

**Evidence to collect:**
- User account policy requiring unique identification
- Active user account list showing unique IDs
- Service account inventory with documented owners
- Device identification method documentation

**Common mistakes:**
- Shared accounts ("admin", "lab-user", "reception")
- Service accounts with no documented owner
- No device identification scheme

---

### IA.L1-3.5.2 — Authentication

**Requirement:** Authenticate (or verify) the identities of users,
processes, or devices, as a prerequisite to allowing access to
organizational systems.

**Why it matters:** Identification says who you claim to be. Authentication
proves it. Without authentication, anyone can claim any identity.

**Implementation guidance:**
- Require password or stronger authentication for all user access
- Implement multi-factor authentication (MFA) for remote and privileged
  access (required at Level 2 — see IA.L2-3.5.3)
- Authenticate devices through certificates or MDM enrollment
- Authenticate service-to-service connections through API keys,
  certificates, or managed identities

**Evidence to collect:**
- Authentication policy
- Authentication method configuration per system
- Evidence that all access requires authentication
- Device authentication configuration

**Common mistakes:**
- Systems accessible without authentication
- Default credentials still in use
- Authentication bypassed for "convenience"

---

## Level 2 Practices (Derived)

### IA.L2-3.5.3 — Multi-Factor Authentication

**Requirement:** Use multifactor authentication for local and network
access to privileged accounts and for network access to non-privileged
accounts.

**Why it matters:** Passwords alone are insufficient. MFA significantly
reduces the risk of account compromise from phishing, credential theft,
and brute-force attacks. This is one of the highest-impact practices
you can implement.

**Implementation guidance:**
- Enable MFA for **all** remote/network access to CUI systems
- Enable MFA for **all** privileged account access (local and remote)
- Acceptable MFA factors: something you know (password) + something you
  have (hardware token, authenticator app, smart card) or something you
  are (biometric)
- SMS-based OTP is discouraged by NIST but not explicitly prohibited in
  800-171r2. Prefer authenticator apps or hardware tokens.
- Integrate MFA with your identity provider for centralized enforcement

**Evidence to collect:**
- MFA policy
- MFA configuration in identity provider
- MFA enrollment records showing all users enrolled
- Evidence of MFA enforcement (conditional access policies)
- MFA method documentation (which factors are used)

**Common mistakes:**
- MFA enabled but not enforced (users can opt out)
- MFA only for remote access, not for privileged local access
- Relying on SMS OTP when stronger options are available
- MFA configured but exceptions exist for certain accounts

---

### IA.L2-3.5.4 — Replay-Resistant Authentication

**Requirement:** Employ replay-resistant authentication mechanisms for
network access to privileged and non-privileged accounts.

**Why it matters:** Replay attacks capture valid authentication tokens
and reuse them to gain unauthorized access. Replay-resistant mechanisms
prevent this by ensuring each authentication attempt is unique.

**Implementation guidance:**
- Use authentication protocols that include replay protection: Kerberos,
  TLS mutual authentication, SAML with time-bounded assertions, OAuth
  with short-lived tokens
- Disable legacy authentication protocols that lack replay resistance
  (NTLM where possible, basic HTTP authentication)
- Configure token expiration and session management

**Evidence to collect:**
- Authentication protocol documentation per system
- Configuration showing replay-resistant protocols in use
- Evidence that legacy protocols are disabled or restricted
- Token expiration settings

**Common mistakes:**
- NTLM still enabled and in use
- Basic authentication enabled on web applications
- Long-lived tokens without expiration

---

### IA.L2-3.5.5 — Identifier Reuse Prevention

**Requirement:** Prevent reuse of identifiers for a defined period.

**Why it matters:** Reusing a former employee's username for a new
employee creates confusion in audit logs and may grant unintended access
if residual permissions exist.

**Implementation guidance:**
- Define a period during which identifiers cannot be reused (e.g., 1 year)
- Implement identifier lifecycle management in your identity provider
- Document the identifier reuse prevention policy
- Maintain historical records of identifier assignments

**Evidence to collect:**
- Identifier management policy with reuse prevention period
- Identity provider configuration showing reuse prevention
- Historical identifier assignment records

**Common mistakes:**
- Reassigning usernames immediately after termination
- No policy defining the reuse prevention period
- No historical record of who had which identifier

---

### IA.L2-3.5.6 — Identifier Disabling

**Requirement:** Disable identifiers after a defined period of inactivity.

**Why it matters:** Inactive accounts (employees on extended leave,
contractors whose projects ended, service accounts for decommissioned
systems) remain attack targets. Disabling them reduces the attack surface.

**Implementation guidance:**
- Define an inactivity threshold (typically 90 days)
- Configure automatic account disabling after the threshold
- Review disabled accounts periodically for permanent removal
- Exclude service accounts from automatic disabling but review them
  separately on a defined schedule

**Evidence to collect:**
- Account inactivity policy with defined threshold
- Identity provider configuration for automatic disabling
- Reports showing disabled inactive accounts
- Service account review schedule and records

**Common mistakes:**
- No automatic disabling — inactive accounts accumulate
- Threshold too long (365+ days)
- Service accounts exempt with no alternative review process

---

### IA.L2-3.5.7 — Password Complexity

**Requirement:** Enforce a minimum password complexity and change of
characters when new passwords are created.

**Why it matters:** Weak passwords are trivially compromised. Complexity
requirements increase the effort required for brute-force and dictionary
attacks.

**Implementation guidance:**
- Enforce minimum length (12+ characters recommended by current NIST
  guidance in SP 800-63B)
- Require a mix of character types or enforce minimum length with
  passphrase option
- Screen passwords against known compromised password lists
- Do not require periodic password changes unless there is evidence of
  compromise (aligned with NIST SP 800-63B recommendation)

**Evidence to collect:**
- Password policy document
- Identity provider password configuration screenshot
- Evidence of compromised password screening (if implemented)
- Password complexity settings per system

**Common mistakes:**
- Minimum length too short (8 characters or fewer)
- Requiring periodic rotation without evidence-based justification
- No screening against known compromised passwords
- Different password policies across different systems

---

### IA.L2-3.5.8 — Password Reuse Prevention

**Requirement:** Prohibit password reuse for a specified number of
generations.

**Why it matters:** If users can immediately reuse old passwords, password
change requirements become meaningless — they cycle through a short list
and return to their favorite.

**Implementation guidance:**
- Configure password history to remember at least the last 12 passwords
- Enforce minimum password age to prevent rapid cycling
- Implement across all authentication systems (OS, applications, cloud
  identity providers)

**Evidence to collect:**
- Password history configuration (number of remembered passwords)
- Minimum password age configuration
- Settings shown across all relevant authentication systems

**Common mistakes:**
- Password history set to 1-3 (trivially circumvented)
- No minimum password age (allows rapid cycling to exhaust history)
- Password history enforced on domain but not on application logins

---

### IA.L2-3.5.9 — Temporary Passwords

**Requirement:** Allow temporary password use for system logons with an
immediate change to a permanent password.

**Why it matters:** Temporary passwords used during account provisioning
or password resets must be changed immediately. Leaving temporary passwords
active creates a known-credential risk.

**Implementation guidance:**
- Configure identity systems to force password change at first login
  when temporary passwords are issued
- Set temporary passwords to expire within a short window (e.g., 24 hours)
- Use unique temporary passwords per user — never a shared default
- Transmit temporary passwords through a secure channel separate from
  the username

**Evidence to collect:**
- Account provisioning procedure showing forced password change
- Identity provider configuration for first-login password change
- Temporary password generation and distribution procedure
- Evidence that temporary passwords expire

**Common mistakes:**
- Default password used for all new accounts
- Temporary passwords that never expire
- Temporary password sent via the same channel as the username
- No forced change at first login

---

### IA.L2-3.5.10 — Cryptographic Password Protection

**Requirement:** Store and transmit only cryptographically-protected
passwords.

**Why it matters:** Passwords stored in plaintext or transmitted
unencrypted can be trivially harvested. Cryptographic protection ensures
that even if password stores or network traffic are compromised, the
actual passwords remain protected.

**Implementation guidance:**
- Ensure all password storage uses strong hashing (bcrypt, scrypt,
  Argon2, PBKDF2 with appropriate iteration counts)
- Verify that no systems store passwords in plaintext or reversible
  encryption
- Ensure all authentication traffic uses TLS 1.2+ encryption
- Audit applications for plaintext password storage or transmission

**Evidence to collect:**
- Documentation of password hashing algorithms in use
- TLS configuration for authentication endpoints
- Audit results showing no plaintext password storage
- Application security assessment results

**Common mistakes:**
- Legacy applications storing passwords in MD5 or SHA-1 without salting
- Authentication traffic over unencrypted HTTP
- Service account passwords stored in plaintext configuration files
- Passwords transmitted in API calls without TLS

---

### IA.L2-3.5.11 — Obscured Feedback

**Requirement:** Obscure feedback of authentication information.

**Why it matters:** Displaying passwords as they are typed (or providing
detailed error messages like "incorrect password" vs "user not found")
leaks authentication information to observers or attackers.

**Implementation guidance:**
- Ensure all password entry fields mask input (display dots or asterisks)
- Use generic authentication failure messages ("authentication failed")
  rather than specific ones ("incorrect password" or "user not found")
- Ensure error messages do not reveal whether a username exists

**Evidence to collect:**
- Login page screenshots showing masked password fields
- Error message screenshots showing generic failure messages
- Application configuration for authentication error handling

**Common mistakes:**
- Login pages that show passwords in cleartext
- Error messages that distinguish between invalid username and invalid
  password (enables username enumeration)
- API responses that leak authentication details in error payloads

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 2 | 9 | 11 |

**Assessment priority:** MFA (IA.L2-3.5.3) is the single highest-impact
practice in this domain. If you implement nothing else first, implement MFA.
It protects against the most common attack vectors and assessors will look
for it early.

**Key relationships:**
- IA.L1-3.5.1 (identify users) and IA.L1-3.5.2 (authenticate users)
  provide the authentication that Access Control (AC) depends on,
  specifically AC.L1-3.1.1 (system access) and AC.L1-3.1.2
  (transaction and function control)
- IA.L2-3.5.3 (MFA) and related practices generate events that
  Audit and Accountability (AU) captures under AU.L2-3.3.2 (user
  traceability)
- IA.L2-3.5.10 (cryptographic password protection) and IA.L2-3.5.11
  (obscured feedback) rely on System and Communications Protection
  (SC) encryption requirements, specifically SC.L2-3.13.11
  (FIPS-validated cryptography)
- Federal Risk and Authorization Management Program (FedRAMP)
  inheritance: IA.L2-3.5.3 (MFA) overlaps with FedRAMP Moderate
  baseline controls derived from NIST SP 800-53 IA-2(1), IA-2(2),
  and IA-2(3). IA.L2-3.5.4 (replay-resistant authentication) maps
  to NIST SP 800-53 IA-2(8) and IA-2(9); IA-2(8) was added to the
  FedRAMP Rev. 5 Moderate baseline and was not in the FedRAMP Rev. 4
  Moderate baseline. See `references/fedramp-gap.md` "Multi-factor
  authentication" family deep-dive for the inheritance pattern and
  the FedRAMP Rev. 4/Rev. 5 baseline delta
