# Media Protection (MP)

> Source: NIST SP 800-171 Rev 2, Section 3.8; CMMC Assessment Guide Level 2

## Overview

Media Protection governs the lifecycle of every object that stores
CUI: laptops and servers, external drives and USB sticks, printed
documents and archived tapes, backup media and loaner devices. The
domain has 9 practices across a 1 Level 1 + 8 Level 2 split.
MP.L1-3.8.3 (sanitize or destroy before disposal or reuse) is the
single L1 practice, so contractors handling only FCI still have the
sanitization obligation. The 8 L2 practices cover physical protection
(3.8.1, 3.8.5), authorized-user access (3.8.2), CUI marking (3.8.4),
cryptographic protection in transport (3.8.6), removable and portable
media control (3.8.7, 3.8.8), and backup confidentiality (3.8.9).

Cross-domain relationships cluster around what CUI lives on media and
who moves it: Maintenance (MA) depends on MP.L1-3.8.3 for the
sanitization of equipment before off-site maintenance under
MA.L2-3.7.3 and on MP discipline for diagnostic media under
MA.L2-3.7.4. Physical Protection (PE) carries the facility-level
physical control that MP.L2-3.8.1 extends to media specifically.
System and Communications Protection (SC) supplies the cryptographic
mechanisms MP.L2-3.8.6 requires for digital media in transport.
Access Control (AC) defines the authorized-users concept that
MP.L2-3.8.2 scopes media access to. Incident Response (IR) invokes
MP during incidents, particularly the DFARS 252.204-7012(e) 90-day
media preservation obligation established in the IR slice.
Identification and Authentication (IA) provides the identity proofing
that makes authorized-users enforcement meaningful under MP.L2-3.8.2
and MP.L2-3.8.5. MP.L2-3.8.6 crypto and MP.L1-3.8.3 sanitization are
load-bearing for Phase 5d endpoints and remote-work content (laptop
encryption baselines, device return and sanitization on separation).

---

## Level 1 Practices

### MP.L1-3.8.3 — Sanitize or Destroy Media Before Disposal or Reuse

**Requirement:** Sanitize or destroy system media containing CUI
(Controlled Unclassified Information) before disposal or release for
reuse.

**Why it matters:** Media leaves organizational control at disposal,
at reuse, and at every vendor handoff. Without sanitization, CUI
persists on the media after the organization's controls no longer
apply. This is the one MP practice that applies even at Level 1
because the failure mode is immediate data exposure.

**Implementation guidance:**
- Sanitization methodology: NIST SP 800-88 (Guidelines for Media
  Sanitization) defines three levels (Clear, Purge, Destroy) mapped
  to media type and residual-risk tolerance. Clear is appropriate
  for media that will remain within the organization's control; Purge
  is the minimum when media leaves organizational control and will be
  reused; Destroy when the media cannot be reliably purged or when
  residual-risk tolerance is zero
- Media inventory: know which devices have held CUI so sanitization
  applies to the right population. Loaner laptops, replaced drives,
  decommissioned servers, end-of-life workstations all qualify
- Sanitization record per event: method used, operator, date,
  verification result, asset identifier. The record is the evidence
  an assessor will request
- Pre-destination sanitization for MA.L2-3.7.3 off-site maintenance:
  Purge or Destroy before the equipment departs when the vendor is
  not under a written agreement specifying CUI handling requirements
- Print media sanitization: CUI printouts go through cross-cut
  shredders or equivalent destruction path. Paper recycling is not
  sanitization
- Optical media (CDs, DVDs) and magnetic media (tapes): physical
  destruction is typically simpler and more reliable than purging;
  dedicated destruction services available for high-volume disposal

**Evidence to collect:**
- Sanitization policy naming SP 800-88 and the organizational
  mapping of media types to methods
- Sanitization records covering a representative cross-section of
  media types
- Destruction service agreements if third-party disposal is used
- Post-sanitization verification records (degaussing confirmation,
  crypto-erase command logs, physical destruction witness records)
- Media inventory tied to the sanitization-eligible population

**Common mistakes:**
- Drive reformatting treated as sanitization; file-level delete or
  quick format leaves data recoverable
- Optical media sent to standard paper recycling
- Vendor destruction services used without certificate-of-destruction
  records
- Sanitization performed but never verified; no operator signature
  or test-read confirmation
- Loaner laptops returned to vendor without sanitization because
  "the vendor handles it"; vendor agreement does not specify CUI
  handling

---

## Level 2 Practices

### MP.L2-3.8.1 — Protect System Media

**Requirement:** Protect (i.e., physically control and securely
store) system media containing CUI, both paper and digital.

**Why it matters:** Physical control over media is the prerequisite
for everything else MP requires. Access controls, marking, and
accountability all presume the media is in a location and state the
organization can enforce rules over.

**Implementation guidance:**
- Secure storage for digital media: locked cabinets, safes,
  controlled server rooms, access-limited file shares for network
  storage. Storage tier matched to CUI sensitivity
- Secure storage for paper: locked file cabinets for active documents,
  secure off-site storage for archived material, clean-desk discipline
  when CUI is checked out for use
- Physical control during use: CUI documents and media do not leave
  designated work areas without accountability (check-in/check-out or
  transport procedure per MP.L2-3.8.5)
- Reciprocal with PE: physical facility controls from PE.L1-3.10.1
  and PE.L1-3.10.5 are the containing layer; MP.L2-3.8.1 adds
  media-specific controls inside that containment

**Evidence to collect:**
- Media storage inventory and location records
- Secure storage equipment documentation (safes, locked cabinets,
  access mechanisms)
- Clean-desk policy and audit records
- Photos or walkthroughs of storage areas for assessor review

**Common mistakes:**
- Paper CUI left on desks overnight or in conference rooms
- Backup tapes stored in an unlocked utility closet
- USB drives containing CUI kept in personal drawer rather than
  controlled storage
- Network shares with CUI accessible by the full organization
  because access controls were never tightened

---

### MP.L2-3.8.2 — Limit Media Access to Authorized Users

**Requirement:** Limit access to CUI on system media to authorized
users.

**Why it matters:** Physical control keeps media in the right place;
access control keeps the right people touching it. Both are required.
An authorized-users list without an access mechanism is a filing
exercise; an access mechanism without a defined users list is
security theater.

**Implementation guidance:**
- Authorized-users definition tied to AC practices: the set of
  individuals cleared, trained, and business-justified to handle CUI
  media
- Access mechanisms matched to media type: combination locks on
  cabinets, cryptographic access to encrypted drives, file-share
  ACLs for network storage, key control for paper archives
- Access logging where feasible: who opened the safe, who checked
  out the document, who accessed the encrypted volume
- Periodic access review: the authorized-users list reconciled
  against current role assignments, with removals driven by
  PS.L2-3.9.2 personnel actions
- Guest and contractor access: explicit authorization, time-bounded,
  logged

**Evidence to collect:**
- Authorized-users list for media access, tied to personnel records
- Access control configuration for media storage (lock combinations,
  ACLs, key inventories)
- Access log samples where logging is implemented
- Periodic access review records

**Common mistakes:**
- Combination on the file cabinet known to everyone in the building
- Authorized-users list in policy but never reconciled against HR
- Contractor given permanent access because time-bounded access was
  "inconvenient"
- Access logs collected but never reviewed

---

### MP.L2-3.8.4 — Mark Media With CUI Markings

**Requirement:** Mark media with necessary CUI markings and
distribution limitations.

**Why it matters:** Marking is how recipients know what they are
handling. Without marking, an authorized recipient cannot distinguish
CUI from non-CUI, and downstream controls (sanitization, encrypted
transport, access restriction) cannot be applied selectively.

**Implementation guidance:**
- Marking standard: 32 CFR Part 2002 CUI marking requirements and the
  CUI Registry categories. Banner markings at the top, portion
  markings on each portion, and dissemination markings as required
- Digital media: cover page, file-level headers, and where applicable
  embedded watermarks identifying CUI status
- Physical media: exterior label clearly visible, interior label
  where applicable (tape cartridge exterior and internal index)
- Dissemination controls under the CUI Registry: FEDCON (Federal
  Government and contractors only), NOCON (no contractor access),
  RELTO (releasable to specified entities), and other controls
  defined in 32 CFR 2002.16 and applied per the CUI category the
  information belongs to. NOFORN is a classified-system marking
  under EO 13526, not a CUI dissemination control, and does not
  apply to standalone unclassified CUI
- Re-marking on reuse: if media is sanitized and reused, old
  markings removed or overwritten

**Evidence to collect:**
- Marking policy referencing 32 CFR 2002 and the CUI Registry
- Sample marked media (redacted screenshots or photos of labels)
- Training records for personnel responsible for applying markings
- CUI Registry category mapping for the organization's CUI types

**Common mistakes:**
- Digital files stored with CUI content but no markings; recipients
  cannot tell without reading the body
- Backup tapes unlabeled; recovery later cannot distinguish CUI
  backups from non-CUI backups
- Marking applied inconsistently across print and digital versions
  of the same document
- Legacy FOUO markings retained without CUI-era equivalents

---

### MP.L2-3.8.5 — Control Media Access and Accountability in Transport

**Requirement:** Control access to media containing CUI and maintain
accountability for media during transport outside of controlled
areas.

**Why it matters:** Media in transport is at its most exposed state.
The facility controls that protect it at rest no longer apply, and
the risk of loss, theft, or mishandling rises. Accountability during
transport is the control that catches deviations while recovery is
still possible.

**Implementation guidance:**
- Transport authorization: who can take CUI media off-site, under
  what circumstances, and to what destinations. Written authorization
  for each event unless under a standing documented procedure
- Chain of custody: signed handoff records at each transfer point.
  Applies to interoffice courier, external shipping service, and
  personnel travel with CUI media
- Packaging: tamper-evident seals, secondary container, shipping
  label that does not disclose the content sensitivity
- Shipping service selection: trackable carriers with signature
  requirements; sensitivity-appropriate service tier
- Personnel-carried media: documented purpose, retention time
  off-site, return confirmation. No overnight storage in personal
  vehicles
- Loss reporting: immediate IR.L2-3.6.1 incident declaration for any
  media loss or suspected loss during transport

**Evidence to collect:**
- Transport authorization policy and sample authorizations
- Chain-of-custody records for recent off-site transport events
- Packaging standards and sample packaging materials
- Shipping carrier agreements with tracking requirements
- Loss-event records and IR declarations tied to transport

**Common mistakes:**
- Courier transport handled verbally without chain-of-custody
  records
- CUI carried in personal luggage without authorization
- Shipping via standard consumer services (no tracking, no
  signature)
- Loss events reported to IT but never escalated to IR intake
- Overnight storage in personal vehicles or hotel rooms without
  physical safeguards

---

### MP.L2-3.8.6 — Cryptographic Mechanisms for Media in Transport

**Requirement:** Implement cryptographic mechanisms to protect the
confidentiality of CUI stored on digital media during transport
unless otherwise protected by alternative physical safeguards.

**Why it matters:** Encryption in transport is the technical control
that keeps CUI confidential when physical custody fails. The
"alternative physical safeguards" exception is real but narrow: it
covers cases like armed courier with continuous custody, not
"the package is in a box."

**Implementation guidance:**
- Full-disk encryption on laptops and removable drives carrying CUI.
  FIPS 140-validated cryptographic modules are required at Level 2
  under SC.L2-3.13.11 regardless of contract language; contracts may
  impose additional specificity (FIPS 140-3 vs 140-2, particular
  module classes) but the validation requirement itself is not
  optional
- File-level or volume-level encryption for media that will be in
  transit but stored unencrypted at destination
- Key management: encryption keys managed separately from the media
  itself; recovery keys escrowed in the organization rather than
  held only by the traveler
- Removable media encryption: USB drives issued with on-device
  encryption (hardware-encrypted drives) or with full-disk encryption
  configured at provisioning
- Alternative physical safeguards: document specifically when and
  how an alternative is being used (e.g., diplomatic pouch, armed
  courier) and why it provides equivalent or stronger protection

**Evidence to collect:**
- Encryption policy for media in transport
- Full-disk encryption enforcement configuration on endpoints
- Hardware-encrypted drive inventory
- Key management documentation
- Alternative-physical-safeguard justifications for any case where
  encryption is not applied

**Common mistakes:**
- BitLocker or FileVault in policy but not enforced on all endpoints
  that carry CUI off-site
- Traveler carries the only copy of the recovery key
- USB drives used for CUI transport without encryption because
  "only for a quick transfer"
- FIPS 140-validated module requirement met for fixed infrastructure
  but not for laptops and removable media

---

### MP.L2-3.8.7 — Control Removable Media Use

**Requirement:** Control the use of removable media on system
components.

**Why it matters:** Removable media is the bidirectional data path
that bypasses most network and endpoint controls. Uncontrolled USB
use is the most common CUI leakage channel and a common malware
injection vector.

**Implementation guidance:**
- Policy on removable media: what types are permitted (organization-
  issued encrypted drives yes; personal USBs no), what can be written
  to it, what can be read from it
- Technical enforcement: endpoint controls that prevent unauthorized
  USB mass-storage mounting, log attempted connections, and prompt
  or block based on device identity. Windows GPO, macOS profile, or
  MDM (Mobile Device Management) enforcement
- Removable-media inventory: organization-issued devices tracked
  like any other asset, with issuance records
- Cross-reference to MA.L2-3.7.4: diagnostic media is a subset of
  removable media and subject to MA pre-connection scanning on top
  of the MP.L2-3.8.7 usage controls

**Evidence to collect:**
- Removable-media policy
- Endpoint-control configuration (GPO, MDM profile, EDR rules)
- Removable-media issuance inventory
- Sample endpoint logs showing blocked or permitted USB events

**Common mistakes:**
- Policy prohibits personal USB use but endpoints do not enforce
- Issued USB drives reconciled at issuance but not at departure;
  former employees retain devices
- Enforcement on Windows only; macOS and Linux endpoints unaddressed
- No audit of what has been written to issued removable media

---

### MP.L2-3.8.8 — Prohibit Unknown-Owner Portable Storage

**Requirement:** Prohibit the use of portable storage devices when
such devices have no identifiable owner.

**Why it matters:** Unknown-owner devices (the USB stick found in
the parking lot, the drive left on a desk) are a classic
social-engineering delivery mechanism. The prohibition removes the
decision point from the user ("should I plug this in?") and makes
the answer structural ("unknown device, do not use").

**Implementation guidance:**
- Explicit policy language prohibiting use of portable storage
  without an identified owner
- Training content covering the unknown-device threat model and the
  prohibition
- Technical overlap with MP.L2-3.8.7: endpoint controls that block
  unknown USB mass-storage devices by default enforce the
  prohibition automatically
- Reporting path: found devices turned in to security for forensic
  examination, not examined by the finder
- Visitor and vendor devices: same policy applies; visitor USB
  drives not connected without identification and authorization

**Evidence to collect:**
- Policy language prohibiting unknown-owner devices
- Training content covering the prohibition
- Found-device reporting and examination records
- Endpoint-control configuration that blocks unknown USB devices
  by default

**Common mistakes:**
- Policy states the prohibition but training does not cover the
  threat model
- Found devices plugged into production endpoints "to see what's
  on them"
- Visitor devices treated as trusted because the visitor is trusted
- Reporting path unclear; found devices sit in a drawer for weeks

---

### MP.L2-3.8.9 — Protect Backup CUI Confidentiality

**Requirement:** Protect the confidentiality of backup CUI at
storage locations.

**Why it matters:** Backups are a complete replica of CUI data,
often held offline and at alternate locations. A breach of backup
storage is equivalent to a breach of production. Backup
confidentiality is a frequently under-engineered control because
backups are not user-facing.

**Implementation guidance:**
- Encryption at rest for backup media, whether on-site or at
  alternate locations. Same FIPS 140 considerations as MP.L2-3.8.6
  in transport
- Access control at backup storage locations matching production
  access standards; lower-than-production controls at backup sites
  is a finding
- Off-site backup locations: vendor agreements specifying CUI
  handling; cloud-backup services under FedRAMP-authorized platforms
  where contract requires FedRAMP
- Backup media marking per MP.L2-3.8.4 applied to backup tapes
  and disks
- Ransomware-resilient backup posture: immutable or air-gapped
  backups protect confidentiality during a production breach only
  if the offline copy is not itself exposed

**Evidence to collect:**
- Backup encryption configuration
- Backup storage location access control evidence
- Vendor agreements for off-site or cloud backup
- Backup-media marking samples
- Backup-location audit records

**Common mistakes:**
- Backup encryption in policy but backup tapes at the off-site
  vendor stored unencrypted
- Off-site vendor access controls weaker than the production
  facility
- Cloud backups in non-FedRAMP regions when contract requires
  FedRAMP authorization
- Backup media unmarked; recovery later cannot distinguish CUI
  backups from non-CUI

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 1 | 8 | 9 |

**Assessment priority:** Start with MP.L1-3.8.3 (sanitization). It
is the only L1 practice, applies to every contractor, and
sanitization failures produce immediate data exposure. Then
MP.L2-3.8.6 (crypto for media in transport) because encryption is
the technical control that covers the largest practical CUI-in-motion
surface (laptops, removable media, shipping). MP.L2-3.8.1 and
MP.L2-3.8.2 (physical control and authorized-users access) together
constitute the at-rest foundation for the other L2 practices.
MP.L2-3.8.7 and MP.L2-3.8.8 (removable and unknown-owner media) are
common finding sources; endpoint enforcement closes both at once.
MP.L2-3.8.4 (marking) is straightforward in policy but easy to miss
in practice; spot-check marked samples during self-assessment.
MP.L2-3.8.9 (backup confidentiality) is the most commonly
under-engineered; review backup practices explicitly.

**Key relationships:**
- Maintenance (MA) invokes MP.L1-3.8.3 sanitization for equipment
  removed off-site under MA.L2-3.7.3 and extends MP discipline to
  diagnostic media under MA.L2-3.7.4
- Physical Protection (PE) carries the facility-level access and
  storage controls that MP.L2-3.8.1 specializes to media, with
  PE.L1-3.10.5 access device management overlapping key control
  for media-storage locks
- System and Communications Protection (SC) supplies the
  FIPS-validated cryptographic mechanisms MP.L2-3.8.6 requires for
  digital media in transport
- Access Control (AC) defines the authorized-users concept
  MP.L2-3.8.2 applies specifically to media, and provides the
  account lifecycle that feeds MP access-list reconciliation
- Incident Response (IR) invokes MP for evidence preservation during
  incidents; DFARS 252.204-7012(e) 90-day media preservation
  obligation sits at the MP/IR intersection
- Identification and Authentication (IA) provides the identity
  proofing that makes MP.L2-3.8.2 and MP.L2-3.8.5 authorized-user
  controls enforceable
