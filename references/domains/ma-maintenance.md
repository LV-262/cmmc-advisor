# Maintenance (MA)

> Source: NIST SP 800-171 Rev 2, Section 3.7; CMMC Assessment Guide Level 2

## Overview

Maintenance governs how systems get worked on and by whom, while CUI
stays protected. The domain has 6 practices: MA.L2-3.7.1 (perform
maintenance), MA.L2-3.7.2 (controls on tools and personnel),
MA.L2-3.7.3 (sanitize equipment before off-site maintenance),
MA.L2-3.7.4 (check diagnostic media for malicious code), MA.L2-3.7.5
(MFA and session termination for nonlocal maintenance), MA.L2-3.7.6
(supervise unauthorized maintenance personnel). All six are at Level
2. No Level 1 MA practices exist, so contractors handling only FCI
have no maintenance requirement under this domain.

Cross-domain relationships cluster around the people, tools, and
channels maintenance uses.
Media Protection (MP) governs the sanitization chain that MA.L2-3.7.3
invokes for equipment leaving the facility and the media-handling
discipline that MA.L2-3.7.4 extends to diagnostic media.
Personnel Security (PS) sets the screening gate for maintenance staff;
MA.L2-3.7.2 authorization and MA.L2-3.7.6 supervision both trace back
to PS.L2-3.9.1.
Identification and Authentication (IA) covers the MFA mechanism
MA.L2-3.7.5 requires for nonlocal maintenance, reciprocating
IA.L2-3.5.3 in the maintenance context.
System and Communications Protection (SC) frames the boundary
crossings that nonlocal maintenance sessions traverse.
System and Information Integrity (SI) overlaps MA.L2-3.7.4 malicious-
code checks with SI.L2-3.14.2 malicious-code protection; the two
practices coordinate on what scans run where.
Physical Protection (PE) carries the physical chain-of-custody when
equipment leaves the facility for off-site maintenance under
MA.L2-3.7.3.

---

## Level 2 Practices

### MA.L2-3.7.1 — Perform Maintenance

**Requirement:** Perform maintenance on organizational systems.

**Why it matters:** The requirement reads narrowly but the assessment
is about controlled execution. Unscheduled, undocumented, or
unauthorized maintenance activity creates the same attack surface as
an insider with system privileges.

**Implementation guidance:**
- Scheduled maintenance windows with change-control tickets; no
  ad-hoc patching or configuration changes outside the window except
  for emergency response with explicit approval
- Maintenance authorization logged: who performed what, on which
  system, when, and under which change ticket
- Post-maintenance verification: functional tests, security-control
  tests (endpoint protection active, logs flowing, access controls
  intact), and confirmation of return to baseline before the system
  returns to production use
- Maintenance records retained for audit review; retention aligned
  with other operational records

**Evidence to collect:**
- Maintenance policy and scheduled-window procedures
- Change tickets for a representative sample of maintenance events
- Maintenance activity logs tied to tickets
- Post-maintenance verification records

**Common mistakes:**
- Emergency-maintenance exception used routinely, bypassing
  change control
- Maintenance activity not logged at the per-event level
- No post-maintenance verification; systems return to production
  without confirming controls survived
- Maintenance records retained in a system administrator's personal
  folder rather than a durable operational record

---

### MA.L2-3.7.2 — Controls on Tools, Techniques, Mechanisms, and Personnel

**Requirement:** Provide controls on the tools, techniques,
mechanisms, and personnel used to conduct system maintenance.

**Why it matters:** Maintenance personnel have privileged access to
systems that process CUI. Maintenance tools sit closer to system
internals than normal user tools. Both surfaces require explicit
controls, not assumed trust.

**Implementation guidance:**
- Maintenance personnel authorization: identified maintainers on an
  approved list; authorization tied to PS.L2-3.9.1 pre-access
  screening and to a documented business need
- Tool inventory: approved diagnostic tools, maintenance laptops,
  vendor-supplied software, and test equipment cataloged. Unknown
  tools do not connect to production
- Tool integrity: maintenance laptops kept under change control;
  software installed from controlled baselines; no personal devices
  used for production maintenance
- Vendor-supplied tools: vetted before first use; vendor maintenance
  accounts provisioned with least-privilege and time-bounded access
- Technique documentation: maintenance runbooks, vendor procedures,
  and approved methods for common tasks; deviation requires approval

**Evidence to collect:**
- Authorized-maintainer list tied to HR and PS records
- Tool and equipment inventory
- Change-control records for maintenance tool baselines
- Vendor vetting records for third-party maintenance providers
- Runbook library and last-updated timestamps

**Common mistakes:**
- Maintenance authorization conflated with general IT administrator
  access; everyone in IT is treated as a maintainer
- Tool inventory missing for vendor-supplied diagnostic equipment
- Maintenance laptops not under change control; drift silently
- Vendor accounts long-lived rather than time-bounded; vendor leaves
  the engagement with persistent access

---

### MA.L2-3.7.3 — Sanitize Equipment Before Off-Site Maintenance

**Requirement:** Ensure equipment removed for off-site maintenance is
sanitized of any CUI (Controlled Unclassified Information).

**Why it matters:** Once equipment leaves the facility, the
contractor loses the physical and logical controls that protected the
CUI on it. Sanitization before departure is the only reliable
boundary. This practice sits at the intersection of MP (sanitization
discipline), PE (physical chain-of-custody), and MA (maintenance
workflow).

**Implementation guidance:**
- Sanitization standard: NIST SP 800-88 guidelines for media
  sanitization (Clear, Purge, Destroy) applied per media type and
  residual-risk tolerance. Purge or Destroy for media that held CUI
  where the vendor is not authorized for CUI handling
- Pre-departure verification: sanitization performed, verified, and
  documented before equipment leaves custody. Chain-of-custody
  record starts at the moment of verification
- Reciprocal framing with MP.L2-3.8.3: MP owns the sanitization
  method and verification; MA invokes it at the off-site-maintenance
  trigger
- Alternatives when sanitization is not feasible: if the equipment
  cannot be sanitized (embedded firmware, sealed devices), require
  the maintenance be performed under contractor supervision or use
  a vendor authorized for CUI handling
- Loaner equipment: when a system is sent out and a replacement
  loaned in, the loaner goes through the same controls as any new
  system entering the environment

**Evidence to collect:**
- Off-site-maintenance procedure covering sanitization and
  chain-of-custody
- Sanitization records per event with method, operator, verification
- Vendor agreements specifying CUI handling authorization where
  applicable
- Sample chain-of-custody records for recent off-site events

**Common mistakes:**
- Sanitization performed but not verified; no record of who confirmed
  the operation succeeded
- Sealed or embedded-firmware devices sent out without supervision or
  CUI-authorization arrangement
- Chain-of-custody starts only when the vendor picks up, not at
  sanitization-verification time
- Loaner equipment returned to production without vetting
- CUI on the device assumed "not CUI anymore" after a simple file
  delete rather than proper sanitization

---

### MA.L2-3.7.4 — Check Diagnostic Media for Malicious Code

**Requirement:** Check media containing diagnostic and test programs
for malicious code before the media are used in organizational
systems.

**Why it matters:** Diagnostic tools connect at a higher trust level
than user devices. Infected diagnostic media gives an attacker a
direct path past endpoint controls into the systems being serviced.

**Implementation guidance:**
- Pre-connection scanning: every diagnostic USB, maintenance laptop,
  vendor-supplied drive, and portable test tool scanned with current
  anti-malware before connection to an in-scope system
- Vendor-supplied media: treated as untrusted until scanned, even
  from authorized vendors
- Reciprocal with SI.L2-3.14.2: SI owns the anti-malware capability
  on systems; MA owns the pre-connection discipline at the
  maintenance boundary. Coordinate so scan signatures and capability
  come from the same source of truth
- Write-blockers where appropriate: for forensic or
  investigation-context diagnostic work, write-blocked connection
  prevents inadvertent modification
- Read-only media when possible: vendor procedures that can run from
  read-only media reduce the malicious-code vector

**Evidence to collect:**
- Pre-connection scanning procedure
- Sample scan records for vendor and internal diagnostic media
- Write-blocker inventory and usage guidance
- Anti-malware signature currency on the maintenance-staging system

**Common mistakes:**
- Vendor media trusted because it came from a vendor; no scan
- Scanning done on the maintenance laptop with stale signatures
- Diagnostic USB passed between technicians without re-scanning
- Write-blockers available but unused because procedure does not
  require them

---

### MA.L2-3.7.5 — MFA for Nonlocal Maintenance Sessions

**Requirement:** Require multifactor authentication to establish
nonlocal maintenance sessions via external network connections and
terminate such connections when nonlocal maintenance is complete.

**Why it matters:** Nonlocal maintenance collapses the contractor's
physical boundary: a vendor or remote administrator reaches in from
outside the facility, often from outside the organization entirely.
Without MFA (multi-factor authentication) on the authentication step
and explicit termination on completion, the session becomes a
persistent external access path.

**Implementation guidance:**
- MFA enforcement on the authentication step for every nonlocal
  maintenance session. Reciprocal with IA.L2-3.5.3 which covers MFA
  for privileged accounts generally; MA.L2-3.7.5 applies the same
  discipline specifically to maintenance access
- External-network framing: SC (System and Communications Protection)
  governs the boundary the session crosses. Nonlocal sessions use
  VPN or dedicated remote-access gateways rather than direct exposure
  of administrative interfaces
- Session termination on completion: either automatic
  (inactivity-triggered plus explicit logout) or procedural (operator
  terminates per runbook step). Long-lived standing connections for
  "convenience" are the failure mode this requirement addresses
- Session logging: authentication event, session duration, commands
  executed where the architecture supports logging, and
  disconnect-event recorded
- Vendor remote-maintenance: vendor accounts meet the same MFA and
  session-termination requirements. Vendor-managed access arranged
  through the contractor's VPN or remote-access platform, not vendor-
  provided tunneling that bypasses contractor controls
- Cloud-administration parallel: administrative sessions into cloud
  management consoles that perform maintenance functions are
  nonlocal maintenance by any practical reading; MFA and session
  termination apply

**Evidence to collect:**
- Remote-access platform configuration showing MFA enforced on
  maintenance account classes
- Sample session logs with authentication event and termination
  timestamps
- Vendor agreements requiring MFA and session-termination compliance
- Policy requiring explicit termination per session
- Cloud-console access logs for administrative sessions

**Common mistakes:**
- MFA on the VPN tunnel but not on the subsequent maintenance-account
  authentication; attacker who compromises the VPN credential reaches
  the maintenance account unprotected
- Vendor bypass: vendor uses their own remote-support tool
  (unencrypted or unmonitored) because the contractor's platform is
  "too hard"
- Standing connections that never terminate; the session from six
  months ago is still technically open
- Administrative sessions into cloud management consoles not treated
  as nonlocal maintenance; MFA enforced but termination not
- Session logging limited to connection event; no command or
  duration detail

---

### MA.L2-3.7.6 — Supervise Unauthorized Maintenance Personnel

**Requirement:** Supervise the maintenance activities of maintenance
personnel without required access authorization.

**Why it matters:** Occasionally the only qualified technician for a
specific system or piece of equipment is someone who has not been
through the full screening and authorization process. Supervision
closes the gap: the unauthorized technician performs the work while
an authorized staff member watches, controls access, and intervenes
if the work drifts outside scope.

**Implementation guidance:**
- Supervisor role: the supervisor is a person authorized for access
  to the system being maintained, with the knowledge to recognize
  out-of-scope activity. PS.L2-3.9.1 screening and MA.L2-3.7.2
  authorization both apply to the supervisor
- Supervision depth: constant presence during maintenance, not
  check-in visits. Remote supervision only where the maintenance
  activity is itself remote and logged end-to-end
- Scope definition: the supervisor knows the scope of the authorized
  maintenance task and intervenes if the technician moves outside it
  (accessing other systems, copying data, installing unauthorized
  software)
- Documentation: each supervised maintenance event logged with
  supervisor and technician identities, start and end times, scope
  agreed, and any interventions
- Post-event review for sensitive maintenance: debrief with the
  supervisor covers what happened and whether any unplanned access
  occurred

**Evidence to collect:**
- Supervision procedure with role definitions
- Supervised-maintenance event records with supervisor attribution
- Scope-of-work documents for sensitive maintenance events
- Post-event review records for high-sensitivity supervised work

**Common mistakes:**
- Supervisor nominally assigned but not present for the full
  maintenance window
- Supervisor not authorized for the system being maintained; they
  cannot actually recognize out-of-scope activity
- Remote-supervised work with no end-to-end recording; the
  supervisor cannot intervene on what they cannot see
- Scope defined verbally, not documented; disagreements about what
  was authorized happen after the fact
- Vendor-performed maintenance supervised by another vendor rather
  than a contractor staff member

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 6 | 6 |

**Assessment priority:** Start with MA.L2-3.7.2. Controlled
authorization of maintenance personnel and tools is the gate the
other five practices depend on. Without a defined maintainer
population and tool inventory, MA.L2-3.7.1 (performing maintenance)
happens outside policy, MA.L2-3.7.6 (supervision) has no baseline
authorized group to contrast against, and MA.L2-3.7.5 (nonlocal MFA)
cannot reliably identify who is connecting. Then focus on MA.L2-3.7.5
(nonlocal sessions are the highest-impact external surface) and
MA.L2-3.7.3 (off-site sanitization is the highest-impact data
departure point). MA.L2-3.7.4 malicious-code checks are operationally
simple but frequently skipped in practice, which is worth a specific
pre-assessment review.

**Key relationships:**
- Media Protection (MP) owns the sanitization method and verification
  that MA.L2-3.7.3 invokes for equipment departing the facility;
  MA.L2-3.7.4 extends MP media-handling discipline to diagnostic
  tools before they connect to production
- Personnel Security (PS) sets the screening gate at PS.L2-3.9.1
  that MA.L2-3.7.2 authorization and MA.L2-3.7.6 supervision both
  depend on; maintainer-population hygiene traces to personnel
  screening outcomes
- Identification and Authentication (IA) provides the MFA mechanism
  MA.L2-3.7.5 requires; IA.L2-3.5.3 multifactor authentication for
  privileged accounts is the generic practice that MA.L2-3.7.5
  specializes for maintenance
- System and Communications Protection (SC) frames the boundary that
  nonlocal maintenance sessions cross; VPN or remote-access gateway
  controls under SC carry the traffic MA.L2-3.7.5 requires be
  authenticated and terminated
- System and Information Integrity (SI) overlaps MA.L2-3.7.4 at the
  malicious-code check; SI.L2-3.14.2 owns anti-malware capability on
  systems, MA owns pre-connection scanning discipline at the
  maintenance boundary
- Physical Protection (PE) carries the physical chain-of-custody for
  equipment leaving the facility under MA.L2-3.7.3; PE.L1-3.10.5
  access device management extends to equipment as well as badges
