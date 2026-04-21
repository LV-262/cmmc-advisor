# Google Cloud Assured Workloads Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); Google Cloud compliance documentation
> (cloud.google.com/security/compliance); Assured Workloads
> documentation (cloud.google.com/assured-workloads/docs); Google
> Cloud DISA compliance page (cloud.google.com/security/compliance/disa);
> FedRAMP Marketplace (marketplace.fedramp.gov); DoD CSP SRG v1r1
> (public.cyber.mil); NIST CMVP validated modules registry
> (csrc.nist.gov).

## Overview

This file maps Google Cloud Assured Workloads capability patterns
to CMMC practice requirements for defense contractors hosting CUI
or FCI workloads on Google Cloud. Unlike AWS GovCloud and Azure
Government, Google Cloud does not operate a separate government
cloud partition or government cloud environment for FedRAMP
High and DoD Impact Level 4 and 5 workloads. Google Cloud
delivers these compliance postures through a
software-defined community cloud approach: Assured Workloads
applies control packages to folders within commercial Google
Cloud, enforcing regulatory and sovereignty controls through
organization policies and managed capabilities rather than
through physical infrastructure separation.

Read this file alongside
`references/modern-it/cloud-platforms/cloud-selection.md` (the
Phase 5c hub carrying the four conventions, the FedRAMP-to-IL
crosswalk, and the tenancy-selection decision tree). The hub's
Decision 3 rationale explicitly acknowledges this architectural
divergence (GCP Assured Workloads is an overlay; AWS and Azure
Government partitions are separate infrastructures); that
divergence shapes Decision 3's second question for GCP. Structural
content in this file names Google Cloud capabilities; third-party
product names appear only in the dated Examples sidebar.

**Architectural framing (load-bearing for this file).** A
contractor reading from Slices K (AWS) or L (Azure) expects a
separate government cloud environment with distinct APIs,
distinct operator staff, and physically separated infrastructure.
Google Cloud does not provide that for FedRAMP High, IL4, or
IL5; it provides equivalent controls through the Assured
Workloads overlay on commercial Google Cloud. The operational
implications differ meaningfully: service availability matches
commercial Google Cloud, the control-plane APIs are the same,
Google Cloud personnel access controls are enforced per
control-package rather than across an entire partition, and key
material can be customer-managed through Cloud KMS, Cloud HSM,
Cloud External Key Manager (Cloud EKM), or Key Access
Justifications depending on the control package selected. IL6
workloads (classified) sit outside this model entirely, on
Google Distributed Cloud air-gapped infrastructure.

**FedRAMP authorization summary (verified 2026-04-21).** Google
Cloud and Google Workspace hold FedRAMP High and FedRAMP
Moderate
Provisional Authorities to Operate (P-ATOs) through the
FedRAMP Joint Authorization Board (JAB). Deployment under
FedRAMP High requires the Assured Workloads FedRAMP High control
package applied to the target folder. Verify current
authorization status at marketplace.fedramp.gov before citing a
specific package identifier in an SSP.

**DoD Impact Level coverage (verified 2026-04-21).** DISA has
granted Google Cloud Provisional Authorizations at IL2, IL4, and
IL5. Google Cloud was the first hyperscaler to receive a DoD
IL5 Provisional Authorization for a software-defined community
cloud (2022). Google Workspace holds PAs at IL2 and IL4 (not
IL5). IL6 is served by Google Distributed Cloud air-gapped and
Google Distributed Cloud air-gapped appliance, which are
separate on-premises-deployed offerings outside commercial
Google Cloud and outside this file's scope.

---

## Scope of this file

Covered:

- Google Cloud Assured Workloads folder postures for FedRAMP
  High, IL2, IL4, and IL5 control packages.
- CMMC practice mapping per Google Cloud capability cluster.
- Evidence-collection patterns for each practice.
- Common mistakes specific to the Assured Workloads overlay
  model.
- Control package selection and the June 2025 renaming.

Not covered:

- Google Workspace IL4 posture (handled via Assured Controls
  Plus rather than Assured Workloads). Productivity-suite
  posture lives in
  `references/modern-it/productivity/google-workspace.md`
  (pending).
- Google Distributed Cloud air-gapped and Google Distributed
  Cloud air-gapped appliance for IL6 classified workloads.
  Separate on-premises infrastructure; outside commercial
  Google Cloud and outside CMMC L2 contractor scope.
- Sovereign Controls by Partners configurations (for
  jurisdiction-specific deployments outside the US federal
  and DoD scope covered here).
- ITAR control package in depth. ITAR posture requires
  export-control counsel engagement; the Assured Workloads
  ITAR control package is one technical control among a
  larger compliance program. See cross-reference to
  `references/modern-it/endpoints/remote-work.md` for ITAR
  framing at the endpoint and personnel layer.
- Regional sovereignty data boundaries (EU, UK, Canada, and
  other non-US regulatory regimes). Those are out of scope
  for a DFARS 252.204-7012 CUI focus.

---

## Tenancy selection

Per the Phase 5c hub (Decision 3), each per-provider file
answers three tenancy-selection questions in the same order.
For Google Cloud, Question 2 acknowledges the overlay
architecture explicitly; the Google-side answer diverges
structurally from AWS and Azure without breaking the symmetric
structure.

**1. Is the provider's commercial tenancy ever acceptable for
CUI?** Yes, when the commercial tenancy is scoped to an
Assured Workloads folder with the appropriate control package
applied (FedRAMP High, IL4, or IL5 depending on the workload).
The Assured Workloads overlay configures the commercial
tenancy with the regulatory controls that separate
AWS-GovCloud-class and Azure-Government-class environments
deliver through infrastructure partitioning. Commercial
Google Cloud resources outside an Assured Workloads folder
are not authorized for CUI.

**2. Which government tenancy or control-plane isolation posture
is the contractor path?** Not a separate cloud environment.
Google Cloud delivers FedRAMP High, IL4, and IL5 posture
through Assured Workloads folders within commercial Google
Cloud. The "tenancy" boundary in Google Cloud is
organization-and-folder-level inside commercial Google Cloud;
the Assured Workloads control package is the enforcement
mechanism. This is structurally different from AWS GovCloud
(separate partition) and Azure Government (separate cloud
environment). A contractor migrating from AWS or Azure should
treat this architectural difference as the primary posture
decision.

**3. What workload-location and support-personnel-citizenship
boundaries apply inside that tenancy?** The Assured Workloads
control package enforces both. Data residency restrictions
restrict resources to US Google Cloud regions for US federal
control packages (FedRAMP High, IL2, IL4, IL5). Personnel
access controls restrict Google Cloud support personnel to
US-persons with enhanced background checks for FedRAMP High
and to IL-adjudicated US-persons located in the US for IL4
and IL5. The enforcement happens at the Assured Workloads
control-package level on the folder, not across an entire
cloud partition. See "Support and operator-access posture"
below for the personnel details.

---

## Organization, folder, and Assured Workloads model

**Capability.** Google Cloud resources sit in a hierarchy:
Organization → Folders → Projects → Resources. Organization
Policies apply at any level and inherit downward. An Assured
Workloads folder is a folder with a specific control package
applied; the control package delivers the compliance posture by
configuring Organization Policy constraints, service
restrictions, Google personnel access controls, encryption
defaults, and monitoring. Resources deployed inside the folder
inherit these controls. IAM policies, Cloud Billing, and
Resource Manager operate the same as commercial Google Cloud
outside the Assured Workloads folder.

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration), CM.L2-3.4.2 (configuration enforcement),
AC.L2-3.1.3 (CUI flow control at the Assured Workloads folder
boundary), and AC.L2-3.1.5 (least privilege through
Organization Policy inheritance).

**Implementation notes.**

- Create a dedicated Assured Workloads folder for CUI
  workloads, separate from non-CUI folders, with the control
  package matching the workload's Impact Level (FedRAMP High
  for FedRAMP-scope work without DoD overlay; IL4 for
  DoD CUI under DFARS 7012; IL5 for higher-sensitivity CUI or
  mission-critical workloads).
- Control package names changed in June 2025. The renaming
  was cosmetic (functionality unchanged) but affects
  references: for example, "Data Boundary for FedRAMP High"
  is now "FedRAMP High"; "Data Boundary for Impact Level 5
  (IL5)" is now "Impact Level 5 (IL5)". SSPs and
  implementation documentation may cite either name; verify
  against cloud.google.com/assured-workloads/docs for current
  naming.
- Workload Updates is the Assured Workloads mechanism for
  applying control-package improvements over time. A folder
  provisioned at one point may not reflect the latest
  version of its control package; evaluate and apply
  Workload Updates on a cadence.
- Organization Policies applied at the Assured Workloads
  folder level enforce the control package. Additional
  Organization Policies can tighten posture further (for
  example, restricting specific services, requiring CMEK
  throughout the folder); they cannot loosen the control
  package's constraints.
- Assured Workloads Monitoring surfaces violations against
  the applied control package (organization-policy
  violations, resource violations). Configure email
  notifications for violations and review on a cadence.

**Evidence to collect.**

- Folder hierarchy export showing the Assured Workloads
  folder with the applied control package and version.
- Organization Policy inventory at and below the Assured
  Workloads folder.
- Assured Workloads Monitoring configuration including
  notification destinations.
- Workload Updates history showing control-package version
  refreshes, with a verification against the current
  control-package release notes at
  cloud.google.com/assured-workloads/docs confirming the
  folder is running a supported version as of the assessment
  date.
- Violation log sample, dated at assessment time.

**Common mistakes.**

- Provisioning resources in commercial Google Cloud folders
  outside any Assured Workloads folder, then claiming
  FedRAMP or IL compliance on those resources. The Assured
  Workloads control package is the compliance boundary; a
  resource outside an Assured Workloads folder is not
  covered by the folder's authorization.
- Applying the FedRAMP Moderate control package to an IL4 or
  IL5 workload. The IL4 and IL5 control packages layer the
  DoD-specific additions on top of FedRAMP High; Moderate is
  insufficient for DoD CUI under v1r1 reciprocity.
- Forgetting to update Assured Workloads folders to current
  control-package versions. A folder provisioned 18 months
  ago may carry outdated controls; Workload Updates
  resynchronizes.

---

## Identity and access management

**Capability.** Google Cloud identity is managed through Cloud
Identity (for Google Cloud organizations without Google
Workspace) or through Google Workspace-provisioned accounts.
Identity and Access Management (IAM) grants access to
resources through role bindings at the organization, folder,
project, or resource level. Workload Identity Federation
enables non-Google identity providers (external OIDC or SAML)
to exchange credentials for short-lived Google Cloud access
tokens. Organization Policy constraints can restrict which
domains can be added to the organization, which identity
providers can federate in, and which service accounts can be
created.

**CMMC practices implemented.** IA.L1-3.5.1 (user
identification), IA.L1-3.5.2 (user authentication),
IA.L2-3.5.3 (MFA), AC.L2-3.1.1 (account management), and
AC.L2-3.1.5 (least privilege).

**Implementation notes.**

- Cloud Identity or Google Workspace identity should be the
  source of truth for workforce identity in CUI-scope
  folders. Federate to an enterprise identity provider (for
  example, an enterprise IdP that supports SAML or OIDC)
  when the contractor's primary identity store is not
  Google-native; Workload Identity Federation handles the
  cross-identity-store integration.
- 2-Step Verification (Google's MFA) must be enforced on all
  users accessing CUI. Phishing-resistant factors (security
  keys, passkeys, Google Authenticator with prompt-plus-
  number-matching) are the assessor-preferred path; SMS is
  deprecated by NIST SP 800-63B for Authenticator Assurance
  Level 2.
- IAM role grants should follow least-privilege principles.
  Use predefined roles aligned with job functions;
  custom-roles for fine-grained permissions where predefined
  roles over-grant. Primitive roles (Owner, Editor, Viewer)
  should not be used for CUI-scope access except at the
  highest administrator level.
- Service accounts for workload-to-workload access should
  use Workload Identity (for GKE) or short-lived credentials
  via Workload Identity Federation rather than long-lived
  service account keys.
- Conditional access equivalent: Context-Aware Access
  policies in BeyondCorp Enterprise evaluate session context
  (user, device posture, IP, time) at access time. Available
  in Assured Workloads folders where BeyondCorp Enterprise
  is in scope.

**Evidence to collect.**

- Cloud Identity or Google Workspace configuration showing
  the tenant's identity source and 2SV enforcement policy.
- IAM role assignment inventory for CUI-scope projects with
  principle-of-least-privilege justification per binding.
- Workload Identity Federation configuration for external
  identity providers.
- Organization Policy constraints on identity (domain
  restriction, service account key restriction).
- Audit log sample from Cloud Audit Logs forwarded to a
  SIEM, dated.

**Common mistakes.**

- Granting primitive Editor or Owner roles to regular staff.
  The audit-trail value diminishes (every action appears as
  "Editor did X") and the blast radius of a compromised
  account is organization-wide.
- Creating long-lived service account keys and emailing them
  to developers. Short-lived credentials via Workload
  Identity Federation eliminate the long-lived-secret
  exposure.
- Federating workforce identity from a non-CUI-capable
  commercial identity provider. If the CUI workload's
  identity plane passes through a non-CUI tenancy, the CUI
  boundary extends into that tenancy.

---

## Encryption and key management

**Capability.** Google Cloud encryption defaults to
Google-managed encryption keys for data at rest and in transit.
Assured Workloads IL4 and IL5 control packages enforce FIPS
140 validated encryption by default.
Cloud Key Management Service (Cloud KMS) provides
customer-managed encryption keys (CMEKs) with software-backed
or HSM-backed storage. Cloud HSM
provides dedicated FIPS 140 Level 3 hardware-module-backed
key storage. Cloud External Key Manager (Cloud EKM) holds
key material with an external key management partner, giving
the customer custody of key material outside Google Cloud.
Key Access Justifications (KAJ) require a documented reason
before Google can access a key for operational purposes; the
customer can approve or deny each access request.

**CMMC practices implemented.** SC.L2-3.13.10 (cryptographic
key management), SC.L2-3.13.11 (FIPS-validated cryptography
for CUI), SC.L2-3.13.8 (transmission confidentiality and
integrity), and SC.L2-3.13.16 (data at rest encryption).

**Implementation notes.**

- For CUI workloads, default to CMEK rather than Google-
  managed keys. The audit-trail value, key rotation control,
  and access-policy control that assessor evidence typically
  requires all improve with CMEK.
- Cloud HSM keys are FIPS 140 Level 3 validated and
  appropriate for CUI workloads requiring hardware-module
  custody. Cloud KMS software keys are FIPS 140 Level 1.
- Cloud EKM is the path for workloads requiring off-Google
  key custody. Supported external key managers vary; the
  contractor retains the key material at the external KMS.
  Operational overhead is higher than Cloud HSM; the choice
  depends on specific audit or regulatory constraints.
- Key Access Justifications (KAJ) is a GCP-specific
  capability: Google operators requesting access to a KAJ-
  protected key must document the justification; the
  customer approves or denies. KAJ is available with Cloud
  EKM and Cloud HSM keys for specific Assured Workloads
  control packages. Use KAJ when the workload requires
  explicit operational-access gating.
- The ITAR control package requires CMEK and uses a separate
  key management project from other deployed resources, with
  unique key rings for storage within a compliance location.
- Enable automatic key rotation on CMEKs; rotation cadence
  configurable per key ring.

**FIPS 140 status (verified 2026-04-21).** Google Cloud KMS
software-backed keys are FIPS 140 validated at Level 1. Cloud
HSM hardware keys are FIPS 140 Level 3 validated. Cloud EKM
keys inherit the validation posture of the external key
manager. The specific CMVP certificate numbers for Google's
cryptographic modules cycle with module revisions; verify the
current active certificate at
csrc.nist.gov/projects/cryptographic-module-validation-program/
validated-modules/search by filtering on Google. Cite the
active certificate number in the SSP and re-verify on an
annual cadence. Both FIPS 140-2 and FIPS 140-3 validated
certificates are acceptable for CUI; FIPS 140-2 certificates
remain valid through their CMVP-published transition dates.

**Evidence to collect.**

- Cloud KMS or Cloud HSM inventory showing CMEKs for CUI
  workloads with key policies and rotation configuration.
- Per-service encryption enforcement (Cloud Storage CMEK on
  buckets, Persistent Disk encryption with CMEK, Cloud SQL
  CMEK).
- KAJ configuration if applicable, with justification
  review workflow.
- SSP section naming the active CMVP certificate(s) for the
  key management tier in use, dated.

**Common mistakes.**

- Using Google-managed encryption keys as the primary
  encryption for CUI workloads. Convenient but offers
  weaker audit-trail and access-policy control than CMEK.
- Storing CMEKs and the resources they encrypt in the same
  project. Separation of duties favors a dedicated key
  management project, and the ITAR control package enforces
  this separation explicitly.
- Citing Cloud KMS software keys (FIPS 140 Level 1) for CUI
  workloads that require FIPS 140 Level 2 or higher.
  SC.L2-3.13.11 does not mandate a specific level but many
  contract-vehicle overlays do; verify the required level
  before selecting Cloud KMS tier.

---

## Logging, monitoring, and threat detection

**Capability.** Cloud Audit Logs record administrative
activity, data access, system events, and policy denials
across Google Cloud services. Cloud Logging aggregates logs
from Google Cloud services and application workloads.
Security Command Center Premium provides
Cloud Security Posture Management (CSPM), vulnerability
detection, and threat
detection across the Google Cloud organization. Chronicle
Security Operations provides SIEM-class log analytics,
correlation, and response orchestration. Access Transparency
surfaces logs of Google operator activity on customer data,
showing what Google personnel did and when. Access Approval
allows the customer to require explicit approval before
Google operators can access customer data in specific
circumstances.

**CMMC practices implemented.** AU.L2-3.3.1 (audit event
creation), AU.L2-3.3.2 (user accountability), AU.L2-3.3.3
(event review), AU.L2-3.3.5 (audit correlation), AU.L2-3.3.8
(audit protection), SI.L2-3.14.3 (security alerts), SI.L2-3.14.6
(system monitoring), SI.L2-3.14.7 (unauthorized use detection),
and CA.L2-3.12.3 (continuous monitoring).

**Implementation notes.**

- Cloud Audit Logs are on by default for Admin Activity and
  System Events. Data Access logs are off by default and
  should be enabled explicitly for CUI-handling services
  (Cloud Storage, BigQuery, Cloud SQL, Compute Engine,
  others). Enabling Data Access logs adds meaningful audit
  value but can incur cost at scale; tune per service.
- Configure Log Router sinks to export selected logs to a
  Cloud Storage bucket in the Assured Workloads folder and
  to the contractor's SIEM. Object retention and versioning
  on the sink bucket prevent log tampering.
- Security Command Center Premium at the organization level
  aggregates findings across all projects and Assured
  Workloads folders. SCC Premium delivers the threat
  detection, posture management, and vulnerability
  findings that AU and SI practices require.
- Chronicle Security Operations sits above Cloud Logging
  and Security Command Center as a SIEM with extended
  retention (12-month default) and cross-source correlation.
  Chronicle is available in government-compliant
  configurations for CUI workloads.
- Access Transparency logs should be enabled and forwarded
  to the SIEM. Access Transparency provides visibility into
  Google operator actions on customer data; the contractor
  uses these logs to verify that operator activity stays
  within the Assured Workloads personnel-access controls.
- Access Approval with Assured Workloads: when Access
  Approval is configured, the Assured Workloads personnel-
  access assurances take precedence; Access Approval
  becomes a supplementary gate for specific access paths.

**Evidence to collect.**

- Cloud Audit Logs configuration showing enabled log types
  for CUI-scope services.
- Log Router sink configuration and destination bucket
  retention settings.
- Security Command Center Premium activation at the
  organization level with findings dashboard export.
- Chronicle configuration if in use.
- Access Transparency log sample forwarded to the SIEM.

**Common mistakes.**

- Leaving Data Access logs disabled for CUI-handling
  services. Admin activity logs show who changed
  configuration; Data Access logs show who accessed CUI. The
  latter is often the more important audit surface.
- Exporting Access Transparency logs only to Cloud Storage
  without SIEM forwarding. The operator-activity visibility
  exists but is not actively monitored.
- Relying on Security Command Center Standard for CUI
  posture monitoring. Standard provides basic findings;
  Premium adds the threat detection and vulnerability
  management that SI.L2-3.14.6 and SI.L2-3.14.7 require.

---

## Boundary protection and network

**Capability.** Google Cloud Virtual Private Cloud (VPC)
provides network isolation. VPC Service Controls (VPC-SC)
provide a service-level perimeter that prevents data
exfiltration between projects and services even where IAM
would otherwise allow access. Private Google Access exposes
Google Cloud services through internal IP addresses without
traversing the public internet. Cloud Interconnect (Dedicated
or Partner) provides private connectivity from contractor
premises to Google Cloud; Cloud VPN provides IPsec VPN as an
alternative. Google Cloud Armor protects public-facing
applications with WAF and DDoS capabilities.
Identity-Aware Proxy (IAP) provides identity-based access to
applications
without a traditional VPN.

**CMMC practices implemented.** SC.L1-3.13.1 (boundary
protection), SC.L1-3.13.5 (public access system separation),
SC.L2-3.13.6 (deny by default), SC.L2-3.13.7 (split-tunneling
prevention on endpoint connections), SC.L2-3.13.2
(architectural design for security), and AC.L2-3.1.12 (remote
access monitoring).

**Implementation notes.**

- VPC Service Controls are GCP's distinctive boundary
  primitive: they operate as a control-plane perimeter
  around a set of projects and services, blocking data
  exfiltration across the perimeter even when IAM would
  permit the access. VPC-SC is a necessary companion to IAM
  for CUI workloads; an attacker with IAM-granted Storage
  Viewer on a CUI project can extract data through the
  public Cloud Storage API unless VPC-SC blocks that path.
- VPC-SC perimeters should encompass the Assured Workloads
  folder's projects. Service perimeter ingress and egress
  rules define which identities and services can traverse
  the perimeter boundary.
- Private Google Access ensures that Google Cloud service
  calls from within a VPC traverse Google's private network
  rather than the public internet. Enable on every subnet
  that hosts CUI-workload resources.
- Cloud Interconnect with appropriate encryption (MACsec
  for Dedicated Interconnect where available, or IPsec VPN
  over Interconnect for Partner Interconnect) delivers
  non-internet private connectivity from contractor
  premises.
- Identity-Aware Proxy wraps web applications and TCP
  services with identity-based access, replacing VPN-style
  perimeter access with per-session identity verification.
  Useful for operator-tool access to CUI environments
  without VPN complexity.
- Cloud Armor enables WAF with the OWASP Core Rule Set and
  bot protection for public-facing applications; rate
  limiting and geo-based restriction complement the
  security policy.

**Evidence to collect.**

- VPC Service Controls perimeter configuration with
  included projects and ingress/egress rules, exported.
- VPC Flow Logs configuration and forwarding destination.
- Firewall rule inventory for CUI-subnet traffic with
  justification per rule.
- Private Google Access enablement per subnet.
- Cloud Interconnect or Cloud VPN configuration if
  on-premises connectivity is in scope.

**Common mistakes.**

- Deploying CUI workloads without VPC Service Controls.
  Relying on IAM alone leaves the data-exfiltration path
  through public service endpoints unprotected.
- Permissive VPC-SC ingress rules that allow identities
  from outside the perimeter. Each ingress rule should
  cite a specific justified-identity-plus-justified-service
  combination.
- Using traditional VPN for per-user access instead of
  Identity-Aware Proxy for HTTP services. IAP removes a
  class of VPN misconfiguration risks.

---

## Compute and storage service parity under Assured Workloads

**Capability.** Assured Workloads restricts which Google
Cloud services can be used within the folder. The list of
supported services varies by control package and updates over
time. The authoritative per-control-package list is at
cloud.google.com/assured-workloads/docs/supported-products.

**CMMC practices implemented.** No CMMC practice maps directly
to service parity; this is a scope-planning concern.

**Implementation notes.**

- Verify service availability against the supported-products
  page before designing a workload. A service available in
  commercial Google Cloud may not be available in an IL5
  Assured Workloads folder, or may be available with a
  reduced feature set.
- Control packages apply to the folder. A service that is
  not supported by the selected control package cannot be
  provisioned in the folder; attempting to do so returns a
  policy violation.
- New Google Cloud services arrive in Assured Workloads
  control packages on a delay relative to commercial
  general availability. A design that depends on a
  just-released service should verify Assured Workloads
  support before committing.
- The supported-products list is dynamic and differs
  between FedRAMP High, IL2, IL4, and IL5 control packages.
  IL5 typically has the tightest restrictions.
- For workloads requiring a service that is not supported in
  the selected control package, options include waiting for
  the service to be added, relaxing to a lower Impact Level
  if the workload permits, or using a Sovereign Controls
  partner configuration if applicable.

**Evidence to collect.**

- SSP section naming the Google Cloud services used by each
  CUI workload with the Assured Workloads control package
  and supported-products page verification date.
- Control-package version documentation from Workload
  Updates history.

**Common mistakes.**

- Assuming commercial Google Cloud service availability in
  an Assured Workloads folder. Design reviews must verify
  every proposed service against the supported-products
  page.
- Using a service that is supported by a control package but
  configuring it outside the folder. The service inherits
  the authorization only when deployed inside the
  Assured Workloads folder.

---

## Support and operator-access posture

**Capability.** Assured Support for Assured Workloads is an
Assured-Workloads-specific support tier available with
Enhanced Support or Premium Support. Google Cloud personnel
handling support cases adhere to geographical and
personnel-based attributes defined by the control package:
for FedRAMP High, first-level and second-level support
personnel and subprocessors must be US-located with enhanced
background checks; for IL4 and IL5, support personnel must
be IL-adjudicated US-persons located in the US.

**CMMC practices implemented.** PS.L2-3.9.1 (personnel
screening) and PS.L2-3.9.2 (personnel transfer) are inherited
from Google for the Google-operator side; the contractor
still owns these practices for contractor personnel. SR
(Supply Chain Risk Management) controls inherit from Google
under the FedRAMP authorization.

**Implementation notes.**

- Enhanced Support or Premium Support is required for
  Assured Support on Assured Workloads folders. Confirm the
  support tier matches the workload's Impact Level before
  incident-response timelines are needed.
- Support case content must not include CUI data in case
  descriptions or attachments. Google Cloud support handles
  FedRAMP-scope cases but case data sanitization is the
  contractor's responsibility.
- Access Transparency logs show Google operator activity on
  customer data; use them to verify that the personnel-
  access posture enforced by the Assured Workloads control
  package is operating as documented.
- The Google Cloud US-person operator-access posture is
  distinct from the contractor's own personnel posture. A
  non-US-person contractor employee cannot serve as a
  Google Cloud escalation contact, and may or may not be
  permitted to administer the contractor's own Google Cloud
  resources depending on the contract's export-control
  terms. If ITAR-controlled or EAR-controlled technical data
  is present in the workload, US-person-only staffing may
  apply to the contractor side as well; consult
  export-control counsel before finalizing personnel policy.
  See `references/modern-it/endpoints/remote-work.md`
  "Travel posture and OCONUS constraints" for the
  contractor-side personnel-access considerations and ITAR
  framing.

**Evidence to collect.**

- Support tier documentation per Google Cloud organization
  or Assured Workloads folder.
- Support case hygiene policy naming the CUI-scrubbing
  requirement before submission.
- Access Transparency log sample showing operator activity
  logs for CUI-scope resources.
- Google Cloud Customer Care attestations from the
  compliance reports manager or Trust Center documentation
  for personnel-screening inheritance.

**Common mistakes.**

- Attaching CUI logs or diagnostic data directly to Support
  cases. Sanitization is required before attach or
  copy-paste of production data.
- Assuming non-Assured-Workloads Support case handling
  applies to IL4 or IL5 workloads. Different posture,
  different personnel assignments; use Assured Support.
- Ignoring Access Transparency logs. The capability exists
  specifically to let the contractor verify the inherited
  personnel-access posture; not reviewing the logs is a
  missed-inheritance-evidence pattern.

---

## FedRAMP and Impact Level posture

**FedRAMP status (verified 2026-04-21).**

- Google Cloud holds FedRAMP High and FedRAMP Moderate JAB
  P-ATOs. FedRAMP High deployment requires the Assured
  Workloads FedRAMP High control package applied to the
  target folder.
- Google Workspace holds FedRAMP High and FedRAMP Moderate
  P-ATOs (via Assured Controls Plus for the productivity
  suite's CUI-adjacent posture).
- Per-service FedRAMP scope is documented at the Google
  Cloud FedRAMP and DoD compliance scope page; verify
  current status at marketplace.fedramp.gov.

**DoD Impact Level posture (verified 2026-04-21).** DISA has
granted Google Cloud Provisional Authorizations at IL2, IL4,
and IL5. Google Cloud was the first hyperscaler to receive
an IL5 PA for a software-defined community cloud offering
(2022). Google Workspace holds IL2 and IL4 PAs (not IL5;
IL4 via Assured Controls Plus). Per the hub crosswalk at
`references/modern-it/cloud-platforms/cloud-selection.md`,
IL5 now requires the FedRAMP High baseline under CSP SRG
v1r1; Google Cloud's FedRAMP High P-ATO is the baseline on
which the IL5 authorization sits. IL6 workloads require
Google Distributed Cloud air-gapped or Google Distributed
Cloud air-gapped appliance (on-premises infrastructure
outside commercial Google Cloud and outside this file's
scope).

**Overlay architecture implications for inheritance.** Unlike
AWS GovCloud and Azure Government, Google Cloud does not
operate separate infrastructure for IL4 and IL5. The
inheritance story for Google Cloud differs accordingly:
infrastructure-level controls (physical security, environmental
controls, network-fabric isolation) are inherited from the
shared Google Cloud infrastructure that also serves commercial
workloads. The control-package overlay delivers the tenant-
isolation and personnel-access guarantees that partition-based
providers deliver through physical separation. An SSP citing
Google Cloud inheritance must describe both dimensions:
infrastructure inheritance from Google Cloud and
control-package inheritance from the Assured Workloads
configuration.

**Scope boundary for IL content in this file.** This section
names Google Cloud's authorization levels and points at the
hub crosswalk. It does not implement IL4 or IL5 end-to-end.
Full IL4/IL5 implementation detail (CNSSI 1253 overlays
beyond M-M-x categorization, NSS controls if applicable,
dedicated-infrastructure requirements where applicable,
workload-category criteria) is deferred to a future
DoD-specific reference per the forward-reference in
`references/fedramp-gap.md` "Relationship to DoD Cloud
Computing Security Requirements Guide." A contractor building
an IL5 SSP should treat this file as the Google-side
capability map, not as the full IL5 control implementation.

---

## Capability appendix — CMMC capability to Google Cloud Assured Workloads native service

The appendix below is the single-provider vertical slice of
the three-column crosswalk in
`references/modern-it/cloud-platforms/cloud-selection.md`.
Rows match the hub table order; only Google Cloud services
are named.

| CMMC capability cluster | Google Cloud service (under Assured Workloads) |
|---|---|
| Identity and authentication (IA family) | Cloud Identity, Google Workspace identity, IAM, Workload Identity Federation, BeyondCorp Enterprise Context-Aware Access |
| Cryptographic key management (SC.L2-3.13.10) | Cloud KMS, Cloud HSM, Cloud External Key Manager (Cloud EKM), Key Access Justifications |
| Data at rest encryption (SC.L2-3.13.11, SC.L2-3.13.16) | Cloud Storage CMEK, Persistent Disk encryption with CMEK, Cloud SQL CMEK |
| Data in transit (SC.L2-3.13.8) | Private Google Access, VPC Service Controls, Cloud HTTPS Load Balancing with managed TLS |
| Network boundary protection (SC.L1-3.13.1, SC.L2-3.13.6) | VPC, VPC firewall rules, VPC Service Controls, Cloud Armor, Identity-Aware Proxy |
| Audit and logging (AU family) | Cloud Audit Logs, Cloud Logging, Log Router, Access Transparency |
| Continuous monitoring and threat detection (SI.L2-3.14.6, SI.L2-3.14.7) | Security Command Center Premium, Chronicle Security Operations |
| Configuration management (CM family) | Organization Policy, Assured Workloads control packages, Security Command Center posture benchmarks |

---

## Cross-domain anchors

Google Cloud Assured Workloads posture composes with the
corpus cross-cutting files and domain practice files:

- **Phase 5c hub.** `references/modern-it/cloud-platforms/cloud-selection.md`
  for the four conventions, FedRAMP-to-IL crosswalk, hybrid
  patterns, and tenancy-selection decision tree. Note the
  hub's explicit acknowledgment that GCP Assured Workloads
  is an overlay (not a separate cloud), which is why this
  file's Tenancy Selection Question 2 answers
  structurally differently from Slices K and L.
- **FedRAMP inheritance.** `references/fedramp-gap.md`
  "Inherited vs shared-responsibility controls" for the
  inheritance taxonomy.
- **CUI scoping.** `references/scoping-and-cui.md` for the
  decision of what sits in CUI scope within a Google Cloud
  tenancy.
- **SSP authoring.** `references/ssp-guidance.md` for how to
  document Assured Workloads inheritance in the SSP,
  including the overlay-architecture distinction.

Domain practice files used for requirement text and evidence
lists:

- Configuration Management (CM) — `references/domains/cm-configuration-mgmt.md`
- System and Information Integrity (SI) — `references/domains/si-system-information-integrity.md`
- System and Communications Protection (SC) — `references/domains/sc-system-comms.md`
- Identification and Authentication (IA) — `references/domains/ia-identification-auth.md`
- Access Control (AC) — `references/domains/ac-access-control.md`
- Audit and Accountability (AU) — `references/domains/au-audit.md`
- Security Assessment (CA) — `references/domains/ca-security-assessment.md`

---

## Examples as of 2026-04

> **Examples as of 2026-04:** The Google Cloud services named
> in the structural sections and the capability appendix are
> platform-native and are not in scope for the
> ranked-examples convention in the same way third-party
> products are. Where a contractor considers third-party
> alternatives for a specific capability (third-party SIEM
> instead of Chronicle, third-party EDR inside a Google
> Cloud workload, third-party identity provider federated
> via Workload Identity Federation), those vendors should
> appear in the sidebar for the relevant capability with the
> dated Examples format from the hub's "Capability-versus-
> product convention." This skill does not rank vendors.
> Verify current FedRAMP Marketplace status on
> marketplace.fedramp.gov before selecting any third-party
> service that operates alongside Google Cloud Assured
> Workloads.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/cloud-platforms/cloud-selection.md`,
`references/modern-it/endpoints/README.md`, or previous Phase
5c slices are not repeated here.

Google Cloud service names and portfolio organization drift on
a roughly annual cadence (Security Command Center tiers, Chronicle
branding, Assured Workloads control-package renaming in June 2025
are recent examples). Service names below are verified as of
2026-04-21; re-verify at cloud.google.com/security/products
before citing in an SSP.

**Assured Workloads.** The Google Cloud service that applies
a regulatory control package to a folder, enforcing
compliance posture through Organization Policy, service
restrictions, personnel access controls, and monitoring.

**Assured Controls Plus.** The Google Workspace control
package that enforces DoD IL4-aligned controls for the
productivity suite (email, calendar, Drive, Meet, Chat).
Distinct from Assured Workloads and authorized independently;
a contractor running IL4 CUI across productivity and compute
uses Assured Controls Plus for the Workspace side and Assured
Workloads for the compute side. Integration happens through
identity federation, not tenant merge. See
`references/modern-it/productivity/google-workspace.md`
(pending) for the productivity-plane treatment.

**Cloud EKM (Cloud External Key Manager).** The Google Cloud
service that holds key material with an external key
management partner outside Google Cloud.

**Cloud HSM.** Google Cloud's dedicated hardware security
module service for FIPS 140 Level 3 key custody.

**Cloud KMS (Cloud Key Management Service).** Google Cloud's
managed key service. Offers software-backed keys (FIPS 140
Level 1) and HSM-backed keys (via Cloud HSM, FIPS 140 Level
3).

**CMEK (Customer-Managed Encryption Key).** The Google Cloud
equivalent of a customer-managed key. Configured through
Cloud KMS or Cloud HSM.

**Control Package.** An Assured Workloads configuration
bundle that applies a specific regulatory baseline (FedRAMP
High, IL5, ITAR, others) to a folder. Renamed in June 2025;
functionality unchanged.

**IAP (Identity-Aware Proxy).** The Google Cloud service
providing identity-based access to applications without a
traditional VPN perimeter.

**P-ATO (Provisional Authority to Operate).** A FedRAMP
authorization historically issued by the Joint Authorization
Board. The JAB P-ATO pathway is now defunct for new
authorizations per the FedRAMP program update; existing
P-ATOs remain in force.

**KAJ (Key Access Justifications).** A Google Cloud control
requiring Google operators to document a justification
before accessing a protected key; the customer approves or
denies each request.

**SCC (Security Command Center).** The Google Cloud cloud
security posture management and threat detection service.
Premium tier required for CUI workload monitoring.

**VPC-SC (VPC Service Controls).** Google Cloud's service-
level perimeter that prevents data exfiltration between
projects and services independent of IAM grants. Necessary
boundary primitive for CUI-scope folders.
