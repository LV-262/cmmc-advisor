# Productivity Suite Compliance (Overview)

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); DFARS 252.204-7012; FedRAMP program documentation
> (fedramp.gov); Microsoft 365 compliance documentation
> (learn.microsoft.com/compliance); Google Workspace compliance
> (workspace.google.com/security); vendor-specific Trust Center
> portals (atlassian.com/trust, servicenow.com/company/trust,
> github.com/security, box.com/trust); DoD CSP SRG v1r1
> (public.cyber.mil).

## Overview

This file is the hub for `references/modern-it/productivity/`. A
defense contractor handling CUI or FCI chooses a productivity
suite for email, collaboration, document editing, messaging, and
adjacent IT-service workflows. That choice has cascading
compliance implications (tenancy, identity, encryption posture,
operator access, export-control story, and cross-suite
collaboration) that this directory maps to CMMC practice
requirements.

Three per-vendor files live alongside this hub:

- **`microsoft-365-gcc.md`** — Microsoft 365 GCC, GCC High, and
  DoD tenancy posture for the Microsoft productivity stack
  (Exchange Online, SharePoint Online, OneDrive, Teams, Intune,
  Purview, Defender for Office 365, Power Platform).
- **`google-workspace.md`** — Google Workspace editions, Assured
  Controls and Assured Controls Plus overlays, per-service
  posture (Gmail, Drive, Meet, Chat, Calendar, Docs), Cloud
  Identity, DLP, Vault, Context-Aware Access, client-side
  encryption.
- **`legacy-dib-tools.md`** — Adjacent productivity tools the
  defense industrial base runs alongside the primary suite:
  Atlassian (Jira, Confluence, Jira Service Management),
  ServiceNow (IT Service Management and workflow platform),
  GitHub (source code collaboration), Box for Government (file
  collaboration).

Read this file for the directory's conventions, the
capability-orthogonal crosswalk, hybrid architectural patterns,
and the decision tree for selecting a productivity suite. Read
the per-vendor files for tenancy detail, per-service
authorization posture, and implementation guidance.

---

## Scope of this directory

Covered:

- Microsoft 365 GCC, GCC High, and DoD government tenancies.
- Google Workspace Enterprise Plus with Assured Controls Plus
  and base Assured Controls configurations.
- Atlassian Government Cloud and Atlassian Data Center
  self-hosted deployments.
- ServiceNow Government Community Cloud.
- GitHub Enterprise Cloud with FedRAMP Tailored authorization
  and self-hosted Enterprise Server.
- Box for Government as a FedRAMP-authorized file
  collaboration adjacency.
- Hybrid architectures combining M365 or Workspace with one or
  more of the legacy tools.

Not covered:

- On-premises Exchange, on-premises SharePoint, and other
  on-premises productivity deployments in depth. These are
  migration sources for CUI contractors, not target architectures;
  on-prem productivity for CUI in 2026 is a migration problem,
  not a compliance-tuning problem.
- Arbitrary SaaS not explicitly listed above. The `legacy-dib-tools.md`
  scope per Decision 7 covers a finite set of tools the defense
  industrial base actually runs. Other SaaS products (Slack
  commercial, Dropbox commercial, Notion, Airtable, many others)
  are generally not FedRAMP-authorized in their commercial forms
  and are not treated here.
- Generic protocols (FTP, SFTP, SMTP relays, S/MIME). Protocol-
  level guidance lives under `references/domains/sc-system-comms.md`.
- Microsoft 365 Copilot and Google Workspace generative-AI
  features in depth. AI-specific posture is covered under
  `references/modern-it/ai-services/` (pending) where the AI
  service scope and FedRAMP or IL authorization for model and
  prompt processing is the load-bearing concern.

---

## The seven conventions this directory follows

Four Decisions carry over from Phase 5c (the cloud-platforms
hub). Three Decisions are Phase 5d specific. Each is stated in
prose with rationale below.

### Decision 1: Provider-primary structural files with per-file capability appendix

**Per-vendor files are organized by that vendor's tenancy model
and service catalog.** Microsoft 365 GCC High by tenancy tier and
service component; Google Workspace by edition and Assured
Controls Plus scope; legacy-dib-tools by product with a Fit
Assessment framing. Each per-vendor file carries a capability
appendix (productivity capability → this vendor's service). This
hub carries the three-column capability-orthogonal crosswalk for
multi-vendor readers.

**Rationale.** Productivity suites are inherently product-centric
in a way endpoint management is not. "MDM" and "EDR" are
capabilities; "Microsoft 365" and "Google Workspace" are products
with architecturally distinct tenancy models. A contractor
committed to GCC High has made a tenancy decision with cascading
implications (FedRAMP High inheritance, ITAR via sovereign
tenancy, identity federation constraints, cross-suite
collaboration costs) that no capability-primary framing
captures. Phase 5b (endpoints) applied capability-primary
structure because MDM-vs-EDR-vs-disk-encryption are genuinely
orthogonal control surfaces; productivity is not like that.

This matches the Phase 5c cloud-platforms convention
(`references/modern-it/cloud-platforms/README.md`-equivalent at
`cloud-selection.md`) and diverges from the Phase 5b endpoints
convention (`references/modern-it/endpoints/README.md`)
deliberately.

**Canonical capability-appendix format for per-vendor files.**
Each of `microsoft-365-gcc.md`, `google-workspace.md`, and
`legacy-dib-tools.md` carries a two-column capability appendix
with this row shape:

| Productivity capability | This vendor's service |
|---|---|
| Email | Exchange Online with Purview retention (GCC High) |
| File storage and collaboration | SharePoint Online + OneDrive with sensitivity labels (GCC High) |

Row order matches the hub's three-column crosswalk below. The
right column names the vendor's specific service plus the tier
or edition context. Per-vendor detail (specific configurations,
evidence, common mistakes) lives in the structural tenancy
sections above the appendix; the appendix is a quick-reference
index, not a place for implementation depth.

### Decision 2: FedRAMP as primary axis; DoD Impact Level as overlay

**Every compliance claim in this directory uses FedRAMP
authorization as the primary axis and DoD Impact Level as a
declared overlay.** Tenancy-level claims (GCC High is FedRAMP
High, Assured Controls Plus is IL4) are the stable anchor; prose
leans on these. Per-service authorization claims (Exchange Online
IL5, Gmail IL4 under Assured Controls Plus, ServiceNow GCC IL4)
carry dated verification stamps inline.

**Rationale.** FedRAMP authorization is what CMMC L2 contractors
encounter directly under DFARS 252.204-7012. Productivity
vendors diverge sharply at the per-service authorization layer
(not every M365 component is IL5-authorized even inside GCC
High; not every Workspace component is IL4-authorized under
Assured Controls Plus; Atlassian Government Cloud carries
FedRAMP Moderate across Jira/Confluence/JSM but legacy tools
have uneven coverage). FedRAMP as the primary axis keeps the
prose legible at tier level while the per-service anchors sit
in the per-vendor files.

Full IL4 and IL5 implementation content remains deferred to a
future DoD-specific reference, consistent with the Phase 5c
hub's treatment (`references/modern-it/cloud-platforms/cloud-selection.md`
"FedRAMP baseline to DoD Impact Level crosswalk") and with
`references/fedramp-gap.md` "Relationship to DoD Cloud Computing
Security Requirements Guide."

### Decision 3: Symmetric Tenancy Selection section for suite vendors, Fit Assessment for the legacy file

**`microsoft-365-gcc.md` and `google-workspace.md` carry a
Tenancy Selection section answering three questions in the same
order** (commercial acceptable for CUI? which government
tenancy or overlay? workload-location and personnel
boundaries?). This matches the Phase 5c cloud-platforms
convention.

**`legacy-dib-tools.md` carries a Fit Assessment section
instead** because tenancy is not the relevant axis for a
multi-vendor catalog. Each legacy tool answers: is it FedRAMP-
authorized, at what level, what is the CUI-handling story, and
what is the migration path if the tool cannot handle CUI
directly. Symmetric shape across tools; asymmetric answers that
reflect each tool's actual compliance posture.

**Rationale.** Productivity suite selection is first a
tenancy decision (GCC vs GCC High vs Workspace Assured Controls
Plus) with downstream implications. Legacy tool selection is
first a fit decision (does this tool handle CUI at the
authorization level my contract requires) with downstream
migration implications when the answer is no. Forcing one
section shape across both would mislead readers on either side.

### Decision 4: Hybrid patterns in this hub only

**Common hybrid architectures live here; per-vendor files
forward-reference rather than duplicate.** See "Hybrid patterns"
below.

**Rationale.** Hybrid is a multi-vendor decision by definition.
Centralization prevents three divergent treatments from
diverging within 12 months of authoring.

### Decision 5: Microsoft 365 GCC versus GCC High tenancy ownership

**`microsoft-365-gcc.md` is the authoritative owner of the
Microsoft tenancy-selection decision (GCC vs GCC High vs DoD vs
commercial).** The full decision tree, per-scenario guidance,
and cross-sectional posture live in that file.
`references/modern-it/endpoints/windows-fleet.md` carries a
compact pointer to `microsoft-365-gcc.md` for contractors
arriving from the endpoint-management perspective.

**Rationale.** The GCC/GCC High decision affects productivity
(email, files, collaboration, compliance tooling), endpoint
management (Intune tenancy), identity (Entra ID Government),
and Azure IaaS (via Azure Government tenancy selection). During
Phase 5b, `windows-fleet.md` carried the decision because the
productivity file did not yet exist. With Phase 5d, the
productivity file becomes the natural owner; endpoint and
cloud-platform files cross-reference rather than re-derive.

**Implementation note.** Phase 5d Slice S rewrites
`windows-fleet.md:44-63` from a full framing block to a compact
pointer. The rewrite is semantic-neutral; content moves to
`microsoft-365-gcc.md` without framing changes. Slice S PR must
include side-by-side pre-rewrite and post-rewrite diff plus a
grep of `windows-fleet.md` for any residual GCC/GCC-High framing
outside the rewritten block.

### Decision 6: Google Workspace Assured Controls Plus ownership

**`google-workspace.md` is the authoritative owner of the
Workspace Assured Controls and Assured Controls Plus overlay
story.** `references/modern-it/cloud-platforms/gcp-assured.md`
keeps a one-paragraph terminology entry (already in place under
"Assured Controls Plus") pointing readers to the productivity
file for the full treatment.

**Rationale.** Assured Controls Plus is a Google Workspace
package distinct from Assured Workloads (the Google Cloud
compliance overlay). The two are authorized independently,
integrate via identity federation rather than tenant merge, and
carry different US-person operator-access mechanisms. The
productivity file is the correct owner because Assured Controls
Plus is a productivity-suite construct; the cloud-platforms file
correctly handles the infrastructure overlay (Assured Workloads)
and points at the productivity file for the adjacent productivity
overlay.

### Decision 7: `legacy-dib-tools.md` scope boundary

**The `legacy-dib-tools.md` file covers a finite, named set of
tools: Atlassian (Jira, Confluence, Jira Service Management),
ServiceNow (IT Service Management and platform), GitHub
(source-code collaboration), Box for Government (file
collaboration).**

In scope:

- Atlassian Government Cloud (FedRAMP Moderate for Jira,
  Confluence, Jira Service Management).
- Atlassian Data Center (self-hosted pattern; contractor owns
  full compliance posture).
- ServiceNow Government Community Cloud (FedRAMP Moderate plus
  DoD IL4 Provisional Authorization).
- GitHub Enterprise Cloud (FedRAMP Tailored — note this is a
  distinct lower-scope baseline rather than FedRAMP Moderate or
  High; implications covered in the per-vendor file).
- GitHub Enterprise Server (self-hosted pattern; contractor
  owns full compliance posture).
- Box for Government (FedRAMP High authorized; runs on AWS
  GovCloud).

Out of scope:

- Slack, Dropbox, Notion, Airtable, and other commercial-only
  SaaS. These are not FedRAMP-authorized in their commercial
  tiers and are not treated here. A contractor needing the
  capabilities those tools provide should evaluate a
  FedRAMP-authorized alternative or treat the tool as
  non-CUI-capable.
- Atlassian Commercial (the non-Government-Cloud Atlassian
  tenancy). Atlassian's commercial cloud offerings are separate
  from Atlassian Government Cloud and are not appropriate for
  CUI. A contractor running Atlassian Commercial for CUI workflow
  has a scope problem, not a fix; migration to Atlassian
  Government Cloud (FedRAMP Moderate) or Atlassian Data Center
  self-hosted under the contractor's own compliance boundary is
  the path. The `legacy-dib-tools.md` file expands both
  migration targets.
- On-premises Exchange, on-premises SharePoint, and other
  on-premises productivity systems in depth.
- Arbitrary SaaS beyond the named list. If a reader asks
  about a tool not covered, this file's response is: "this
  skill documents the tools defense industrial base contractors
  actually run; for an unlisted tool, consult the FedRAMP
  Marketplace or the vendor's Trust Center directly."
- Generic protocols (FTP, SFTP, SMTP, S/MIME). Protocol
  content lives under `references/domains/sc-system-comms.md`.

**Rationale.** The legacy-tools file is the kitchen-sink risk
of this phase. Scope discipline prevents the file from becoming
an ever-growing catalog of every tool any defense contractor
has ever asked about. The four named vendor families cover the
DIB's typical productivity adjacencies; expansion beyond them
requires a deliberate decision, not an author's judgment call.

---

## Tier-level authorization snapshot

All claims below verified 2026-04-21 via FedRAMP Marketplace
and vendor compliance pages. Per-service authorization detail
lives in the per-vendor files; this snapshot is tier-level only.

| Vendor / tenancy | FedRAMP tier | DoD IL | CUI suitability |
|---|---|---|---|
| Microsoft 365 Commercial | FedRAMP High (on specific services) | IL2 | Non-CUI federal; not appropriate for CUI |
| Microsoft 365 GCC | FedRAMP Moderate | IL2 | Limited CUI scenarios with agency agreement |
| Microsoft 365 GCC High | FedRAMP High | IL5 | Appropriate for CUI under DFARS 7012 |
| Microsoft 365 DoD | FedRAMP High | IL5 (DoD-exclusive) | DoD mission owners only |
| Google Workspace (Enterprise Plus) | FedRAMP High (on specific services) | n/a directly | Use Assured Controls Plus for CUI |
| Google Workspace + Assured Controls Plus | FedRAMP High services + overlay | IL4-aligned | Appropriate for CUI under DFARS 7012 |
| Atlassian Government Cloud | FedRAMP Moderate | n/a | CUI scenarios with agency agreement |
| Atlassian Data Center (self-hosted) | Contractor-owned | Contractor-owned | Contractor holds full compliance; FIPS and boundary posture depend on hosting |
| ServiceNow Government Community Cloud | FedRAMP Moderate | IL4 | Appropriate for CUI under DFARS 7012 |
| GitHub Enterprise Cloud | FedRAMP Tailored | n/a | Source-code-only low-risk SaaS; not a general CUI file store |
| GitHub Enterprise Server (self-hosted) | Contractor-owned | Contractor-owned | Contractor holds full compliance |
| Box for Government | FedRAMP High | n/a directly | Appropriate for CUI file collaboration under DFARS 7012 |

**Reading the snapshot.** This table is a directory-level map,
not an implementation guide. Per-vendor files in this directory
carry the service-by-service authorization breakdown (which M365
services are in scope at IL5 versus which are GCC-only, which
Workspace services are covered under Assured Controls Plus,
which Atlassian apps are in Government Cloud versus Data Center
only). A contractor building an SSP cites the per-vendor file's
dated per-service claims, not this snapshot.

**GitHub Tailored note.** FedRAMP Tailored is a distinct baseline
from FedRAMP Low, Moderate, and High. It was designed for
low-risk SaaS where the stored data is itself considered
low-risk (code, for example). GitHub Enterprise Cloud under
FedRAMP Tailored is appropriate for source-code collaboration
but does not by itself provide CUI coverage for arbitrary files
or data. A contractor handling CUI in GitHub issues, pull-request
descriptions, or repository metadata must treat those as
CUI-adjacent surfaces and evaluate whether Tailored coverage
meets the contract's requirement.

**GCC High versus Workspace Assured Controls Plus — equivalence
is not symmetric.** Both tenancies can host CUI workflows under
DFARS 7012, but they deliver that posture through different
mechanisms. GCC High is a sovereign tenancy (FedRAMP High plus
DoD IL5, physically and logically separate from commercial
Microsoft 365, US-person operator access enforced at the
tenancy partition). Workspace Assured Controls Plus is an
overlay on the commercial Google Workspace tenancy (FedRAMP
High-authorized services plus the Assured Controls Plus
package, US-person operator access enforced at the control-
package level rather than at the tenancy boundary, IL4-aligned
not IL5). A contractor choosing between the two is choosing
between an architectural model (sovereign tenancy versus
overlay) as much as between a vendor. See the per-vendor files
for tenancy-specific deep dives.

---

## Capability-orthogonal crosswalk

The table below maps productivity capabilities to each vendor
family's service. Rows are capability clusters; columns are the
three vendor families. Per-vendor files decompose each cell into
the specific service-to-practice mapping.

| Productivity capability | Microsoft 365 (GCC/GCC High) | Google Workspace (Assured Controls Plus) | Legacy DIB tools |
|---|---|---|---|
| Email | Exchange Online | Gmail | Atlassian JSM email integration, legacy on-prem Exchange (migration source) |
| File storage and collaboration | SharePoint Online, OneDrive | Drive, Shared Drives | Box for Government, Atlassian Confluence (pages), GitHub (code only) |
| Real-time messaging and chat | Teams | Chat, Meet Chat | Atlassian JSM chat integration, ServiceNow chat |
| Calendaring and meetings | Outlook Calendar, Teams Meetings | Calendar, Meet | — |
| Document editing (word, spreadsheet, presentation) | Word, Excel, PowerPoint (Online and desktop) | Docs, Sheets, Slides | — |
| IT service management and ticketing | — | — | ServiceNow GCC, Atlassian Jira Service Management |
| Issue tracking and project management | Planner, Project | — | Atlassian Jira, GitHub Issues |
| Source code collaboration | DevOps services (limited) | — | GitHub Enterprise Cloud, Atlassian Bitbucket (Government Cloud) |
| Knowledge base and wiki | SharePoint sites, OneNote | Sites, Docs | Atlassian Confluence, ServiceNow Knowledge |
| Identity and access | Entra ID Government, Conditional Access, PIM | Cloud Identity, Context-Aware Access | Federated via the primary suite's identity plane |
| DLP and sensitivity labeling | Microsoft Purview DLP, Sensitivity Labels | Workspace DLP, Client-Side Encryption with EKM | Limited native; usually rely on primary suite DLP |
| Retention and records management | Purview Records Management | Vault, Drive Retention | Atlassian archive policies (limited), ServiceNow record retention |
| eDiscovery | Purview eDiscovery | Vault | ServiceNow and Atlassian audit logs (limited) |
| Compliance dashboard and audit | Purview Compliance Portal | Security Center, Workspace Audit | Per-tool admin dashboards |

**Reading the crosswalk.** A hyphen in a cell means that vendor
family does not provide that capability in a CUI-suitable way;
the capability is typically delivered by the primary suite when
present. A capability spanning multiple cells (for example, Atlassian
Jira for issue tracking alongside Microsoft Planner) means
contractors often mix; hybrid patterns below treat the
coexistence.

**What the crosswalk does not claim.** It does not claim feature
parity across cells. Gmail and Exchange Online are both email;
they differ substantially in mail flow, delegation, archiving,
and governance. Assured Controls Plus and GCC High deliver
CUI-suitable productivity through different mechanisms (residency
plus personnel plus contract for Workspace; sovereign tenancy
for GCC High). Migration between vendors is not a drop-in
exercise.

---

## Hybrid patterns

Productivity architectures in the defense industrial base are
rarely single-vendor. Four recurring patterns are named here;
per-vendor files forward-reference this section.

### Pattern A: Primary suite plus Atlassian for ticketing and dev

A contractor runs Microsoft 365 GCC High or Google Workspace
Assured Controls Plus for email, files, meetings, and
collaboration; runs Atlassian Government Cloud for
Jira Service Management, Jira (project tracking), and
Confluence (knowledge base); and federates identity from the
primary suite into Atlassian.

**When this works.** ITSM workflows and engineering project
tracking are Atlassian's strength; the primary suite's built-in
options (Microsoft Planner, Google Sites) do not match the
operational maturity. Atlassian Government Cloud's FedRAMP
Moderate authorization covers most CUI scenarios with agency
agreement.

**When this fails.** CUI residing in Jira issue descriptions,
Confluence pages with CUI body content, or Jira attachments
requires the contractor to treat Atlassian as a CUI asset and
apply the same practices as the primary suite. A contractor
running Atlassian Commercial (not Government Cloud) for CUI has
a scope problem, not a fix.

### Pattern B: Primary suite plus ServiceNow for enterprise ITSM

A contractor runs the primary suite for productivity and runs
ServiceNow Government Community Cloud for enterprise IT service
management, workflow automation, and adjacent SaaS workflows.
ServiceNow's IL4 authorization covers the CUI-adjacent workflow
use cases.

**When this works.** Enterprise ITSM at scale, workflow
automation for procurement or change management, and platform-
as-a-service use cases are ServiceNow's strength.

**When this fails.** ServiceNow GCC is FedRAMP Moderate with
DoD IL4; extending into IL5 territory requires the DoD-specific
path that is out of the standard GCC offering.

### Pattern C: Primary suite plus GitHub Enterprise Cloud for code

A contractor runs the primary suite for general productivity
and runs GitHub Enterprise Cloud (FedRAMP Tailored) for source
code collaboration. CUI code stays in private repositories;
identity federates from the primary suite's IdP.

**When this works.** Code is the stored data; code is
considered low-risk relative to arbitrary CUI documents, so
FedRAMP Tailored coverage aligns with the risk profile.

**When this fails.** Treating GitHub issues and pull-request
discussions as arbitrary chat channels carrying CUI content.
GitHub Tailored coverage does not extend to CUI held in issue
descriptions or CI/CD artifacts.

### Pattern D: Primary suite plus Box for Government for large-file collaboration

A contractor runs the primary suite for email and internal
collaboration and runs Box for Government for external file
sharing with government customers and subcontractors. Box's
FedRAMP High authorization supports the CUI-scope file
exchange that primary suites handle awkwardly across tenancy
boundaries.

**When this works.** External file exchange with entities
outside the contractor's primary tenancy. Large files that
exceed primary-suite attachment limits. Customer-contractor
file workflows with defined access controls.

**When this fails.** Using Box as a general file store duplicating
the primary suite's document library. The operational overhead
of two file stores rarely earns its keep when Box is not the
external-exchange surface.

---

## Productivity suite selection decision tree

When selecting a productivity suite for a CUI workload, walk
the questions in this order. Store the answers in the SSP.

1. **Is CUI present in the workload?** If no, FedRAMP Moderate
   equivalence under DFARS 7012 is not triggered; commercial
   tenancies are available. If yes, continue.
2. **Which CC SRG Impact Level applies?** IL4 (standard CUI),
   IL5 (mission-critical CUI, NSS non-classified). If IL5,
   continue with the understanding that the productivity-suite
   decision narrows to GCC High or Google Workspace Assured
   Controls Plus; Atlassian Government Cloud at FedRAMP Moderate
   does not carry IL5 for primary productivity workflows.
3. **Is ITAR or EAR export-controlled data present in the
   productivity workflow?** If yes, the contractor needs
   sovereign-tenancy assurance (GCC High), residency-plus-
   personnel assurance (Workspace Assured Controls Plus), or
   equivalent contractual assurance. Commercial and GCC
   tenancies are ruled out. Consult export-control counsel
   before finalizing.
4. **What existing infrastructure does the contractor have?**
   An existing M365 Commercial tenant, an existing Workspace
   Enterprise tenant, or an existing on-premises Exchange
   installation shifts the decision toward building on what
   exists rather than greenfield. Migration between primary
   suites mid-program is operationally expensive.
5. **What workload-specific capabilities matter?** Teams-heavy
   collaboration favors M365; Docs-centric real-time editing
   favors Workspace; developer-team workflows favor Atlassian
   plus GitHub adjacency.
6. **Single primary suite, or primary-plus-adjacent pattern?**
   Most DIB contractors run one primary suite plus one or two
   of the hybrid patterns above. Default to this; pure single-
   suite is viable for small contractors but rare at scale.
7. **Which government tenancy in the chosen primary suite?**
   The per-vendor file (`microsoft-365-gcc.md` or
   `google-workspace.md`) answers this with its Tenancy
   Selection section.

This is a decision process, not a ranking. No primary suite is
better for CUI in the abstract; each fits different contractor
circumstances.

---

## Cross-domain anchors

Productivity-suite posture composes with corpus cross-cutting
files and domain practice files:

- **FedRAMP framing.** `references/fedramp-gap.md` for FedRAMP
  program context, CSP SRG v1r1 reciprocity, and DFARS 7012
  CSP-equivalence mechanics.
- **Cloud-platform dependencies.** `references/modern-it/cloud-platforms/cloud-selection.md`
  for the cloud-platform selection that a productivity tenancy
  often sits adjacent to (M365 GCC High on Azure Government;
  Workspace on Google Cloud infrastructure; Atlassian Government
  Cloud on AWS; ServiceNow GCC on AWS GovCloud; Box for
  Government on AWS GovCloud).
- **Endpoint-plane interaction.** `references/modern-it/endpoints/windows-fleet.md`
  for the compact GCC-vs-GCC-High pointer (full decision tree
  in `microsoft-365-gcc.md` per Decision 5).
- **CUI scoping.** `references/scoping-and-cui.md` for the
  decision of what sits in CUI scope across the productivity
  surfaces.
- **SSP authoring.** `references/ssp-guidance.md` for how to
  document productivity-suite inheritance in the SSP.

Domain practice files used for requirement text and evidence
lists:

- Access Control (AC) — `references/domains/ac-access-control.md`
  for account management and remote access patterns.
- System and Communications Protection (SC) —
  `references/domains/sc-system-comms.md` for encryption and
  boundary protection.
- Configuration Management (CM) —
  `references/domains/cm-configuration-mgmt.md` for change
  control on productivity-suite feature rollouts.
- Media Protection (MP) — `references/domains/mp-media-protection.md`
  for retention and records.
- Audit and Accountability (AU) — `references/domains/au-audit.md`
  for audit logging.
- Identification and Authentication (IA) —
  `references/domains/ia-identification-auth.md` for identity
  and authentication posture.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/cloud-platforms/cloud-selection.md`,
`references/modern-it/endpoints/README.md`, or previous Phase 5
slices are not repeated here.

**Assured Controls Plus.** The Google Workspace CUI-capable
overlay (Enterprise Plus edition plus the Assured Controls Plus
add-on). Distinct from Assured Workloads (the Google Cloud
compliance overlay). Authorized independently; integrates via
identity federation, not tenant merge.

**Context-Aware Access.** The Google Workspace policy engine
that evaluates session context (user, device, location,
network) at access time and enforces policy outcomes.
Analogous in purpose to Microsoft Conditional Access.

**DLP (Data Loss Prevention).** Defined in
`references/modern-it/endpoints/README.md` "Terminology."
Used across all three vendor families in this directory; each
delivers it through different tooling.

**EAR (Export Administration Regulations).** Defined in
`references/modern-it/cloud-platforms/cloud-selection.md`
"Terminology." Relevant for productivity tenancy selection
when export-controlled data is present.

**IL4, IL5 (DoD Impact Level 4, Impact Level 5).** Defined in
`references/modern-it/cloud-platforms/cloud-selection.md`
"Terminology." In Phase 5d scope, IL4 is the typical landing
spot for Google Workspace Assured Controls Plus and ServiceNow
GCC; IL5 is the typical landing spot for Microsoft 365
GCC High.

**ITAR (International Traffic in Arms Regulations).** Defined
in `references/modern-it/endpoints/remote-work.md`
"Terminology." Interacts with productivity tenancy selection
when defense-article or defense-service technical data is
processed through the productivity suite.

**Data Center (Atlassian Data Center).** Atlassian's self-hosted
pattern for Jira, Confluence, and Jira Service Management. The
contractor hosts the software and owns the compliance posture;
Atlassian provides the license.

**EKM (External Key Manager).** Defined in
`references/modern-it/cloud-platforms/gcp-assured.md`; used
here for Workspace client-side encryption.

**Enterprise Plus (Google Workspace Enterprise Plus).** The
Google Workspace edition that carries Assured Controls Plus as
an available add-on for CUI workloads.

**GCC (Government Community Cloud).** Microsoft 365 tenancy at
FedRAMP Moderate plus DoD IL2.

**GCC High (Government Community Cloud High).** Microsoft 365
sovereign tenancy at FedRAMP High plus DoD IL5. Physically and
logically separate from commercial M365.

**ITSM (IT Service Management).** The operational discipline
and tooling category covering incident, change, request, and
problem management workflows.

**Purview (Microsoft Purview).** The Microsoft productivity
compliance tooling covering DLP, sensitivity labels, records
management, eDiscovery, and the Compliance Portal.

**Tailored (FedRAMP Tailored).** A FedRAMP baseline distinct
from Low, Moderate, and High, designed for low-risk SaaS where
the stored data is itself considered low-risk. GitHub Enterprise
Cloud operates under Tailored.

**Vault (Workspace Vault).** The Google Workspace eDiscovery
and retention tool.

---

## Versioning and drift

Productivity suites are the highest-drift content in this
corpus. Microsoft and Google ship features monthly; sometimes
weekly. Per-service FedRAMP authorization status changes on a
quarterly-or-faster cadence. Compliance center tooling (Purview,
Vault, Context-Aware Access) rebrands and restructures
repeatedly.

Per the verify-at-source-with-dated-stamp pattern:

- Tier-level claims (GCC High is FedRAMP High, Assured Controls
  Plus is IL4, ServiceNow GCC is IL4, Atlassian Government Cloud
  is FedRAMP Moderate, GitHub Enterprise Cloud is FedRAMP
  Tailored, Box for Government is FedRAMP High) are the stable
  anchors. This hub leans on these.
- Per-service authorization claims carry dated stamps inline in
  the per-vendor files. Each stamp reads "verified YYYY-MM-DD"
  with a pointer to the primary source.
- Feature-level claims (Purview DLP detects X, Sensitivity
  Labels auto-apply on Y condition, Vault retains Z) are
  scoped tightly and labeled "as of YYYY-MM, verify current
  vendor documentation before implementing."
- Vendor rebranding (Azure AD → Entra ID is a recent example;
  Chronicle → Google SecOps is another) may shift names; the
  underlying authorization and capability typically survive.
  Verify names at vendor documentation sites when citing in
  SSP authoring.

This hub's content is verified 2026-04-21. Next full
re-verification pass is scheduled for the corpus review cycle
or when any primary-suite vendor announces a tenancy-tier
restructuring (for example, a new IL-level authorization).
