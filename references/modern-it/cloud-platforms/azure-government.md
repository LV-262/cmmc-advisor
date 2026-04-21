# Azure Government Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); Microsoft Azure compliance documentation
> (learn.microsoft.com/en-us/azure/compliance); Azure Government
> documentation (learn.microsoft.com/en-us/azure/azure-government);
> FedRAMP Marketplace (marketplace.fedramp.gov); DoD CSP SRG v1r1
> (public.cyber.mil); NIST CMVP validated modules registry
> (csrc.nist.gov).

## Overview

This file maps Microsoft Azure Government capability patterns to
CMMC practice requirements for defense contractors hosting CUI or
FCI workloads on Azure. Azure Government is a physically and
logically separate Azure cloud environment, operated from Azure
regions in the continental United States with US-person operator
access, authorized at FedRAMP High and DoD Impact Level 5 (IL5)
under the CSP SRG v1r1 reciprocity rules.

Read this file alongside
`references/modern-it/cloud-platforms/cloud-selection.md` (the
Phase 5c hub carrying the four conventions, the FedRAMP-to-IL
crosswalk, and the tenancy-selection decision tree) and
`references/modern-it/endpoints/windows-fleet.md` (Phase 5b
per-Operating-System file carrying the GCC-versus-GCC-High
treatment that this file cross-references rather than
re-derives). Structural content here names Azure-native
capabilities; product names outside the Microsoft stack appear
only in the dated Examples sidebar.

**FedRAMP authorization summary (verified 2026-04-21).** Azure
Government holds a JAB Provisional Authority to Operate (P-ATO)
at the FedRAMP High baseline covering Azure Government Regions
US Gov Arizona, US Gov Texas, and US Gov Virginia. Microsoft
Azure Commercial Regions (non-Government) also hold a FedRAMP
High P-ATO, but Azure Commercial is not appropriate for CUI
under DFARS 252.204-7012 because Azure Commercial does not meet
the DoD IL4/IL5 operator-access requirements. Verify current
authorization status at marketplace.fedramp.gov before citing a
specific package identifier in an SSP.

**DoD Impact Level coverage.** Azure Government regions US Gov
Arizona, US Gov Texas, and US Gov Virginia hold DISA Provisional
Authorizations at IL2, IL4, and IL5 under the DoD CSP SRG v1r1
reciprocity rules. Two additional regions, US DoD Central and
US DoD East, are reserved for the exclusive use of the US
Department of Defense under a separate IL5 PA. IL6 workloads
require Azure Government Secret or Azure Government Top Secret
(classified-network environments); IL6 is out of scope for this
file. See
`references/modern-it/cloud-platforms/cloud-selection.md`
"FedRAMP baseline to DoD Impact Level crosswalk" for the full
IL-to-FedRAMP mapping under CSP SRG v1r1.

**Note on vendor documentation currency.** Microsoft's public
compliance offering pages reference the retired CC SRG v1r4 in
several places (pages dated 2023-04-04 at the time of this
file's verification). The CSP SRG v1r1 reciprocity framing in
this file follows public.cyber.mil primary-source guidance (see
`references/fedramp-gap.md` "Relationship to DoD Cloud Computing
Security Requirements Guide"), which supersedes legacy vendor
documentation where the two disagree on IL-to-FedRAMP mappings.
Microsoft's Azure Government authorizations themselves (the
FedRAMP High P-ATO, the IL2/IL4/IL5 PAs) remain in force; the
reciprocity framing is what changed.

---

## Scope of this file

Covered:

- Azure Government Regions (US Gov Arizona, US Gov Texas, US Gov
  Virginia) tenancy and service posture for CMMC Level 2
  contractors handling CUI.
- CMMC practice mapping per Azure Government capability cluster.
- Evidence-collection patterns for each practice.
- Common mistakes specific to Azure Government deployments.

Not covered:

- Azure Commercial Regions (the non-Government public Azure
  cloud). Azure Commercial holds FedRAMP High but does not meet
  DoD IL4/IL5 operator-access requirements and is not
  appropriate for CUI under DFARS 252.204-7012.
- Azure Government DoD Regions (US DoD Central, US DoD East) and
  Azure Government Secret, Azure Government Top Secret
  environments. DoD-exclusive regions serve DoD mission owners
  directly; the classified environments sit at IL6 and above.
  Contractor access patterns for those environments are
  workload-specific and outside CMMC L2 scope.
- Microsoft 365 productivity suite posture. Exchange Online,
  SharePoint Online, Teams, and productivity suite compliance
  live in `references/modern-it/productivity/microsoft-365-gcc.md`.
- The GCC versus GCC High versus Azure Government distinction at
  the Microsoft 365 productivity-plane level. Note that GCC and
  GCC High refer to Microsoft 365 productivity-plane tenancies
  (Exchange Online, SharePoint Online, Teams, Intune), whereas
  Azure Government (this file's scope) is a separate Azure
  IaaS and platform-service control-plane environment.
  The productivity-plane tenancy distinction lives in
  `references/modern-it/endpoints/windows-fleet.md`
  "Management-plane split" and is not re-derived here.
- Azure Stack (hybrid on-premises), Azure Arc (hybrid
  management), and on-premises Windows Server. Hybrid cloud
  architectures sit in the Phase 5c hub's "Hybrid patterns"
  section.

---

## Tenancy selection

Per the Phase 5c hub (Decision 3), each per-provider file
answers three tenancy-selection questions in the same order.
For Azure:

**1. Is the provider's commercial tenancy ever acceptable for
CUI?** No. Azure Commercial Regions hold FedRAMP High but do
not meet the DoD CSP SRG v1r1 operator-access restrictions that
IL4 and IL5 impose. Azure Commercial is appropriate for non-CUI
federal workloads or non-federal workloads, but CUI subject to
DFARS 252.204-7012 must reside in an Azure Government Region
where the US-person operator-access posture is in place. The
Microsoft 365 GCC tenancy is also not appropriate for CUI in
most contractor contexts; see
`references/modern-it/endpoints/windows-fleet.md`
"Management-plane split" for the GCC-versus-GCC-High
distinction at the productivity-plane level.

**2. Which government tenancy or control-plane isolation posture
is the contractor path?** Azure Government is a separate Azure
cloud environment (not an overlay on Azure Commercial). The
partition has its own Entra ID tenant structure, its own
subscription and management-group hierarchy, its own ARM
endpoints, and its own operator staff. Azure Government
Regions in scope for CMMC CUI workloads are US Gov Arizona,
US Gov Texas, and US Gov Virginia. The DoD-exclusive Azure
Government DoD Regions (US DoD Central, US DoD East) and the
classified Azure Government Secret and Azure Government Top
Secret environments are separate offerings outside CMMC L2
contractor scope.

**3. What workload-location and support-personnel-citizenship
boundaries apply inside that tenancy?** Azure Government
Regions are physically located in the continental United
States. Microsoft operator personnel with production access to
Azure Government infrastructure are screened US-persons
(citizens, US nationals, or US-persons as defined under
CSP SRG v1r1). Microsoft support handling for Azure Government
cases runs with US-person support personnel. The contractor-
side personnel posture is distinct from the Microsoft-side
posture; see "Support and operator-access posture" below and
the ITAR/EAR discussion for how contractor personnel
constraints interact.

---

## Tenancy and subscription model

**Capability.** Azure Government tenancy is organized through
Microsoft Entra ID (formerly Azure Active Directory) Government
tenants. Each Entra ID tenant holds subscriptions; subscriptions
are grouped through Management Groups in a hierarchy that
supports policy inheritance. Within a subscription, Resource
Groups hold Azure resources as a unit of deployment and access
control. Azure Policy applies at the management-group,
subscription, or resource-group level; Azure Policy initiatives
bundle related policies for a compliance framework. Azure
Blueprints and the Azure Landing Zone Accelerator reference
architecture deliver compliance-oriented multi-subscription
baselines.

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration), CM.L2-3.4.2 (configuration enforcement),
AC.L2-3.1.3 (CUI flow control), and AC.L2-3.1.5 (least
privilege at the subscription and resource-group boundary).

**Implementation notes.**

- A separate Entra ID Government tenant for CUI workloads is
  the expected posture. Some contractors operate both a
  commercial Entra ID tenant for non-CUI work and a separate
  Entra ID Government tenant for CUI; the two are federated
  for cross-tenant collaboration rather than merged.
- Management Groups should reflect the CMMC scope split (CUI
  management group, Security Protection management group,
  Contractor Risk Managed management group, out-of-scope
  management group) so Azure Policy inherits down the scope
  hierarchy.
- Azure Policy built-in initiatives exist for FedRAMP High
  (421 controls), FedRAMP Moderate (325 controls), and DoD
  IL5 (FedRAMP High plus FedRAMP+ overlays) in Azure
  Government. Select the initiative matching the workload's
  Impact Level: FedRAMP High or DoD IL5 for IL4 and IL5
  workloads; FedRAMP Moderate for IL2 workloads only. Apply
  the selected initiative at the management-group root for
  the CUI scope and review the compliance dashboard on a
  cadence.
- The Azure Landing Zone Accelerator is a Microsoft-published
  reference architecture for a compliance-oriented multi-
  subscription structure. Not a compliance requirement, but
  a well-maintained baseline when starting a new Azure
  Government deployment.
- Subscription-level Activity Log forwarding must be enforced
  through Policy to prevent a subscription from disabling its
  own audit trail.

**Evidence to collect.**

- Management Group hierarchy export showing the scope split.
- Azure Policy initiative assignments at the management-group
  level for the CUI scope (FedRAMP High and DoD IL5
  initiatives specifically).
- Policy compliance report, dated at assessment time.
- Subscription-to-scope mapping naming which subscriptions
  hold CUI workloads.

**Common mistakes.**

- Using a single Entra ID tenant spanning commercial and
  Government cloud workloads. The Entra ID tenants are
  separate identities by design; cross-cloud guest access is
  a federation concern, not a merge.
- Creating subscriptions outside the management-group
  hierarchy, then discovering Policy initiatives don't apply
  to them. Policy is inherited from the parent management
  group; an orphan subscription escapes the baseline.
- Applying a FedRAMP Moderate initiative to an IL5 scope
  instead of the FedRAMP High or DoD IL5 initiative. The
  Moderate baseline is 325 controls; the High baseline is 421
  controls; IL5 requires High plus FedRAMP+ control
  enhancements.

---

## Identity and access management

**Capability.** Microsoft Entra ID Government is the Azure
Government cloud identity and directory service (formerly
called Azure Active Directory Government). Entra ID supports
Conditional Access policies,
Privileged Identity Management (PIM) for just-in-time role
elevation, multi-factor
authentication enforcement, B2B guest collaboration, and SCIM-
based user provisioning from external identity providers.
Entra ID P1 and P2 license tiers gate specific features;
Azure Government licensing is sold separately from Azure
Commercial licensing.

**CMMC practices implemented.** IA.L1-3.5.1 (user
identification), IA.L1-3.5.2 (user authentication),
IA.L2-3.5.3 (MFA), IA.L2-3.5.4 (replay-resistant
authentication), AC.L2-3.1.1 (account management),
AC.L2-3.1.5 (least privilege), AC.L2-3.1.7 (privileged
function logging, through PIM activation events), and
AC.L2-3.1.8 (unsuccessful logon attempts, through Conditional
Access lockout policies).

**Implementation notes.**

- Workforce identity should live in the Entra ID Government
  tenant, not in a commercial tenant federated to
  Government. The identity plane is the CUI attack surface;
  CUI-capable workloads require a CUI-capable identity
  plane.
- Conditional Access is the primary enforcement mechanism for
  session-level security posture. Policies should require
  phishing-resistant MFA (FIDO2 security keys, Windows Hello
  for Business, or certificate-based authentication) for
  privileged actions. SMS-based MFA is deprecated by NIST
  SP 800-63B for Authenticator Assurance Level 2.
- PIM for Entra ID roles, Azure roles, and (where applicable)
  PIM for Groups delivers just-in-time privileged access
  with approval workflows and activation logging. Standing
  privileged role assignments should be the exception, not
  the default.
- B2B guest collaboration enables external-user access to
  specific resources without extending the Entra ID tenant.
  Guests accessing CUI require the same MFA and Conditional
  Access posture as members.
- Hybrid identity patterns: Entra Connect synchronizes from
  on-premises Active Directory to Entra ID Government. For
  CUI contractors with existing on-premises AD, Entra Connect
  is the typical integration; the on-premises AD becomes an
  in-scope identity source for CUI workloads.
- FedRAMP requirements for MFA are tightening under the
  ongoing FedRAMP Rev 5 RFC process; contractors should
  review the current FedRAMP phishing-resistant-MFA guidance
  and NIST SP 800-63B for authenticator selection.

**Evidence to collect.**

- Entra ID tenant configuration export showing the tenant
  location (Government cloud) and the directory identity
  provider configuration.
- Conditional Access policy export with the MFA and
  session-control policies applied to CUI scope.
- PIM role assignment inventory showing just-in-time versus
  permanent assignments.
- Authentication methods policy showing phishing-resistant
  methods enforced.
- Sign-in log sample from Entra ID forwarded to the SIEM,
  dated.

**Common mistakes.**

- Configuring Entra Connect to synchronize all on-premises AD
  users to Entra ID Government, including users outside the
  CUI scope. The Entra ID Government tenant should receive
  only users who need CUI-capable identity; other users stay
  in a separate identity plane.
- Using SMS or phone-call MFA as the primary factor.
  Phishing-resistant methods are the assessor-preferred
  default; SMS fallback is acceptable only as a recovery
  path for a phishing-resistant primary.
- Granting standing privileged roles (Global Administrator,
  User Access Administrator) to regular staff. These roles
  are PIM-eligible-only by default; standing assignment is a
  deliberate exception.

---

## Encryption and key management

**Capability.** Azure Key Vault provides managed cryptographic
key storage in three tiers: Standard (software-protected
keys), Premium (HSM-protected keys in shared HSMs), and
Managed HSM (dedicated single-tenant HSMs). Azure Managed HSM
is the single-tenant FIPS 140 Level 3 option. Azure Storage
Service Encryption, Azure Disk Encryption,
SQL Transparent Data Encryption (TDE), and other services
integrate with Key Vault for customer-managed-key (CMK)
scenarios. Azure
Confidential Computing extends the encryption model with
trusted execution environments for data-in-use protection.

**CMMC practices implemented.** SC.L2-3.13.10 (cryptographic
key management), SC.L2-3.13.11 (FIPS-validated cryptography
for CUI), SC.L2-3.13.8 (transmission confidentiality and
integrity), and SC.L2-3.13.16 (data at rest encryption).

**Implementation notes.**

- For CUI workloads, default to Key Vault Premium (shared
  HSMs, FIPS 140 Level 2-or-3 validated) or Managed HSM
  (dedicated HSMs, FIPS 140 Level 3) for CMKs. Key Vault
  Standard is software-protected and is not appropriate as
  the primary key custody for CUI.
- Managed HSM is the path for workloads requiring single-
  tenant HSM custody of key material. The operational
  overhead (administrator-role model, backup-and-recovery
  workflow, quorum operations) is non-trivial; use Key Vault
  Premium unless a specific requirement demands Managed HSM
  custody.
- Enable key rotation on CMKs. Customer-managed keys for
  Azure Storage, SQL TDE, and Azure Disk Encryption support
  automatic rotation on a configurable cadence.
- Configure service-specific encryption to use the CMK rather
  than Microsoft-managed keys. Storage accounts, SQL
  databases, Azure Disk Encryption, and other services each
  have their own CMK selection; the default is Microsoft-
  managed unless explicitly set.
- For FIPS-validated transport endpoints, Azure services
  expose TLS endpoints that negotiate FIPS-approved cipher
  suites by default in Azure Government. Verify TLS minimum
  version enforcement (TLS 1.2 or later) at the service
  configuration level.

**FIPS 140 status (verified 2026-04-21).** Azure services in
Azure Government use FIPS 140-validated cryptographic modules.
Azure Key Vault Premium uses HSMs validated at FIPS 140 Level
2. Azure Managed HSM uses HSMs validated at FIPS 140 Level 3.
The specific CMVP certificate numbers for Microsoft's HSM
modules cycle with firmware revisions; verify the current
active certificate at
csrc.nist.gov/projects/cryptographic-module-validation-program/
validated-modules/search by filtering on Microsoft. Cite the
active certificate number in the SSP and re-verify on an
annual cadence. Both FIPS 140-2 and FIPS 140-3 validated
certificates are acceptable for CUI; FIPS 140-2 certificates
remain valid through their CMVP-published transition dates.

**Evidence to collect.**

- Key Vault / Managed HSM inventory showing CMKs for CUI
  workloads with access policies, rotation settings, and
  purge protection enabled.
- Per-service encryption enforcement (Storage account
  encryption scope, SQL TDE with CMK, Disk Encryption sets).
- TLS version enforcement at the App Service / API Management
  / storage firewall level.
- SSP section naming the active CMVP certificate(s) for the
  Key Vault or Managed HSM tier in use, dated.

**Common mistakes.**

- Using Microsoft-managed keys as the primary encryption
  keys for CUI workloads. Customer-managed keys via Key
  Vault or Managed HSM are the assessor-preferred pattern;
  Microsoft-managed keys are convenient but offer weaker
  audit-trail and access-policy control.
- Forgetting to enable purge protection on Key Vault. A
  deleted key without purge protection is recoverable but a
  deleted key with purge protection prevents permanent data
  loss during a disaster-recovery scenario or a rogue-admin
  deletion event.
- Mixing Key Vault Standard and Premium for the same CUI
  workload. Some keys are in HSM custody; others are in
  software. The SSP evidence becomes harder to defend.

---

## Logging, monitoring, and threat detection

**Capability.** Azure Monitor collects resource-level metrics,
Activity Logs (management-plane operations), Diagnostic Logs
(resource-specific events), and application-level telemetry.
Log Analytics Workspaces provide centralized log storage and
KQL-based querying. Microsoft Sentinel sits on top of Log
Analytics as a SIEM and SOAR platform. Microsoft Defender for
Cloud provides cloud security posture management (CSPM) and
workload protection across Azure, hybrid, and multi-cloud
environments. Microsoft Defender services (Defender for
Servers, Defender for Storage, Defender for Containers,
Defender for Key Vault, Defender for SQL, others) provide
service-specific threat detection and vulnerability management.

**CMMC practices implemented.** AU.L2-3.3.1 (audit event
creation), AU.L2-3.3.2 (user accountability), AU.L2-3.3.3
(event review), AU.L2-3.3.5 (audit correlation), AU.L2-3.3.6
(audit reduction and reporting), AU.L2-3.3.8 (audit
protection), SI.L2-3.14.3 (security alerts), SI.L2-3.14.6
(system monitoring), SI.L2-3.14.7 (unauthorized use
detection), and CA.L2-3.12.3 (continuous monitoring).

**Implementation notes.**

- Enable Diagnostic Settings on every resource in CUI scope
  to forward resource-level logs to a Log Analytics Workspace
  in the same tenant. Use Azure Policy to enforce Diagnostic
  Settings at the subscription or management-group level.
- Activity Log forwarding from every subscription to a
  dedicated security Log Analytics Workspace owned by the
  security team is the typical centralization pattern. Use
  a dedicated logging subscription so workload administrators
  cannot tamper with log retention.
- Microsoft Sentinel should be enabled on the security Log
  Analytics Workspace. Sentinel connectors ingest Entra ID
  sign-in logs, Activity Logs, Defender findings, and
  third-party sources. Analytics rules translate to
  incidents; SOAR playbooks automate response.
- Defender for Cloud enabled at the subscription level
  surfaces posture findings (misconfiguration, missing
  patches, weak encryption) and, with Defender plans enabled
  per service, workload-protection alerts.
- Defender for Servers (Plan 1 or Plan 2) provides EDR-like
  telemetry for Azure VMs, Arc-enabled servers, and
  on-premises servers. Plan 2 adds vulnerability assessment
  and file-integrity monitoring.
- Log retention: Log Analytics Workspace default retention
  should be set to a CUI-appropriate floor (often 365 days
  minimum); archive tier for longer retention at lower cost.
  Retention is tuned per workspace and per table.

**Evidence to collect.**

- Diagnostic Settings policy assignment at the management-
  group level.
- Log Analytics Workspace configuration showing connected
  data sources and retention settings.
- Sentinel configuration showing enabled analytics rules,
  connectors, and incident workflows.
- Defender for Cloud Secure Score report, dated at
  assessment time.
- Sample end-to-end trace of a CUI resource event through
  Diagnostic Settings to Sentinel, dated.

**Common mistakes.**

- Leaving Diagnostic Settings unconfigured on many
  resources. Default Azure resource behavior is not to
  forward logs; each resource needs explicit configuration
  or a Policy assignment.
- Putting the security Log Analytics Workspace in the same
  subscription as workload administrators have write access
  to. An attacker with workload-subscription administrator
  access can tamper with the workspace unless it is in a
  separate locked-down subscription.
- Enabling Defender for Cloud at the free tier and assuming
  it covers CUI monitoring. The free tier provides CSPM
  only; workload protection (Defender for Servers, Storage,
  Key Vault, others) requires the paid tier and is where
  the SI.L2-3.14.6 monitoring value lives.

---

## Boundary protection and network

**Capability.** Azure Virtual Network (VNet) is the network
isolation primitive. Network Security Groups (NSGs, stateful
filtering) and Azure Firewall Premium (stateful, IDS/IPS,
TLS inspection) enforce traffic policy. Azure Private Link
exposes Azure services as private endpoints inside a VNet.
Azure ExpressRoute provides private connectivity from
contractor premises to Azure, with ExpressRoute Government
variants for Azure Government Regions. Azure Front Door and
Azure Web Application Firewall (WAF) protect public-facing
applications. Azure Bastion provides RDP and SSH access to
VMs without public IP addresses.

**CMMC practices implemented.** SC.L1-3.13.1 (boundary
protection), SC.L1-3.13.5 (public access system separation),
SC.L2-3.13.6 (deny by default), SC.L2-3.13.7 (split-tunneling
prevention where endpoint VPNs or ExpressRoute are in use),
SC.L2-3.13.2 (architectural design for security), and
AC.L2-3.1.12 (remote access monitoring).

**Implementation notes.**

- Separate VNets for CUI and non-CUI workloads. Shared VNets
  across scope boundaries create unnecessary CUI scope
  creep.
- Network Security Groups operate at subnet and NIC levels.
  Principle of least privilege applies; NSG rules should be
  source-specific and port-specific.
- Azure Firewall Premium provides centralized stateful
  filtering including TLS inspection and IDS/IPS. Use as
  the hub firewall in a hub-and-spoke topology; per-subnet
  NSGs provide defense-in-depth.
- Private Link and Private Endpoints move Azure service
  traffic off the public Azure endpoint and into the VNet.
  Every Azure service call from within a CUI VNet should
  traverse a private endpoint unless documented otherwise.
- ExpressRoute Government for on-premises connectivity
  terminates in Azure Government Regions with end-to-end
  private transport. Configure ExpressRoute with FIPS-
  compliant encryption where the link crosses non-Microsoft
  infrastructure.
- Azure Bastion delivers browser-based SSH and RDP access
  without exposing VM public IPs. Use Bastion instead of
  jump-host VMs on the public internet.
- Azure WAF (in Azure Front Door or Azure Application
  Gateway) protects public-facing applications from common
  web attacks. Enable the managed rule sets for
  OWASP Top 10 and bot protection.

**Evidence to collect.**

- VNet inventory with subnet-to-scope mapping.
- Network Security Group ruleset export for CUI subnets
  with justification per ingress rule.
- Azure Firewall Premium policy configuration and IDS/IPS
  enablement state.
- Private Endpoint inventory showing service-by-service
  private-endpoint configuration.
- ExpressRoute configuration and BGP peering documentation
  if on-premises connectivity is in scope.

**Common mistakes.**

- Relying on public-service endpoints with IP-address
  allowlisting instead of Private Link. IP allowlists are
  weaker than private endpoints and drift as network
  topology changes.
- Permissive NSG rules (`Internet` source on non-public
  services). Common finding; Defender for Cloud surfaces
  these as misconfigurations.
- Disabling Azure Firewall for development environments
  without restoring it in production.

---

## Compute and storage service parity

**Capability.** Azure Government supports a subset of Azure
Commercial services. Service availability in Azure Government
Regions is documented at
azure.microsoft.com/global-infrastructure/services and at
learn.microsoft.com/en-us/azure/azure-government for
Government-specific differences. New Azure services arrive
in Azure Government on a delay relative to Azure Commercial.

**CMMC practices implemented.** No CMMC practice maps directly
to service parity; this is a scope-planning concern that
affects which services the contractor actually uses.

**Implementation notes.**

- The authoritative list of Azure services in scope for
  FedRAMP High and DoD IL2/IL4/IL5 in Azure Government is at
  learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope.
  Verify service availability and authorization level at
  that page before designing a workload.
- Service availability differs between US Gov Arizona, US
  Gov Texas, and US Gov Virginia. Multi-region
  architectures must verify per-Region service availability.
- FedRAMP or IL authorization for a service in Azure
  Government is service-level, not feature-level. An
  authorized service may have specific features or
  configurations that are not in the authorization
  boundary.
- Azure Government Regions operate with the same ARM API
  surface as Azure Commercial but on a separate endpoint
  (`management.usgovcloudapi.net`). Deployment tooling
  (Terraform, Bicep, ARM templates, Azure CLI, Azure
  PowerShell) requires explicit cloud-selection
  configuration to target Azure Government.

**Evidence to collect.**

- SSP section naming the specific Azure Government services
  used by each CUI workload with the FedRAMP / IL
  authorization level for each, dated.
- Verification record showing the services-in-scope page was
  consulted at SSP authoring time.

**Common mistakes.**

- Assuming Azure Commercial service availability in Azure
  Government. Design reviews must verify every proposed
  service against the services-in-scope page.
- Deploying to Azure Commercial by mistake due to tooling
  default-cloud selection. Terraform, Azure CLI, Azure
  PowerShell, and Bicep tooling all default to the commercial
  cloud; Azure Government deployment requires explicit cloud
  override (`az cloud set --name AzureUSGovernment` for
  Azure CLI; `environment = "usgovernment"` in Terraform
  azurerm provider; `Connect-AzAccount -Environment
  AzureUSGovernment` in Azure PowerShell). Verify the active
  cloud context before any deployment command.

---

## Microsoft Compliance Manager overlay

**Compliance Manager is not an authorization source.** It is
a workflow artifact maintained by Microsoft that maps
Microsoft-operated control attestations to regulatory
frameworks. The actual authorizations (FedRAMP High P-ATO,
DoD IL2/IL4/IL5 PAs) exist independently of Compliance
Manager and are issued by FedRAMP PMO and DISA respectively.
Do not treat Compliance Manager output as the authoritative
interpretation of FedRAMP or DoD CSP SRG requirements;
Compliance Manager is a starting point for SSP evidence, not
the control implementation itself.

**Capability.** Microsoft Purview Compliance Manager (formerly
Service Trust Portal Compliance Manager) is a Microsoft-
provided compliance posture tool that maps Microsoft-operated
controls to regulatory frameworks including FedRAMP High,
FedRAMP Moderate, CMMC Level 1, CMMC Level 2, NIST SP 800-171,
and DoD IL5. Compliance Manager provides a scored view of
customer versus Microsoft responsibility per control,
downloadable implementation details for Microsoft-operated
controls, and improvement-action tracking for customer-side
controls.

**CMMC practices implemented.** Compliance Manager is a
documentation and tracking surface, not a control
implementation. It supports the SSP authoring workflow
(CA.L2-3.12.1 assessment, CA.L2-3.12.2 deficiency tracking,
CA.L2-3.12.3 continuous monitoring) by providing
Microsoft-side control inheritance details that feed the
SSP narrative.

**Implementation notes.**

- Compliance Manager is accessed through
  compliance.microsoft.com with an Entra ID account that has
  the appropriate role. Azure Government tenants access
  Compliance Manager through the Government-tenant endpoint
  separately from Commercial.
- Microsoft-side controls downloaded from Compliance Manager
  are Microsoft's attestations of their own control
  implementation. They are useful for SSP inheritance
  sections but are not a substitute for the contractor's
  own SSP narrative.
- Compliance Manager assessment content updates on
  Microsoft's release cadence; verify the content currency
  at the tool when pulling an artifact for an SSP.
- Compliance Manager is a Microsoft-specific tool, not a
  regulatory framework. The FedRAMP and DoD IL authorizations
  themselves exist independently of the tool; Compliance
  Manager provides a customer-facing view of the existing
  authorizations.

**Compliance Manager status (verified 2026-04-21).** Compliance
Manager assessment packs for FedRAMP High, CMMC Level 2, DoD
IL5, and NIST SP 800-171 are maintained by Microsoft and
updated on Microsoft's release cadence. The CMMC Level 2
assessment pack reflects the DoD CMMC 2.0 final rule; verify
the pack's metadata version and last-update date at the tool
before extracting artifacts for an SSP.

**Evidence to collect.**

- Compliance Manager assessment status export for the
  relevant assessments (FedRAMP High, CMMC Level 2, DoD
  IL5, NIST SP 800-171) with the assessment pack version and
  export date.
- Microsoft-side control responsibility attestations pulled
  from Compliance Manager for each inherited control.
- Improvement-action progress report if Compliance Manager
  is used as the customer-side tracking tool.

**Common mistakes.**

- Treating Compliance Manager output as a completed SSP.
  The tool provides Microsoft-side inheritance content; the
  customer-side narrative, evidence, and implementation
  details are the contractor's responsibility.
- Using Compliance Manager Commercial data to support an
  Azure Government SSP. The tenancy-specific data is
  different; use the Azure Government Compliance Manager
  instance.
- Letting Compliance Manager assessment packs go stale in
  the SSP. Re-verify the assessment pack version at each
  SSP update cadence.

---

## Support and operator-access posture

**Capability.** Microsoft Azure Government Support operates
with screened US-person support personnel handling cases for
Azure Government tenants. Azure Support plans (Developer,
Standard, Professional Direct, Unified) apply separately to
Azure Government tenants from Azure Commercial tenants.
Microsoft Azure Government operator personnel with production
access to Azure Government infrastructure are screened
US-persons per CSP SRG v1r1 CSP Personnel Requirements.

**CMMC practices implemented.** PS.L2-3.9.1 (personnel
screening) and PS.L2-3.9.2 (personnel transfer) are inherited
from Microsoft for the Microsoft-operator side; the contractor
still owns these practices for contractor personnel. SR
(Supply Chain Risk Management) controls inherit from Microsoft
under the FedRAMP authorization.

**Implementation notes.**

- Azure Government Support plans are priced separately from
  Azure Commercial. CUI workloads typically require
  Professional Direct tier or Unified for incident response
  SLAs that match CMMC assessment expectations.
- Support cases must not include CUI data in case
  descriptions or attachments. Microsoft support handles
  FedRAMP-scope cases for Government tenants, but case data
  sanitization is the contractor's responsibility.
- The Microsoft US-person operator-access posture is
  distinct from the contractor's own personnel posture. A
  non-US-person contractor employee cannot serve as a
  Microsoft escalation contact, and may or may not be
  permitted to administer the contractor's own Azure
  Government resources depending on the contract's
  export-control terms. If ITAR-controlled or EAR-controlled
  technical data is present in the workload, US-person-only
  staffing may apply to the contractor side as well;
  consult export-control counsel before finalizing
  personnel policy. See
  `references/modern-it/endpoints/remote-work.md`
  "Travel posture and OCONUS constraints" for the
  contractor-side personnel-access considerations and ITAR
  framing.

**Evidence to collect.**

- Azure Government Support plan level documentation per
  tenant.
- Support case hygiene policy naming the CUI-scrubbing
  requirement before submission.
- Relevant sections of Microsoft's FedRAMP System Security
  Plan downloaded through Service Trust Portal or
  Compliance Manager for personnel-screening inheritance.

**Common mistakes.**

- Attaching CUI logs or diagnostic data directly to Support
  cases. Sanitization is required before any attach or
  copy-paste of production data.
- Assuming Azure Commercial Support case handling applies in
  Azure Government. Different posture, different case-
  management portals.

---

## FedRAMP and Impact Level posture

**FedRAMP status (verified 2026-04-21).**

- Azure Government holds a JAB Provisional Authority to
  Operate (P-ATO) at the FedRAMP High baseline covering
  Azure Government Regions US Gov Arizona, US Gov Texas, and
  US Gov Virginia.
- Per-service authorization detail is at
  learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope.
  Verify specific services used in a workload at that page
  at SSP authoring time.
- Regulatory Compliance initiatives in Azure Policy (FedRAMP
  High, FedRAMP Moderate, DoD IL5) provide a built-in
  starting point for control implementation tracking.

**DoD Impact Level posture (verified 2026-04-21).** Azure
Government Regions US Gov Arizona, US Gov Texas, and US Gov
Virginia hold DISA Provisional Authorizations at IL2, IL4, and
IL5 under the CSP SRG v1r1 reciprocity rules. Azure Government
DoD Regions US DoD Central and US DoD East hold a separate IL5
PA for DoD-exclusive mission owners. Per the hub crosswalk at
`references/modern-it/cloud-platforms/cloud-selection.md`, IL5
now requires the FedRAMP High baseline (a change from the
retired CC SRG v1r4); Azure Government's FedRAMP High P-ATO
is the baseline on which the IL5 authorization sits.

**Scope boundary for IL content in this file.** This section
names Azure Government's authorization levels and points at the
hub crosswalk. It does not implement IL4 or IL5 end-to-end.
Full IL4/IL5 implementation detail (CNSSI 1253 overlays, NSS
controls if applicable, dedicated-infrastructure requirements,
workload-category criteria) is deferred to a future
DoD-specific reference per the forward-reference in
`references/fedramp-gap.md` "Relationship to DoD Cloud
Computing Security Requirements Guide." A contractor building
an IL5 SSP should treat this file as the Azure-side capability
map, not as the full IL5 control implementation.

---

## Capability appendix — CMMC capability to Azure Government native service

The appendix below is the single-provider vertical slice of the
three-column crosswalk in
`references/modern-it/cloud-platforms/cloud-selection.md`. Rows
match the hub table order; only Azure Government services are
named.

| CMMC capability cluster | Azure Government service |
|---|---|
| Identity and authentication (IA family) | Microsoft Entra ID Government, Conditional Access, PIM, Entra Connect |
| Cryptographic key management (SC.L2-3.13.10) | Azure Key Vault Premium, Azure Managed HSM |
| Data at rest encryption (SC.L2-3.13.11, SC.L2-3.13.16) | Storage Service Encryption, Disk Encryption with CMK, SQL TDE with CMK |
| Data in transit (SC.L2-3.13.8) | Private Link, Private Endpoints, ExpressRoute Government, TLS via Key Vault certificates |
| Network boundary protection (SC.L1-3.13.1, SC.L2-3.13.6) | VNet, NSGs, Azure Firewall Premium, WAF, Azure Bastion |
| Audit and logging (AU family) | Azure Monitor, Log Analytics, Activity Log, Diagnostic Settings, Microsoft Sentinel |
| Continuous monitoring and threat detection (SI.L2-3.14.6, SI.L2-3.14.7) | Microsoft Defender for Cloud, Defender plans (Servers, Storage, Containers, Key Vault, SQL), Microsoft Sentinel |
| Configuration management (CM family) | Azure Policy, Azure Blueprints, Management Groups, Defender for Cloud posture benchmarks |

---

## Cross-domain anchors

Azure Government posture composes with the corpus cross-cutting
files and domain practice files:

- **Phase 5c hub.** `references/modern-it/cloud-platforms/cloud-selection.md`
  for the four conventions, FedRAMP-to-IL crosswalk, hybrid
  patterns, and tenancy-selection decision tree.
- **FedRAMP inheritance.** `references/fedramp-gap.md`
  "Inherited vs shared-responsibility controls" for the
  inheritance taxonomy.
- **CUI scoping.** `references/scoping-and-cui.md` for the
  decision of what sits in CUI scope within an Azure
  Government tenancy.
- **SSP authoring.** `references/ssp-guidance.md` for how to
  document Azure Government inheritance in the SSP.
- **Windows endpoint management on Azure Government.**
  `references/modern-it/endpoints/windows-fleet.md`
  "Management-plane split" carries the GCC versus GCC High
  versus Azure Government distinction at the Microsoft 365
  productivity-plane level. This file (azure-government.md)
  handles Azure IaaS and platform services; windows-fleet.md
  handles Intune management-plane tenancy decisions.
- **Remote work.** `references/modern-it/endpoints/remote-work.md`
  for VDI and DaaS patterns (Azure Virtual Desktop, Windows
  365) that run on Azure Government.

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

> **Examples as of 2026-04:** The Microsoft Azure Government
> services named in the structural sections and the capability
> appendix are platform-native and are not in scope for the
> ranked-examples convention in the same way third-party
> products are. Where a contractor considers third-party
> alternatives for a specific capability (third-party SIEM
> instead of Microsoft Sentinel, third-party EDR instead of
> Defender for Servers, third-party identity provider federated
> into Entra ID Government), those vendors should appear in the
> sidebar for the relevant capability with the dated Examples
> format from the hub's "Capability-versus-product convention."
> This skill does not rank vendors. Verify current FedRAMP
> Marketplace status on marketplace.fedramp.gov before selecting
> any third-party service that operates alongside Azure
> Government.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/cloud-platforms/cloud-selection.md`,
`references/modern-it/endpoints/README.md`, or
`references/modern-it/endpoints/windows-fleet.md` are not
repeated here.

**ARM (Azure Resource Manager).** The deployment and
management API surface for Azure resources.

**CMK (customer-managed key).** A cryptographic key the
customer controls through Azure Key Vault or Azure Managed
HSM, as distinct from a Microsoft-managed key where
Microsoft holds key custody.

**CSPM (Cloud Security Posture Management).** A category of
tooling (Microsoft Defender for Cloud, among others) that
surfaces misconfiguration and posture weaknesses in cloud
deployments.

**Conditional Access.** The Entra ID policy engine that
evaluates session context (user, device, location, risk) at
sign-in time and enforces policy outcomes.

**Entra Connect.** Microsoft's directory synchronization tool
from on-premises Active Directory to Microsoft Entra ID
(formerly Azure AD Connect).

**ExpressRoute.** The Microsoft private-connectivity service
from on-premises networks to Azure. ExpressRoute Government
serves Azure Government Regions.

**KQL (Kusto Query Language).** The query language used in
Log Analytics Workspaces and Microsoft Sentinel.

**Managed HSM (Azure Key Vault Managed HSM).** The single-
tenant FIPS 140 Level 3 HSM offering in Azure Key Vault.

**NSG (Network Security Group).** The Azure stateful
per-subnet or per-NIC traffic filter.

**PIM (Privileged Identity Management).** The Entra ID
just-in-time privileged-role activation service.

**SOAR (Security Orchestration, Automation, and Response).**
A category of tooling that automates incident response
playbooks. Microsoft Sentinel includes SOAR capabilities.

**TDE (Transparent Data Encryption).** The SQL Server and
Azure SQL data-at-rest encryption feature.

**VNet (Virtual Network).** The Azure network isolation
primitive; the Azure counterpart to AWS VPC.
