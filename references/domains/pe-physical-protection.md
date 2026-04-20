# Physical Protection (PE)

> Source: NIST SP 800-171 Rev 2, Section 3.10; CMMC Assessment Guide
> Level 2

## Overview

Physical Protection governs who gets inside the facility and the rooms
where CUI systems operate. The domain has 6 practices: 4 at Level 1
(physical access limits, visitor escort, access audit logs, physical
access device management) and 2 at Level 2 (facility infrastructure
protection PE.L2-3.10.2, and CUI safeguards at alternate work sites
PE.L2-3.10.6). Level 1 establishes basic facility access control that
any contractor handling FCI must implement. Level 2 adds facility and
support-infrastructure monitoring, plus remote-work and alternate-site
obligations that most small contractors underestimate until assessment.

Key cross-domain relationships: Access Control (AC) handles the logical
reflection of PE, Personnel Security (PS) governs who is eligible to
receive a badge in the first place, Identification and Authentication
(IA) connects the badge to the logical identity, Media Protection (MP)
covers the physical handling of CUI artifacts moving between sites,
Incident Response (IR) handles physical-incident response with evidence
preservation, and System and Communications Protection (SC) frames the
physical component of boundary protection. Scope signals: PE.L1-3.10.1
is the locus of cloud shared-responsibility framing for contractors
who run CUI on cloud platforms authorized under FedRAMP (the Federal
Risk and Authorization Management Program). PE.L2-3.10.6 is the
locus of remote-work and alternate-work-site compliance; any contractor
with remote or hybrid workers handling CUI must be able to cite this
practice and demonstrate enforcement.

---

## Level 1 Practices

### PE.L1-3.10.1 — Limit Physical Access

**Requirement:** Limit physical access to organizational systems,
equipment, and the respective operating environments to authorized
individuals.

**Why it matters:** Logical controls protect data while the physical
boundary holds. An attacker with hands on a server, endpoint, or
network jack can bypass most logical controls.

**Implementation guidance:**
- Maintain a physical access list for every facility or room that
  houses CUI systems. Reconcile the list against HR status at least
  quarterly; more frequently for high-turnover environments
- Enforce badge-based or PIV (Personal Identity Verification, FIPS 201)
  entry at the facility perimeter and at sensitive interior doors
  (server rooms, network closets, secure work areas)
- Lock server and network rooms when unattended; do not prop doors open
  during maintenance windows
- Establish a clean-desk expectation for areas where CUI is handled,
  and endpoint lockout policy for workstations left unattended
- Cloud shared-responsibility: for CUI processed on FedRAMP-authorized
  cloud platforms (AWS GovCloud, Azure Government, GCP Assured
  Workloads), the cloud service provider (CSP) handles data-center
  physical protection under the shared-responsibility model. Contractor
  PE obligation shifts to endpoints, on-premise equipment, and
  alternate work sites. The SSP (System Security Plan) must document
  which party owns each PE practice, with a citation to the CSP's
  FedRAMP authorization package as evidence of the CSP-side controls
- For hybrid deployments, trace each PE practice across the boundary:
  some practices are fully inherited from the CSP, some are hybrid, and
  some remain fully contractor-owned (endpoints, alternate work sites)

**Evidence to collect:**
- Physical access authorization list with recent reconciliation
  timestamp
- Badge or PIV issuance and revocation records tied to personnel
  records
- Sample access logs from the facility access control system
- Visitor logs for the reporting period
- CSP FedRAMP authorization package and a shared-responsibility matrix
  in the SSP showing PE practice ownership

**Common mistakes:**
- Physical access list not reconciled against HR status; former
  employees retain badge access
- Cloud shared-responsibility not documented in the SSP, so the
  assessor cannot tell who owns the data-center PE controls
- Authorization equated with badge possession rather than a reviewed
  business-justification decision
- Server rooms unlocked during maintenance and left unlocked after
- Remote-hands and third-party service providers treated as unescorted
  vendors

---

### PE.L1-3.10.3 — Escort Visitors

**Requirement:** Escort visitors and monitor visitor activity.

**Why it matters:** An unescorted visitor inside a CUI-handling area is
an uncontrolled insider for the duration of the visit. Escort failures
produce both physical and logical incident exposure.

**Implementation guidance:**
- Define visitor in policy. A visitor is any person without standing
  access authorization, including vendors, delivery staff, prospective
  employees, auditors, and contractors not on the access roster
- Sign-in and sign-out with timestamps captured for every visitor
- Distinguish visitors from staff via badge color, lanyard, or sticker
  that is visible from a distance
- Require escort at all times inside CUI-handling areas. Escort
  responsibility belongs to the host accepting the visitor, not to
  reception
- Prohibit visitor activity inconsistent with the visit purpose: no
  photography, no USB or peripheral attachment, no unaccompanied system
  logins
- Document escort handoffs when a visit spans multiple hosts

**Evidence to collect:**
- Visitor policy document
- Visitor log with entry and exit timestamps, host names, and escort
  assignments
- Visitor badge inventory and reissue log
- Training records for personnel designated as escorts

**Common mistakes:**
- Visitor log maintained by reception but no active escort during the
  visit
- Trusted vendors treated as employees without formal access
  authorization
- Tailgating tolerated at the perimeter
- Short-stay visitors (a five-minute delivery) exempted from escort
- Escort handoffs undocumented, so responsibility is untraceable

---

### PE.L1-3.10.4 — Maintain Audit Logs of Physical Access

**Requirement:** Maintain audit logs of physical access.

**Why it matters:** Physical access logs are the forensic record for
after-the-fact investigation and the primary evidence an assessor uses
to verify the other PE practices are real.

**Implementation guidance:**
- Electronic access control system (EACS) captures each badge read at
  every controlled door with timestamp, badge identifier, and
  authorization result
- CCTV coverage at primary entry points and sensitive interior doors
  with retention aligned to the access log retention
- SIEM integration where feasible, so physical access events can be
  correlated with logical access events during an investigation
- Manual logs for spaces without EACS (paper sign-in at server rooms);
  logs reviewed for completeness rather than filed and forgotten
- Retention commonly 1 to 3 years, guided by contract requirements and
  the DFARS 252.204-7012(e) 90-day media preservation obligation during
  incident response
- Periodic review cadence defined in policy, with a designated reviewer
  who attests to the review in writing

**Evidence to collect:**
- Sample EACS logs for the reporting period
- CCTV retention configuration and sample footage
- SIEM integration diagram showing EACS feeds where applicable
- Manual log samples (paper sign-in sheets for server rooms)
- Physical access log retention policy
- Periodic review attestation records

**Common mistakes:**
- Log retention shorter than the contract requirement
- Manual paper logs that nobody reviews
- CCTV cameras operating but the DVR overwrites every 7 days
- No review cadence; logs exist but nothing is done with them
- Physical access logs kept separate from logical access logs, so
  correlation during incident investigation is impractical

---

### PE.L1-3.10.5 — Control Physical Access Devices

**Requirement:** Control and manage physical access devices.

**Why it matters:** Access device lifecycle (badges, keys, combinations,
cards) is the most common source of PE findings. Badge management is
the operational reflection of personnel actions governed by Personnel
Security (PS).

**Implementation guidance:**
- Access device inventory covering keys, badges, cards, PIV tokens, and
  combinations. Inventory reconciled against issuance records at least
  annually
- Issuance tied to a personnel record and a business-justification
  review, not handed out by reception at the badge machine
- Revocation on separation, transfer, or role change within a defined
  SLA (same-day for termination; within one business day for transfer
  or role change)
- Badge audit cadence with corrective action when the physical
  inventory does not match the issuance records
- Combination rotation schedule for any combination-based locks;
  commonly annual, or immediately upon departure of a person who knew
  the combination
- Lost-device reporting process that triggers immediate deactivation,
  not a next-day batch run
- Temporary-badge procedures for visitors, contractors, and loaned
  badges; temporary badges expire automatically at end of day

**Evidence to collect:**
- Access device inventory document with reconciliation history
- Issuance and revocation records correlated to HR personnel actions
- Badge audit reports and discrepancy resolution records
- Combination change logs
- Lost-device reports with remediation timestamps
- Temporary-badge issuance procedures and sample records

**Common mistakes:**
- Badge revocation delayed past the termination date, leaving the
  former employee with physical access for days after exit
- Lost badges reported but never deactivated in the EACS
- Master keys held by too many people, making revocation impractical
- Combinations unchanged since facility lease start
- Contractor badges issued without expiration dates, so they outlive
  the contract

---

## Level 2 Practices

### PE.L2-3.10.2 — Protect and Monitor the Physical Facility

**Requirement:** Protect and monitor the physical facility and support
infrastructure for organizational systems.

**Why it matters:** Disruption does not require touching the systems.
Damage to the electrical, network, or environmental infrastructure
that supports CUI systems produces the same availability impact as a
direct compromise, often with less attacker sophistication.

**Implementation guidance:**
- Intrusion detection and after-hours alarm monitoring for the primary
  facility and any secondary sites housing CUI systems
- CCTV coverage of facility perimeter and sensitive interior spaces,
  integrated with the physical access logs under PE.L1-3.10.4
- Support-infrastructure hardening: locked electrical rooms, protected
  network distribution closets, UPS and generator coverage for
  critical loads, fire suppression sized for equipment (clean agent or
  pre-action systems for server rooms, not standard office sprinklers)
- Environmental monitoring (temperature, humidity, water detection) in
  server and network spaces with alerting routed to a monitored inbox
  or ticketing queue, not an unmonitored group alias
- Threat assessment covering natural hazards (flood, wildfire, storm
  exposure) and adversarial scenarios (social-engineering entry,
  sabotage of support infrastructure)
- Multi-tenant buildings require contract visibility into the parts of
  the facility the landlord controls (electrical panels in shared
  spaces, network distribution in building risers, fire protection
  across floors)

**Evidence to collect:**
- Facility monitoring system documentation and sample alerts
- CCTV retention configuration and review records
- Electrical and network closet access control evidence
- UPS battery test logs and generator maintenance records
- Fire suppression inspection records
- Environmental monitoring configuration and alert response records
- Multi-tenant lease or service agreement covering shared
  infrastructure responsibility

**Common mistakes:**
- System protection mature while facility protection is an
  afterthought
- Multi-tenant buildings where the landlord controls critical
  infrastructure with no contractual visibility or audit rights
- UPS batteries not tested; discovered dead during the first real
  outage
- Environmental alerts routed to an unmonitored email alias
- Generator maintenance skipped; fails during extended outage
- Fire suppression sized for office occupancy, not for equipment
  protection, damaging equipment during activation

---

### PE.L2-3.10.6 — Safeguard CUI at Alternate Work Sites

**Requirement:** Enforce safeguarding measures for CUI at alternate
work sites.

**Why it matters:** Remote and hybrid work shifted the largest portion
of the CUI handling surface outside managed facilities. Home offices,
travel, customer sites, and coworking spaces are alternate work sites
under PE.L2-3.10.6, and they are the hardest PE practice to enforce
because the organization usually cannot inspect them.

**Implementation guidance:**
- Remote-work policy enumerating which alternate-site contexts are
  permitted for CUI handling (home office approved; travel under
  specific conditions; coworking space typically prohibited or
  allowed only with extra safeguards; customer-site handling governed
  by contract)
- Physical safeguards at the home office: privacy filter or screen
  blocking over-the-shoulder viewing, locked storage for CUI documents
  and issued devices, CUI non-visibility to household members and
  visible-to-passersby locations (no CUI work facing a street-view
  window), no shared household printers or devices for CUI
- Network routing: VPN configuration that forces CUI traffic across
  the organizational boundary, no split-tunneling that leaves CUI
  traffic on the home network, no CUI handling on personal devices
- Travel guidance: no CUI on personal devices, hotel safe for issued
  devices and hardcopy, no CUI work in airport lounges or public
  spaces, travel reporting for high-risk destinations
- Coworking space guidance: typically prohibited for CUI work; if
  permitted, requires privacy booth or private office, not open seating
- Cloud access from alternate sites: CUI accessed via FedRAMP-
  authorized CSP services preserves the cloud side of the shared-
  responsibility boundary, but contractor-side endpoint and home-office
  controls still apply
- User attestation for home-office setup (photo of workspace, privacy
  filter confirmation, locked-storage confirmation) captured at
  onboarding and at least annually
- Training on alternate-site safeguards, delivered separately from
  generic security awareness, because the concrete rules (privacy
  filter, VPN, household visibility) need practitioner-level detail

**Evidence to collect:**
- Remote-work policy document
- Training records specific to alternate-site safeguards
- Privacy-filter issuance records
- Remote-access VPN configuration showing CUI-route enforcement
- User attestations for home-office setup
- Incident records for alternate-site compliance failures and their
  remediation

**Common mistakes:**
- Remote-work policy exists but training does not follow
- VPN split-tunneling permitted, so CUI traffic leaves the
  organizational boundary
- Privacy filters required by policy but never distributed or
  confirmed in use
- Coworking space use unaddressed; employees assume it is allowed
- Travel guidance missing entirely
- Household members and roommates visible in video calls with CUI
  visible on screen or physical documents in frame
- Shared household printers used for CUI hardcopy
- Attestation captured at onboarding but never refreshed, so home-
  office drift is invisible

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 4 | 2 | 6 |

**Assessment priority:** Start with PE.L1-3.10.1 and PE.L1-3.10.5.
PE.L1-3.10.1 is the authorization gate; without it, the other access
practices cannot be shown to be selective. PE.L1-3.10.5 (access device
management) is the most common finding source because badge lifecycle
is where personnel actions and physical access diverge in practice.
PE.L2-3.10.6 is the practice most likely to fail in the real world
regardless of how strong the policy is, because alternate-site drift
is invisible without attestation and refresh.

**Key relationships:**
- Access Control (AC) is the logical reflection of PE; the two
  together form the end-to-end access boundary and must be reconciled
  during assessment
- Personnel Security (PS) governs who is eligible to receive a badge;
  PE.L1-3.10.5 revocation triggers come from PS personnel actions
- Identification and Authentication (IA) connects the physical badge
  to the logical identity for attribution
- Media Protection (MP) covers the physical handling of CUI documents
  and media moving between facilities and alternate work sites
- Incident Response (IR) handles physical-incident response; DFARS
  252.204-7012(e) 90-day media preservation overlaps with physical
  evidence chain-of-custody
- System and Communications Protection (SC) frames the boundary that
  PE enforces at the physical layer; VPN routing for alternate work
  sites under PE.L2-3.10.6 is an SC-PE integration point
