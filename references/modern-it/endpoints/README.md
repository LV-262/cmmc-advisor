# Endpoint Fleet Compliance (Overview)

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); NIST SP 800-53 Rev 5; FedRAMP program documentation
> (fedramp.gov); NIST CMVP (Cryptographic Module Validation Program)
> module registry (csrc.nist.gov/projects/cryptographic-module-validation-program).

## Overview

An "endpoint" in this directory is a user-operated computing
device that handles Controlled Unclassified Information (CUI)
or Federal Contract Information (FCI). That includes laptops,
desktops, tablets, managed mobile devices, and the thin clients
or browsers that terminate Virtual Desktop Infrastructure (VDI)
and Desktop as a Service (DaaS) sessions. The fleet is the
population of those devices under a single management plane.
This hub exists because endpoint controls cluster differently
from server-side controls: a single endpoint can sit inside CUI
scope, security protection scope, and Contractor Risk Managed
Asset scope simultaneously depending on how the user operates
it, and the management capability that makes the device
compliant spans four CMMC domains (CM, SI, SC, IA) rather than
sitting inside one.

CMMC treats endpoints as systems subject to the same practices
as any other system in scope. No domain is named "endpoint
management." The compliance pattern for endpoints is a
composition across five domains:

- Configuration Management (CM) owns baselining and hardening.
- System and Information Integrity (SI) owns anti-malware and
  monitoring.
- System and Communications Protection (SC) owns encryption and
  boundary enforcement.
- Identification and Authentication (IA) owns account and
  credential posture.
- Media Protection (MP) owns sanitization at end of life.

This directory maps that composition explicitly so a contractor
building or auditing a fleet program can trace each control
surface back to its practice anchors.

---

## Scope of this directory

Files currently planned in `references/modern-it/endpoints/`:

- **`README.md`** (this file) — hub, capability-to-practice
  crosswalk, and the capability-versus-product convention. The
  hub is named `README.md` rather than `endpoints-overview.md`
  because the SKILL.md knowledge-base router accepts any file
  path and the `README.md` convention makes the hub
  automatically discoverable when a reader browses the
  directory. The SKILL.md routing table carries a first-class
  row pointing at this file.
- **`macos-fleet.md`** — macOS endpoint capability patterns
  mapped to CMMC.
- **`windows-fleet.md`** — Windows endpoint capability patterns
  mapped to CMMC.
- **`remote-work.md`** — VDI, DaaS, BYOD, mobile, travel, and
  Outside Continental United States (OCONUS) posture mapped to
  CMMC.

Out of scope for this directory:

- Server hardening. Server-side baselining and patch management live
  in the domain practice files directly (CM, SI). Server and
  endpoint patterns diverge enough that combining them in one file
  would blur both.
- Network infrastructure. Firewalls, switches, and router
  configuration are boundary-protection content under
  `references/domains/sc-system-comms.md`.
- Cloud platform posture. AWS GovCloud, Azure Government, and
  GCP Assured Workloads are treated under
  `references/modern-it/cloud-platforms/` (see
  `cloud-selection.md` for the hub, `aws-govcloud.md`,
  `azure-government.md`, and `gcp-assured.md` for per-provider
  detail). The management-plane of an endpoint fleet may run in
  one of those environments; that is covered in the
  cloud-platform files, not here.
- Productivity suite posture. Microsoft 365 GCC and GCC High posture
  lives in `references/modern-it/productivity/microsoft-365-gcc.md`.
  Endpoint files reference it when the productivity suite is part of
  an endpoint's attack surface.
- Server or endpoint FedRAMP Marketplace product recommendations.
  The FedRAMP Marketplace (marketplace.fedramp.gov) is the
  authoritative registry. This directory does not duplicate it. See
  "Capability-versus-product convention" below.

---

## Capability-versus-product convention

**Structural sections in this directory discuss capabilities. Product
names appear only in clearly-marked example sidebars.** This is a
deliberate authoring choice, not a stylistic preference. The
rationale matters, so it is stated in prose rather than buried in a
note.

The endpoint product landscape churns faster than compliance
guidance can track. A single calendar year routinely carries a
vendor acquisition, an End-of-Life (EOL) announcement for a
major management product, a FedRAMP Marketplace status change
(In Process, Authorized, Ready, Removed), and a fresh
Federal Information Processing Standard (FIPS) 140 module
validation cycle. Guidance pinned to a specific product version
ages poorly: six months after authoring, a recommendation may
point at a product that has been re-platformed, acquired, or
lost its authorization. Guidance pinned to a capability stays
valid across those changes, because the CMMC practice the
capability implements did not change.

A reader who needs "do I have Mobile Device Management (MDM) on
macOS for my fleet?" is better served by a stable capability
discussion ("an MDM capability must support supervised enrollment,
configuration profile delivery, and remote wipe") than by a dated
product recommendation ("use Jamf Pro 10.x"). The capability
question is also the one an assessor asks: the assessor verifies
that the capability exists and that evidence shows it operating, not
that a specific brand is installed.

### What this means for contributors

Within this directory, structural content (section bodies,
capability descriptions, control narratives, crosswalk tables) names
capabilities: "configuration baselining," "disk encryption with a
FIPS 140-validated module," "Endpoint Detection and Response (EDR)
agent." Structural content does not name products.

Product names appear only inside an **Examples sidebar** block,
clearly dated and clearly framed as illustrative. The canonical
sidebar format is:

> **Examples as of 2026-04:** Jamf Pro, Microsoft Intune, Mosyle.
> Verify current FedRAMP Marketplace status before selecting. This
> skill does not rank vendors.

Four rules govern every sidebar:

1. Dated. Every sidebar opens with a "as of YYYY-MM" stamp. A
   reader six months later knows the product landscape may have
   moved.
2. Non-ranking. Vendors appear alphabetically, never ranked by
   fit. The skill is a map, not a review site.
3. Marketplace-verification prompt. Every sidebar prompts the
   reader to check the FedRAMP Marketplace directly.
   Authorization status changes on a cadence the skill cannot
   match in-place.
4. No product inside structural claims. A sentence like "FIPS
   validation on $Product covers the filesystem driver" belongs
   in a sidebar, not in a capability paragraph.

### FIPS 140 module citations

Federal Information Processing Standard 140 (FIPS 140, currently
FIPS 140-3 for new validations; FIPS 140-2 modules remain valid
until sunset per the CMVP transition schedule) validated
cryptographic modules are the encryption enforcement mechanism
that SC.L2-3.13.11 requires. Both FIPS 140-2 and FIPS 140-3
validated modules are acceptable for CUI; FIPS 140-2 certificates
remain valid through their CMVP-published transition dates. When an endpoint capability depends on a
specific FIPS-validated module, cite the CMVP certificate number
directly and stamp the verification date. Example form:

> **FIPS 140 status.** Apple CoreCrypto Kernel Module v14.0 is CMVP
> certificate #4832 (verified 2026-04-20 on csrc.nist.gov). Module
> status transitions (Active, Historical, Revoked) occur
> continuously; verify before citing.

A certificate number without a date is unverifiable. A vendor
assertion ("FIPS validated") without a certificate number is not
evidence an assessor will accept. The CMVP module registry at
csrc.nist.gov is the authoritative source.

---

## Endpoint capability to CMMC practice crosswalk

Each row names an endpoint management capability and the CMMC
practices the capability implements or partially implements.
Practice IDs use the canonical CMMC label form
(DOMAIN.LEVEL-3.X.Y). FedRAMP Moderate control anchors appear in
the next section.

| Capability | Primary CMMC practices | Level |
|---|---|---|
| Configuration baselining (golden image, OS hardening) | CM.L2-3.4.1, CM.L2-3.4.2 | L2 |
| Least-functionality enforcement (unused services disabled) | CM.L2-3.4.6, CM.L2-3.4.7 | L2 |
| Application allowlisting / execution policy | CM.L2-3.4.8 | L2 |
| User-installed software control | CM.L2-3.4.9 | L2 |
| Change tracking (endpoint-level config drift detection) | CM.L2-3.4.3 | L2 |
| Disk encryption at rest (FIPS 140-validated module) | SC.L2-3.13.11, SC.L2-3.13.16, MP.L2-3.8.1 | L2 |
| Data-in-transit encryption from the endpoint | SC.L2-3.13.8, SC.L2-3.13.11 | L2 |
| Patch management (operating system and application) | SI.L1-3.14.1, CM.L2-3.4.9 | L1/L2 |
| Anti-malware capability on endpoints | SI.L1-3.14.2, SI.L1-3.14.4, SI.L1-3.14.5 | L1 |
| Endpoint Detection and Response (EDR) — monitoring surface | SI.L2-3.14.3, SI.L2-3.14.6, SI.L2-3.14.7 | L2 |
| Multi-Factor Authentication (MFA) endpoint agent | IA.L2-3.5.3, IA.L2-3.5.4 | L2 |
| Endpoint account identification and authentication | IA.L1-3.5.1, IA.L1-3.5.2 | L1 |
| Screen lock and idle timeout | AC.L2-3.1.10, AC.L2-3.1.11 | L2 |
| Remote wipe / device decommissioning | MP.L1-3.8.3, MP.L2-3.8.1 | L1/L2 |
| Remote access posture (VPN, ZTNA, split-tunnel block) | AC.L2-3.1.12, AC.L2-3.1.13, SC.L2-3.13.7 | L2 |
| External system connection gate (BYOD, contractor laptops) | AC.L1-3.1.20, AC.L2-3.1.21 | L1/L2 |
| Mobile device management (MDM) — overall capability | CM.L2-3.4.1, CM.L2-3.4.2, CM.L2-3.4.6, AC.L2-3.1.18, AC.L2-3.1.19 | L2 |
| Endpoint audit log forwarding to SIEM | AU.L2-3.3.1, AU.L2-3.3.2, AU.L2-3.3.5 | L2 |

A capability that does not appear in this table is either out of
scope for this directory (server-side, network, or cloud-platform
content) or not yet identified. Per-Operating-System files
(`macos-fleet.md`, `windows-fleet.md`) add capability-to-OS
specifics without changing the practice anchors in this table.

---

## FedRAMP Moderate overlap for endpoint capabilities

Endpoint management runs on a management plane. When that management
plane is operated by a FedRAMP Moderate Cloud Service Provider (CSP)
(Microsoft Intune on the Intune cloud service, Jamf Pro on
Jamf Cloud for Government, etc.), the capability inherits
substantial FedRAMP control coverage. Inheritance is not a free pass:
the contractor still configures the capability, operates the agents
on the endpoints, and evidences the result. See
`references/fedramp-gap.md` "Inherited vs shared-responsibility
controls" for the full inheritance taxonomy.

The table below names the FedRAMP Moderate control anchors that
align with endpoint capabilities. It is a pointer, not a
reproduction; the substantive crosswalk with assessor-facing prose
lives in `references/fedramp-gap.md` "CMMC to FedRAMP Moderate
Overlap Crosswalk" and its focused subsections. Read that file for
the inheritance narrative and the control-family deep dives.

| Endpoint capability | FedRAMP Moderate anchor | fedramp-gap.md section |
|---|---|---|
| Configuration baselining and hardening | CM-2, CM-6, CM-7 | "CMMC to FedRAMP Moderate Overlap Crosswalk" (CM) |
| Disk encryption with FIPS-validated module | SC-13, SC-28, SC-28(1) | "FIPS-validated cryptography" |
| Data-in-transit encryption | SC-8, SC-8(1), SC-13 | "FIPS-validated cryptography" |
| MFA on endpoint login and privileged actions | IA-2(1), IA-2(2) | "Multi-factor authentication" |
| Boundary and remote-access posture | SC-7, AC-17, AC-17(2) | "Boundary protection" |
| Endpoint audit logging to SIEM | AU-2, AU-3, AU-6, AU-12 | "Audit and accountability" |
| Anti-malware and EDR monitoring | SI-3, SI-4, SI-4(4) | "CMMC to FedRAMP Moderate Overlap Crosswalk" (SI) |
| Patch management flaw remediation | SI-2 | "CMMC to FedRAMP Moderate Overlap Crosswalk" (SI) |

A contractor whose endpoint management plane is FedRAMP Moderate
authorized typically claims CM-2, CM-6, IA-2 variants, SC-8, SC-13,
SI-2, SI-3, and AU-2/3/6/12 as shared-responsibility inheritance.
The contractor is still responsible for evidencing that the agents
are deployed, the policies are set, and the endpoints report
findings. The CSP's FedRAMP package covers the management plane;
the endpoints are the contractor's.

If the management plane is not FedRAMP Moderate authorized, the
contractor cannot claim inheritance for any of these controls.
Non-FedRAMP management tooling is common (on-premises Active
Directory-joined management servers, self-hosted MDM instances) and
is compliant if the controls are operated correctly; it just
doesn't inherit from a FedRAMP ATO. See
`references/fedramp-gap.md` "The CUI Baseline Decision" for the
DFARS 252.204-7012(b)(2)(ii)(D) requirement and how it applies to
management-plane services that handle CUI metadata.

---

## How to use this directory

Start with this file to locate the capability you care about in
the crosswalk. Then read the Operating System-specific file for
your fleet:

- A macOS fleet sends you to `macos-fleet.md` for MDM
  enrollment, FileVault escrow, Gatekeeper and XProtect posture,
  System Integrity Protection (SIP), and the FIPS 140 posture on
  Apple platforms.
- A Windows fleet sends you to `windows-fleet.md` for Intune and
  co-management patterns, Microsoft Entra join options, BitLocker
  and key escrow, Microsoft Defender for Endpoint posture,
  AppLocker and Windows Defender Application Control (WDAC), and
  FIPS mode tradeoffs.
- Remote work, VDI, DaaS, Bring Your Own Device (BYOD), mobile,
  travel, and OCONUS posture send you to `remote-work.md`, which
  treats devices that are outside the office, outside the
  contractor's direct control, or outside the continental United
  States.

The three Operating System-specific files are authored
incrementally (dev-56av, dev-uwz3, dev-a6ig). If the file you need
is not yet populated, use the capability crosswalk above as the
CMMC-practice anchor and the relevant domain file in
`references/domains/` for the assessor-facing requirement.

When a question spans both a per-Operating-System file and this
hub, this hub owns capability and practice mapping; the per-OS
file owns implementation detail. When a question spans this
directory and a domain practice file, the domain file owns the
assessor-facing requirement language and the evidence list; this
directory owns the how-it-composes-on-endpoints view. When a
question is "capability X or capability Y, which fits our fleet?"
(for example, EDR versus an antivirus-only posture; UEM versus
separate MDM and desktop management), the capability definitions
in the crosswalk and the Terminology section below frame the
decision; product-specific selection belongs in the per-OS file's
Examples sidebar.

---

## Cross-domain relationships

This directory composes across several domain files. Read the
linked practice file when the endpoint-side decision you are making
requires the requirement text or the evidence list:

- **Configuration Management (CM).** Baselining, hardening,
  allowlisting, and user-installed software control anchors live in
  `references/domains/cm-configuration-mgmt.md`.
- **System and Information Integrity (SI).** Patch management,
  anti-malware, EDR monitoring, and advisory intake anchors live in
  `references/domains/si-system-information-integrity.md`.
- **System and Communications Protection (SC).** Disk encryption,
  transport encryption, FIPS validation, and boundary protection
  anchors live in `references/domains/sc-system-comms.md`.
- **Identification and Authentication (IA).** MFA, authentication,
  and password posture anchors live in
  `references/domains/ia-identification-auth.md`.
- **Media Protection (MP).** Endpoint sanitization at reuse or
  disposal anchors live in
  `references/domains/mp-media-protection.md`. The Maintenance (MA)
  domain depends on MP for off-site equipment sanitization.
- **Access Control (AC).** Remote access, external system
  connection, and mobile device access control anchors live in
  `references/domains/ac-access-control.md`.
- **Audit and Accountability (AU).** Endpoint log generation,
  forwarding, and retention anchors live in
  `references/domains/au-audit.md`.
- **CUI Scoping.** Whether an endpoint is a CUI Asset, a Security
  Protection Asset, a Contractor Risk Managed Asset, or out of
  scope is a scoping decision, not an endpoint-management one. See
  `references/scoping-and-cui.md`.

---

## Terminology

Acronyms used across this file and the per-Operating-System files
in this directory.

**MDM (Mobile Device Management).** A management capability that
enrolls a device, delivers configuration profiles and compliance
policies, monitors posture, and can remotely wipe or retire the
device.

**EDR (Endpoint Detection and Response).** A monitoring and response
capability that records endpoint telemetry, detects suspicious
behavior, and supports remote investigation or containment.

**XDR (Extended Detection and Response).** A detection capability
that correlates telemetry across endpoints, identity, email, and
network surfaces. In this directory, XDR appears only when an EDR
discussion explicitly extends beyond endpoint scope.

**UEM (Unified Endpoint Management).** A management capability that
combines MDM for mobile devices with traditional desktop endpoint
management in a single plane.

**DLP (Data Loss Prevention).** A capability that detects, blocks,
or audits CUI moving off an endpoint through email, upload,
clipboard, removable media, or similar exfiltration paths.

**VDI (Virtual Desktop Infrastructure).** A pattern where the user
operates a remote virtual desktop hosted on a server; the endpoint
runs a thin client or browser that terminates the session.

**DaaS (Desktop as a Service).** A VDI variant delivered as a
managed cloud service (Azure Virtual Desktop, Amazon WorkSpaces,
Windows 365, Citrix DaaS). The desktop runs in the service
provider's cloud.

**BYOD (Bring Your Own Device).** A pattern where the user's
personal device accesses contractor systems or data. For CUI, BYOD
is usually not appropriate; see `remote-work.md` for the decision
tree.

**ZTNA (Zero Trust Network Access).** A remote access pattern that
replaces a perimeter-style VPN with per-session, identity-driven,
policy-evaluated access to specific applications.

**CMVP (Cryptographic Module Validation Program).** The NIST
program that validates cryptographic modules against FIPS 140-2 or
FIPS 140-3 and publishes the module certificate registry.

**FIPS 140 (Federal Information Processing Standard 140).** The
federal standard for cryptographic module validation. FIPS 140-3
is current for new validations; FIPS 140-2 modules remain valid
through CMVP-published transition dates.

**SIP (System Integrity Protection).** An Apple platform mechanism
that restricts root-level modification of protected system paths.
Expanded in `macos-fleet.md`.

**WDAC (Windows Defender Application Control).** A Microsoft
application control mechanism. Expanded in `windows-fleet.md`.

**OCONUS (Outside Continental United States).** A posture
distinction that introduces additional policy constraints for
contractor endpoints and remote workers. Expanded in
`remote-work.md`.

---

## Versioning and drift

This file tracks capability-to-practice mapping, which is stable as
long as NIST SP 800-171 Rev 2 remains the CMMC safeguarding
baseline. If CMMC adopts NIST SP 800-171 Rev 3 (see
`references/rev3-transition.md` for current status), the crosswalk
table requires full re-authoring rather than delta patches. Rev 3
restructures practice numbering and drops the Basic-versus-Derived
distinction; endpoint-capability mappings anchored to Rev 2
practice identifiers will not survive a Rev 3 transition unchanged.

Product sidebars in the per-Operating-System files and the FedRAMP
Marketplace status of referenced management planes drift on a
faster cadence than the practice mapping. Each sidebar carries its
own date stamp. When the corpus is re-reviewed, sidebars older than
twelve months are candidates for verification against the current
FedRAMP Marketplace state.
