# Windows Fleet Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); Microsoft Learn documentation for Intune, Entra ID, and
> Windows (learn.microsoft.com); DISA STIG library
> (public.cyber.mil/stigs); Microsoft Security Baselines
> (microsoft.com/en-us/download/details.aspx?id=55319 and
> learn.microsoft.com/en-us/windows/security/threat-protection
> /windows-security-configuration-framework); NIST CMVP validated
> modules registry (csrc.nist.gov/projects/cryptographic-module-
> validation-program).

## Overview

This file maps Windows endpoint management capabilities to CMMC
practice requirements. It applies to contractor fleets running
Windows 10, Windows 11, and Windows Server when the server hosts
fleet-side endpoint capabilities (Windows Server Update Services,
on-premises MDM connectors). Workload servers are out of scope;
see the domain practice files for server-side controls.

Read this file alongside
`references/modern-it/endpoints/README.md`, which carries the
capability-versus-product convention and the endpoint-capability
→ CMMC-practice crosswalk. Structural content here names
capabilities; product names appear only in the dated Examples
sidebar.

**Management-plane split.** Windows fleet management sits across
three management planes that frequently coexist in the same
contractor environment: on-premises Active Directory (AD) with
Group Policy Objects (GPOs) delivered via the domain controller;
Microsoft Intune cloud-delivered configuration policy; and System
Center Configuration Manager (SCCM, rebranded Microsoft
Configuration Manager) delivering configuration, patches, and
application management from an on-premises or hybrid server.
Co-management (Intune plus SCCM on the same device) is common
during migrations and remains a supported steady state. This file
speaks capability-level across all three planes; per-plane
payload and policy names change with Microsoft release cadence
and must be verified against current Microsoft Learn documentation
before deployment.

**GCC versus GCC High.** The Microsoft 365 tenancy-selection
decision (commercial, GCC, GCC High, DoD) is the authoritative
subject of `references/modern-it/productivity/microsoft-365-gcc.md`
"Tenancy Selection" per Phase 5d hub Decision 5. The decision
drives what FedRAMP inheritance a contractor can claim for the
Intune and Defender control surfaces sitting on top. The capability
and control mapping in this file applies regardless of tenancy,
but FedRAMP inheritance depends on which tenancy hosts the
management plane; read the productivity file for the full decision
tree.

---

## Scope of this file

Covered:

- Windows 10 and Windows 11 endpoint capability patterns under
  Intune, SCCM, on-premises Group Policy, or co-management.
- CMMC practice mapping for each capability.
- Evidence to collect for each practice.
- Common mistakes specific to Windows.

Not covered:

- Workload server hardening. Application servers, database
  servers, and domain controllers are server-side surfaces
  treated in the domain practice files directly.
- Microsoft 365 productivity suite compliance. Exchange Online,
  SharePoint Online, Teams, and the DLP, retention, and
  sensitivity-label layers ride in
  `references/modern-it/productivity/microsoft-365-gcc.md`.
- Azure IaaS platform posture. Azure tenancy and subscription
  posture lives in
  `references/modern-it/cloud-platforms/azure-government.md`;
  the platform-selection hub with the FedRAMP-to-IL crosswalk
  lives in
  `references/modern-it/cloud-platforms/cloud-selection.md`.
- Legacy Windows versions below Windows 10 22H2 for CUI
  endpoints. Windows 8.1 and earlier are out of security-update
  support; handling CUI on them is a non-starter.

---

## MDM enrollment: Intune, co-management, and hybrid Entra join

**Capability.** A Mobile Device Management (MDM) solution enrolls
each Windows endpoint, delivers configuration policy that sets
security settings, monitors compliance, and supports remote lock
or wipe. On Windows, the primary MDM is Microsoft Intune,
delivering policy via the Configuration Service Provider (CSP)
protocol. Enrollment methods include Microsoft Entra join
(formerly Azure AD join) for cloud-native devices; hybrid Entra
join for devices also joined to on-premises Active Directory; and
group policy or provisioning-package enrollment for devices staying
on-premises.

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration), CM.L2-3.4.2 (configuration enforcement),
CM.L2-3.4.6 (least functionality), and AC.L2-3.1.18 (mobile device
connection control) anchor to the MDM capability.

**Implementation notes.**

- Cloud-native fleets target Microsoft Entra join plus
  Intune-only management. This is the recommended posture for new
  deployments and carries the cleanest FedRAMP inheritance story
  when the tenancy is GCC High.
- Hybrid Entra join covers devices that must remain AD-joined for
  legacy line-of-business applications. Configuration flows from
  both planes; resolve conflicts in favor of the stricter policy.
- Co-management with SCCM is a supported and common steady state
  during long Intune migrations. Each CMMC-relevant workload
  (compliance policies, endpoint protection, software updates,
  device configuration) is assigned to either Intune or SCCM; the
  sliders are configured in the co-management settings.
- Configuration Service Provider (CSP) policy names and
  Administrative Template settings shift across Windows feature
  updates. Policy names referenced in this file are current for
  Windows 10 22H2 and Windows 11 23H2 or later; verify against
  Microsoft Learn's Windows CSP reference and the current
  Administrative Templates (ADMX) catalog before deploying.
- This guidance applies whether the Intune management plane runs
  in commercial, GCC, or GCC High. FedRAMP inheritance claims
  depend on tenancy selection; see
  `references/fedramp-gap.md` "Inherited vs shared-responsibility
  controls."

**Evidence to collect.**

- Intune device inventory report listing every enrolled endpoint,
  its operating system version, join state (Entra, hybrid,
  workgroup), and assigned compliance policy.
- Baseline configuration policy export from Intune or SCCM (JSON
  or equivalent).
- Compliance posture report showing each device's deviation from
  policy, dated at assessment time.

**Common mistakes.**

- Mixing Intune and SCCM configuration for the same workload
  without a documented co-management slider. Policies fight; the
  effective configuration is non-deterministic.
- Leaving devices in a workgroup or unjoined state while policy
  delivery is assumed. Unjoined devices receive no policy.
- Treating Entra join as interchangeable with hybrid Entra join
  for on-premises Kerberos-dependent applications. Pure Entra
  join breaks Kerberos against on-premises resources unless Azure
  AD Kerberos is configured.

---

## BitLocker encryption and key escrow

**Capability.** BitLocker Drive Encryption provides full-volume
encryption for system and data volumes. It uses XTS-AES 128-bit
(default) or 256-bit keys with a Volume Master Key protected by
the Trusted Platform Module (TPM) on supported hardware.
MDM-delivered BitLocker configuration enforces encryption,
selects the algorithm and key size, and escrows recovery keys to
Entra ID (for Entra-joined devices), Active Directory (for
domain-joined devices), or the MDM service.

**CMMC practices implemented.** SC.L2-3.13.11 (FIPS-validated
cryptography for CUI), SC.L2-3.13.16 (data at rest encryption),
MP.L2-3.8.1 (physical media protection), and MP.L1-3.8.3
(sanitization before reuse or disposal, through cryptographic
erasure).

**Implementation notes.**

- Enforce BitLocker via Intune Endpoint Security disk encryption
  profile, SCCM compliance setting, or Group Policy.
  MDM-delivered enforcement triggers encryption during Autopilot
  or first-sign-in without user interaction.
- Select XTS-AES 256-bit for CUI fleets unless a specific
  compatibility constraint requires 128-bit. The performance
  difference is negligible on modern hardware; the assessor-facing
  story is cleaner with the stronger key size.
- Escrow recovery keys to Entra ID for Entra-joined devices and
  Active Directory for domain-joined devices. Verify the escrow
  by sampling recovery keys from the directory and matching them
  against the device inventory.
- TPM-only key protection is the baseline. PIN-at-boot (TPM+PIN)
  provides an additional factor when physical-access risk is
  elevated (OCONUS travel, high-value engineering laptops).
- Cryptographic erasure (destroying the FVEK) is the standard
  sanitization path for BitLocker-enabled devices going through
  the MP.L1-3.8.3 flow. `manage-bde -forcerecovery` and a factory
  reset effectively render the previous contents unrecoverable.

**Evidence to collect.**

- Intune BitLocker policy export or GPO export showing enforcement
  payload and algorithm selection.
- BitLocker recovery key inventory from Entra ID, Active
  Directory, or the MDM escrow showing every managed device has
  an escrowed key.
- Fleet BitLocker status report (encryption state, algorithm, key
  protection method) from Intune or SCCM.
- Sanitization records for devices removed from the fleet showing
  the cryptographic-erasure method used.

**Common mistakes.**

- Enforcing BitLocker without escrow. The volume is encrypted but
  recovery fails when a user forgets the PIN or loses the TPM
  (hardware replacement, firmware reset).
- Letting BitLocker encrypt with the default algorithm on older
  Windows versions that default to AES-CBC 128, then not
  migrating to XTS-AES after a Windows feature update.
- Encrypting the system volume but not fixed data volumes on
  engineering workstations that store CUI in a separate partition.

---

## Endpoint Detection and Response integration

**Capability.** An Endpoint Detection and Response (EDR) agent on
Windows provides anti-malware, exploit protection, endpoint
telemetry, detection against attack patterns, and remote
response. On Microsoft-native stacks this is
Microsoft Defender for Endpoint (MDE), delivered through Intune
or SCCM and
integrated with the Defender portal. Third-party EDR products
(CrowdStrike, SentinelOne, and others) replace or supplement MDE
and ingest telemetry into their own consoles.

**CMMC practices implemented.** SI.L1-3.14.2 (malicious code
protection), SI.L1-3.14.4 (update malicious code mechanisms),
SI.L1-3.14.5 (periodic and real-time scanning), SI.L2-3.14.3
(security alerts and advisories), SI.L2-3.14.6 (system
monitoring), SI.L2-3.14.7 (unauthorized use detection), and
AU.L2-3.3.1 (endpoint audit event generation).

**Implementation notes.**

- Deploy the EDR agent through Intune Endpoint Security or SCCM
  client deployment. The agent must be tenant-attached and
  reporting before an endpoint is considered in compliance.
- For Microsoft Defender for Endpoint, verify the tenancy
  (commercial, GCC, GCC High) matches the fleet's CUI posture.
  MDE in GCC High is a separate service instance from MDE
  commercial; crossing tenancies is not a supported
  configuration.
- CMMC L1 anti-malware practices (SI.L1-3.14.2, 14.4, 14.5) are
  satisfied by Defender Antivirus alone. The CMMC L2 monitoring
  and unauthorized-use-detection practices (SI.L2-3.14.6, 14.7)
  require the EDR telemetry and response surface; Defender for
  Endpoint's EDR tier or a third-party equivalent is mandatory
  at L2.
- Tamper Protection must be enabled. It prevents local
  administrators from disabling Defender components. Tamper
  Protection is a Defender-portal or Intune-delivered setting.
- Telemetry export to the SIEM realizes AU.L2-3.3.5 correlation;
  see "Centralized logging to SIEM" below.

**Evidence to collect.**

- Intune or SCCM configuration showing EDR agent deployment and
  Tamper Protection enforcement.
- MDE or third-party console inventory showing every endpoint is
  onboarded and reporting with current signatures.
- Sample alert record routed to the SIEM for an
  indicator-of-compromise test.

**Common mistakes.**

- Leaving Tamper Protection off. An attacker or a misguided
  administrator can disable Defender on the endpoint, and the
  EDR silently stops protecting that device.
- Running Defender Antivirus alongside a third-party AV without
  setting Defender to passive mode. The two engines compete and
  degrade performance; Windows behavior in this case is driven by
  registry state that is easy to misconfigure.
- Assuming Defender commercial and Defender GCC High data planes
  are equivalent for CUI. They are not. CUI telemetry must
  terminate in the GCC High tenancy.

---

## AppLocker and Windows Defender Application Control

**Capability.** Application allowlisting and execution policy on
Windows is implemented through AppLocker (legacy, still supported)
or Windows Defender Application Control (WDAC, the modern
replacement). Both block execution of non-authorized binaries;
WDAC operates lower in the stack (kernel code integrity) and
supports richer signer and policy options. Both are delivered via
Intune, SCCM, or Group Policy.

**CMMC practices implemented.** CM.L2-3.4.7 (nonessential
functionality restriction), CM.L2-3.4.8 (application execution
policy), and CM.L2-3.4.9 (user-installed software control).

**Implementation notes.**

- For new deployments, target WDAC. WDAC policies can be merged,
  signed, and deployed in audit mode before enforcement, which
  materially reduces deployment risk compared to AppLocker.
- AppLocker is acceptable for in-place fleets; migration to WDAC
  is a Microsoft-recommended trajectory but not a CMMC
  requirement.
- Run the allowlist in audit mode for a minimum observation
  window (typically 30 to 60 days) before enforcement. Capture
  the AppLocker or WDAC event logs to identify blocked
  legitimate applications before they break production.
- Signed policies defeat local-administrator tampering. Unsigned
  policies are easier to author but can be disabled by an
  administrator with console access.
- WDAC supplemental policies allow per-device or per-group
  exceptions without weakening the base policy.

**Evidence to collect.**

- Intune, SCCM, or GPO export of the active AppLocker or WDAC
  policy.
- Event log extract showing AppLocker or WDAC enforcement events
  across the fleet.
- Policy change log showing who approved each supplemental
  policy and why.

**Common mistakes.**

- Leaving the allowlist in audit mode indefinitely. Audit mode
  satisfies logging and observation but not the enforcement
  practice.
- Authoring a policy that allowlists `C:\Program Files` wholesale
  without signer-based narrowing. An attacker who writes a binary
  there runs it unhindered.
- Disabling WDAC to install a vendor's unsigned driver, then
  forgetting to re-enable it.

---

## Windows Update for Business and patch management

**Capability.** Windows Update for Business (WUfB) is the
cloud-delivered update orchestration for Windows endpoints.
Intune-delivered update rings control deferral, deadline, and
active-hours behavior. Windows Server Update Services (WSUS) and
SCCM software-update groups are the on-premises alternatives for
fleets not yet migrated to WUfB. Windows Update for Business
reports into Intune compliance for assessor-facing patch posture
reporting.

**CMMC practices implemented.** SI.L1-3.14.1 (flaw remediation)
and CM.L2-3.4.9 (user-installed software, as third-party
applications update alongside the OS).

**Implementation notes.**

- Deploy Intune update rings with defined deferrals for quality
  updates (security monthly) and feature updates (annual
  releases). Industry-typical deferral: quality updates 7 to 14
  days post-release, feature updates 90 to 180 days.
- Set a compliance deadline for quality updates. Without a
  deadline, updates that require restart can be postponed
  indefinitely by the user.
- Update Compliance in Intune surfaces devices falling behind
  deadline. Configure alerting or recurring review for the
  non-compliant population.
- Third-party applications update through their own mechanisms,
  through Intune app deployment (Microsoft Store for Business or
  Win32 app packaging), or through SCCM application deployment.
  SI.L1-3.14.1 covers these alongside OS updates.
- WSUS-only fleets are compliant but are missing the cloud
  reporting surface; patch posture reporting is a separate build
  effort on WSUS.

**Evidence to collect.**

- Intune update ring export and compliance deadline settings.
- Fleet patch posture report showing OS version and update
  recency across the fleet, dated at assessment time.
- Third-party application version inventory from Intune app
  management.

**Common mistakes.**

- Configuring deferrals without deadlines. Devices accumulate
  update backlog indefinitely.
- Assuming WSUS synchronization equals applied updates. WSUS
  approves updates; endpoint-side agents apply them. A
  synchronized but disconnected device remains unpatched.
- Excluding executive laptops from update rings for convenience.
  Executives carry the same CUI as other roles and cannot be
  exempt from patch discipline.

---

## Group Policy and Microsoft Security Baseline

**Capability.** Windows ships hundreds of security-relevant
settings. Microsoft publishes Security Baselines (sets of
recommended values for each setting) as Group Policy Object
backup files and equivalent Intune policy definitions. DISA
publishes Security Technical Implementation Guides (STIGs) that
apply DoD-specific hardening on top of Microsoft baselines. A
CMMC fleet generally starts from a named baseline (Microsoft
Security Baseline or a DISA STIG) and tailors to fit.

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration) and CM.L2-3.4.2 (configuration enforcement).

**Implementation notes.**

- Select a baseline and document the choice in the SSP.
  Microsoft Security Baseline is sufficient for most CMMC L2
  contractors; DISA STIG is expected where the contract
  references DoD STIG compliance directly.
- Tailor consciously. A baseline setting that breaks a
  CUI-bearing line-of-business application must be changed; the
  change must be documented with rationale.
- Verify baseline versions against the publisher before applying.
  Microsoft publishes Security Baseline updates with each major
  Windows release (Windows 11 23H2 baseline, 24H2 baseline,
  etc.); DISA STIGs are revised on a quarterly-ish cadence.
  Baseline version numbers cited in the SSP must match what is
  deployed.
- Deploy the baseline as Intune policy (import the GPO backup as
  a Settings Catalog or Administrative Templates profile) or as
  GPO on-premises; hybrid fleets run both and resolve conflicts
  through documented precedence.

**Evidence to collect.**

- SSP section naming the selected baseline and version, dated.
- Intune Settings Catalog or GPO export showing applied baseline
  settings.
- Deviation log showing any tailored setting with rationale and
  approver.
- Fleet configuration scan (Security Compliance Toolkit,
  PowerStig, or vendor equivalent) dated at assessment time.

**Common mistakes.**

- Citing "Microsoft Security Baseline" in the SSP without naming
  the version. Baselines evolve; an assessor cannot verify
  compliance against an unnamed version.
- Importing a baseline, tailoring heavily, and failing to
  document the tailoring. The deployed configuration no longer
  matches the named baseline and no record exists of what was
  changed.
- Applying a baseline designed for a different Windows edition
  (Enterprise versus Pro versus LTSC). Some settings behave
  differently.

---

## Windows Defender Firewall

**Capability.** Windows Defender Firewall with Advanced Security
provides per-profile (domain, private, public) inbound and
outbound filtering. Intune Endpoint Security firewall profiles
and GPO firewall policies configure rules and state across the
fleet.

**CMMC practices implemented.** SC.L1-3.13.1 (boundary protection,
at the host edge) and SC.L2-3.13.6 (deny by default, allow by
exception).

**Implementation notes.**

- Enable the firewall for all three profiles. Public profile is
  the strictest default; public-network connections should
  restrict inbound traffic to essential services.
- Deny inbound by default; allow by exception with documented
  rules. Each allow rule should cite the application it supports
  and the reason for the exception.
- Do not disable the firewall to troubleshoot a connectivity
  issue without restoring it immediately. Disabled-for-
  troubleshooting states tend to become permanent.
- Centralize rule management through Intune or GPO. Endpoint-
  local rules created by users or applications should be
  monitored and reconciled against the central policy.

**Evidence to collect.**

- Intune firewall profile export or GPO firewall policy export.
- Fleet compliance report showing firewall enabled across all
  profiles on every endpoint.
- Rule inventory with justification per rule.

**Common mistakes.**

- Disabling the firewall on developer workstations for
  convenience, then forgetting to re-enable it. Developer
  endpoints often hold CUI source code and are in full scope.
- Relying on endpoint firewalls as the only boundary protection.
  Network-side boundaries also need to be cited.

---

## Credential Guard and LSASS protection

**Capability.** Virtualization-based security (VBS) features on
Windows isolate credential material from user-mode processes.
Credential Guard runs the Local Security Authority (LSA)
secrets-handling in a virtualized trust boundary (Isolated LSA,
LSAIso) so that a local-administrator compromise cannot dump
credentials from LSASS directly. LSA protection (RunAsPPL) marks
the LSASS process as a Protected Process Light, blocking
unsigned code injection and casual credential theft tooling.
Both are delivered via Intune, GPO, or SCCM.

**CMMC practices implemented.** IA.L2-3.5.3 (MFA; Credential
Guard is an enabler for credential-theft-resistant
authentication), AC.L2-3.1.7 (privileged function logging, as
related event generation), and SC.L2-3.13.16 (information-at-rest
protection, for the credential material in memory).

**Implementation notes.**

- Credential Guard requires VBS, which requires hardware support
  (UEFI, Secure Boot, TPM 2.0, virtualization extensions) and a
  Windows edition that includes the feature (Enterprise, Education,
  or Server). Contractor fleets on Windows 10/11 Pro cannot enable
  Credential Guard.
- Enable VBS, Hypervisor-Enforced Code Integrity (HVCI), and
  Credential Guard together as a baseline for CUI endpoints on
  capable hardware.
- LSA protection (RunAsPPL) is available on all Windows
  editions and does not require VBS. Enable it even when
  Credential Guard is not feasible.
- Test driver and application compatibility before enforcement.
  HVCI in particular blocks unsigned kernel-mode code; legacy
  drivers fail.

**Evidence to collect.**

- Intune, SCCM, or GPO export showing VBS, HVCI, Credential
  Guard, and LSA protection enabled.
- `msinfo32` or equivalent fleet inventory showing
  virtualization-based-security state across endpoints.
- Exception log for any endpoint where Credential Guard is
  disabled, with rationale.

**Common mistakes.**

- Buying Pro-edition endpoints for a CUI fleet and discovering
  Credential Guard is unavailable. Enterprise or equivalent is
  the expected edition.
- Enabling HVCI without testing kernel-mode driver compatibility,
  then facing fleet-wide boot failures after a driver update.

---

## Screen lock and idle timeout

**Capability.** Windows lock-screen and screen-saver settings
lock the session after a defined period of inactivity. GPO or
Intune settings enforce the idle timeout, require a password on
resume, and configure the grace period.

**CMMC practices implemented.** AC.L2-3.1.10 (session lock after
inactivity) and AC.L2-3.1.11 (session termination conditions).

**Implementation notes.**

- Set the interactive-logon inactivity limit
  (`InactivityTimeoutSecs` policy) to no more than 900 seconds (15
  minutes) for CUI endpoints; shorter is stronger.
- Require a password (or MFA credential) on wake; disable "login
  without password on return from screensaver" convenience
  options.
- Force the setting via Intune or GPO; do not rely on user-level
  configuration.

**Evidence to collect.**

- Intune policy export or GPO export showing the screen lock
  payload.
- Fleet compliance report confirming the policy applies to every
  managed endpoint.

**Common mistakes.**

- Setting the idle timeout at the OS level but allowing a local
  energy-saving configuration to override it.

---

## Centralized logging to SIEM

**Capability.** Windows generates audit events through the
Security, System, Application, and Windows PowerShell event logs,
plus operational channels for Defender, AppLocker, WDAC, and
other security components. A log-forwarding agent (Windows Event
Forwarding to a collector, an EDR agent's telemetry export, or a
SIEM-native collector) exports selected streams to the
Security Information and Event Management (SIEM) platform.

**CMMC practices implemented.** AU.L2-3.3.1 (audit event
creation), AU.L2-3.3.2 (user accountability), AU.L2-3.3.3 (event
review), AU.L2-3.3.5 (audit correlation), AU.L2-3.3.7
(authoritative time source), and AU.L2-3.3.8 (audit protection
through centralization).

**Implementation notes.**

- Enable the audit policy subcategories named in the DISA STIG or
  Microsoft Security Baseline audit configuration. Logon/logoff,
  account management, privilege use, and process creation are
  the highest-value subcategories for CMMC.
- Forward Security-channel events to the SIEM. Include Defender
  operational events and the AppLocker or WDAC enforcement logs.
- Time synchronization via Windows Time Service (W32Time) to an
  authoritative internal or external source is the AU.L2-3.3.7
  anchor. Domain-joined devices inherit from the PDC emulator;
  Entra-joined devices use Windows Time against an external NTP
  source.
- Endpoint-local logs are rotational and may be overwritten
  before review. Forwarding to the SIEM is what realizes
  AU.L2-3.3.8 audit protection.

**Evidence to collect.**

- Audit policy configuration export (GPO auditpol extract or
  Intune policy export).
- Log-forwarder configuration per endpoint.
- SIEM dashboard or query confirming event arrival from managed
  endpoints, dated.
- Time-sync configuration and source documentation.

**Common mistakes.**

- Enabling auditing at the parent category (`Account Logon`)
  instead of the specific subcategory. Parent-category settings
  are ignored when any subcategory is explicitly set.
- Forwarding only Security-channel events and missing Defender
  operational events where the EDR alerts surface.
- Leaving W32Time pointed at the Windows default public NTP
  without documenting the source in the SSP.

---

## FIPS 140 mode on Windows

**Capability.** Windows can be configured to restrict cryptographic
operations to FIPS 140-validated algorithms through the
"System cryptography: Use FIPS compliant algorithms for
encryption, hashing, and signing" security setting. The validated
modules involved include the Windows Cryptographic Primitives
Library (bcryptprimitives.dll and ncryptsslp.dll), the Windows
Boot Manager crypto module, and related Windows cryptographic
providers. CMVP certificate numbers cycle with each Windows
feature release.

**CMMC practices implemented.** SC.L2-3.13.11 (FIPS-validated
cryptography for CUI), SC.L2-3.13.8 (transmission confidentiality
and integrity), and SC.L2-3.13.16 (data at rest encryption).

**Implementation notes.**

- The FIPS mode security setting restricts SChannel and
  .NET-framework cryptography to FIPS-validated algorithms. It
  does not by itself enable every validated module; it enforces
  algorithm selection within Microsoft's cryptographic stacks.
- Microsoft's official guidance is that FIPS mode is not
  required on Windows to use FIPS-validated cryptography;
  validated modules operate in their FIPS-validated mode by
  default when called through the relevant APIs. The FIPS mode
  toggle forces algorithm restriction at an OS-wide level and
  carries operational side effects that should be weighed
  against the compliance benefit.
- Operational side effects of FIPS mode:
  - Breaks or downgrades TLS to systems that do not negotiate a
    FIPS-approved cipher suite. Legacy line-of-business
    applications, embedded devices, or older printer or scanner
    firmware may fail to establish TLS.
  - Limits cipher suite selection to FIPS-approved suites. Some
    older clients (including certain mobile platforms and older
    email clients) cannot negotiate and will fail.
  - Blocks cryptographic functions that are not FIPS-approved,
    including some Windows features that ride on
    non-FIPS-approved hashes (older MD5 code paths in specific
    tools).
  - .NET applications enforcing FIPS policy will throw
    CryptographicException when an unvalidated algorithm is
    requested; applications that quietly use non-FIPS hashing
    (for example, MD5 for non-security internal identifiers)
    will crash.
- Evaluate whether FIPS mode is appropriate fleet-wide, or
  whether explicitly enforcing validated algorithm selection at
  the application and SChannel policy layers meets the
  SC.L2-3.13.11 objective without the blast radius of the
  OS-wide toggle. Many CMMC contractors rely on
  application-level and SChannel-level enforcement rather than
  the OS toggle.
- FIPS 140-2 and FIPS 140-3 validated modules are both
  acceptable; FIPS 140-2 certificates remain valid through
  CMVP-published transition dates.

**FIPS 140 status (verified 2026-04-21).** Microsoft publishes
CMVP certificates for Windows cryptographic modules per feature
release. Active certificates cycle with Windows updates. Fleet
operators identify the Windows version in production and verify
the active certificate for the Windows Cryptographic Primitives
Library and related modules at
csrc.nist.gov/projects/cryptographic-module-validation-program/
validated-modules/search, filtering by vendor "Microsoft" and
matching to the deployed Windows build. Cite the specific
certificate number in the SSP and re-verify on an annual
cadence.

**Evidence to collect.**

- SSP section naming the Windows version in production, the
  FIPS-enforcement posture (OS-wide toggle, application-level,
  or SChannel-level), and the active CMVP certificate(s) for
  the deployed Windows cryptographic modules, dated.
- Intune or GPO export showing the FIPS-mode policy setting if
  the OS-wide toggle is used.
- Compatibility test results for the fleet's line-of-business
  applications if FIPS mode is enforced OS-wide.

**Common mistakes.**

- Enabling FIPS mode fleet-wide without testing, then spending
  weeks debugging TLS failures to legacy line-of-business
  systems and reverting the policy without documenting why.
- Citing "Windows is FIPS 140 validated" in the SSP without a
  specific certificate number. Only specific Microsoft modules
  for specific Windows versions carry certificates.
- Citing a single certificate family when the fleet spans
  multiple Windows feature versions with different active
  certificates.
- Assuming FIPS mode enforcement at the OS level covers
  third-party application cryptography. Applications that bundle
  their own cryptographic libraries (some Java runtimes, certain
  VPN clients, some databases) may not honor the OS FIPS
  policy.

---

## Cross-domain anchors

Windows-specific guidance here composes with the domain practice
files for assessor-facing requirement text and evidence lists:

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

For FedRAMP Moderate inheritance relevant when the Intune, SCCM,
or Defender management planes are operated by a FedRAMP-
authorized tenancy (GCC Moderate or GCC High), see
`references/fedramp-gap.md` "Inherited vs shared-responsibility
controls."

---

## Examples as of 2026-04

> **Examples as of 2026-04:** BigFix, CrowdStrike Falcon,
> Microsoft Defender for Endpoint, Microsoft Intune, Microsoft
> System Center Configuration Manager (SCCM / Microsoft
> Configuration Manager), SentinelOne Singularity, Tanium.
> Listed alphabetically. Some products in this list are endpoint
> management planes (Intune, SCCM, BigFix, Tanium); others are
> EDR agents (CrowdStrike, Defender for Endpoint, SentinelOne);
> most CUI fleets combine one of each. Verify current FedRAMP
> Marketplace status on marketplace.fedramp.gov before selecting;
> GCC High coverage is required for Intune and Defender when CUI
> flows through the management plane. This skill does not rank
> vendors.

---

## Terminology

Most acronyms used in this file are defined in
`references/modern-it/endpoints/README.md` "Terminology."
Windows-specific terms below.

**AD (Active Directory).** The on-premises Microsoft directory
service. Stores user and computer objects, enforces Group
Policy, and provides Kerberos authentication.

**ADMX (Administrative Templates).** The XML-based Group Policy
and Intune Settings Catalog definition format.

**Autopilot (Windows Autopilot).** The Microsoft service that
zero-touch provisions a new Windows device into Intune and
Entra ID at first boot.

**CSP (Configuration Service Provider).** The Windows MDM
protocol interface through which Intune delivers configuration
policy. Distinct from the FedRAMP "Cloud Service Provider"
abbreviation, which is also CSP; this file disambiguates via
context.

**Entra ID (Microsoft Entra ID, formerly Azure Active Directory).**
The Microsoft cloud identity and directory service.

**GCC (Government Community Cloud).** The Microsoft 365 and Azure
tenancy variant authorized at FedRAMP Moderate, targeting
federal, state, and local government workloads.

**GCC High (Government Community Cloud High).** The Microsoft 365
and Azure tenancy variant authorized at FedRAMP High and aligned
with IL5, targeting contractors handling CUI under DFARS
252.204-7012.

**GPO (Group Policy Object).** An Active Directory-delivered
configuration policy container.

**HVCI (Hypervisor-Enforced Code Integrity).** A Windows VBS
feature that enforces kernel-mode code integrity in a
virtualized trust boundary.

**LSA (Local Security Authority).** The Windows subsystem
responsible for authentication and security policy enforcement,
hosted in the LSASS process.

**LSAIso (Isolated LSA).** The virtualized trust boundary where
Credential Guard runs LSA secrets-handling, isolated from the
main LSASS process.

**MDE (Microsoft Defender for Endpoint).** Microsoft's EDR
product.

**PPL (Protected Process Light).** A Windows process-protection
level that restricts code injection and debugging access.
LSA protection marks LSASS as PPL to resist credential-theft
tooling.

**RunAsPPL.** The Windows registry value and group policy that
enables LSA protection (PPL for the LSASS process).

**SCCM (System Center Configuration Manager / Microsoft
Configuration Manager).** The on-premises or hybrid Microsoft
endpoint management product.

**STIG (Security Technical Implementation Guide).** DoD-published
configuration standards maintained by DISA.

**TPM (Trusted Platform Module).** A hardware or firmware root of
trust used by BitLocker, Credential Guard, and other Windows
security features.

**VBS (Virtualization-Based Security).** A Windows feature that
uses the hypervisor to isolate security-sensitive operations
from the main operating system.

**WDAC (Windows Defender Application Control).** The modern
Microsoft application allowlisting mechanism, successor to
AppLocker.

**WSUS (Windows Server Update Services).** The on-premises
Windows update distribution server.

**WUfB (Windows Update for Business).** The cloud-delivered
Windows update orchestration, configured through Intune update
rings.
