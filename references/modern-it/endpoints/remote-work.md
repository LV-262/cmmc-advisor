# Remote Work, VDI, BYOD, and Mobile Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); DFARS 252.204-7012; FedRAMP Marketplace
> (marketplace.fedramp.gov); DoDI 8551.01 (Ports, Protocols, and
> Services Management); DoDI 8500.01 (Cybersecurity); State
> Department Foreign Clearance Guide (fcg.pentagon.mil); Apple
> Platform Deployment and Android Enterprise documentation.

## Overview

This file maps remote-work capability patterns to CMMC practice
requirements. It covers four operational modes that take an
endpoint out of the contractor's office environment: virtual
desktop delivery from the cloud (VDI and DaaS); remote access
from contractor-owned endpoints (VPN and Zero Trust Network
Access, ZTNA); personally-owned devices accessing contractor
data (BYOD); and mobile devices running iOS or Android. It also
covers travel and Outside Continental United States (OCONUS)
posture, which layers additional constraints on any of the four
modes.

Read this file alongside
`references/modern-it/endpoints/README.md` (capability-versus-
product convention and the endpoint-capability → CMMC-practice
crosswalk), `references/modern-it/endpoints/macos-fleet.md`, and
`references/modern-it/endpoints/windows-fleet.md`. Structural
content here names capabilities; product names appear only in
dated Examples sidebars.

**The boundary question remote work forces.** Every remote-work
pattern asks the same CMMC scoping question: where does CUI
actually land, and which endpoint or session is in scope? A
well-designed VDI pattern keeps CUI inside the cloud session and
never on the local device; the local device becomes a thin
client, out of CUI scope for most practices. A poorly-designed
VPN pattern downloads CUI onto the laptop; the laptop is fully
in scope. A BYOD pattern where CUI touches the personal device
puts that personal device in CUI scope, which is usually not
survivable. Treat every pattern choice below as a scoping
decision first and a technical decision second. See
`references/scoping-and-cui.md` for the scoping taxonomy.

---

## Scope of this file

Covered:

- VDI and DaaS delivery patterns for CUI work.
- Contractor-owned endpoint remote access (VPN and ZTNA) when the
  device operates off the contractor's network.
- Home office physical posture and the PE.L2-3.10.6 alternate
  work site practice.
- BYOD decision and requirements if allowed.
- iOS and Android mobile device management when mobile is used
  for CUI or FCI.
- Travel and OCONUS posture for contractor endpoints.

Not covered:

- Per-OS endpoint management detail. macOS lives in
  `macos-fleet.md`; Windows lives in `windows-fleet.md`. This
  file cites those files when a capability is OS-specific.
- Cloud platform posture. Azure Government, AWS GovCloud, and
  GCP Assured Workloads are treated under
  `references/modern-it/cloud-platforms/`; see
  `cloud-selection.md` for the platform-selection hub and the
  per-provider files (`aws-govcloud.md`,
  `azure-government.md`, `gcp-assured.md`) for DaaS/VDI
  platform posture including AVD, WorkSpaces, and Windows 365
  hosting.
- Physical facility security for primary contractor offices.
  Alternate work sites are covered here; primary facilities live
  in the PE domain file directly.
- ITAR and export-control posture for remote workers handling
  defense articles or technical data. Those carry additional
  regulatory constraints beyond CMMC; the contractor's export
  control manual is the primary reference.

---

## VDI and DaaS for CUI

**Capability.** Virtual Desktop Infrastructure (VDI) delivers a
desktop operating system as a remote session from a server or
cloud-hosted virtual machine. Desktop as a Service (DaaS) is the
managed-cloud variant of VDI. The user's local device becomes a
thin client or browser-based terminal; the desktop, its
applications, and the data they process run in the cloud. When
the cloud hosting the virtual desktop is FedRAMP Moderate
authorized or higher and appropriately configured, CUI can be
processed inside the session without landing on the local
device. This is the strongest remote-work pattern for CUI work
because it compresses the CUI boundary into the cloud tenancy
and keeps local endpoints out of direct CUI scope.

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration, applied to the virtual desktop image),
CM.L2-3.4.2 (configuration enforcement), AC.L2-3.1.3 (CUI flow
control across the session boundary), SC.L2-3.13.4 (shared
resource control on the multi-tenant infrastructure),
SC.L2-3.13.16 (data at rest encryption on the virtual volumes),
AC.L2-3.1.12 (remote access monitoring), and AC.L2-3.1.13
(remote access encryption for the session transport).

**Implementation notes.**

- Select a DaaS or VDI service whose FedRAMP authorization level
  matches the CUI requirement. DFARS 252.204-7012(b)(2)(ii)(D)
  requires FedRAMP Moderate equivalence for CSPs handling CUI.
- Session containment policies decide the boundary. Disable
  clipboard copy-out, printer redirection, USB device
  redirection, and local drive mapping from the session to the
  local device unless a specific CUI-handling workflow requires
  an exception. Each exception widens the CUI boundary to
  include the local device.
- Persistent versus non-persistent images: non-persistent
  desktops (discarded at logout) are stronger from a
  configuration-drift perspective and cleaner for forensic
  reset. Persistent desktops are often required for
  development environments with long-running build state.
- Identity integration: the virtual desktop must authenticate
  against the contractor's identity provider with MFA at the
  session boundary, not at the local device alone.
- Local device hardening still matters. A compromised local
  device can screen-capture the session, keylog the password, or
  route traffic through an attacker-controlled proxy. The local
  device is typically a Contractor Risk Managed Asset under the
  scoping taxonomy; it still needs baseline hardening per
  `macos-fleet.md` or `windows-fleet.md`.

**FedRAMP authorization status of named services (verified
2026-04-21).** Several commonly-considered DaaS services carry
FedRAMP authorizations. Authorization levels and package
identifiers cycle; verify on marketplace.fedramp.gov before
citing a specific package ID in an SSP.

- Microsoft Azure Virtual Desktop (AVD) operates on Azure.
  Azure Commercial is FedRAMP High. Azure Government is FedRAMP
  High and aligned with IL5. AVD in Azure Government or Azure
  Government Secret is the typical contractor path for CUI.
- Amazon WorkSpaces in AWS GovCloud operates inside the AWS
  GovCloud tenancy (FedRAMP High / IL5). Commercial AWS
  WorkSpaces is not in GovCloud and typically not appropriate
  for CUI.
- Windows 365 Cloud PC has GCC and GCC High variants. Verify
  which variant the contractor is licensed for; commercial
  Windows 365 is not authorized for CUI.
- Citrix DaaS offers a Government service tier separate from
  commercial. Verify the specific service edition's FedRAMP
  authorization.

**Evidence to collect.**

- DaaS service selection document citing the specific service
  edition, its FedRAMP Marketplace package identifier, and the
  date of SSP authoring.
- Session containment policy export showing clipboard, printer,
  USB, and drive-mapping controls.
- Virtual desktop golden-image configuration export (the
  baseline CM.L2-3.4.1 evidence applied at the image level).
- Identity integration documentation showing MFA at the session
  boundary.

**Common mistakes.**

- Selecting a DaaS service edition outside the appropriate
  FedRAMP tenancy (commercial rather than government, for
  example) and discovering during assessment that the CSP
  equivalence requirement is unmet.
- Leaving clipboard and USB redirection enabled by default
  because user friction was flagged during pilot. Every
  redirection path is a documented CUI egress that must be
  controlled.
- Treating the local thin client as out of scope entirely. Local
  devices participating in a CUI session are Contractor Risk
  Managed Assets at minimum.

---

## Remote access: VPN and Zero Trust Network Access

**Capability.** When contractor-owned endpoints operate off the
contractor's office network, they reach internal resources
through a Virtual Private Network (VPN) or a
Zero Trust Network Access (ZTNA) service. VPN extends the contractor's network
perimeter to the remote endpoint and authenticates the endpoint
into that perimeter. ZTNA flips the model: each session is
authenticated and authorized per-application, with no
full-network extension. Both patterns carry FIPS-validated
transport encryption when configured correctly.

**CMMC practices implemented.** AC.L2-3.1.12 (remote access
monitoring), AC.L2-3.1.13 (remote access cryptographic
protection), AC.L2-3.1.14 (remote access routing through
managed access control points), AC.L2-3.1.15 (remote access
authorization for privileged functions), SC.L2-3.13.7 (split
tunneling prevention), SC.L2-3.13.8 (transmission
confidentiality and integrity), and IA.L2-3.5.3 (MFA for remote
access).

**Implementation notes.**

- Enforce MFA at the remote access gate, regardless of whether
  the user is on a contractor-issued laptop. The endpoint-based
  posture check is complementary, not a replacement.
- Disable split tunneling. SC.L2-3.13.7 requires that remote
  access sessions route protected traffic through the managed
  access control point; split tunneling allows the remote
  endpoint to bypass the control point for some traffic, which
  undermines the practice. Some ZTNA patterns achieve the same
  objective through per-application tunneling rather than
  full-network tunneling; the practice intent (no bypass of
  managed control points for CUI-relevant traffic) is the
  assessor-facing requirement.
- Endpoint posture check at the VPN or ZTNA gate should verify
  disk encryption, EDR reporting, patch currency, and screen
  lock policy before admitting the session. Non-compliant
  endpoints should be denied or routed to a remediation
  enclave.
- Cryptographic transport must be FIPS-validated. For VPN,
  verify the selected cipher suites and the TLS or IPsec
  implementation is FIPS-compliant. For ZTNA, verify the same
  for the mTLS or QUIC transport.
- Log every remote access session establishment, authentication,
  and termination to the SIEM per `macos-fleet.md` or
  `windows-fleet.md` "Centralized logging to SIEM."

**Evidence to collect.**

- VPN or ZTNA configuration export showing authentication
  method, split-tunneling setting, and cipher suite selection.
- Endpoint posture policy export showing the admission
  prerequisites.
- Remote access session log sample from the SIEM.
- Cryptographic validation documentation for the VPN or ZTNA
  service's transport.

**Common mistakes.**

- Allowing split tunneling "for performance" and citing the
  split-tunnel prevention practice as met by the VPN existing.
  An assessor will ask to see the split-tunneling configuration.
- Treating MFA on the endpoint as sufficient and skipping MFA at
  the gate. The gate must authenticate the session
  independently.
- Configuring an older VPN protocol (L2TP/PPTP) without
  FIPS-validated transport and citing SC.L2-3.13.8 as met.
- Assuming VPN or ZTNA encryption covers CUI content. The
  transport is protected; the endpoint still receives CUI
  into local files, clipboard, printer queue, or email
  client unless endpoint-side DLP or containerization
  policies stop it. Unlike a DaaS session where the
  container is the CUI boundary, a VPN session puts CUI on
  the local laptop by design and the laptop must therefore
  be a fully-managed CUI endpoint (see `macos-fleet.md` or
  `windows-fleet.md`).

---

## Home office physical posture

**Capability.** A contractor employee working from home operates
in a physical environment the contractor does not own and only
partly controls. CMMC Practice PE.L2-3.10.6 (safeguard CUI at
alternate work sites) is the direct anchor: the contractor must
extend enough of its physical-access and environmental controls
to remote work locations that CUI is not exposed through the
physical dimension.

**CMMC practices implemented.** PE.L2-3.10.6 (alternate work
site CUI safeguards) is the primary anchor. Related: PE.L1-3.10.1
(limit physical access) and PE.L1-3.10.5 (control physical
access devices) apply at the home office for CUI-bearing
devices; these practices are implemented through policy and
training at the alternate work site rather than through the
primary facility's access control system.

**Implementation notes.**

- Written remote work policy that names the expectations: CUI
  work happens in a private space, screens are not visible to
  non-authorized household members or visitors, paper CUI is
  stored in a lockable container, screen auto-lock is enforced,
  and the workstation is powered down or locked when unattended.
- Endpoint-level controls (screen lock timeout, encryption,
  password requirements) carry the enforcement weight that a
  primary facility would carry through badge readers and CCTV.
- Physical access to the endpoint itself (device theft scenario)
  is handled by full-disk encryption and remote-wipe capability
  through the MDM. PE.L1-3.10.5 physical access device control
  applies: the laptop is a CUI-bearing device and must be
  controlled by the employee assigned to it.
- Paper CUI should not routinely be at an alternate work site.
  If it must be (for example, a limited printed-output workflow
  for a specific contract), the remote work policy names the
  storage requirement (lockable container) and the disposal
  requirement (cross-cut shredder or destruction service).
- Training is the mitigation for controls the contractor cannot
  technically enforce. AT domain practices (AT.L2-3.2.1,
  AT.L2-3.2.2) carry the remote-worker awareness requirement;
  see `references/domains/at-awareness-training.md`.

**Evidence to collect.**

- Remote work policy document naming the alternate work site
  expectations.
- Employee acknowledgment record for the remote work policy.
- Training records covering the remote-worker module.
- Incident records (if any) for alternate-work-site physical
  security events.

**Common mistakes.**

- Treating remote work as implicitly compliant because "the
  laptop is encrypted." Encryption handles some scenarios
  (device theft); it does not handle screen-visibility,
  household-member exposure, or paper CUI.
- Allowing printing of CUI to a home printer connected by USB or
  Wi-Fi without any policy on storage or disposal. Paper CUI at
  home is a common audit finding.
- Having no alternate-work-site policy at all, then citing
  PE.L2-3.10.6 as "inherited from the office facility."
  Assessors read this as an unmet practice.

---

## Bring Your Own Device (BYOD)

**Default recommendation: do not allow BYOD for CUI work.** A
personally-owned device used for CUI work brings the device into
CUI scope. Every CUI-scope CMMC practice that applies to
contractor-owned endpoints applies equally to the BYOD device,
and the contractor has no legal or operational authority to
enforce most of them on a device the contractor does not own.
The common failure path is that the contractor permits BYOD,
cannot enforce the necessary controls, and discovers during
assessment that the personal devices are un-managed CUI-bearing
assets. **The expected posture for CUI fleets is contractor-
issued devices only.** BYOD for FCI-only work (no CUI) is a
lower-risk decision; BYOD for CUI is a posture that consumes
more operational effort than issuing devices.

**If BYOD is allowed for CUI, the contractor accepts the
following obligations.**

**CMMC practices implemented (or that must be).** AC.L1-3.1.20
(external system connection), AC.L1-3.1.22 (publicly accessible
content, by extension when the personal device is multi-purpose),
CM.L2-3.4.1 and CM.L2-3.4.2 (baseline configuration and
enforcement on the personal device), SC.L2-3.13.11 (FIPS-
validated encryption of CUI on the personal device), and
IA.L2-3.5.3 (MFA to access CUI from the personal device).

**Implementation notes.**

- Containerization is the survivable BYOD path. The personal
  device hosts a managed container (or a managed profile, for
  mobile) that holds CUI-adjacent applications and data; the
  container is encrypted and wiped independently of the
  personal side. Without containerization, BYOD for CUI is not
  operationally feasible.
- A written BYOD agreement names the contractor's right to: wipe
  the managed container on employment separation, audit the
  container, enforce device posture requirements (OS version,
  disk encryption, screen lock), and require specific software
  (the MDM agent, the EDR container, the VPN client).
- VDI or DaaS delivery through a browser on the personal device
  is the better alternative where feasible. The personal device
  becomes a thin client; CUI never lands on it; the BYOD scope
  collapses.
- Legal and HR review is required before BYOD for CUI is
  implemented. Employer access to a personal device raises
  privacy and labor-law questions that vary by jurisdiction.

**Evidence to collect.**

- Written policy naming BYOD as disallowed (for the common
  default posture) or stating the allowance with its conditions.
- If BYOD is allowed: signed BYOD agreements, container
  deployment records, enrollment evidence showing the personal
  devices are managed, posture-compliance reports for the
  managed containers.

**Common mistakes.**

- "Informal BYOD" where an employee uses a personal laptop for
  CUI work without a formal agreement and without managed
  container deployment. This is the most common audit finding
  in BYOD scenarios.
- Allowing BYOD to reduce hardware cost, then discovering the
  operational cost (MDM licensing, container deployment, legal
  review) exceeds the hardware cost saved.
- Treating a bare MDM enrollment as sufficient BYOD control.
  MDM on a personal device can enforce some posture, but
  without a container it cannot separate CUI from personal
  data.

---

## Mobile device management for iOS and Android

**Capability.** When mobile devices (smartphones and tablets
running iOS or Android) access CUI or FCI, they are endpoints in
the fleet and require MDM enrollment and configuration. iOS and
Android differ in management primitives but converge on similar
capability patterns: device or user enrollment, containerization
through a managed profile or work profile, posture compliance
checks, and remote wipe.

**CMMC practices implemented.** CM.L2-3.4.1 and CM.L2-3.4.2
(baseline configuration and enforcement), AC.L2-3.1.18 (mobile
device connection control), AC.L2-3.1.19 (mobile device
encryption), SC.L2-3.13.11 (FIPS-validated encryption),
SC.L2-3.13.16 (data at rest encryption, applied to mobile
storage), IA.L2-3.5.3 (MFA for mobile access to CUI), and
AC.L2-3.1.10 (session lock for mobile screen lock).

**Implementation notes for iOS.**

- Device enrollment via Apple Business Manager and
  Automated Device Enrollment (ADE) puts iOS devices in
  supervised mode
  equivalent to the macOS pattern. Supervised iOS devices
  support the restriction payloads (disable iCloud sync, force
  managed open-in, restrict application installation) that CUI
  posture requires.
- User enrollment (without supervision) is the typical BYOD
  path for iOS. It carves out a managed container where work
  apps and data live; personal apps are unaffected and the
  contractor cannot access them.
- Managed Open-In (under supervised or user-enrollment) controls
  whether a file opened in one app can be opened or shared to
  another. Enabling managed Open-In for CUI apps is how the
  iOS-level container boundary is enforced.
- iOS encryption is always on and is backed by the Secure
  Enclave on devices with one (effectively every recent iOS
  device). The encryption module carries CMVP validation under
  Apple's vendor listing; see the FIPS 140 posture note in
  `macos-fleet.md` for the Apple Corecrypto validation pattern.
- Per-app VPN delivers the remote-access transport for managed
  apps without putting the entire device on the VPN. Configure
  via MDM profile.

**Implementation notes for Android.**

- Android Enterprise with a work profile is the typical BYOD
  containerization path. The work profile is a managed
  Android user isolated from the personal profile; the
  contractor controls the work profile and can wipe it
  independently.
- Fully-managed Android (company-owned, enrolled through
  zero-touch or QR-code provisioning) is the parallel to iOS
  supervised mode. The MDM controls the entire device.
- Android encryption is on by default on devices shipped with
  Android 10 or later (file-based encryption). Hardware-backed
  key storage through the Keymaster/Keystore provides the
  equivalent of Secure Enclave protection on Android devices
  with a Trusted Execution Environment (TEE) or StrongBox
  secure element.
- Verify the device vendor and model support the security
  features required. Low-cost Android devices sometimes ship
  without hardware-backed key storage or with delayed security
  update delivery.

**Evidence to collect.**

- MDM inventory listing every managed mobile device with OS
  version, enrollment mode, and managed-profile state.
- Configuration profile or managed-profile policy exports for
  the CUI posture.
- Compliance report showing devices meeting encryption, screen
  lock, and OS-version policy.
- For Android fleets: allowed-device-model list naming the
  vendor's security-update commitment window and the
  hardware-backed key storage status (Keymaster/Keystore TEE
  or StrongBox) for each approved model.

**Common mistakes.**

- Enrolling iOS devices in user-enrollment mode for a fully-
  company-owned fleet, losing the supervision restrictions that
  would otherwise be available.
- Allowing Android devices from vendors that ship delayed or no
  security updates. A device that will not receive patches
  within SI.L1-3.14.1 flaw remediation timeframes is a failing
  device.
- Relying on a mobile device's lock screen as the only
  authentication. CUI applications on the device should
  themselves require authentication (biometric or passcode on
  the container, MFA on the CUI application).

---

## Travel posture and OCONUS constraints

**Capability.** Contractor employees travel with endpoints both
domestically and internationally. International travel, or
travel to higher-risk domestic locations (certain conferences,
border crossings), changes the threat model and may introduce
regulatory constraints. "Outside Continental United States"
(OCONUS) covers international travel and travel to U.S.
territories.

**CMMC practices implemented.** PE.L2-3.10.6 (alternate work
site safeguards apply to the temporary work location),
AC.L1-3.1.20 (external system connections, when using hotel or
conference Wi-Fi), AC.L2-3.1.12 (remote access monitoring, for
the sessions initiated during travel), SC.L2-3.13.7 (split
tunneling prevention on travel-network connections), and
MP.L2-3.8.1 (physical media protection, for devices crossing
borders).

**Implementation notes.**

- Travel-specific device posture: consider issuing a
  "travel laptop" loaned for the trip with only the data and
  applications needed, rather than sending the employee's
  primary laptop. At return, the travel laptop is re-imaged as
  a standard precaution.
- Full-disk encryption is mandatory, not optional, for traveling
  devices. Loss or theft during travel is the common scenario;
  encryption is the control that makes the loss contained.
- TPM+PIN or BitLocker PIN-at-boot (Windows) or FileVault with
  a strong password (macOS) add a second factor against a
  stolen device. Consider enforcing these for travel endpoints.
- OCONUS-specific constraints vary by destination country and
  by contract clause:
  - Some countries require declaration of encrypted devices at
    customs; some restrict cryptographic imports.
  - Defense contracts with ITAR or export-controlled technical
    data add significant OCONUS restrictions; consult the
    export control manual and Contracting Officer guidance
    before travel.
  - The State Department Foreign Clearance Guide
    (fcg.pentagon.mil) is the primary source for DoD-related
    foreign travel clearance requirements; verify current
    requirements for the destination country.
  - Contract-specific OCONUS clauses may prohibit access to CUI
    from certain countries; DFARS flow-downs and agency-
    specific policy govern here. The Contracting Officer
    Representative is the authoritative interpreter.
- Remote access to CUI from certain countries may be blocked
  regardless of contract. Geofencing at the VPN or ZTNA gate
  is the mechanism.

**Evidence to collect.**

- Travel policy naming pre-travel, during-travel, and post-
  travel requirements.
- Pre-travel checklist completed per trip (encryption verified,
  data minimization confirmed, travel laptop assignment if
  applicable).
- Geofencing configuration on the VPN or ZTNA gate.
- Post-travel re-imaging or validation records for high-risk
  trips. OCONUS travel and travel to known
  targeted-surveillance venues are the typical high-risk
  triggers; the contractor's travel policy should name the
  specific conditions that require post-travel re-imaging or
  a forensic EDR sweep before the device re-enters the CUI
  network.

**Common mistakes.**

- Letting employees travel OCONUS with their primary CUI-bearing
  laptop and no travel-specific preparation. The primary
  laptop returns compromised or loses data at a border check;
  neither was anticipated.
- Treating geofencing as blocking only connections from blocked
  countries, without realizing commercial VPN endpoints can
  route traffic through apparent non-blocked origins. Geofence
  at multiple layers or require hardware-token MFA that
  resists geographic relocation.
- Assuming ITAR or export-controlled data handling is addressed
  by CMMC. It is not; ITAR carries a separate regulatory
  regime that imposes OCONUS controls CMMC does not cover.

---

## Cross-domain anchors

Remote-work guidance composes with the domain practice files for
assessor-facing requirement text and evidence lists:

- Physical Protection (PE).
  `references/domains/pe-physical-protection.md` for PE.L1-3.10.1
  through PE.L1-3.10.5 and PE.L2-3.10.6.
- Access Control (AC). `references/domains/ac-access-control.md`
  for AC.L1-3.1.20, AC.L2-3.1.12 through AC.L2-3.1.15, AC.L2-3.1.18,
  and AC.L2-3.1.19.
- System and Communications Protection (SC).
  `references/domains/sc-system-comms.md` for SC.L2-3.13.7
  and SC.L2-3.13.8.
- Configuration Management (CM).
  `references/domains/cm-configuration-mgmt.md` for
  CM.L2-3.4.1 and CM.L2-3.4.2 applied to virtual desktop or
  managed-container baselines.
- Identification and Authentication (IA).
  `references/domains/ia-identification-auth.md` for remote-
  access MFA.
- Awareness and Training (AT).
  `references/domains/at-awareness-training.md` for the
  remote-worker training module.
- Media Protection (MP).
  `references/domains/mp-media-protection.md` for traveling-
  device sanitization.
- CUI Scoping. `references/scoping-and-cui.md` for the scope
  decision that every pattern above hinges on.

For FedRAMP Moderate inheritance when DaaS, VDI, or remote
access services run on FedRAMP-authorized tenancies, see
`references/fedramp-gap.md` "Inherited vs shared-responsibility
controls."

---

## Examples as of 2026-04

> **VDI and DaaS examples as of 2026-04:** Amazon WorkSpaces
> (GovCloud), Citrix DaaS Government, Microsoft Azure Virtual
> Desktop (Azure Government), Microsoft Windows 365 Cloud PC
> (GCC High), VMware Horizon Cloud on Azure Government.
> Listed alphabetically. Verify current FedRAMP Marketplace
> status and authorization package identifier on
> marketplace.fedramp.gov before selecting.

> **Remote access examples as of 2026-04:** Cisco AnyConnect
> Secure Mobility Client, Cloudflare Access, Microsoft Entra
> Private Access, Netskope Private Access, Palo Alto Networks
> GlobalProtect, Palo Alto Networks Prisma Access, Zscaler
> Private Access. Listed alphabetically; mix of traditional VPN
> and ZTNA patterns. Verify current FedRAMP Marketplace status
> before selecting.

> **Mobile MDM examples as of 2026-04:** BlackBerry UEM, IBM
> MaaS360, Ivanti Neurons for MDM, Microsoft Intune, VMware
> Workspace ONE. Listed alphabetically. Many desktop MDM
> products also manage mobile devices; see
> `references/modern-it/endpoints/README.md` Examples for the
> desktop-side list. Verify current FedRAMP Marketplace status
> before selecting.

This skill does not rank vendors.

---

## Terminology

Most acronyms used in this file are defined in
`references/modern-it/endpoints/README.md` "Terminology."
Remote-work-specific terms below.

**ADE (Automated Device Enrollment).** Defined in
`macos-fleet.md`; applies equally to iOS supervised enrollment
via Apple Business Manager.

**Android Enterprise.** The Google-provided framework for
enterprise management of Android devices, including
work-profile and fully-managed modes.

**Container (managed container).** A partitioned area on a
device where managed applications and data run, isolated from
the personal or non-managed area of the device.

**ITAR (International Traffic in Arms Regulations).** The U.S.
regulatory regime governing export of defense articles and
defense services, administered by the State Department. CMMC
does not cover ITAR; ITAR imposes additional OCONUS and
foreign-national-access constraints beyond CMMC.

**Managed Open-In.** The iOS mechanism that controls whether a
file or document opened in a managed application can be shared
to unmanaged applications. Configuration-profile delivered.

**Per-app VPN.** A VPN pattern where specific managed
applications tunnel through the VPN while other applications
use the device's direct network connection. Configuration-
profile delivered on iOS and Android.

**StrongBox.** The Android hardware-backed keystore
implementation running in a discrete secure element on
supported devices.

**TEE (Trusted Execution Environment).** A secure area of the
main processor providing isolated execution and storage.
Backs the Android Keymaster and Keystore on devices without
StrongBox.

**Work profile.** The Android Enterprise managed profile
container on a personal device. Separates managed applications
and data from the personal profile.

**ZTNA (Zero Trust Network Access).** Defined in
`references/modern-it/endpoints/README.md` "Terminology."
