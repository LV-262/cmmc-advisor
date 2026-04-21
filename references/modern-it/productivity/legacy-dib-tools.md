# Legacy DIB Tools Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); DFARS 252.204-7012; FedRAMP program documentation
> (fedramp.gov) and FedRAMP Marketplace
> (marketplace.fedramp.gov); Atlassian Trust Center
> (atlassian.com/trust/compliance/resources/fedramp and
> atlassian.com/blog/announcements/atlassiangovernmentcloud);
> ServiceNow Trust and Compliance
> (servicenow.com/company/trust/compliance.html);
> GitHub FedRAMP FAQ (government.github.com/fedramp-faq) and
> GitHub Trust Center (ghec.github.trust.page); Box government
> solutions page (box.com/industries/government) and Box Trust
> Center (box.com/trust); DoD CSP SRG v1r1 (public.cyber.mil);
> NIST CMVP validated modules registry (csrc.nist.gov).

## Overview

This file covers adjacent productivity tools the defense industrial
base (DIB) runs alongside a primary suite (Microsoft 365 GCC High
or Google Workspace with Assured Controls Plus). Scope is a finite,
named catalog of four vendor families, including government-cloud
and self-hosted variants where applicable, per hub Decision 7. Not
a general SaaS compliance directory.

Read alongside `references/modern-it/productivity/README.md` (Phase
5d hub carrying the seven conventions), `microsoft-365-gcc.md`, and
`google-workspace.md`.

**Why Fit Assessment instead of Tenancy Selection.** Per hub
Decision 3, a four-vendor catalog is a fit decision, not a tenancy
decision. Each tool answers four questions: is it FedRAMP-
authorized, at what level, what is the CUI-handling story, and what
is the migration path when the answer is no.

**Primary-source verification pattern.** Every tier-level
authorization claim is primary-source verified against the vendor's
compliance page or the FedRAMP Marketplace, with the verification
date stamped inline. This matters more here than in the primary-
suite files because one vendor (Atlassian) was authorized only in
March 2025 and another (ServiceNow) is widely mis-cited as Moderate
when the current authorization is High.

---

## Scope of this file

Covered:

- **Atlassian Government Cloud** (Jira, Jira Service Management,
  Confluence). Bitbucket is explicitly NOT part of Atlassian
  Government Cloud as of the verification date; see the Atlassian
  Fit Assessment below.
- **Atlassian Data Center** (self-hosted deployment pattern
  including Bitbucket Data Center, Jira Data Center, Confluence Data
  Center). Contractor holds full compliance posture.
- **ServiceNow Government Community Cloud (GCC)**. ITSM and platform
  services including custom applications built on the Now Platform.
- **GitHub Enterprise Cloud** (the FedRAMP-authorized multi-tenant
  SaaS). Source-code collaboration, issues, pull requests, Actions
  CI/CD.
- **GitHub Enterprise Server** (the self-hosted on-premises or IaaS-
  hosted variant). Contractor holds full compliance posture.
- **Box for Government** (the FedRAMP-authorized Box offering for
  federal workloads). File collaboration, Box Sign, Box Shield.

Not covered:

- Commercial SaaS tiers of the four named vendors (Atlassian
  Commercial, ServiceNow commercial, GitHub Enterprise Cloud outside
  the FedRAMP scope, Box Commercial) for CUI workloads. Running CUI
  in these tiers is a scope problem; migration paths to the
  government-tier offerings are in the Fit Assessment sections.
- Slack, Dropbox, Notion, Airtable, Monday.com, Asana, Zoom
  commercial, and similar popular SaaS. Not FedRAMP-authorized in
  commercial tiers and outside hub Decision 7 scope.
- On-premises Exchange, on-premises SharePoint, on-premises Skype
  for Business. Migration sources, not target architectures; on-prem
  productivity for CUI in 2026 is a migration problem covered under
  the primary-suite files.
- Generic protocols (FTP, SFTP, SMTP, S/MIME) and on-prem file
  servers — see `references/domains/sc-system-comms.md`.
- Generative-AI features bundled with the listed tools (Atlassian
  Intelligence, ServiceNow Now Assist, GitHub Copilot, Box AI).
  Covered under `references/modern-it/ai-services/` where model
  hosting, prompt processing, and output retention are the load-
  bearing concerns.

---

## Fit Assessment — symmetric four-question structure

Each tool below answers the four Fit Assessment questions in the
same order:

1. Is the tool FedRAMP-authorized for the scope the contractor
   needs, and at what impact level?
2. Does the tool carry any DoD Impact Level authorization on top of
   FedRAMP?
3. What is the CUI-handling story — which categories of CUI is the
   tool appropriate for, and which are out of bounds?
4. What is the migration path when the tool cannot handle the
   contractor's CUI scope directly?

Questions are identical across tools; answers differ sharply because
each vendor has distinct authorization posture, scope of coverage,
and residual-risk profile.

---

## Atlassian Government Cloud — Jira, JSM, Confluence

**Atlassian Government Cloud** is Atlassian's FedRAMP-authorized
multi-tenant cloud covering Jira Software, Jira Service Management
(JSM), and Confluence. Bitbucket Cloud is NOT in the authorization
boundary at the verification date.

**1. FedRAMP authorization and impact level.** Atlassian Government
Cloud holds **FedRAMP Moderate Authorization** for Jira, Confluence,
and JSM (verified 2026-04-21 via
atlassian.com/trust/compliance/resources/fedramp and the March 2025
announcement at
atlassian.com/blog/announcements/atlassiangovernmentcloud). The
authorization is an Agency ATO route rather than a JAB P-ATO. Trello
Enterprise carries a separate FedRAMP Tailored (LI-SaaS)
authorization and is out of scope for this file's CUI focus.

**Bitbucket Cloud posture.** Bitbucket Cloud is not in the
Atlassian Government Cloud boundary and Atlassian has not
published a public FedRAMP roadmap date for Bitbucket Cloud. A
contractor needing FedRAMP-authorized Git hosting uses GitHub
Enterprise Cloud (FedRAMP Tailored) or self-hosts via Bitbucket
Data Center or GitHub Enterprise Server. The October 2025 Atlassian
announcement references "FedRAMP High and Impact Level 5 on the
horizon" as roadmap, not current authorization; verify current
package scope on the FedRAMP Marketplace before citing.

**2. DoD Impact Level.** None as of 2026-04-21. Contracts requiring
DoD IL4/IL5 reciprocity at the ITSM or knowledge-base plane cannot
be satisfied by Atlassian Government Cloud alone. Substitute
ServiceNow GCC at IL4 for ITSM, or accept the Moderate Agency ATO
ceiling with documented agency agreement.

**3. CUI-handling story.** Appropriate for CUI workflows where the
contract accepts FedRAMP Moderate equivalence under DFARS 252.204-
7012 without DoD IL overlay: engineering-team issue tracking that
references CUI systems in bodies and comments; Confluence knowledge
bases documenting CUI-adjacent procedures; JSM workflow for
internal IT. Not appropriate for IL4/IL5-required workloads, for
CUI categories exceeding agency authorization-letter scope, or for
ITAR-controlled technical data without a separate operator-access
assessment.

**4. Migration path when fit is no.** A contractor running
Atlassian Commercial with CUI has a scope problem; options are (a)
migrate to Atlassian Government Cloud via Atlassian's government-
migration team, (b) migrate to Atlassian Data Center inside the
contractor's own boundary (see next section), or (c) migrate off
Atlassian to primary-suite-native equivalents — rarely feasible at
engineering-team scale.

**Data flow and identity.** Federates identity via SAML 2.0 from
the contractor's primary-suite IdP (Entra ID Government or Cloud
Identity). SCIM user provisioning supported. Audit logs export to
the primary suite's SIEM. Inherit IA-2 MFA from the primary-suite
IdP and document inheritance in the SSP.

---

## Atlassian Data Center — self-hosted pattern

**Atlassian Data Center** is the self-hosted deployment pattern
licensed separately from Atlassian Cloud: Jira, JSM, Confluence,
and Bitbucket Data Center. The contractor hosts on its own
infrastructure (on-premises, Azure Government, AWS GovCloud, or
hybrid); Atlassian licenses the software and compliance posture is
the contractor's responsibility.

**1. FedRAMP authorization.** None — Data Center is self-hosted.
FedRAMP inheritance flows from the underlying cloud platform when
Data Center runs on Azure Government or AWS GovCloud; see
`references/modern-it/cloud-platforms/azure-government.md` and
`references/modern-it/cloud-platforms/aws-govcloud.md`.

**2. DoD Impact Level.** Determined by hosting. Data Center on
Azure Government IL5 with IL5-appropriate configuration operates
inside a contractor-authored IL5 package.

**3. CUI-handling story.** Appropriate for CUI and ITAR-controlled
technical data when the contractor's SSP places the Data Center
instance inside the contractor's FedRAMP-equivalent or IL4/IL5
boundary. Common scenarios: ITAR-controlled technical data that
cannot live in Atlassian Government Cloud (no ITAR-specific
operator-access commitment) or Bitbucket Cloud (not authorized);
heavy Atlassian investment consolidated under the contractor's
primary tenancy; contract-specific CUI categories not covered by
the Government Cloud agency ATO. Not appropriate for small
contractors without operations capacity to run Atlassian at
compliance-grade reliability, or for contractors minimizing SSP
scope where the Government Cloud Moderate ceiling would suffice.

**4. Migration path when fit is no.** Move to Atlassian Government
Cloud (if Moderate matches the contract) or to a different vendor
family (ServiceNow GCC for ITSM; GitHub Enterprise Cloud for source
control).

**Operator access and cryptography.** Atlassian personnel do not
touch Data Center instances except under explicit Professional
Services engagement with NDA. Running Data Center on a FIPS-mode
OS image and a FIPS-validated JDK (Red Hat OpenJDK with FIPS
enabled, Azul Zulu with FIPS module) is the standard path;
document the CMVP validated module references in the SSP.

---

## ServiceNow Government Community Cloud

**ServiceNow Government Community Cloud (GCC)** is ServiceNow's
government-dedicated SaaS offering spanning ITSM, IT Operations
Management (ITOM), IT Business Management (ITBM), Customer Service
Management, HR Service Delivery, and the platform for custom
applications built on the Now Platform.

**1. FedRAMP authorization and impact level.** ServiceNow GCC holds
a **FedRAMP High JAB Provisional Authority to Operate (P-ATO)**
(verified 2026-04-21 via
servicenow.com/company/trust/compliance.html). Initial FedRAMP High
P-ATO: August 2019. This is a common misconception point: ServiceNow
GCC is frequently cited as FedRAMP Moderate in compliance
literature, but the current authorization is High. A contractor
building an SSP cites the current FedRAMP Marketplace package
listing and the verification date, not the widely-circulated
Moderate claim.

**2. DoD Impact Level.** ServiceNow GCC carries **DoD Impact Level
4 (IL4) Provisional Authorization** under CSP SRG v1r1 reciprocity
(verified 2026-04-21). Additionally, ServiceNow GCC satisfies
CNSSI 1253F Privacy Overlay High for PII and PHI control
requirements. ServiceNow GCC does not carry IL5 authorization; IL5
contracts requiring ITSM reciprocity must evaluate ServiceNow's
National Security Cloud offering or alternative IL5-authorized
ITSM platforms.

**3. CUI-handling story.** Appropriate for DIB CUI workflow
spanning ITSM, change management, incident management, service
catalog, and workflow automation. Typical fit: enterprise ITSM at
scale where incidents and change requests reference CUI systems
and may carry CUI attachments; workflow automation for
procurement, acquisition, and program management; custom Now
Platform applications handling CUI data (employee, contract,
CUI-metadata catalogs); GRC (governance, risk, compliance)
automation where CMMC evidence collection, POA&M workflow, and
control-mapping live in the ServiceNow GRC module. Not appropriate
for IL5 contracts requiring DoD reciprocity at the ITSM plane
(evaluate ServiceNow's National Security Cloud instead), or for
small ITSM volume where Atlassian JSM at Moderate or primary-suite-
native tooling is more cost-appropriate.

**4. Migration path when fit is no.** ServiceNow commercial (non-
GCC) with CUI is a scope problem; migration to GCC is a tenant
cutover handled by ServiceNow's government-migration team. IL5-
requiring contracts route to ServiceNow National Security Cloud
(out of this file's scope).

**Platform vs. application distinction.** ServiceNow GCC is
simultaneously a platform (Now Platform) and a set of packaged
applications (ITSM, ITOM, ITBM, Customer Service Management, HR
Service Delivery, GRC, Security Operations). FedRAMP authorization
covers the platform and packaged apps; custom applications the
contractor builds inherit the platform's authorization but are not
separately certified. Document the inheritance and contractor-layer
controls (classification logic, field-level encryption, access-
control configuration) in the SSP.

**Identity, MID Server, and audit.** SAML 2.0 or OIDC federation
from the primary-suite IdP; SCIM provisioning supported. MID Server
(ServiceNow's in-network agent for discovery and orchestration)
runs inside the contractor's boundary and inherits contractor
posture. System audit logs export to the contractor's SIEM via the
Now Platform audit API or event-management connectors; configure
export at provisioning time to avoid retention-store migration.

---

## GitHub Enterprise Cloud

**GitHub Enterprise Cloud** is GitHub's multi-tenant SaaS offering
for source-code collaboration, issue tracking, pull requests,
GitHub Actions CI/CD, GitHub Packages, GitHub Advanced Security,
and related developer services.

**1. FedRAMP authorization and impact level.** GitHub Enterprise
Cloud holds a **FedRAMP Tailored (Low Impact SaaS) Authorization**
(verified 2026-04-21 via government.github.com/fedramp-faq).
FedRAMP Tailored is a distinct baseline from FedRAMP Low, Moderate,
and High. It was designed by the FedRAMP program for low-risk SaaS
systems where the stored data is itself considered low-risk and
where the SaaS pattern does not warrant the full Moderate or High
control catalog. GitHub's public reasoning for the Tailored
authorization rests on the premise that "best practices suggest
that source code contain no information — personally identifiable
or otherwise — so it is seen as low risk to operations."

**Moderate authorization roadmap.** The GitHub Enterprise Cloud
Trust Center (ghec.github.trust.page) describes FedRAMP Moderate
compliance as a forward commitment rather than a current
authorization. Contractors needing FedRAMP Moderate at the code-
collaboration plane should track the FedRAMP Marketplace package
listing directly rather than rely on roadmap descriptions; verify
status before citing in an SSP.

**2. DoD Impact Level.** None as of 2026-04-21. GitHub Enterprise
Cloud does not carry a DoD Impact Level P-ATO. Contractors
requiring IL4/IL5 reciprocity at the code-collaboration plane
must use GitHub Enterprise Server inside an IL4/IL5 authorization
boundary the contractor authors, or an alternative Git platform
inside the primary-suite's platform-as-a-service offering (Azure
DevOps Services for Government inside Azure Government, with
Azure DevOps's own authorization posture).

**3. CUI-handling story.** Tailored fits tightly around source
code in private repositories. Issues, pull-request descriptions,
commit messages, and repository metadata sit outside the Tailored
risk model's design intent; a contractor treating them as
arbitrary CUI channels has a scope problem. Document organizational
policy prohibiting CUI content in issues and PR descriptions;
enforce via pre-commit hooks and periodic audit. Actions CI/CD
secrets are a separate compliance concern (rotation policy, scope
discipline, approval gates apply independently). Large binary CUI
attachments (CAD files, CUI-marked documents) belong in the primary-
suite file store or Box for Government, referenced from GitHub by
URL or ID.

**4. Migration path when fit is no.** (a) Move source hosting to
GitHub Enterprise Server inside a contractor-authored FedRAMP-
equivalent or IL4/IL5 boundary (next section); (b) move to Azure
DevOps Services for Government inside Azure Government's FedRAMP
High + IL5 boundary where tooling allows; (c) keep Enterprise Cloud
for code-only scope and rigorously exclude CUI-beyond-source-code
content — the most common DIB pattern.

**Operator access, residency, and GitHub AE.** Enterprise Cloud
operator access is governed by the Tailored authorization.
Enterprise Cloud with Data Residency offers region-scoped storage
as an adjacent configuration; verify the specific residency
commitment against the current FedRAMP Marketplace package before
citing in an SSP. GitHub AE (the earlier single-tenant government
offering) is deprecated; the 2026 government paths are Enterprise
Cloud (Tailored) or Enterprise Server (self-hosted IL4/IL5). Verify
current migration guidance at docs.github.com/en/enterprise-cloud
before planning a migration off AE.

---

## GitHub Enterprise Server — self-hosted pattern

**GitHub Enterprise Server** is the self-hosted Git platform
deployable on contractor infrastructure (on-premises, Azure
Government, AWS GovCloud, hybrid). Same product surface as
Enterprise Cloud with architecture differences appropriate to
self-hosted operation.

**1. FedRAMP authorization.** None — self-hosted. Inheritance
flows from the underlying IaaS platform.

**2. DoD Impact Level.** Determined by hosting. Enterprise Server
on Azure Government IL5 with IL5-appropriate configuration
operates inside a contractor-authored IL5 package.

**3. CUI-handling story.** Appropriate for CUI and ITAR-controlled
technical data when the contractor's SSP places the Server instance
inside the contractor's FedRAMP-equivalent or IL4/IL5 boundary.
Typical fit: ITAR-controlled source code where Enterprise Cloud's
Tailored operator-access commitment is insufficient; CUI scope
exceeding Tailored design intent; heavy GitHub investment
consolidated under a contractor-authored boundary. Not appropriate
for small contractors lacking operations capacity, or for scopes
that Enterprise Cloud Tailored already serves adequately.

**4. Migration path when fit is no.** Move to Enterprise Cloud
if Tailored suffices, or to Azure DevOps Services for Government
where tooling allows.

**Operator access and cryptography.** GitHub personnel do not
touch Enterprise Server instances except under explicit NDA
support engagements. Updates are distributed as offline packages.
FIPS-mode OS images (RHEL or Ubuntu on Azure Government; FIPS-mode
AMI on AWS GovCloud) inherit FIPS-validated cryptographic modules;
document CMVP module references in the SSP.

---

## Box for Government

**Box for Government** is Box's FedRAMP-authorized file-collaboration
offering, distinct from the Box commercial cloud. Covers file
storage, sharing (internal and external), Box Sign (e-signature),
Box Shield (DLP and threat detection), Box Relay (workflow), and
Box Governance (retention and records management).

**1. FedRAMP authorization and impact level.** Box for Government
holds a **FedRAMP High Authorization** (verified 2026-04-21 via
box.com/industries/government and Box's public compliance posture
at box.com/trust). Agency-ATO or JAB package details live on the
current FedRAMP Marketplace listing; verify package ID and scope
before citing in an SSP.

**2. DoD Impact Level.** Publicly available Box compliance pages
do not state a DoD Impact Level P-ATO at the verification date
beyond the FedRAMP High authorization itself; a contractor whose
contract vehicle references a specific DoD IL for the file-
collaboration plane should verify the current Box package scope on
the FedRAMP Marketplace and request the most recent compliance
letter from Box directly. Do not assert a Box IL posture in an SSP
without a dated primary source.

**3. CUI-handling story.** Fits DIB CUI file-collaboration where
the workload calls for external file exchange with government
customers and subcontractors (Box external-share links with
expiration, download-limit, and require-login policies handle
cross-tenancy friction); large-file collaboration exceeding
primary-suite attachment limits (Exchange Online 150MB;
Gmail 25MB); file-centric business processes (customer-document
intake, subcontractor submissions, contract-file exchange) where
Box is the system of record. Not a fit for general-purpose file
collaboration duplicating the primary suite's document library
(SharePoint Online or Drive); for ITAR-controlled technical data
without a vendor commitment letter for the contractor's specific
ITAR scope; or as a primary-suite replacement (Box is an
adjacency).

**4. Migration path when fit is no.** Box Commercial with CUI is
a scope problem; migration to Box for Government is a tenant
cutover handled by Box's government-migration team.

**Identity, operator access, and primary-suite integration.**
SAML 2.0 federation from the primary-suite IdP; SCIM supported.
Operator access follows the FedRAMP High package; verify the
specific US-person operator-access commitment and personnel-
screening regime against Box's current authorization package.
Box for Microsoft 365 enables Office co-authoring on files stored
in Box; Box for Google Workspace enables Docs editing on files
stored in Box. Verify each integration's FedRAMP scope before
relying on it — not every integration path is inside the Box
government package.

---

## Hybrid patterns

Hybrid patterns live in the Phase 5d hub at
`references/modern-it/productivity/README.md` under "Hybrid
patterns." This file's four vendor families map to the hub's four
pattern slots: Pattern A (Atlassian ticketing and dev) → Atlassian
Government Cloud; Pattern B (enterprise ITSM) → ServiceNow GCC;
Pattern C (code collaboration) → GitHub Enterprise Cloud;
Pattern D (large-file collaboration) → Box for Government. See the
hub for the "when this works" and "when this fails" narrative on
each pattern.

---

## Capability appendix — CMMC capability to legacy DIB tool

Per hub Decision 1 canonical format, this appendix follows the
hub row order. `—` in a row means the legacy DIB tool families do
not provide that capability in a CUI-suitable way; the primary
productivity suite is expected to own that capability.

| Productivity capability | Legacy DIB tool service |
|---|---|
| Email and calendar | — |
| Chat and team messaging | — |
| Meetings and video conferencing | — |
| Document authoring | — |
| Spreadsheets | — |
| Presentations | — |
| File storage and internal collaboration | Box for Government (FedRAMP High) |
| Intranet and employee communications | — |
| Forms and workflow intake | ServiceNow GCC (FedRAMP High + IL4) |
| Issue tracking and project management | Atlassian Jira (Government Cloud at FedRAMP Moderate); GitHub Issues (FedRAMP Tailored, source-code scope only) |
| Knowledge base and wiki | Atlassian Confluence (Government Cloud at FedRAMP Moderate) |
| IT service management and ticketing | ServiceNow GCC (FedRAMP High + IL4); Atlassian Jira Service Management (Government Cloud at FedRAMP Moderate) |
| Source code collaboration | GitHub Enterprise Cloud (FedRAMP Tailored); GitHub Enterprise Server (contractor-owned); Bitbucket Data Center (contractor-owned) |
| CI/CD | GitHub Actions on Enterprise Cloud (FedRAMP Tailored); GitHub Actions on Enterprise Server (contractor-owned) |
| External file exchange and large-file collaboration | Box for Government (FedRAMP High) |
| Records management and retention | Box Governance (on Box for Government); ServiceNow GRC record retention |
| E-signature | Box Sign (on Box for Government) |
| DLP (on legacy-tool content) | Box Shield (on Box for Government); limited native on other tools |
| Workflow automation (platform-level) | ServiceNow GCC Now Platform; Atlassian Automation (limited in Government Cloud) |
| Custom application development platform | ServiceNow Now Platform (GCC) |
| GRC tooling and CMMC evidence collection | ServiceNow GRC (on ServiceNow GCC) |
| Identity and access | Federated via the primary suite's identity plane |

**Reading the capability appendix.** The asymmetric rows reflect
the intentional scope of each vendor family. Atlassian does not
compete for source-code collaboration at FedRAMP Moderate because
Bitbucket is not in Atlassian Government Cloud; the Atlassian row
for source code appears only under Data Center (contractor-owned).
ServiceNow does not compete for file collaboration because
ServiceNow GCC is ITSM plus platform, not file storage. Box for
Government does not compete for issue tracking or source-code
collaboration because Box is file-collaboration. The rows map
actual current capability, not hypothetical overlap.

---

## Cross-domain anchors

Legacy DIB tool posture composes with corpus cross-cutting files
and domain practice files:

- **Phase 5d hub.** `references/modern-it/productivity/README.md`
  for the seven conventions including Decision 7 which pins this
  file's scope.
- **Microsoft 365 primary suite.** `references/modern-it/productivity/microsoft-365-gcc.md`
  for the primary suite typically paired with these legacy tools
  in a Microsoft-centric DIB architecture.
- **Google Workspace primary suite.** `references/modern-it/productivity/google-workspace.md`
  for the primary suite typically paired with these legacy tools
  in a Google-centric DIB architecture.
- **Phase 5c cloud-platforms hub.** `references/modern-it/cloud-platforms/cloud-selection.md`
  for the FedRAMP-to-IL crosswalk underlying the authorization
  claims here.
- **Azure Government platform.** `references/modern-it/cloud-platforms/azure-government.md`
  for self-hosted Atlassian Data Center and GitHub Enterprise
  Server inheritance on Azure Government.
- **AWS GovCloud platform.** `references/modern-it/cloud-platforms/aws-govcloud.md`
  for self-hosted Atlassian Data Center and GitHub Enterprise
  Server inheritance on AWS GovCloud.
- **FedRAMP inheritance and CSP equivalence.**
  `references/fedramp-gap.md` for the FedRAMP Tailored baseline
  context (GitHub Enterprise Cloud's authorization type) and the
  DFARS 7012 CSP-equivalence mechanics.
- **CUI scoping.** `references/scoping-and-cui.md`.
- **SSP authoring.** `references/ssp-guidance.md` for documenting
  legacy-tool authorization inheritance in the SSP.

Domain practice files used for requirement text and evidence
lists:

- Access Control (AC) — `references/domains/ac-access-control.md`
  for account management, remote access, and session controls.
- System and Information Integrity (SI) —
  `references/domains/si-system-information-integrity.md` for
  vulnerability management and malware protection at the legacy-
  tool plane.
- System and Communications Protection (SC) —
  `references/domains/sc-system-comms.md` for encryption and
  boundary protection.
- Identification and Authentication (IA) —
  `references/domains/ia-identification-auth.md` for identity
  federation from primary suite IdP.
- Configuration Management (CM) —
  `references/domains/cm-configuration-mgmt.md` for change
  control on legacy-tool configurations.
- Audit and Accountability (AU) — `references/domains/au-audit.md`
  for audit logging and SIEM ingestion.
- Media Protection (MP) —
  `references/domains/mp-media-protection.md` for retention and
  records management.

---

## Examples as of 2026-04

> **Examples as of 2026-04:** The four vendor families named in
> this file are the Decision 7 scope. Third-party alternatives
> serving overlapping capability needs — source control hosts
> outside the four named vendors, ITSM platforms outside
> ServiceNow, file-collaboration platforms outside Box — would
> require a deliberate scope expansion per Decision 7 rather than
> an author's judgment call. This skill does not rank vendors.
> Verify current FedRAMP Marketplace status and the current vendor
> authorization letter before selecting any legacy-tool adjacency
> operating alongside Microsoft 365 GCC High or Google Workspace
> Assured Controls Plus.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/productivity/README.md`,
`references/modern-it/cloud-platforms/cloud-selection.md`, or
previous Phase 5 slices are not repeated here.

**Agency ATO.** The FedRAMP authorization path where a single
federal agency issues the Authority to Operate based on the FedRAMP
package rather than the Joint Authorization Board (JAB). Distinct
from a JAB P-ATO; operationally equivalent for contract-accepting
purposes but reflects a different authorization route.

**Atlassian Government Cloud.** Atlassian's FedRAMP-authorized
multi-tenant cloud offering covering Jira, Jira Service Management,
and Confluence at FedRAMP Moderate (achieved March 2025).

**Box for Government.** Box's FedRAMP High authorized file-
collaboration offering, distinct from Box Commercial.

**CNSSI 1253.** Committee on National Security Systems
Instruction 1253. Security categorization and control selection
framework overlaying FIPS 199 for national security systems and
certain CUI workloads.

**CNSSI 1253F Privacy Overlay.** The privacy-overlay annex of
CNSSI 1253 specifying additional controls for systems processing
PII and PHI.

**GHE (GitHub Enterprise).** The umbrella term for GitHub's
enterprise products: GitHub Enterprise Cloud (multi-tenant SaaS)
and GitHub Enterprise Server (self-hosted).

**GitHub AE.** The single-tenant government cloud offering in
GitHub's earlier product history; deprecated at the 2026-04
verification date.

**IL4.** DoD Impact Level 4. Defined in
`references/modern-it/cloud-platforms/cloud-selection.md`
Terminology.

**JAB P-ATO.** Joint Authorization Board Provisional Authority
to Operate. The FedRAMP authorization path where the Joint
Authorization Board (composed of CIOs from DoD, DHS, and GSA)
issues the P-ATO. Distinct from an Agency ATO.

**JSM (Jira Service Management).** Atlassian's ITSM product
branded around service request, incident, problem, and change
management workflows on top of the Jira platform.

**LI-SaaS (Low Impact SaaS).** The FedRAMP Tailored baseline for
SaaS systems qualifying for reduced FedRAMP control scope based
on the low-risk profile of the stored data.

**Now Platform.** ServiceNow's underlying application-development
and workflow-automation platform. ServiceNow's ITSM, ITOM, ITBM,
and adjacent application modules run on the Now Platform.

**P-ATO (Provisional Authority to Operate).** The FedRAMP
authorization issued by the JAB or an Agency that attests to the
CSP's security posture against the FedRAMP control baseline at
the applicable impact level.

---

## Versioning and drift

Legacy-tool authorizations change on a quarterly-or-faster cadence.
Atlassian Government Cloud is recently authorized (March 2025);
ServiceNow GCC has a tier widely mis-cited; GitHub deprecated AE
and is pursuing Moderate on Enterprise Cloud. The tier-level
anchors for this verification date are Atlassian Government Cloud
at FedRAMP Moderate; ServiceNow GCC at FedRAMP High + IL4; GitHub
Enterprise Cloud at FedRAMP Tailored; Box for Government at
FedRAMP High. Per-service and per-SKU scope carries dated stamps
inline in the Fit Assessment sections. Feature-level claims (Box
Shield DLP, ServiceNow GRC module scope, Atlassian Automation in
Government Cloud) are labeled "as of 2026-04, verify current
vendor documentation before implementing." Roadmap claims
(Atlassian "FedRAMP High + IL5 on the horizon"; GitHub Enterprise
Cloud FedRAMP Moderate in progress) are roadmap, not current
authorization — contractors do not cite roadmap in an SSP.

Content verified 2026-04-21 against the vendor compliance pages
named at top. Next re-verification at the corpus review cycle or
when a vendor announces a FedRAMP Marketplace tier change.
