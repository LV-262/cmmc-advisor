# macOS Fleet Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); Apple Platform Security Guide (support.apple.com/guide/security);
> Apple Platform Deployment (support.apple.com/guide/deployment);
> NIST CMVP validated modules registry
> (csrc.nist.gov/projects/cryptographic-module-validation-program).

## Overview

This file maps macOS endpoint management capabilities to CMMC
practice requirements. It applies to contractor fleets running
macOS on Mac laptops and desktops used for CUI or FCI work.

Read this file alongside
`references/modern-it/endpoints/README.md`, which carries the
capability-versus-product convention and the endpoint-capability
→ CMMC-practice crosswalk that anchors every section below.
Structural content here names capabilities; product names appear
only in a dated Examples sidebar.

CMMC does not reference macOS by name, and no macOS version or
feature is inherently "compliant" or "non-compliant." The
compliance question is always: can the fleet demonstrate that a
CMMC practice is operating against evidence an assessor will
accept? macOS supplies the capability primitives (configuration
profile delivery, encryption modules, code-signing enforcement,
system integrity mechanisms); the fleet operator composes them
into the practice implementations this file names.

**Apple Silicon versus Intel.** Most security primitives discussed
below have different underlying implementations on Apple Silicon
(M1 family and later) versus Intel Macs. Apple Silicon uses the
Secure Enclave as the key-protection root; Intel Macs use the T2
Security Chip (2018 to 2020) or fall back to software-only key
protection (pre-T2). For new CUI fleet deployments, Apple Silicon
is the expected target. Pre-T2 Intel Macs should be out of the CUI
scope.

---

## Scope of this file

Covered:

- macOS capability patterns on Apple Silicon and T2-generation
  Intel Macs under MDM management.
- CMMC practice mapping for each capability.
- Evidence to collect for each practice.
- Common mistakes specific to macOS.

Not covered:

- Apple Business Manager purchasing, Volume Purchase Program (VPP)
  mechanics, or license administration. Those are procurement
  concerns, not compliance surfaces.
- Detailed MDM product configuration. Product-specific guidance
  belongs to the vendor's own documentation; the Examples sidebar
  at the bottom lists the common products.
- iOS and iPadOS fleet patterns. Mobile endpoint guidance lives
  in `references/modern-it/endpoints/remote-work.md` where
  mobile is treated alongside BYOD and VDI patterns.
- macOS Server. Apple deprecated macOS Server in 2022; contemporary
  fleet management does not rely on it.

---

## MDM enrollment and supervision

**Capability.** A Mobile Device Management (MDM) solution enrolls
each Mac, delivers configuration profiles that set security
policies, monitors compliance, and supports remote lock or wipe.
Automated Device Enrollment (ADE) through Apple Business Manager
puts a Mac into supervised mode during initial setup; supervision
unlocks the restrictions and payloads an MDM can enforce (for
example, disabling iCloud sync, preventing MDM removal, forcing
FileVault activation).

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration), CM.L2-3.4.2 (configuration enforcement),
CM.L2-3.4.6 (least functionality), and AC.L2-3.1.18 (mobile device
connection control) anchor to the MDM capability. Profile-delivered
policies realize the "enforced baseline" that these practices
require.

**Implementation notes.**

- Supervised enrollment via Automated Device Enrollment is the
  baseline posture. Manual (user-initiated) enrollment works for
  legacy or BYOD cases but loses the MDM-removal restriction and
  several payload restrictions.
- Configuration profiles are the primary policy mechanism. Declare
  the CMMC-required settings in profiles: FileVault activation,
  screen lock timeout, software update cadence, firewall state,
  gatekeeper policy, installer restrictions, certificate trust.
- Declarative device management (the successor protocol) is
  supported on recent macOS releases and covers an expanding set
  of payloads; verify the current MDM product supports declarative
  payloads for the settings you enforce.
- Configuration profile key names and payload schemas evolve
  across macOS releases. Specific key names referenced in this
  file (for example `ForceEnableInSetupAssistant`, `askForPassword`)
  are current for macOS 14 and 15; verify against your MDM
  vendor's payload documentation and Apple's developer
  documentation before deploying.
- This guidance applies whether the MDM management plane is
  cloud-hosted on a FedRAMP Moderate CSP or self-hosted on
  contractor infrastructure. FedRAMP inheritance claims apply
  only to cloud-CSP management planes; self-hosted MDM requires
  the contractor to evidence the underlying controls directly.
  See `references/fedramp-gap.md` "Inherited vs shared-
  responsibility controls" for the inheritance taxonomy.
- Compliance state must be observable from the MDM. A profile that
  is queued but not applied is not evidence of enforcement.

**Evidence to collect.**

- Inventory report from the MDM listing every enrolled Mac, its
  OS version, supervision state, and current profile assignment.
- Baseline configuration profile export (XML or equivalent).
- Compliance posture report showing each Mac's deviation from
  baseline, dated at assessment time.

**Common mistakes.**

- Enrolling Macs into MDM without supervision, then being surprised
  when users unenroll themselves and drop out of management.
- Treating MDM enrollment as the compliance evidence without
  exporting the baseline profile or the compliance deviation
  report.
- Running two MDM solutions in parallel with inconsistent profiles
  during a migration. Assessors read this as unenforced baseline.

---

## Apple Business Manager and Apple Configurator

**Capability.** Apple Business Manager (ABM) is the enterprise
portal that assigns devices to an MDM server at purchase time,
manages Managed Apple IDs, and administers app and book purchasing.
Apple Configurator is a macOS utility that can enroll a Mac into
an MDM server post-purchase or re-enroll a device that was not
purchased through an ABM reseller.

**CMMC practices implemented.** ABM itself does not directly
implement a CMMC practice; it is the procurement and enrollment
substrate that makes CM.L2-3.4.1 and CM.L2-3.4.2 feasible at scale
by routing every Mac into a managed configuration from first boot.

**Implementation notes.**

- Purchase Macs through an ABM-linked reseller (Apple itself, or
  an authorized reseller that supports ADE linking) so every new
  Mac enrolls automatically on activation.
- Macs purchased retail can be added to ABM with Apple Configurator
  by running a provisioning workflow once before the Mac is
  handed to the user. The Mac then behaves like an
  ABM-provisioned device.
- Managed Apple IDs are separate from personal Apple IDs and are
  appropriate where the contractor needs to enforce sign-in policy
  on iCloud services. For a CUI fleet that disables iCloud syncing
  entirely, Managed Apple IDs are not required.

**Evidence to collect.**

- ABM device list showing enrollment status and MDM server
  assignment.
- Procurement process document stating that all new Macs purchase
  flows through the ABM reseller or an Apple Configurator
  onboarding step.

**Common mistakes.**

- Buying Macs outside the ABM channel and relying on user-initiated
  enrollment to close the gap. This works functionally but fails
  the "every CUI endpoint is supervised" control posture.

---

## FileVault encryption and key escrow

**Capability.** FileVault is Apple's full-disk encryption feature.
On Apple Silicon, FileVault uses the AES engine in the Secure
Enclave for hardware-accelerated XTS-AES-128 encryption of the
system volume, with keys protected by the Secure Enclave's
hardware root of trust. On T2-era Intel Macs, the T2 chip provides
equivalent key protection. MDM-delivered configuration profiles
activate FileVault and escrow the recovery key to the MDM.

**CMMC practices implemented.** SC.L2-3.13.11 (FIPS-validated
cryptography for CUI protection), SC.L2-3.13.16 (data at rest
encryption), and MP.L2-3.8.1 (physical media protection) anchor
here. MP.L1-3.8.3 (sanitize media before disposal) benefits from
FileVault because cryptographic erasure is the default path for
sanitizing a FileVault-enabled Mac.

**Implementation notes.**

- Force FileVault at enrollment via the MDM configuration profile.
  The user cannot defer; the profile sets `ForceEnableInSetupAssistant`
  or the equivalent payload key.
- Escrow the Personal Recovery Key (PRK) to the MDM so the fleet
  operator can unlock a user's disk without the user's password.
  Store the PRK in the MDM's key escrow with access restricted to
  authorized fleet administrators.
- Rotate PRKs on a defined cadence or after every unlock event.
  Many MDM products automate rotation.
- Cryptographic erasure (destroying the key) is the standard
  sanitization path for FileVault-enabled Macs going through the
  MP.L1-3.8.3 reuse or disposal flow. A factory reset of an Apple
  Silicon Mac cryptographically erases the volume without needing
  physical destruction.

**Evidence to collect.**

- MDM configuration profile XML showing FileVault enforcement
  payload.
- PRK escrow report showing every managed Mac has a recovery key
  escrowed with the MDM.
- Key rotation log if rotation is in place.
- Sanitization records for Macs removed from the fleet showing the
  cryptographic-erasure method used.

**Common mistakes.**

- Activating FileVault without escrowing the recovery key. The Mac
  is encrypted, but the fleet has no way to recover data if the
  user forgets the password, and no authoritative key inventory.
- Relying on the FileVault institutional recovery key (FVIRK)
  approach on modern Macs. Apple deprecated FVIRK for new
  deployments; use the MDM-escrowed PRK pattern.
- Treating FileVault activation as sufficient evidence without
  sampling the escrow state in the MDM.

---

## Gatekeeper, XProtect, and Notarization

**Capability.** Gatekeeper enforces code-signing and Notarization
checks at application launch. Unsigned or un-notarized applications
are blocked by default policy; the user (or an MDM-delivered
policy) can allow specific exceptions. XProtect is Apple's built-in
anti-malware signature engine, updated continuously through a
mechanism independent of the full OS update cycle. XProtect Remediator
actively removes known malware variants when they execute. Together
Gatekeeper, XProtect, and Notarization form the default
application-control substrate on macOS.

**CMMC practices implemented.** CM.L2-3.4.7 (nonessential
functionality restrictions), CM.L2-3.4.8 (application execution
policy), SI.L1-3.14.2 (malicious code protection capability),
SI.L1-3.14.4 (update malicious code protection), and SI.L1-3.14.5
(periodic and real-time scanning).

**Implementation notes.**

- Gatekeeper policy is enforced by default at "App Store and
  identified developers." Configuration profiles can tighten this
  to "App Store only" or can whitelist specific developer IDs for
  internally distributed tools.
- Notarization is Apple's scan-for-malicious-content service
  applied to developer-signed builds. A notarized app carries a
  Notarization ticket stapled into the binary; Gatekeeper verifies
  the ticket at launch.
- XProtect signatures update through the Apple Software Update
  mechanism independent of full OS updates. XProtect updates
  install silently; there is no user-facing update dialog.
  SI.L1-3.14.4 currency discipline here means verifying that the
  XProtect data files on each Mac are current.
- XProtect alone is not an enterprise-grade EDR. It is a baseline
  anti-malware capability. CMMC L2 fleets must pair XProtect with
  a separate EDR product to meet the SI.L2-3.14.6 monitoring and
  SI.L2-3.14.7 unauthorized-use-detection scope; XProtect provides
  detection and remediation for known malware variants, not the
  telemetry and response surface those practices require.

**Evidence to collect.**

- Configuration profile export showing Gatekeeper policy and any
  developer-ID allowlist.
- MDM report of XProtect data file versions across the fleet,
  dated at assessment time.
- Screenshot or export of Gatekeeper/XProtect enforcement state
  from a sample Mac.

**Common mistakes.**

- Disabling Gatekeeper to accommodate a specific unsigned
  internal tool, then forgetting to re-enable it. The fleet now
  runs with code-signing enforcement off on some devices.
- Assuming XProtect is the SI.L2-3.14.6 monitoring capability.
  XProtect is detection and remediation for known malware, not
  the EDR telemetry and response surface.

---

## System Integrity Protection

**Capability.** System Integrity Protection (SIP) restricts
root-level modification of protected system paths and kernel
behaviors. Even a privileged process cannot modify `/System`,
load unsigned kexts, or attach to system processes while SIP is
active. SIP is enabled by default on every Mac and is controlled
only by booting into recovery mode.

**CMMC practices implemented.** CM.L2-3.4.7 (nonessential
functionality restrictions), SC.L2-3.13.2 (architectural design
for security), and SI.L1-3.14.2 (malicious code protection
capability, through attack-surface reduction).

**Implementation notes.**

- SIP is on by default. Do not disable it on fleet Macs. If a
  vendor's installation instructions require disabling SIP, treat
  that as a red flag for whether the tool is appropriate for a
  CUI endpoint.
- SIP status is readable from `csrutil status` in Terminal. MDM
  products generally report SIP state in fleet inventory.
- On Apple Silicon, SIP works alongside the
  Signed System Volume (SSV) mechanism, which cryptographically
  verifies the system partition at boot. SSV further restricts
  modification of the system.

**Evidence to collect.**

- MDM inventory report showing SIP enabled across the fleet.
- Policy document stating the fleet runs with SIP enabled and
  naming the process for any exception.

**Common mistakes.**

- Disabling SIP for developer convenience on engineering-team
  Macs, then leaving it disabled. An engineering Mac handling CUI
  source code or CUI documentation is in scope for the same
  practice enforcement as any other fleet Mac.

---

## Application Firewall

**Capability.** macOS ships with a socket-filter firewall
(`socketfilterfw`) that allows or blocks incoming connections on
a per-application basis. Configuration profiles can set the
firewall to "block all incoming" or to enforce
per-application rules. The firewall is an inbound-connection gate;
it does not inspect outbound traffic.

**CMMC practices implemented.** SC.L1-3.13.1 (boundary
protection). The endpoint firewall is one layer of boundary
protection; the network firewall, CSP security group, and tenancy
edge are the others.

**Implementation notes.**

- Enable the firewall via configuration profile. Block all
  incoming connections unless a service is explicitly required.
- Stealth mode (do not respond to probe traffic) is usually on by
  default through the profile.
- For outbound-connection inspection (needed for EDR-style
  telemetry or data-loss prevention), use an EDR agent or a
  per-endpoint ZTNA client. The macOS Application Firewall does
  not cover that scope.

**Evidence to collect.**

- Configuration profile export showing firewall state.
- MDM inventory report confirming firewall enabled fleet-wide.

**Common mistakes.**

- Treating the Application Firewall as the boundary-protection
  evidence for the full boundary. It is one component; the
  network-side controls also need to be cited.

---

## Endpoint Detection and Response integration

**Capability.** An Endpoint Detection and Response (EDR) agent
deployed on macOS records endpoint telemetry (process events,
file changes, network connections, authentication events), detects
suspicious behavior against a rule engine, and supports remote
investigation or containment. EDR integration on macOS uses
Apple's Endpoint Security framework (since macOS 10.15) rather
than the deprecated kernel-extension pathway.

**CMMC practices implemented.** SI.L2-3.14.3 (security alerts and
advisories intake), SI.L2-3.14.6 (system monitoring and traffic
monitoring), SI.L2-3.14.7 (unauthorized use detection), and
AU.L2-3.3.1 (system audit event generation at the endpoint).

**Implementation notes.**

- EDR agents on macOS request System Extension approval and Full
  Disk Access. MDM configuration profiles can pre-approve the
  Team ID and the system-extension bundle, eliminating the
  user-prompt step that blocks enrollment at scale.
- MDM payload categories involved: `SystemExtensions`,
  `PrivacyPreferencesPolicyControl` (also called TCC), and the
  `EndpointSecurity` entitlement review for the specific vendor.
- Verify the EDR agent does not disable Gatekeeper, SIP, or the
  Application Firewall as part of installation. Any agent that
  requires disabling those is an immediate scope-appropriateness
  question.
- Telemetry export from the EDR to the SIEM is what realizes
  AU.L2-3.3.5 correlation; see "Centralized logging to SIEM"
  below.

**Evidence to collect.**

- Configuration profile showing the System Extension Team ID
  pre-approval payload.
- MDM inventory report showing EDR agent installation and
  health-check state across the fleet.
- Sample EDR alert record routed to the SIEM for an indicator-of-
  compromise test (for example, an EICAR test file or a benign
  advisory-driven detection).

**Common mistakes.**

- Installing the EDR agent without the System Extension
  pre-approval profile; the agent installs but fails to load,
  silently on some Macs.
- Buying an EDR that pre-dates the Endpoint Security framework
  and still uses kernel extensions. Kext-based agents will not
  load on recent macOS versions.

---

## Patch management (software update)

**Capability.** macOS receives security updates through the
Apple Software Update mechanism. MDM-delivered software update
profiles can defer major-version updates, enforce minimum versions,
and schedule install windows. Rapid Security Response (RSR) is a
smaller-scoped update pathway for critical security fixes between
full OS updates.

**CMMC practices implemented.** SI.L1-3.14.1 (flaw remediation)
and CM.L2-3.4.9 (user-installed software control, where third-
party application updates ride alongside OS updates).

**Implementation notes.**

- Deploy a software update configuration profile that sets minor-
  update install deadlines and allows major-version deferrals for
  compatibility testing. Industry-typical deferral: 30 days for
  minor updates, 90 days for major releases, adjusted by the
  organization's risk tolerance.
- Rapid Security Response (RSR) updates are separate from major
  OS updates and should install within days of release. MDM
  payloads support RSR scheduling independent of the main OS
  update cadence.
- Third-party applications (browsers, productivity tools, EDR
  agents) update through their own mechanisms or through the MDM
  app management. SI.L1-3.14.1 covers these alongside OS updates.
- User-installed software outside the MDM app catalog is
  controlled through CM.L2-3.4.9. Gatekeeper and notarization
  provide the execution-policy gate; the fleet-operator's
  software policy defines what users may install.

**Evidence to collect.**

- MDM software update deferral and deadline policy export.
- Fleet patch posture report showing each Mac's OS version and
  RSR state, dated at assessment time.
- Third-party application version inventory from the MDM app
  management report.

**Common mistakes.**

- Indefinitely deferring major-version updates on older hardware.
  When Apple stops shipping security updates for an OS version,
  deferring past that point puts the fleet on an unsupported
  codebase for SI.L1-3.14.1 purposes.
- Assuming Rapid Security Response updates install automatically
  when the MDM profile disables "Install macOS updates
  automatically."

---

## Screen lock and idle timeout

**Capability.** macOS can be configured to lock after a defined
period of inactivity, require password on wake, and limit the
unlock grace period after sleep.

**CMMC practices implemented.** AC.L2-3.1.10 (session lock after
inactivity) and AC.L2-3.1.11 (session termination conditions).

**Implementation notes.**

- Configuration profile keys: `askForPassword` (require password
  after sleep), `askForPasswordDelay` (grace period, typically
  0), `loginWindowIdleTime` or equivalent for the screen saver
  idle timer.
- 15 minutes is the assessor-typical maximum for CUI endpoints;
  shorter timers are stronger. Document the chosen value in the
  SSP with the rationale.
- Force the setting with a profile; do not rely on user
  discretion. User-set preferences can be overridden.

**Evidence to collect.**

- Configuration profile showing the screen lock payload.
- MDM fleet compliance report confirming the profile applies to
  every managed Mac.

**Common mistakes.**

- Setting a generous grace period (for example, 5 minutes) on
  `askForPasswordDelay`. A user stepping away is expected to lock
  the screen immediately when idle, not after an additional
  delay.

---

## Centralized logging to SIEM

**Capability.** macOS emits log data through the Unified Logging
system (`log` command, subsystem-and-category-tagged events). The
fleet operator exports selected log streams to a
Security Information and Event Management (SIEM) platform
for retention, correlation, and review.

**CMMC practices implemented.** AU.L2-3.3.1 (audit event
creation), AU.L2-3.3.2 (user accountability through audit),
AU.L2-3.3.5 (audit correlation), and AU.L2-3.3.7 (authoritative
time source, through network time protocol sync).

**Implementation notes.**

- The macOS Unified Logging system records subsystem-tagged events
  including authentication, MDM command execution, system
  extension events, and application activity. The EDR agent's
  telemetry is usually the richer log source for security
  monitoring; Unified Logging is complementary.
- A log-forwarding agent (built into the EDR, or a standalone
  collector) exports selected streams to the SIEM. The fleet
  operator decides which subsystems to export; the floor is
  authentication events, admin activity, and EDR alerts.
- Time synchronization via `timed` to an authoritative source is
  the AU.L2-3.3.7 anchor. Document the NTP source in the SSP.

**Evidence to collect.**

- Log-forwarder configuration for each Mac (MDM profile export).
- SIEM dashboard or query confirming event arrival from managed
  Macs, dated.
- Time-sync source documentation.

**Common mistakes.**

- Exporting only the EDR alerts to the SIEM without forwarding
  authentication events. AU.L2-3.3.2 user-accountability evidence
  is thin when the SIEM only has detection alerts.
- Local log retention without export. Local logs are lost on
  disk-wipe or compromise; AU.L2-3.3.8 (audit protection) is not
  realized.

---

## FIPS 140 posture on Apple platforms

**Capability.** macOS cryptographic operations are performed by the
Apple Corecrypto module family. Two CMVP-validated modules are
relevant for CUI encryption claims: the Apple Corecrypto Kernel
Module (kernel-mode operations, including XTS-AES for FileVault on
APFS) and the Apple Corecrypto User Space Module (TLS, SSH, and
application-layer crypto). On Apple Silicon, the Secure Enclave
Processor provides the hardware root of trust for key material;
Apple publishes Secure Enclave validation information separately.

**CMMC practices implemented.** SC.L2-3.13.11 (FIPS-validated
cryptography for CUI) and SC.L2-3.13.16 (data at rest encryption).

**Implementation notes.**

- Apple validates updated Corecrypto modules against FIPS 140-3
  on a cadence tied to macOS release cycles. CMVP certificate
  numbers for Apple modules cycle multiple times per year; there
  is no single long-lived certificate for "macOS."
- For a specific CUI fleet deployment, the fleet operator
  determines which macOS version is in production and verifies
  the active CMVP certificate for the Apple Corecrypto Kernel
  Module and the Apple Corecrypto User Space Module at
  csrc.nist.gov/projects/cryptographic-module-validation-program
  /validated-modules/search. Filter by vendor "Apple" and match
  to the macOS version.
- Apple platform cryptography does not have a user-facing "FIPS
  mode" toggle on modern macOS. The Corecrypto modules operate
  in their validated mode by default for operations routed
  through system APIs. Bypassing the system APIs (for example,
  using an in-application bundled OpenSSL rather than the system
  libraries) takes that operation out of the FIPS boundary.
- The FileVault XTS-AES operation is performed by the AES engine
  in the Secure Enclave on Apple Silicon; the key is protected
  by the Secure Enclave. On T2 Intel Macs, the T2 chip performs
  the equivalent role.

**FIPS 140 status (verified 2026-04-21).** Apple Corecrypto
Kernel Module and Apple Corecrypto User Space Module hold active
CMVP certificates under the Apple vendor listing. The specific
active certificate for a given macOS version cycles with release
updates; verify on csrc.nist.gov before citing a specific
certificate number in an SSP. Secure Enclave Processor validation
is published separately under Apple's vendor listing on the same
registry. Both FIPS 140-2 and FIPS 140-3 validated certificates
are acceptable for CUI; FIPS 140-2 certificates remain valid
through their CMVP-published transition dates.

**Evidence to collect.**

- SSP section naming the macOS version in production and citing
  the current active CMVP certificate(s) for Apple Corecrypto,
  dated at SSP authoring and re-verified on an annual cadence.
- Configuration documentation confirming CUI applications use
  system cryptographic APIs rather than bundled third-party
  libraries where feasible.

**Common mistakes.**

- Citing "macOS is FIPS 140 validated" without a specific
  certificate number. No such blanket validation exists; only
  specific modules validated for specific OS versions hold
  certificates.
- Using an in-application cryptographic library (a third-party
  OpenSSL build, a language-runtime-bundled crypto library) for
  CUI encryption and then citing Apple Corecrypto validation.
  The validation applies to the Apple module, not the bundled
  library.
- Letting the SSP's cited CMVP certificate number go stale after
  the fleet moves to a new macOS version with a different cert.
- Citing a single certificate family when the fleet spans both
  Apple Silicon and T2-era Intel Macs. The SSP must cover both
  device families and note the distinct key-protection roots
  (Secure Enclave versus T2) in the risk assessment.

---

## Cross-domain anchors

macOS-specific guidance in this file composes with the domain
practice files for assessor-facing requirement text and evidence
lists:

- Configuration Management (CM) — `references/domains/cm-configuration-mgmt.md`
- System and Information Integrity (SI) —
  `references/domains/si-system-information-integrity.md`
- System and Communications Protection (SC) —
  `references/domains/sc-system-comms.md`
- Identification and Authentication (IA) —
  `references/domains/ia-identification-auth.md`
- Access Control (AC) — `references/domains/ac-access-control.md`
- Audit and Accountability (AU) — `references/domains/au-audit.md`
- Media Protection (MP) — `references/domains/mp-media-protection.md`

For FedRAMP Moderate inheritance on any of the capabilities above
(relevant when the MDM management plane or the SIEM is operated
by a FedRAMP Moderate CSP), see `references/fedramp-gap.md`
"Inherited vs shared-responsibility controls."

---

## Examples as of 2026-04

> **Examples as of 2026-04:** Jamf Pro, Kandji, Microsoft Intune,
> Mosyle. Listed alphabetically. Verify current FedRAMP
> Marketplace status on marketplace.fedramp.gov before selecting.
> This skill does not rank vendors; each product implements the
> capability set above with different tradeoffs in configuration
> ergonomics, declarative-management coverage, integration
> breadth, and pricing. Product selection is a procurement
> decision outside this skill's scope.

---

## Terminology

Most acronyms used in this file are defined in
`references/modern-it/endpoints/README.md` "Terminology." macOS-
specific terms below.

**ADE (Automated Device Enrollment).** The Apple Business Manager
workflow that routes a Mac into a pre-assigned MDM server at
first boot, enabling supervised management.

**ABM (Apple Business Manager).** The Apple enterprise portal for
device assignment, Managed Apple IDs, and app/book purchasing.

**APFS (Apple File System).** The default filesystem on modern
macOS. FileVault encryption operates at the APFS volume level.

**FVIRK (FileVault Institutional Recovery Key).** A legacy
shared recovery key mechanism for FileVault. Deprecated for new
deployments in favor of MDM-escrowed Personal Recovery Keys.

**PRK (Personal Recovery Key).** A per-Mac FileVault recovery key
escrowed to the MDM.

**RSR (Rapid Security Response).** Apple's small-scoped security
update mechanism for fixes between major OS updates.

**SSV (Signed System Volume).** The cryptographically verified
macOS system partition on Apple Silicon.

**TCC (Transparency, Consent, and Control).** The macOS privacy
framework that governs access to protected resources (camera,
microphone, full disk access). MDM
`PrivacyPreferencesPolicyControl` payloads pre-approve access
for managed applications.
