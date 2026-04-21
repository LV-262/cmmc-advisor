# Cloud Platform Selection for CUI

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); FedRAMP program documentation (fedramp.gov); NIST SP 800-53
> Rev 5 baselines; DFARS 252.204-7012; DoD CSP Security Requirements
> Guide (DoD CSP SRG v1r1) and DoD Mission Owner Security Requirements
> Guide (DoD MO SRG), both available at
> public.cyber.mil/dccs/dccs-documents/ (readers must verify the
> current revisions directly; see "CC SRG revision handling" below);
> CNSSI 1253 (the Committee on National Security Systems categorization
> and control selection overlay); provider compliance documentation
> (aws.amazon.com/compliance, learn.microsoft.com/azure-government/
> compliance, cloud.google.com/security/compliance).

## Overview

This file is the hub for `references/modern-it/cloud-platforms/`.
A contractor selecting a cloud platform for CUI work faces four
decisions that do not collapse into a single "which provider is
best" question:

1. Which DoD Impact Level (IL) does the workload fall under, and
   what FedRAMP baseline does that IL demand.
2. Which provider tenancy (commercial, government community,
   sovereign government) the workload must land in, and how
   tenancy selection differs across AWS, Azure, and Google Cloud.
3. Whether the architecture is single-provider or hybrid
   (non-CUI in commercial, CUI in a government tenancy).
4. How CMMC practice coverage maps to each provider's native
   services, so a reader committed to one provider can build a
   full control implementation without leaving that provider's
   file.

This hub handles the first three decisions directly and frames
the fourth with a capability-orthogonal three-column crosswalk
that the per-provider files (`aws-govcloud.md`,
`azure-government.md`, `gcp-assured.md`) slice vertically inside
their own capability appendices. The regulatory anchor for every
decision in this file is DFARS 252.204-7012(b)(2)(ii)(D) and the
FedRAMP Moderate equivalence requirement; see
`references/fedramp-gap.md` "The CUI Baseline Decision" for the
clause text and the full equivalence mechanics.

**Pending per-provider files.** The three per-provider slices
(`aws-govcloud.md`, `azure-government.md`, `gcp-assured.md`)
are authored incrementally under Phase 5c. Until those files
land, a reader asking a provider-specific question (for
example, "does GCC Moderate or GCC High apply to my Azure CUI
workload?") should anchor to this hub's FedRAMP-to-IL crosswalk
and the four conventions, then consult the provider's own
compliance documentation directly. Slice N will replace this
banner once the per-provider files are complete.

**fedramp-gap.md version-reconciliation note.** This file
reflects CSP SRG v1r1 framing (verified 2026-04-21). The
`references/fedramp-gap.md` "Relationship to DoD Cloud
Computing Security Requirements Guide" section (lines 169-183
in the current fedramp-gap.md) still carries the retired
v1r4 framing. A separate residue issue (dev-4yor) tracks that
refresh. If reading both files side-by-side, use this hub's
FedRAMP-to-IL crosswalk as the current-truth source; the
fedramp-gap.md IL mappings will be refreshed to align with
this hub.

---

## The four conventions this directory follows

These four Decisions govern every file in
`references/modern-it/cloud-platforms/`. Downstream per-provider
slices adhere to them; future contributors do the same. The
rationale for each is stated because these conventions will be
second-guessed under vendor pressure or reader ergonomics
pressure, and the reasoning needs to survive those arguments.

### Decision 1: Provider-primary structure with per-file capability appendix

**Per-provider files are organized by that provider's tenancy
and service model.** AWS GovCloud by account and Organizations
posture; Azure Government by tenant, subscription, and
management-group posture; Google Cloud Assured Workloads by
organization, folder, and project posture. Within each
provider's structural model, capability sections (identity,
encryption, logging, boundary) map to CMMC practices and state
evidence and common mistakes.

**Each per-provider file also carries a capability appendix.**
The appendix is a single-column table: "CMMC capability → this
provider's native service." A reader already committed to one
provider answers "what in this provider covers SC.L2-3.13.11?"
without leaving the file. The hub (this file) carries the
three-column version of the same mapping for multi-provider
readers.

**Rationale.** Endpoints (Phase 5b) are capability-primary
because endpoint products churn fast while capabilities stay
stable. Cloud platforms invert that: provider architectural
models are load-bearing and stable; forcing capability-primary
across three providers flattens three distinct tenancy models
into fake symmetry. The clearest example is Google Cloud's
Assured Workloads, which is a control-plane overlay on
commercial Google Cloud rather than a separate cloud. A
capability-primary layout would hide that structural fact. A
provider-primary layout surfaces it and tells the reader which
Assured Workloads posture applies to their workload.

The per-file capability appendix exists because a single-
provider reader (a contractor committed to AWS only, for
example) shouldn't have to open the hub to answer
"what AWS services cover this CMMC practice." The appendix is
a strict vertical slice of the hub crosswalk, authored once in
each provider file at minimal additional cost.

**Canonical appendix format for per-provider files.** The
appendix in `aws-govcloud.md`, `azure-government.md`, and
`gcp-assured.md` uses a two-column table: "CMMC capability
cluster | Native service." Example shape:

| CMMC capability cluster | AWS GovCloud service |
|---|---|
| Identity and authentication (IA family) | IAM, IAM Identity Center |
| Cryptographic key management (SC.L2-3.13.10) | KMS GovCloud, CloudHSM |

The left column matches the hub's left column one-for-one; the
right column is the vertical slice of the hub's three-column
crosswalk for that provider. Rows stay in the same order as
the hub. Per-provider detail (which specific services, which
evidence, which common mistakes) lives in the structural
tenancy-model sections above the appendix; the appendix itself
is a quick-reference index, not a place for implementation
depth.

### Decision 2: FedRAMP as primary axis; DoD Impact Level as overlay

**Every compliance claim in this directory uses FedRAMP
authorization as the primary axis and DoD Impact Level as a
declared overlay.** This hub carries the FedRAMP-to-IL
crosswalk once; per-provider files cite the crosswalk and state
which IL overlays their provider's government tenancy supports,
rather than re-deriving the mapping.

**Rationale.** FedRAMP is the authorization program most CMMC
Level 2 contractors encounter directly under DFARS
252.204-7012. CC SRG Impact Levels are a DoD-specific overlay
that extends FedRAMP with workload-category and
infrastructure-dedication requirements. Framing FedRAMP first
keeps the hub legible to the majority audience (CMMC L2
contractors handling CUI under 7012) and defers IL detail to
the contractors who actually need IL4 or IL5 posture. Full IL4
and IL5 content remains deferred to a future DoD-specific
reference, consistent with `references/fedramp-gap.md` "Relationship
to DoD Cloud Computing Security Requirements Guide."

### Decision 3: Tenancy selection as a dedicated symmetric section in each provider file

**Each per-provider file carries a "Tenancy selection" section
that answers three questions in the same order.**

1. Is the provider's commercial tenancy ever acceptable for CUI?
2. Which government tenancy or control-plane isolation posture
   is the contractor path? (For AWS and Azure, this is a
   separate cloud or region. For Google Cloud, it is an
   Assured Workloads configuration on commercial GCP.)
3. What workload-location and support-personnel-citizenship
   boundaries apply inside that tenancy or configuration?

**Rationale.** The three providers diverge sharply on tenancy
architecture, and that divergence is load-bearing. AWS
GovCloud is a physically separate set of AWS Regions with
US-person-only operator access. Azure Government is a
physically separate cloud environment with US-person operator
controls. Google Cloud Assured Workloads is an overlay on
commercial Google Cloud that enforces workload-location and
personnel-access controls through the control plane rather
than by running on separate infrastructure. Symmetric section
structure across the three provider files makes the asymmetric
answers directly comparable.

### Decision 4: Hybrid patterns in this hub, not in per-provider files

**Common hybrid architectures (non-CUI in commercial, CUI in
government; productivity in Microsoft 365 GCC High, compute in
AWS GovCloud; and similar patterns) live in this hub file.**
Per-provider files note that hybrid exists and forward-
reference here. Three separate hybrid treatments across three
provider files would diverge within 12 months of authoring;
centralization prevents that.

**Rationale.** Hybrid is a multi-provider decision by
definition. A single treatment in the hub gives the reader a
consolidated view and gives maintainers a single place to
update when hybrid patterns shift.

---

## CC SRG revision handling

The DoD cloud computing security requirements guidance moved
through a significant restructuring in 2024. **The monolithic
Cloud Computing Security Requirements Guide (CC SRG) v1r4 has
been officially retired** and replaced by two separate
documents:

- **DoD CSP SRG v1r1.** Security requirements Cloud Service
  Providers must meet to deliver cloud service offerings to
  DoD Mission Owners.
- **DoD Mission Owner (MO) SRG.** Technical requirements that
  apply to the Mission Owner (the DoD organization or
  contractor using the CSP's cloud service).

Both documents are published at public.cyber.mil/dccs/dccs-documents/.
Contractors operating a CSP-hosted workload under DFARS
252.204-7012 must review both: the CSP SRG constrains the
provider's offering, and the MO SRG constrains the contractor's
use of that offering.

**Readers must verify the current revision of both documents
directly on public.cyber.mil before citing either in their SSP.**
This hub file, and the per-provider files that cite it, do not
embed a specific CSP SRG or MO SRG revision number in
structural claims. Dated verification stamps accompany any IL
mapping or operator-access requirement.

**This slice verified the DoD CSP SRG and DoD MO SRG framing on
2026-04-21** via a combination of public.cyber.mil directory
review and a reputable 3PAO practitioner-grade summary of the
v1r1 transition. The IL-to-FedRAMP mappings below reflect the
new CSP SRG v1r1 reciprocity rules. Contractors with an
Authorization to Operate (ATO) package predating the v1r4
retirement should coordinate their transition timeline with
their DoD Sponsor/Authorizing Official; the DoD timeline named
end of calendar year 2025 as the deadline for existing IL5/IL6
packages to transition to Rev 5 under the new SRG.

**Downstream note.** The Phase 5a
`references/fedramp-gap.md` "Relationship to DoD Cloud Computing
Security Requirements Guide" section was authored against the
v1r4 framing. Its IL mappings require a follow-up refresh to
align with the CSP SRG v1r1 reciprocity; tracked as a separate
Phase 5a residue issue.

---

## FedRAMP baseline to DoD Impact Level crosswalk

The table below maps FedRAMP impact-level baselines to the
corresponding DoD Impact Levels under the CSP SRG v1r1
reciprocity rules. Readers must verify against the current
revisions at public.cyber.mil.

| Impact Level | Information category | FedRAMP baseline under CSP SRG v1r1 | Additional overlay requirements |
|---|---|---|---|
| IL2 | Non-Controlled Unclassified Information (public-releasable federal data) | FedRAMP Moderate | None beyond FedRAMP Moderate |
| IL4 | Controlled Unclassified Information (CUI) and non-critical mission data | Two authorized paths: (a) FedRAMP Moderate + DoD FedRAMP+ security controls + CNSSI 1253 Moderate Confidentiality and Integrity overlays; or (b) FedRAMP High baseline with General Readiness Requirements and security clearance policy review | US-person operator access; DoD-specific connection restrictions; CSP SRG v1r1 Appendix D additional control parameters |
| IL5 | CUI with higher sensitivity, mission-critical information, and National Security Systems data (non-classified) | FedRAMP High (required under CSP SRG v1r1) | CNSSI 1253 High Confidentiality and Integrity overlays; NSS controls if the offering is designated as an NSS; US-person operator access |
| IL6 | Classified information up to SECRET | FedRAMP High (required) | CNSSI 1253 High Confidentiality and Integrity overlays; classified-network / SIPRNet resident; DoD retains right to perform independent penetration testing |

**Key change from the retired CC SRG v1r4.** Under v1r4, IL5
was specified as FedRAMP Moderate plus a Level 5 overlay
including dedicated-infrastructure separation. The new CSP SRG
v1r1 formalizes what most commercial providers had already
implemented in practice: **IL5 now requires the FedRAMP High
baseline**, with CNSSI 1253 overlays on top. IL4 gained an
explicit second authorized path that permits a CSP already
holding FedRAMP High authorization to skip the Moderate +
FedRAMP+ overlay path.

**Transition path for contractors with existing ATOs.** A
contractor holding a FedRAMP Moderate ATO cannot simply re-use
it for IL5 workloads under CSP SRG v1r1; a new FedRAMP High
authorization package is required. Contractors holding
IL5 or IL6 packages that predate the CSP SRG v1r1 transition
were expected to complete their Rev 5 updates by end of
calendar year 2025; as of this slice's verification date
(2026-04-21) that deadline has passed. Packages in a
post-deadline state are handled case-by-case by the DoD
Sponsor and the Authorizing Official. This skill does not
advise on ATO remediation; coordinate directly with the
Authorizing Official for a package predating the transition.

**For most CMMC Level 2 contractors, IL2 or IL4 is the
operative level.** DFARS 252.204-7012 CUI triggers IL4
posture. IL5 applies to specific defense-workload categories
(mission-critical CUI, National Security Systems). IL6 is out
of scope for CMMC L2 contractor stacks; it sits on classified
networks.

Full IL4 and IL5 implementation detail is deferred to a future
DoD-specific reference, per the forward-reference declared in
`references/fedramp-gap.md` "Relationship to DoD Cloud
Computing Security Requirements Guide."

---

## Capability-orthogonal three-column crosswalk

The table below maps CMMC capability clusters to each
provider's native service. It is a hub-level map; each
per-provider file carries a single-column vertical slice
(Decision 1) with implementation detail, evidence, and common
mistakes.

| CMMC capability cluster | AWS GovCloud | Azure Government | GCP Assured Workloads |
|---|---|---|---|
| Identity and authentication (IA family) | IAM, IAM Identity Center, Cognito GovCloud | Entra ID Government, conditional access, PIM | Cloud Identity, Workload Identity Federation |
| Cryptographic key management (SC.L2-3.13.10) | KMS GovCloud, CloudHSM | Key Vault Premium, Managed HSM | Cloud KMS, Cloud HSM, External Key Manager |
| Data at rest encryption (SC.L2-3.13.11, SC.L2-3.13.16) | S3 SSE, EBS encryption, RDS encryption using KMS | Azure Storage Service Encryption, Disk Encryption, SQL TDE | Cloud Storage CMEK, Persistent Disk encryption, Cloud SQL CMEK |
| Data in transit (SC.L2-3.13.8) | VPC endpoints, TLS via ACM, PrivateLink | Private Link, ExpressRoute, TLS via Key Vault certificates | Private Google Access, VPC Service Controls, Cloud HTTPS Load Balancing |
| Network boundary protection (SC.L1-3.13.1, SC.L2-3.13.6) | VPC, Security Groups, Network ACLs, WAF, Shield | VNet, NSGs, Azure Firewall Premium, WAF | VPC, firewall rules, Cloud Armor, VPC Service Controls |
| Audit and logging (AU family) | CloudTrail, Config, CloudWatch, Security Hub | Activity Log, Azure Monitor, Log Analytics, Sentinel | Cloud Audit Logs, Cloud Logging, Security Command Center Premium |
| Continuous monitoring and threat detection (SI.L2-3.14.6, SI.L2-3.14.7) | GuardDuty, Inspector, Security Hub | Defender for Cloud, Sentinel | Security Command Center Premium, Chronicle |
| Configuration management (CM family) | Config, Systems Manager, Organizations SCPs | Azure Policy, Defender for Cloud benchmarks, Management Groups | Organization Policy, Security Command Center posture, Folder-level policies |

**Reading the crosswalk.** A row is a capability cluster, not
a single CMMC practice. Per-provider files in this directory
decompose each cluster into the specific practice-to-service
mapping with the assessor-facing evidence list.

**What the crosswalk does not do.** It does not claim
functional equivalence across services in a row. AWS Security
Hub and Azure Sentinel and Google Security Command Center
Premium each implement continuous monitoring differently;
migration between providers is not a drop-in exercise. The
crosswalk establishes that the capability is available in each
provider, not that the implementations are interchangeable.

**Known divergences worth flagging at hub level.** The
per-provider files treat implementation differences in depth;
three divergences are large enough that a single-provider
reader should not assume cross-provider parity from this
table alone:

- Key management: AWS KMS and Azure Key Vault both support
  customer-managed keys, but AWS supports external key material
  and custom key stores backed by CloudHSM differently than
  Azure Managed HSM or Google Cloud External Key Manager. Key
  sovereignty and rotation-policy posture differ meaningfully.
- Boundary enforcement: GCP VPC Service Controls operate as a
  control-plane perimeter around services, not as a
  network-subnet boundary in the AWS VPC or Azure VNet sense.
  An architecture depending on subnet-level boundary semantics
  is not directly portable.
- Audit logging retention: provider-default retention windows
  and long-term archival mechanisms (CloudTrail Lake, Log
  Analytics Workspaces, Cloud Logging buckets) have different
  defaults and different cost curves; operational cost
  differences can be substantial.

**Service names drift.** The service names in this table
reflect provider branding verified on 2026-04-21. Vendors
rename services on a multi-year cadence (AWS SSO became IAM
Identity Center; Azure AD became Entra ID). Verify current
service names on the provider's documentation site when
citing specific services in an SSP or implementation
artifact.

---

## Hybrid patterns

A contractor with CUI work does not always run pure-GovCloud or
pure-government-tenancy. Several hybrid architectures are
common, survive CMMC assessment, and are operationally
reasonable. This section names the recurring ones. Per-provider
files forward-reference this section rather than duplicate it.

### Pattern A: Commercial productivity, GovCloud compute

Non-CUI email, calendaring, and commercial SaaS on a
commercial-tenancy productivity suite; CUI processing and
storage on a government-tenancy compute platform. Example
composition: Microsoft 365 Commercial for non-CUI email,
AWS GovCloud for CUI analytics and storage. The boundary
between the two is a gate (SC.L1-3.13.1 boundary protection):
CUI never transits the commercial productivity plane.

**When this works.** The contractor's CUI workflow is
well-contained (a specific engineering workload, a specific
set of documents) and the commercial plane never receives CUI
by policy or by technical control.

**When this fails.** The workflow includes emailing CUI as
attachments, collaborating on CUI documents through commercial
SharePoint or Google Drive, or routing CUI through a
commercial-tenancy messaging application. Any of those
scenarios pulls the commercial plane into CUI scope and the
hybrid boundary collapses.

### Pattern B: Microsoft 365 GCC High for productivity, separate GovCloud for compute

CUI-capable productivity (M365 GCC High for email, SharePoint,
Teams) plus a separate government-tenancy compute platform
(AWS GovCloud, Azure Government, or Assured Workloads) for
specialized workloads. Both planes are CUI-capable; the
separation is about workload fit rather than CUI boundary.
Integration happens through documented connections and
FedRAMP-authorized service connections.

**When this works.** The productivity posture is stable in
one provider (typically Microsoft, for Office and Teams
workflow continuity with commercial counterparts) while
compute or specialized analytics ride a different provider
that fits a specific workload (GPU availability, data-gravity
considerations, existing infrastructure investment).

**When this fails.** Identity federation between the two
planes is built on a commercial directory by mistake, pulling
a non-government tenancy into the CUI scope. Identity must be
handled inside the government tenancy on both sides.

### Pattern C: Multi-government-cloud with workload separation

CUI workloads distributed across two or more government
tenancies, each running a specific workload. Example: M365
GCC High for productivity, Azure Government for platform
services, AWS GovCloud for specialized compute. All planes
are CUI-capable; the distribution is workload-specific.

**When this works.** The contractor has operational reasons
to run in multiple government clouds (vendor-specific
capabilities, acquisition history, regulatory diversification)
and has the operational staff to manage multiple government
tenancies.

**When this fails.** The contractor is running multiple
government clouds because "it seemed like a good idea" without
a specific workload fit. Each government tenancy carries its
own operational overhead; running two or three without a
specific need is an operational cost the CUI program
eventually cannot carry.

### Pattern D: Sovereign government tenancy with on-premises hybrid

CUI processing primarily in a government-tenancy cloud, with
on-premises systems handling specific workloads that cannot
cloud-migrate (specialized laboratory equipment, air-gapped
development environments, certain engineering simulations).
The on-premises side is fully in CUI scope and must implement
the CMMC practices directly rather than inheriting from a CSP.

**When this works.** Specific workloads genuinely cannot move
to cloud (physical equipment, classification adjacency, export
control constraints).

**When this fails.** "We have too much on-prem" becomes the
default answer and the cloud migration never happens; the
contractor carries the full CMMC burden on the on-prem side
indefinitely. Legitimate hybrid is workload-specific;
convenience-hybrid is technical debt.

---

## Tenancy-selection decision tree

When selecting a cloud platform and tenancy for a CUI workload,
walk the questions in this order. Answering each in writing
and storing the answer in the SSP is the recommended
documentation pattern.

1. **Is CUI present in this workload?** If no, FedRAMP Moderate
   equivalence under DFARS 7012 is not triggered; commercial
   tenancies are available. If yes, continue.
2. **Which CC SRG Impact Level applies?** IL2 (non-CUI federal
   data; no 7012 trigger), IL4 (standard CUI under 7012), IL5
   (mission-critical CUI or NSS data), or IL6 (classified; out
   of scope for CMMC L2). If IL4 or IL5, continue.
3. **Is ITAR or EAR export-controlled data present?** If yes,
   the provider tenancy must be verified-US-person-operator and
   located in US geographic boundaries. This narrows the
   tenancy choice to GovCloud-class environments and rules
   out commercial tenancies regardless of FedRAMP
   authorization.
4. **What existing infrastructure does the contractor have?**
   An existing Microsoft 365 GCC High tenancy, an existing
   AWS Organizations posture, or an existing GCP foundation
   shifts the decision toward building on what exists rather
   than greenfield. Switching providers mid-program is
   operationally expensive.
5. **What workload-specific capabilities matter?** GPU
   availability, specialized compliance certifications (HIPAA
   overlay, CJIS overlay), data-gravity considerations
   (existing datasets already on a provider), or partnership
   preferences (integration with a specific contract partner
   who runs on a specific provider).
6. **Single-provider or hybrid?** Hybrid adds operational
   complexity; single-provider is simpler. Default to
   single-provider unless a specific workload need drives
   hybrid.
7. **Which government tenancy in the chosen provider?** Each
   per-provider file answers this symmetrically (Decision 3).

This is a decision process, not a ranking. No provider is
"better" for CUI workloads in the abstract; each fits
different contractor circumstances. The skill does not
recommend a specific provider.

---

## Cross-domain anchors

Cloud platform selection composes with other cross-cutting
references and the domain practice files:

- **FedRAMP and DFARS 7012 framing.** `references/fedramp-gap.md`
  "The CUI Baseline Decision" for the DFARS clause and
  equivalence. "Inherited vs shared-responsibility controls"
  for the inheritance taxonomy that applies across all three
  providers.
- **CUI scoping.** `references/scoping-and-cui.md` for the
  decision of what sits in CUI scope versus Contractor Risk
  Managed Asset scope versus out of scope.
- **SSP authoring.** `references/ssp-guidance.md` for how to
  document the tenancy selection and the inheritance claims in
  the System Security Plan.
- **Endpoint management planes.** The Intune, Jamf, and similar
  management planes that administer endpoints often run in
  government tenancies themselves. See
  `references/modern-it/endpoints/README.md` for the endpoint
  convention and `references/modern-it/endpoints/windows-fleet.md`
  for the GCC-versus-GCC-High treatment that Azure Government
  picks up.
- **Remote work.** `references/modern-it/endpoints/remote-work.md`
  for VDI and DaaS patterns that run on the government
  tenancies documented in this directory.

---

## Terminology

Acronyms and terms used across this hub and the per-provider
files. Acronyms previously defined in `references/fedramp-gap.md`
or `references/modern-it/endpoints/README.md` are not repeated.

**CSP SRG (DoD Cloud Service Provider Security Requirements
Guide).** The DoD publication that names security requirements
CSPs must meet to deliver offerings to DoD Mission Owners.
Current revision as of this slice's verification: v1r1.
Replaces the retired CC SRG v1r4 (along with the MO SRG).
Published at public.cyber.mil/dccs/dccs-documents.

**MO SRG (DoD Mission Owner Security Requirements Guide).**
The companion DoD publication defining technical requirements
for Mission Owners (the DoD organization or contractor using
the CSP's cloud service). Published alongside the CSP SRG.

**CC SRG v1r4.** The retired monolithic predecessor of the
CSP SRG and MO SRG. Contractor SSPs predating the transition
may still cite v1r4; those authorizations are in transition
per DoD direction.

**Impact Level (IL).** A DoD tier defining information
sensitivity and the corresponding cloud infrastructure and
operator-access requirements. IL2, IL4, IL5, IL6 are the
levels defined under the CSP SRG v1r1 reciprocity rules.

**CNSSI 1253 (Committee on National Security Systems Instruction 1253).**
The categorization and control-selection overlay document
referenced by the CSP SRG Appendix D for the DoD-specific
control additions layered on top of FedRAMP baselines at IL4,
IL5, and IL6. CNSSI 1253 uses a Confidentiality-Integrity-
Availability triplet categorization (for example,
High-High-High); the "Confidentiality and Integrity overlays"
language in the IL crosswalk above refers to the C and I
dimensions of that triplet. Revision 5 of CNSSI 1253 is the
current revision as of 2026-04-21 and is under DoD-wide
adoption; verify at dcsa.mil or the DoD CIO library before
citing in an SSP.

**NSS (National Security Systems).** A category of federal
information systems handling classified information or
information the loss of which would be detrimental to national
security. At IL5, NSS designation adds further control overlays
beyond the baseline IL5 requirements.

**GovCloud.** In this directory, "GovCloud" used alone refers
to the AWS GovCloud (US) Regions. Azure's equivalent is
called "Azure Government." Google's equivalent is called
"Assured Workloads" and is not a separate cloud but an overlay
(see Decision 1 rationale).

**CJIS (Criminal Justice Information Services).** An FBI
compliance overlay that some cloud providers support in their
government tenancies. CJIS is not a CMMC requirement but may
overlap with CMMC posture for specific contracts.

**EAR (Export Administration Regulations).** The Department of
Commerce regulatory regime governing dual-use and certain
defense-adjacent exports. Affects tenancy selection when EAR-
controlled data is present. Separate from CMMC.

**ITAR (International Traffic in Arms Regulations).** The
State Department regulatory regime governing defense articles
and defense services. Defined in
`references/modern-it/endpoints/remote-work.md` "Terminology."
Relevant here because ITAR data triggers US-person operator
access requirements that narrow the tenancy choice.

**US-person.** A citizen or lawful permanent resident of the
United States, or an entity organized under US law. Relevant
for IL4, IL5, and ITAR compliance where operator access must
be restricted to US-persons.

---

## Versioning and drift

This hub file tracks FedRAMP-program-level and DoD SRG-level
content. Both drift on their own cadences. The FedRAMP
baseline moved from Rev 4 to Rev 5 in 2023; a further revision
is not on the published roadmap but the program's Rev 5 RFC
cycle is active as of early 2026. The DoD cloud SRG structure
moved from the monolithic CC SRG v1r4 to the CSP SRG v1r1 +
MO SRG split in 2024; contractors with pre-transition ATO
packages were given until end of calendar year 2025 to
transition to Rev 5 under the new SRG.

**When either lands, this hub file is the first Phase 5c file
to re-verify.** Per-provider files cite this hub for the
FedRAMP-to-IL mapping and the program-level framing; updating
the hub cascades the correction without re-authoring the
provider files.

Provider-specific authorization status drifts faster than the
program level. Per-provider files carry their own dated
stamps on provider-level authorization claims. Neither the hub
nor the provider files embed FedRAMP Marketplace package IDs
in structural claims; readers verify specific package IDs at
marketplace.fedramp.gov when citing them in their own SSPs.
