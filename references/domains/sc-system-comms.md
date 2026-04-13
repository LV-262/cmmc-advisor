# System and Communications Protection (SC)

> Source: NIST SP 800-171 Rev 2, Section 3.13; CMMC Assessment Guide Level 2

## Overview

System and Communications Protection covers boundary defense, encryption,
network segmentation, and communications security. This domain has 16
practices — 2 at Level 1 and 14 additional at Level 2.

SC is where your technical architecture either proves or undermines your
compliance story. Assessors will examine your network boundaries,
encryption implementations, and communications paths closely. This domain
has the most interaction with modern IT choices (cloud platforms,
encryption modules, network design).

---

## Level 1 Practices (Basic)

### SC.L1-3.13.1 — Boundary Protection

**Requirement:** Monitor, control, and protect communications (i.e.,
information transmitted or received by organizational systems) at the
external boundaries and key internal boundaries of organizational systems.

**Why it matters:** Your system boundary is the perimeter of your CUI
environment. Controlling what crosses that boundary — in both directions —
is fundamental to protecting CUI.

**Implementation guidance:**
- Deploy firewalls at the external boundary of your CUI environment
- Configure firewall rules to deny-by-default (block everything, then
  allow specific approved traffic)
- Monitor traffic crossing the boundary for anomalies
- Implement internal segmentation between CUI and non-CUI networks
- Document all boundary points in your network diagram

**Evidence to collect:**
- Firewall configuration and rule sets
- Network diagram showing boundary points
- Traffic monitoring configuration
- Deny-by-default evidence (default deny rule)
- Internal segmentation documentation

**Common mistakes:**
- Allow-by-default firewall rules (permit everything, block specific threats)
- No internal segmentation — CUI network and corporate network are flat
- Boundary exists but is not monitored
- Network diagram does not accurately reflect actual boundary

---

### SC.L1-3.13.5 — Public Access System Separation

**Requirement:** Implement subnetworks for publicly accessible system
components that are physically or logically separated from internal
networks.

**Why it matters:** Public-facing systems (web servers, email gateways)
are exposed to the internet and are frequent attack targets. Separating
them from internal CUI systems ensures that a compromise of a public
system does not provide direct access to CUI.

**Implementation guidance:**
- Place public-facing systems in a DMZ (demilitarized zone) or separate
  subnet
- Implement firewall rules controlling traffic between DMZ and internal
  networks
- Do not store CUI on public-facing systems
- Monitor traffic between DMZ and internal networks

**Evidence to collect:**
- DMZ network architecture documentation
- Firewall rules between DMZ and internal network
- Evidence that CUI is not present on public-facing systems
- Traffic monitoring between zones

**Common mistakes:**
- Public-facing web server on the same network as CUI systems
- No DMZ — public services directly on the internal network
- DMZ exists but firewall rules allow broad access to internal network

---

## Level 2 Practices (Derived)

### SC.L2-3.13.2 — Architectural Design

**Requirement:** Employ architectural designs, software development
techniques, and systems engineering principles that promote effective
information security within organizational systems.

**Why it matters:** Security should be designed into your architecture,
not bolted on after. This practice requires that security is a
consideration in system design decisions, not an afterthought.

**Implementation guidance:**
- Apply defense-in-depth principles (multiple layers of protection)
- Use network segmentation to isolate CUI environments
- Implement least privilege in system architecture
- Document security architecture decisions and their rationale
- Review architecture when systems change or new threats emerge

**Evidence to collect:**
- Security architecture documentation
- Defense-in-depth implementation evidence
- Network segmentation design documents
- Architecture review records

**Common mistakes:**
- Flat network with no segmentation
- Security controls at the perimeter only (no internal layers)
- No documented security architecture

---

### SC.L2-3.13.3 — Role Separation

**Requirement:** Separate user functionality from system management
functionality.

**Why it matters:** Users performing daily work should not have access
to system management interfaces. Separating these prevents accidental
or malicious system modifications during normal operations.

**Implementation guidance:**
- Separate user-facing interfaces from administrative interfaces
- Require separate authentication for management interfaces
- Place management interfaces on a separate network or VLAN when feasible
- Restrict management interface access to specific authorized workstations

**Evidence to collect:**
- Management interface access restrictions
- Network separation of management interfaces
- Administrative access policy
- Management workstation designation

**Common mistakes:**
- Management interfaces accessible from any workstation
- No separate authentication for management access
- Users and administrators sharing the same network path to systems

---

### SC.L2-3.13.4 — Shared Resource Control

**Requirement:** Prevent unauthorized and unintended information transfer
via shared system resources.

**Why it matters:** Shared resources (memory, storage, processing) can
leak information between users or processes if not properly controlled.
This is especially relevant in multi-tenant cloud environments.

**Implementation guidance:**
- Clear shared resources between user sessions
- Implement memory protection in operating systems
- In cloud environments, use dedicated instances or assured workload
  isolation for CUI processing
- Clear temporary files and caches after CUI processing

**Evidence to collect:**
- Shared resource management procedures
- OS memory protection configuration
- Cloud isolation configuration (dedicated instances, assured workloads)
- Temporary file cleanup procedures

**Common mistakes:**
- CUI in temporary files or caches accessible by other users
- Multi-tenant cloud without isolation controls
- Shared workstations without session cleanup between users

---

### SC.L2-3.13.6 — Network Communication by Exception

**Requirement:** Deny network communications traffic by default and
allow network communications traffic by exception (i.e., deny all,
permit by exception).

**Why it matters:** Deny-by-default ensures only explicitly approved
traffic can flow. This prevents unauthorized communications and reduces
the attack surface to known, approved paths.

**Implementation guidance:**
- Configure all firewalls with a default deny rule
- Explicitly permit only required traffic (source, destination, port,
  protocol)
- Apply deny-by-default to both inbound and outbound traffic
- Document all permit rules with business justification
- Review firewall rules periodically and remove stale rules

**Evidence to collect:**
- Firewall configuration showing default deny rules
- Permit rule documentation with justification
- Firewall rule review schedule and records
- Evidence of outbound traffic restrictions

**Common mistakes:**
- Default allow rules still in place
- Outbound traffic unrestricted (only inbound controlled)
- Stale firewall rules from decommissioned systems
- No documentation of why each rule exists

---

### SC.L2-3.13.7 — Split Tunneling Prevention

**Requirement:** Prevent remote devices from simultaneously establishing
non-remote connections with organizational systems and communicating via
some other connection to resources in external networks (i.e., split
tunneling).

**Why it matters:** Split tunneling allows a remote device to access your
CUI network and the internet simultaneously. This creates a path for CUI
to leak to the internet or for threats from the internet to reach your
CUI network through the remote device.

**Implementation guidance:**
- Configure VPN clients to route all traffic through the VPN tunnel
  when connected to the CUI network (full tunnel, no split tunnel)
- Technically enforce split tunnel prevention in VPN configuration
- Monitor for split tunnel violations
- Document the split tunnel policy

**Evidence to collect:**
- VPN configuration showing full tunnel enforcement
- Split tunnel prevention policy
- VPN client configuration screenshots
- Monitoring for split tunnel violations

**Common mistakes:**
- Split tunnel enabled for "performance" without security analysis
- VPN configuration allows split tunnel as user option
- Policy prohibits split tunnel but no technical enforcement

---

### SC.L2-3.13.8 — Data in Transit Encryption

**Requirement:** Implement cryptographic mechanisms to prevent
unauthorized disclosure of CUI during transmission unless otherwise
protected by alternative physical safeguards.

**Why it matters:** CUI traversing networks — internal or external — can
be intercepted. Encryption ensures confidentiality during transmission.

**Implementation guidance:**
- Encrypt all CUI in transit using TLS 1.2 or higher
- Require encrypted email for CUI transmission (TLS between mail servers,
  or S/MIME/PGP for end-to-end)
- Encrypt file transfers containing CUI (SFTP, FTPS, HTTPS)
- Verify that encryption uses FIPS-validated cryptographic modules
- Disable unencrypted protocols for CUI systems (HTTP, FTP, Telnet)

**Evidence to collect:**
- TLS configuration for web applications
- Email encryption configuration
- File transfer encryption configuration
- FIPS validation certificates for cryptographic modules
- Evidence that unencrypted protocols are disabled

**Common mistakes:**
- TLS 1.0/1.1 still enabled alongside TLS 1.2+
- Email transmitted without TLS between servers
- FTP used instead of SFTP for file transfers
- Encryption present but not FIPS-validated

---

### SC.L2-3.13.9 — Network Disconnect

**Requirement:** Terminate network connections associated with
communications sessions at the end of the sessions or after a defined
period of inactivity.

**Why it matters:** Idle network connections represent risk. Terminating
them after inactivity prevents abandoned sessions from being hijacked.

**Implementation guidance:**
- Configure session timeouts for all network connections to CUI systems
- Implement timeouts for VPN, RDP, SSH, and web application sessions
- Define timeout periods appropriate for each connection type
- Document timeout configurations

**Evidence to collect:**
- Session timeout configurations per connection type
- VPN timeout settings
- Application session timeout settings
- Timeout policy documentation

**Common mistakes:**
- No timeouts configured — sessions remain active indefinitely
- Inconsistent timeouts across different connection types
- Timeouts set too long (hours instead of minutes for sensitive systems)

---

### SC.L2-3.13.10 — Cryptographic Key Management

**Requirement:** Establish and manage cryptographic keys for cryptography
employed in organizational systems.

**Why it matters:** Encryption is only as strong as its key management.
Poor key management — reused keys, unrotated keys, unprotected key
storage — undermines the entire encryption implementation.

**Implementation guidance:**
- Define key management procedures covering generation, distribution,
  storage, rotation, and destruction
- Use hardware security modules (HSMs) or managed key services for
  critical keys
- Rotate encryption keys on a defined schedule
- Protect key storage with access controls
- Document key management procedures

**Evidence to collect:**
- Key management policy and procedures
- Key rotation schedule and records
- Key storage protection configuration
- HSM or key management service documentation
- Key inventory

**Common mistakes:**
- Encryption keys stored in plaintext configuration files
- No key rotation — same keys used since initial deployment
- No documented key management procedures
- Keys shared across multiple environments (dev and production)

---

### SC.L2-3.13.11 — CUI Encryption

**Requirement:** Employ FIPS-validated cryptography when used to protect
the confidentiality of CUI.

**Why it matters:** FIPS validation confirms that cryptographic modules
have been independently tested and certified. Using non-validated
cryptography means your encryption has not been verified to work correctly.

**This is the most commonly misunderstood SC practice.** "We use AES-256"
is not sufficient. The specific cryptographic module implementation must
be FIPS 140-2 or FIPS 140-3 validated. Check the NIST CMVP list.

**Implementation guidance:**
- Identify all points where cryptography protects CUI (disk encryption,
  TLS, VPN, email encryption, database encryption)
- Verify each cryptographic module against the NIST CMVP list:
  https://csrc.nist.gov/projects/cryptographic-module-validation-program
- Common FIPS-validated modules: Windows BitLocker (with TPM), Apple
  FileVault (with Apple corecrypto), OpenSSL FIPS Object Module,
  AWS encryption services (in GovCloud)
- Document FIPS validation certificate numbers for each module

**Evidence to collect:**
- Inventory of cryptographic modules in use
- FIPS validation certificate numbers per module
- CMVP listing printouts or references
- Configuration showing FIPS mode is enabled where applicable

**POA&M note:** This practice has a special carve-out — it can be placed
on a POA&M if encryption exists but is not FIPS-validated, provided
you are actively pursuing FIPS-validated alternatives. This is the only
3-point practice eligible for POA&M. See `poam-management.md`.

**Common mistakes:**
- Assuming the algorithm name (AES-256) equals FIPS validation — it does not
- Not checking the CMVP list for specific module validation
- Using encryption libraries that are not FIPS-validated
- FIPS mode available but not enabled in the configuration

> Source: NIST CMVP — https://csrc.nist.gov/projects/cryptographic-module-validation-program

---

### SC.L2-3.13.12 — Collaborative Device Control

**Requirement:** Prohibit remote activation of collaborative computing
devices and provide indication of devices in use to users.

**Why it matters:** Collaborative devices (cameras, microphones, screen
sharing tools) can be remotely activated to eavesdrop on CUI discussions.
Users must know when these devices are active and be able to prevent
remote activation.

**Implementation guidance:**
- Disable remote activation of cameras and microphones by default
- Provide visual or audible indicators when collaborative devices are
  active (camera LED, microphone indicator)
- Allow users to physically disable collaborative devices (camera covers,
  microphone mute switches)
- Configure conferencing software to require user consent before enabling
  camera or microphone

**Evidence to collect:**
- Collaborative device policy
- Configuration preventing remote activation
- Evidence of user-facing indicators (camera LEDs, software indicators)
- User training on collaborative device controls

**Common mistakes:**
- Conference room devices always active with no indicators
- Software that can silently activate cameras or microphones
- No physical disable option for built-in cameras/microphones

---

### SC.L2-3.13.13 — Mobile Code Control

**Requirement:** Control and monitor the use of mobile code.

**Why it matters:** Mobile code (JavaScript, ActiveX, Java applets, macros,
scripts) can execute on your systems and potentially access or exfiltrate
CUI. Controlling mobile code execution reduces this risk.

**Implementation guidance:**
- Configure browsers to restrict or control JavaScript and plugin execution
- Block or restrict Office macro execution (especially from untrusted sources)
- Implement web content filtering to block known malicious mobile code
- Monitor for unauthorized mobile code execution
- Define approved and restricted mobile code types

**Evidence to collect:**
- Browser security configuration
- Office macro policy (Group Policy or equivalent)
- Web content filtering configuration
- Mobile code control policy

**Common mistakes:**
- All macros enabled in Office applications
- No browser security hardening
- No web content filtering

---

### SC.L2-3.13.14 — Voice over IP

**Requirement:** Control and monitor the use of Voice over Internet
Protocol (VoIP) technologies.

**Why it matters:** VoIP systems can transmit CUI through voice
conversations. They also represent an attack vector if not properly
secured — VoIP traffic can be intercepted, and VoIP systems can be
compromised.

**Implementation guidance:**
- Encrypt VoIP traffic (SRTP for media, TLS for signaling)
- Place VoIP systems on a separate VLAN from CUI data networks
- Implement access controls on VoIP management interfaces
- Monitor VoIP usage and log call records
- Apply the same security controls to VoIP infrastructure as to other
  in-scope systems

**Evidence to collect:**
- VoIP encryption configuration
- VoIP network segmentation (separate VLAN)
- VoIP management interface access controls
- VoIP monitoring configuration

**Common mistakes:**
- VoIP traffic unencrypted on the network
- VoIP on the same VLAN as CUI data systems
- VoIP management interface accessible with default credentials

---

### SC.L2-3.13.15 — Communications Authenticity

**Requirement:** Protect the authenticity of communications sessions.

**Why it matters:** Session hijacking and man-in-the-middle attacks can
intercept or modify communications. Protecting authenticity ensures that
the parties in a communication are who they claim to be and that the
communication has not been altered in transit.

**Implementation guidance:**
- Use TLS with valid certificates for all web communications
- Implement certificate validation (reject invalid or self-signed
  certificates in production)
- Use authenticated protocols for email (SPF, DKIM, DMARC)
- Implement mutual TLS for service-to-service communications where
  appropriate

**Evidence to collect:**
- TLS certificate management procedures
- Certificate validation configuration
- Email authentication configuration (SPF, DKIM, DMARC records)
- Mutual TLS configuration (if applicable)

**Common mistakes:**
- Self-signed certificates in production
- Certificate validation disabled in client applications
- No email authentication (SPF, DKIM, DMARC) configured
- Expired certificates not detected or renewed

---

### SC.L2-3.13.16 — Data at Rest Encryption

**Requirement:** Protect the confidentiality of CUI at rest.

**Why it matters:** CUI stored on disk, in databases, on mobile devices,
or in cloud storage must be encrypted so that physical theft or
unauthorized access to storage does not expose CUI.

**Implementation guidance:**
- Enable full-disk encryption on all endpoints handling CUI:
  - Windows: BitLocker with TPM
  - macOS: FileVault
  - Linux: LUKS
  - Mobile: Device encryption (enabled by default on modern iOS/Android)
- Encrypt CUI in databases (transparent data encryption or column-level
  encryption)
- Encrypt CUI in cloud storage (server-side encryption with customer-
  managed keys when possible)
- Verify encryption uses FIPS-validated modules (see SC.L2-3.13.11)

**Evidence to collect:**
- Full-disk encryption configuration per endpoint type
- Encryption status reports from MDM or management tools
- Database encryption configuration
- Cloud storage encryption configuration
- FIPS validation status of encryption modules

**Common mistakes:**
- Disk encryption enabled but not enforced through management tools
- Encryption on endpoints but not on servers or cloud storage
- CUI in databases without encryption
- Assuming cloud provider default encryption satisfies the requirement
  without verifying FIPS validation

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 2 | 14 | 16 |

**Assessment priority:** Focus on SC.L2-3.13.11 (FIPS-validated
encryption) first — this is the practice most organizations struggle
with because they assume using a known algorithm is sufficient when FIPS
module validation is actually required. Then address SC.L2-3.13.8 (data
in transit) and SC.L2-3.13.16 (data at rest) as they directly protect
CUI confidentiality.

**Key relationships:**
- SC encryption practices interact with IA authentication practices
  (encrypted authentication channels)
- SC boundary protection supports Access Control (AC) enforcement
- SC split tunnel prevention relates to AC remote access practices
- SC FIPS validation applies wherever cryptography is used — this
  practice cascades across IA, AU, and MP domains
