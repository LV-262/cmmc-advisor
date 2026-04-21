# AWS GovCloud Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); AWS FedRAMP compliance documentation
> (aws.amazon.com/compliance/fedramp); AWS Services in Scope
> (aws.amazon.com/compliance/services-in-scope); AWS DoD CC SRG
> compliance (aws.amazon.com/compliance/dod); AWS GovCloud User Guide
> (docs.aws.amazon.com/govcloud-us); DoD CSP SRG v1r1 (public.cyber.mil);
> NIST CMVP validated modules registry (csrc.nist.gov).

## Overview

This file maps AWS GovCloud (US) capability patterns to CMMC
practice requirements for defense contractors hosting CUI or FCI
workloads on AWS. AWS GovCloud is a physically and logically
separate set of AWS Regions (AWS GovCloud US-East and
AWS GovCloud US-West) designed for US government workloads
with US-person operator access, hardened against FedRAMP High
and DoD Impact Level (IL) overlay requirements.

Read this file alongside
`references/modern-it/cloud-platforms/cloud-selection.md` (the
Phase 5c hub carrying the four conventions this directory
follows, the FedRAMP-to-IL crosswalk, and the tenancy-selection
decision tree). Structural content here names AWS GovCloud
capabilities; product names outside AWS appear only in the
dated Examples sidebar.

**FedRAMP authorization summary (verified 2026-04-21).** AWS
GovCloud (US) holds a
JAB Provisional Authority to Operate (P-ATO) at the FedRAMP
High baseline. The FedRAMP marketplace identifier for the AWS
GovCloud (US) package is F1603047866.
The JAB P-ATO pathway is now defunct for new authorizations;
the AWS GovCloud P-ATO remains in force but will not be
re-issued as an Agency ATO because FedRAMP no longer issues
ATOs to CSPs. Agencies issue their own ATOs against the AWS
authorization package. AWS GovCloud is listed with FedRAMP
High authorization on marketplace.fedramp.gov; verify current
status at the marketplace before citing in an SSP.

**DoD Impact Level coverage.** AWS GovCloud (US) supports
workloads at IL2, IL4, and IL5 per the DoD CSP SRG v1r1
reciprocity rules. IL6 workloads require classified-network
hosting (out of scope for AWS GovCloud commercial service).
See `references/modern-it/cloud-platforms/cloud-selection.md`
"FedRAMP baseline to DoD Impact Level crosswalk" for the
IL-to-FedRAMP mapping.

---

## Scope of this file

Covered:

- AWS GovCloud (US-East) and AWS GovCloud (US-West) tenancy
  and service posture.
- CMMC practice mapping per capability cluster.
- Evidence-collection patterns for each practice.
- Common mistakes specific to AWS GovCloud deployments.

Not covered:

- AWS US East-West commercial Regions (Northern Virginia, Ohio,
  Oregon, Northern California). Those Regions hold FedRAMP
  Moderate (P-ATO ID AGENCYAMAZONEW) and may be appropriate
  for non-CUI federal workloads, but are not in scope for this
  CUI-focused file.
- AWS China Regions, AWS Secret Region, AWS Top Secret Region.
  Those are separate partitions with different authorization
  pathways outside CMMC scope.
- Workload-level architecture decisions. This file maps the
  posture of AWS GovCloud services to CMMC practices; specific
  workload architectures (which services to use for a given
  application) are engineering decisions outside this skill.
- Commercial AWS service-feature releases and quota management.
  Those drift on AWS's commercial release cadence and are
  covered by AWS documentation directly.

---

## Tenancy selection

Per the Phase 5c hub (Decision 3), each per-provider file
answers three tenancy-selection questions in the same order.
For AWS:

**1. Is the provider's commercial tenancy ever acceptable for
CUI?** No. AWS commercial Regions (US East-West, Europe,
Asia-Pacific, and others) hold FedRAMP Moderate only; their
operator-access posture does not meet the US-person
requirement that DoD Impact Level overlays impose for CUI.
Commercial AWS is appropriate for non-CUI federal workloads
(IL2-equivalent Moderate) and non-federal workloads but must
not host CUI subject to DFARS 252.204-7012.

**2. Which government tenancy or control-plane isolation
posture is the contractor path?** AWS GovCloud (US) is a
separate AWS partition (`aws-us-gov`) with two Regions
(US-East and US-West). The partition is physically and
logically isolated from commercial AWS with distinct
accounts, distinct IAM principals, distinct APIs, and
distinct operator staff. There is no control-plane-overlay
path on commercial AWS that is equivalent to GovCloud for
CUI; the partition separation is the tenancy boundary.

**3. What workload-location and support-personnel-citizenship
boundaries apply inside that tenancy?** AWS GovCloud Regions
are located in the continental United States. AWS operator
personnel with production access to GovCloud Region
infrastructure are US-persons (citizens or lawful permanent
residents). GovCloud Support handles cases with US-person
support personnel; support case handling runs in a separate
posture from commercial AWS Support. The contractor-side
personnel posture is distinct from the AWS-side personnel
posture; see "Support and operator-access posture" below and
"ITAR and EAR note" for how contractor personnel constraints
interact with AWS's posture.

---

## Tenancy and account model

**Capability.** AWS GovCloud (US) is a separate AWS partition
(`aws-us-gov`) containing two Regions: AWS GovCloud (US-East)
and AWS GovCloud (US-West). A contractor subscribes to the
GovCloud partition separately from commercial AWS; a GovCloud
root account is distinct from a commercial root account, even
under the same corporate ownership. AWS Organizations operates
within GovCloud to manage multi-account tenancies, and
AWS Control Tower delivers landing-zone automation for GovCloud
Organizations. AWS Landing Zone Accelerator (open-source
reference implementation) builds on Control Tower for
federal-specific multi-account baselines.

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration), CM.L2-3.4.2 (configuration enforcement),
AC.L2-3.1.3 (CUI flow control at account boundaries), and
AC.L2-3.1.5 (least privilege at the organizational unit
boundary). The account model is the substrate for every other
capability on this list.

**Implementation notes.**

- Separate AWS Organizations for CUI and non-CUI workloads is
  the expected posture. Mixing CUI and non-CUI accounts under
  the same Organization creates CUI-scope ambiguity and is
  harder to defend in assessment.
- AWS Control Tower is available in both GovCloud Regions.
  Control Tower delivers guardrails (Service Control Policies,
  Config rules, CloudTrail enforcement) as a baseline.
  Resource Control Policies (RCPs) are available in both
  GovCloud Regions as of 2025.
- Landing Zone Accelerator on AWS (LZA) is an AWS-published
  reference implementation that automates a compliance-oriented
  multi-account structure including federal-specific features
  (logging account, security account, centralized KMS). LZA is
  not a compliance requirement; it is a well-maintained
  reference architecture.
- Account-level CloudTrail and Config must be enforced through
  Control Tower guardrails or equivalent SCPs to prevent a
  member account from disabling them locally.

**Evidence to collect.**

- Organization structure export showing CUI-scope OU hierarchy.
- Service Control Policy inventory with the CUI-protecting
  SCPs (block non-GovCloud Region usage, enforce CloudTrail,
  deny public S3 access, enforce encryption-required).
- Control Tower guardrail compliance report, dated.
- Account inventory mapping each account to its
  scope-category (CUI, Security Protection, Contractor Risk
  Managed, out of scope).

**Common mistakes.**

- Using a single AWS Organization spanning commercial and
  GovCloud partitions. This is not technically possible; the
  partitions are isolated. Contractors sometimes discover this
  mid-design after planning for "one Organization."
- Creating GovCloud accounts without enrolling them in Control
  Tower, then discovering that the baseline guardrails are not
  enforced. Manual per-account configuration drifts.
- Failing to restrict IAM in the management account. Write
  access to the management account grants override of every
  SCP; treat the management account as the most-privileged
  asset in the CUI scope.

---

## Identity and access management

**Capability.** AWS Identity and Access Management (IAM) is
the core identity service in AWS GovCloud. AWS IAM Identity
Center (the current name for the service formerly called
AWS SSO) provides workforce-identity federation, multi-account
access, and SCIM-based user provisioning. Amazon Cognito
supports application-layer user pools and identity pools.

**CMMC practices implemented.** IA.L1-3.5.1 (user
identification), IA.L1-3.5.2 (user authentication),
IA.L2-3.5.3 (MFA), AC.L2-3.1.1 (account management), and
AC.L2-3.1.5 (least privilege).

**Implementation notes.**

- IAM Users are available but workforce identity should route
  through IAM Identity Center federated to an enterprise
  identity provider (Entra ID Government, Okta Government, or
  equivalent). Long-lived IAM User credentials are a common
  assessment finding.
- IAM Identity Center is available in both AWS GovCloud
  Regions. SCIM 2.0 provisioning from the enterprise IdP keeps
  group memberships and user lifecycle in sync.
- MFA is mandatory for all human users accessing CUI scope.
  Hardware security keys (FIDO2 / WebAuthn) are the
  assessor-preferred factor; virtual MFA apps are acceptable;
  SMS-based MFA is deprecated by NIST SP 800-63B for
  Authenticator Assurance Level 2 and should not be the sole
  factor.
- Amazon Cognito is available in both AWS GovCloud Regions as
  of the verification date. Cognito is for application-layer
  identity (customer identity and access management, B2C user
  pools), not workforce identity. Service availability across
  GovCloud Regions historically follows an asymmetric pattern
  (some services launch in one Region before the other);
  verify current Region availability at
  docs.aws.amazon.com/govcloud-us before relying on Cognito
  for a specific deployment.
- IAM Access Analyzer and IAM Access Advisor surface least-
  privilege gaps and should be run on a cadence; findings feed
  into AC.L2-3.1.5 evidence.

**Evidence to collect.**

- IAM Identity Center configuration export showing the
  federated identity provider and SCIM provisioning
  configuration.
- MFA enforcement policy showing MFA required for all console
  access and privileged API actions.
- Permissions-boundary configuration for developer and
  administrator roles.
- IAM Access Analyzer findings report, dated.

**Common mistakes.**

- Using the root account for day-to-day operations. Root
  access should be locked behind hardware MFA, used only for
  root-required tasks, and its credentials rotated and
  monitored as the highest-sensitivity secret.
- Creating long-lived access keys for developers. Assume-role
  via IAM Identity Center-issued credentials avoids
  long-lived-credential sprawl.
- Federating IAM Identity Center against a commercial-tenancy
  Entra ID or IdP when the CUI workload is in GovCloud. The
  identity plane must live in a government tenancy for CUI
  posture.

---

## Encryption and key management

**Capability.** AWS Key Management Service (KMS) provides
managed customer-master-key (CMK) services in AWS GovCloud,
backed by hardware security modules (HSMs). As of May 2025,
AWS KMS HSMs are validated to FIPS 140-3 Security Level 3
across all commercial and GovCloud Regions (upgraded from
FIPS 140-2 Security Level 3). AWS CloudHSM provides dedicated
single-tenant HSMs for workloads that require customer-
controlled key material, also available in AWS GovCloud. AWS
Certificate Manager (ACM) handles TLS certificate issuance
and renewal for managed services.

**CMMC practices implemented.** SC.L2-3.13.10 (cryptographic
key management), SC.L2-3.13.11 (FIPS-validated cryptography
for CUI), SC.L2-3.13.8 (transmission confidentiality and
integrity), and SC.L2-3.13.16 (data at rest encryption).

**Implementation notes.**

- Default to AWS KMS customer-managed keys (CMKs) for CUI
  workloads rather than AWS-managed keys. CMKs give the
  contractor the audit trail (CloudTrail KMS events), the
  key-rotation policy, and the key-access-policy control that
  assessor evidence typically requires.
- Enable automatic annual key rotation on CMKs unless a
  specific cryptographic reason requires manual rotation.
- For workloads requiring FIPS-validated cryptographic
  endpoints from within a VPC, use VPC endpoints with FIPS
  endpoint URLs (services expose `<service>-fips.<region>.
  amazonaws.com` endpoints).
- CloudHSM is the path for workloads requiring single-tenant
  HSM custody of key material (some DoD-specific overlays,
  customer-controlled key custody requirements). Operational
  overhead is non-trivial; use KMS CMKs unless a specific
  requirement demands CloudHSM.
- Bring Your Own Key (BYOK) imports wrap customer key material
  into KMS; the imported key material inherits the validation
  posture of the KMS HSMs it lands in.

**FIPS 140 status (verified 2026-04-21).** AWS KMS HSMs are
validated to FIPS 140-3 Security Level 3. The specific CMVP
certificate numbers for the AWS KMS HSM modules cycle with
HSM firmware revisions; verify the current active certificate
at csrc.nist.gov/projects/cryptographic-module-validation-program
/validated-modules/search by filtering on AWS. Cite the
active certificate number in the SSP and re-verify on an
annual cadence. Both FIPS 140-2 and FIPS 140-3 validated
certificates are acceptable for CUI; FIPS 140-2 certificates
remain valid through their CMVP-published transition dates.
AWS-LC (the AWS-maintained FIPS-validated cryptographic
library used by AWS SDKs) carries its own CMVP validation;
cite separately when application-layer cryptography is
claimed.

**Evidence to collect.**

- KMS key inventory showing CMKs for CUI workloads with key
  policies, rotation state, and grant inventory.
- Per-service encryption enforcement (S3 bucket policies
  requiring `x-amz-server-side-encryption`, EBS default
  encryption, RDS encryption-at-rest flag, DynamoDB
  encryption-at-rest flag).
- TLS endpoint usage pattern showing `-fips` endpoints where
  applicable.
- SSP section naming the active CMVP certificate(s) for AWS
  KMS HSMs and AWS-LC for the deployed usage, dated.

**Common mistakes.**

- Relying on AWS-managed keys for CUI workloads. The
  audit-trail and access-policy story is weaker; assessor
  evidence is thinner.
- Enabling KMS CMKs but leaving S3 buckets or EBS volumes
  with no encryption enforcement. The CMK exists but is not
  being used by default; unencrypted objects or volumes
  remain in scope.
- Failing to distinguish FIPS endpoints from standard
  endpoints. An application calling
  `kms.<region>.amazonaws.com` (standard) when the SSP claims
  `kms-fips.<region>.amazonaws.com` (FIPS) has a posture
  gap.

---

## Logging, monitoring, and threat detection

**Capability.** AWS CloudTrail records control-plane and
data-plane API activity. AWS Config records resource
configuration history and evaluates compliance rules. Amazon
CloudWatch aggregates metrics, logs, and alarms. AWS Security
Hub aggregates findings from Config, GuardDuty, Inspector, and
third-party integrations. Amazon GuardDuty provides threat
detection against VPC flow logs, DNS logs, CloudTrail, and
S3 access patterns. Amazon Inspector performs automated
vulnerability assessments on EC2 instances, container images,
and Lambda functions.

**CMMC practices implemented.** AU.L2-3.3.1 (audit event
creation), AU.L2-3.3.2 (user accountability), AU.L2-3.3.3
(event review), AU.L2-3.3.5 (audit correlation), AU.L2-3.3.8
(audit protection), SI.L2-3.14.3 (security alerts), SI.L2-3.14.6
(system monitoring), SI.L2-3.14.7 (unauthorized use detection),
CA.L2-3.12.1 (security control assessment), and CA.L2-3.12.3
(continuous monitoring).

**Implementation notes.**

- Enable CloudTrail in every account with a trail logging to
  a dedicated log-archive account owned by the Organization.
  Cross-account delivery with object-lock prevents a
  compromised account from tampering with its own audit
  trail.
- Data events (S3 object-level, Lambda invocation-level) add
  meaningful audit value for CUI-bearing buckets and
  functions; enable selectively rather than universally to
  manage cost.
- AWS Config should be enabled in every account with a
  recording configuration that captures resource
  configuration changes and evaluates the FedRAMP/NIST
  managed-rule packs.
- Security Hub aggregates findings; enable it as the
  primary findings aggregation plane and forward findings to
  the SIEM. Security Hub controls map to FedRAMP, NIST
  800-53, CIS AWS Foundations, and PCI, which is useful for
  cross-framework evidence.
- GuardDuty should be enabled in every account and every
  Region in scope, with delegated administration through
  Organizations so findings aggregate into the Security
  account.
- Inspector should scan EC2 and ECR (container image)
  inventory on a continuous cadence; findings feed
  SI.L1-3.14.1 flaw remediation evidence.
- Log forwarding to the SIEM terminates the AWS-native
  logging plane in the contractor's broader audit
  environment; see
  `references/modern-it/endpoints/macos-fleet.md` or
  `windows-fleet.md` "Centralized logging to SIEM" for the
  endpoint-side counterpart.

**Evidence to collect.**

- Organization-wide CloudTrail configuration showing
  cross-account delivery, object-lock on the archive bucket,
  and retention settings.
- Config recorder and rule-pack configuration per account;
  Config aggregator in the Security account showing
  org-wide compliance view.
- Security Hub configuration showing enabled standards and
  the finding-aggregation pattern.
- GuardDuty detector inventory across accounts and Regions,
  with delegated admin configuration.
- Sample end-to-end trace of a CloudTrail API call through
  to a SIEM dashboard entry, dated at assessment time.

**Common mistakes.**

- Enabling CloudTrail only in the management account. Member
  accounts must also have their trails configured; the
  Organization-level trail covers management-plane events
  but individual account activity requires per-account
  configuration or an Organization trail that includes all
  accounts.
- Leaving the log-archive account under the same
  administrator access as production workload accounts. An
  attacker with workload-account administrator access can
  tamper with logs unless the archive account is isolated.
- Forwarding only GuardDuty findings to the SIEM, leaving
  CloudTrail raw events in CloudWatch Logs. The correlation
  depth is thinner; audit reconstruction after an incident
  is harder.

---

## Boundary protection and network

**Capability.** Amazon Virtual Private Cloud (VPC) provides
the network isolation substrate. Security Groups (stateful)
and Network ACLs (stateless) enforce per-subnet and
per-instance traffic policies. AWS Transit Gateway
interconnects VPCs and on-premises networks through a
managed hub. AWS Direct Connect provides private connectivity
from contractor premises to the GovCloud Region. AWS
PrivateLink exposes AWS services and third-party services as
interface endpoints reachable only from inside the VPC. AWS
Network Firewall and AWS WAF provide stateful inspection and
web-application-layer filtering.

**CMMC practices implemented.** SC.L1-3.13.1 (boundary
protection), SC.L1-3.13.5 (public access system separation),
SC.L2-3.13.6 (deny by default, allow by exception),
SC.L2-3.13.7 (split-tunneling prevention where AWS-side
endpoints are involved), and SC.L2-3.13.2 (architectural
design for security).

**Implementation notes.**

- Separate VPCs for CUI and non-CUI workloads is the
  assessor-expected posture. Shared VPC across scope
  boundaries creates unnecessary scope creep.
- VPC Flow Logs must be enabled on every VPC in scope,
  logging to CloudWatch Logs or S3 for SIEM ingestion.
  GuardDuty also consumes flow logs directly.
- Security Groups operate as the primary per-instance
  boundary. Principle of least privilege applies at the
  Security Group level; ingress rules should be
  source-specific, not `0.0.0.0/0` except at the public-
  facing edge with justification.
- VPC endpoints (Interface and Gateway) keep traffic to AWS
  services off the public internet. Every AWS service call
  from within a CUI VPC should route through a VPC endpoint
  unless there is a documented exception.
- FIPS-mode VPC endpoints use the `-fips` variant of the
  service endpoint DNS; configure endpoint policies to
  allow only FIPS endpoints for SC.L2-3.13.11 compliance.
- Direct Connect provides non-internet connectivity from
  contractor facilities to GovCloud. Direct Connect
  Gateway allows a single Direct Connect connection to
  reach multiple VPCs across Regions.
- AWS Network Firewall sits in-line in the VPC for
  stateful filtering at scale; use in combination with
  Security Groups for a defense-in-depth posture.

**Evidence to collect.**

- VPC inventory with subnet-to-scope mapping showing which
  subnets host CUI workloads.
- Security Group ruleset export for CUI subnets with
  justification for each ingress rule.
- VPC Flow Logs configuration and forwarding destination.
- VPC endpoint inventory showing FIPS-endpoint usage.
- Direct Connect / VPN configuration documentation if
  on-premises connectivity is in scope.

**Common mistakes.**

- Using default VPCs for CUI workloads. Default VPCs have
  permissive Security Groups and should be deleted in
  GovCloud accounts before provisioning CUI resources.
- Overly-permissive Security Groups with `0.0.0.0/0`
  ingress on non-public services. Common finding during
  assessment; automated scanning via Security Hub catches
  most cases.
- Disabling VPC Flow Logs to reduce cost during development,
  then forgetting to re-enable in production.

---

## Compute and storage service parity

**Capability.** AWS GovCloud supports a large but not complete
subset of commercial AWS services. Service parity gaps are
the primary operational consideration when porting a design
from commercial AWS to GovCloud.

**CMMC practices implemented.** No CMMC practice maps
directly to service parity; this section is a scope-planning
concern. The CMMC-relevant practices apply to whichever
services the contractor actually uses within GovCloud.

**Implementation notes.**

- The authoritative list of AWS services in scope for
  GovCloud FedRAMP High and DoD CC SRG IL2/IL4/IL5 is
  aws.amazon.com/compliance/services-in-scope. Verify
  service availability and authorization level at that page
  before designing a workload.
- The `docs.aws.amazon.com/govcloud-us/latest/UserGuide`
  documents GovCloud service differences against commercial
  AWS: available services, feature gaps, regional
  limitations.
- New AWS services arrive in GovCloud on a delay relative to
  commercial AWS. A design that depends on a just-released
  commercial service should verify GovCloud availability
  before committing.
- FedRAMP authorization for a service in GovCloud is
  service-level, not feature-level. An authorized service
  may have specific features or configurations that are not
  in the authorization boundary; the AWS Services in Scope
  page specifies the authorized scope per service.
- Regional parity between GovCloud US-East and GovCloud
  US-West is not universal; some services are available in
  only one Region or launch in one Region before the other.
  The authoritative per-service Region availability matrix is
  at docs.aws.amazon.com/govcloud-us. Design reviews should
  verify Region availability before committing architecture
  to a specific Region.

**Evidence to collect.**

- SSP section naming the specific AWS GovCloud services used
  by each CUI workload with the FedRAMP authorization level
  for each, dated.
- Verification record showing the Services in Scope page was
  consulted at SSP authoring time.

**Common mistakes.**

- Assuming commercial-AWS service availability in GovCloud.
  Design reviews should verify every proposed service
  against the Services in Scope page.
- Using a service that is in GovCloud but outside the FedRAMP
  High authorization boundary for the specific feature set
  being used. The service being "in GovCloud" is not the
  same as the specific feature being authorized.

---

## Support and operator-access posture

**Capability.** AWS GovCloud Support operates with US-person
support personnel for case handling. GovCloud Support is a
separate entitlement from commercial AWS Support. The AWS
GovCloud Root Account owner certifies US-person status at
provisioning; AWS operator personnel with production access
to GovCloud Region infrastructure are US-persons.

**CMMC practices implemented.** PS.L2-3.9.1 (personnel
screening) and PS.L2-3.9.2 (personnel transfer) are
inherited from AWS for the AWS-operator side; the
contractor still owns these practices for contractor
personnel. SR (Supply Chain) controls inherit from AWS under
the FedRAMP authorization.

**Implementation notes.**

- AWS Support plans (Developer, Business, Enterprise On-Ramp,
  Enterprise) apply separately in GovCloud. CUI workloads
  typically require Business-tier or higher for incident
  response SLAs.
- Support cases must not include CUI data in case
  descriptions or attachments. GovCloud Support handles
  FedRAMP-scope cases, but the case-management workflow
  itself operates under a separate posture; the contractor
  is responsible for scrubbing CUI before submission.
- The AWS US-person operator-access posture is distinct from
  the contractor's own personnel posture. A non-US-person
  contractor employee cannot serve as an AWS operator
  escalation contact, and may or may not be permitted to
  administer the contractor's own GovCloud resources
  depending on the contract's export-control terms. If
  ITAR-controlled or EAR-controlled technical data is present
  in the workload, US-person-only staffing may apply to the
  contractor side as well; consult export-control counsel
  before finalizing personnel policy. The contractor's
  personnel posture is an export-control and contract
  question, not an AWS question. See
  `references/modern-it/endpoints/remote-work.md`
  "Travel posture and OCONUS constraints" for the
  contractor-side personnel-access considerations and ITAR
  framing.

**Evidence to collect.**

- Support plan level documentation per GovCloud account.
- Support case hygiene policy naming the CUI-scrubbing
  requirement before submission.
- AWS Artifact download of AWS's FedRAMP System Security
  Plan relevant sections for inheritance of personnel
  screening.

**Common mistakes.**

- Attaching CUI logs or diagnostic data directly to Support
  cases. A sanitization step is required before any attach
  or copy-paste of production data into a case.
- Assuming commercial AWS Support case handling applies in
  GovCloud. Different posture, different case-management
  URLs, and different escalation contacts.

---

## FedRAMP and Impact Level posture

**FedRAMP status (verified 2026-04-21).**

- AWS GovCloud (US) holds a JAB Provisional Authority to
  Operate (P-ATO) at the FedRAMP High baseline.
- FedRAMP marketplace identifier: F1603047866.
- The JAB P-ATO pathway is now defunct; the AWS GovCloud
  P-ATO remains in force but will not be re-issued as an
  Agency ATO. Agencies issue their own ATOs against the AWS
  authorization package.
- Per-service authorization detail (which services are in
  scope at FedRAMP High for AWS GovCloud) is at
  aws.amazon.com/compliance/services-in-scope. Verify the
  specific services used in a workload against that page at
  SSP authoring time.

**DoD Impact Level posture (verified 2026-04-21).** AWS
GovCloud (US) holds DISA Provisional Authorizations at IL2,
IL4, and IL5 under the DoD CSP SRG v1r1 reciprocity rules.
Per the hub crosswalk at
`references/modern-it/cloud-platforms/cloud-selection.md`,
IL5 now requires the FedRAMP High baseline (a change from
the retired CC SRG v1r4); AWS GovCloud's FedRAMP High P-ATO
is the baseline on which the IL5 authorization sits. IL6
workloads (classified up to SECRET) require a separate
classified-network partition (AWS Secret Region); IL6 is
out of scope for AWS GovCloud.

**Scope boundary for IL content in this file.** This section
names AWS GovCloud's authorization levels and points at the
hub crosswalk. It does not implement IL4 or IL5 end-to-end.
Full IL4/IL5 implementation detail (CNSSI 1253 overlays, NSS
controls if applicable, dedicated-infrastructure
requirements, workload-category criteria) is deferred to a
future DoD-specific reference per the forward-reference in
`references/fedramp-gap.md` "Relationship to DoD Cloud
Computing Security Requirements Guide." A contractor building
an IL5 SSP should treat this file as the AWS-side capability
map, not as the full IL5 control implementation.

**Service-level authorization.** A service being available
in AWS GovCloud is not the same as that service being in
the FedRAMP / IL authorization boundary. The
services-in-scope page is the authoritative per-service
record; verify there before claiming specific service
inheritance in an SSP.

---

## Capability appendix — CMMC capability to AWS GovCloud native service

The appendix below is the single-provider vertical slice of
the three-column crosswalk in
`references/modern-it/cloud-platforms/cloud-selection.md`.
Rows match the hub table order; only AWS GovCloud services
are named.

| CMMC capability cluster | AWS GovCloud service |
|---|---|
| Identity and authentication (IA family) | IAM, IAM Identity Center, Amazon Cognito (both GovCloud Regions) |
| Cryptographic key management (SC.L2-3.13.10) | AWS KMS GovCloud, AWS CloudHSM |
| Data at rest encryption (SC.L2-3.13.11, SC.L2-3.13.16) | S3 SSE, EBS encryption, RDS encryption using KMS CMKs |
| Data in transit (SC.L2-3.13.8) | VPC endpoints with FIPS endpoint URLs, TLS via ACM, PrivateLink |
| Network boundary protection (SC.L1-3.13.1, SC.L2-3.13.6) | VPC, Security Groups, Network ACLs, Network Firewall, WAF, Shield |
| Audit and logging (AU family) | CloudTrail, Config, CloudWatch, Security Hub |
| Continuous monitoring and threat detection (SI.L2-3.14.6, SI.L2-3.14.7) | GuardDuty, Inspector, Security Hub |
| Configuration management (CM family) | Config, Systems Manager, Organizations SCPs, Control Tower guardrails |

---

## Cross-domain anchors

AWS GovCloud posture composes with the corpus cross-cutting
files and domain practice files:

- **Phase 5c hub.** `references/modern-it/cloud-platforms/cloud-selection.md`
  for the four conventions, FedRAMP-to-IL crosswalk, hybrid
  patterns, and tenancy-selection decision tree.
- **FedRAMP inheritance.** `references/fedramp-gap.md`
  "Inherited vs shared-responsibility controls" for the
  inheritance taxonomy that applies to AWS GovCloud.
- **CUI scoping.** `references/scoping-and-cui.md` for the
  decision of what sits in CUI scope within a GovCloud
  tenancy.
- **SSP authoring.** `references/ssp-guidance.md` for how to
  document GovCloud-based inheritance in the SSP.
- **Endpoint management.** When CUI flows between AWS
  GovCloud and endpoint fleets (laptops, mobile), see
  `references/modern-it/endpoints/README.md`.

Domain practice files used for requirement text and
evidence lists:

- Configuration Management (CM): `references/domains/cm-configuration-mgmt.md`
- System and Information Integrity (SI): `references/domains/si-system-information-integrity.md`
- System and Communications Protection (SC): `references/domains/sc-system-comms.md`
- Identification and Authentication (IA): `references/domains/ia-identification-auth.md`
- Access Control (AC): `references/domains/ac-access-control.md`
- Audit and Accountability (AU): `references/domains/au-audit.md`

---

## Examples as of 2026-04

> **Examples as of 2026-04:** The AWS GovCloud services named
> in the structural sections and the capability appendix are
> AWS-native and are not in scope for the ranked-examples
> convention in the same way third-party products are. Where
> a customer considers third-party alternatives for a
> specific capability (third-party EDR, third-party SIEM
> instead of Security Hub, third-party identity provider
> instead of IAM Identity Center), those vendors should
> appear in the sidebar for the relevant capability with the
> dated Examples format from the hub's "Capability-versus-
> product convention." This skill does not rank vendors.
> Verify current FedRAMP Marketplace status on
> marketplace.fedramp.gov before selecting any third-party
> service that operates alongside AWS GovCloud.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/cloud-platforms/cloud-selection.md` or
`references/modern-it/endpoints/README.md` are not repeated.

**ACM (AWS Certificate Manager).** The AWS service that
provisions, manages, and deploys TLS certificates for use
with AWS services.

**ADE (Automated Device Enrollment).** Defined in
`references/modern-it/endpoints/macos-fleet.md`; referenced
here only in cross-domain context.

**BYOK (Bring Your Own Key).** An AWS KMS feature that
imports customer-provided key material into a KMS CMK.

**CMK (Customer-Master Key).** The managed cryptographic key
container in AWS KMS. Customer-managed CMKs are the
assessor-preferred pattern for CUI workloads; AWS-managed
keys are convenient but offer less control.

**HSM (Hardware Security Module).** Tamper-resistant
cryptographic hardware. AWS KMS HSMs are multi-tenant
(shared); AWS CloudHSM provides single-tenant dedicated
HSMs.

**IAM (Identity and Access Management).** The AWS core
identity service.

**LZA (Landing Zone Accelerator on AWS).** An AWS-published
open-source reference implementation for multi-account
compliance-oriented landing zones.

**OU (Organizational Unit).** A grouping of AWS accounts
within AWS Organizations used for hierarchical policy
application.

**P-ATO (Provisional Authority to Operate).** A FedRAMP
authorization historically issued by the Joint Authorization
Board. The JAB P-ATO pathway is now defunct for new
authorizations; existing P-ATOs remain in force.

**RCP (Resource Control Policy).** An AWS Organizations
policy type (companion to Service Control Policies) that
restricts resource-level permissions across member
accounts.

**SCP (Service Control Policy).** An AWS Organizations
policy that restricts the permissions available in member
accounts, independent of IAM policies in those accounts.

**SCIM (System for Cross-domain Identity Management).** The
open standard protocol used by IAM Identity Center for
provisioning user and group lifecycle events from an
enterprise identity provider.

**VPC (Virtual Private Cloud).** The AWS network isolation
primitive; a logically isolated private network within a
Region.
