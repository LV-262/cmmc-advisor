# FedRAMP Marketplace Practitioner Guide

> Source: FedRAMP program documentation (fedramp.gov); FedRAMP
> Marketplace (marketplace.fedramp.gov); FedRAMP PMO publications
> including the Agency Authorization and JAB Authorization
> process guides; CMMC Assessment Guide Level 2 (DoD CIO); DFARS
> 252.204-7012; 32 CFR Part 170 CMMC Program Final Rule (effective
> 2024-12-16); DoD CSP SRG v1r1 (public.cyber.mil) for IL
> reciprocity; NIST SP 800-53 control baselines for Low, Moderate,
> High. Vendor-specific authorization claims verified 2026-04-21
> against the vendor's public compliance page or a linked FedRAMP
> Marketplace package entry.

## Overview

This file is the practitioner guide to navigating the FedRAMP
Marketplace for CMMC-aligned tooling decisions. Two kinds of
guidance:

- **How to search the Marketplace yourself** — the authoritative
  source for FedRAMP authorization status is
  marketplace.fedramp.gov. This file teaches the practitioner
  query patterns that produce usable results rather than
  drowning in unfiltered listings.
- **Curated category short-lists** — representative vendors per
  capability category that are commonly authorized at FedRAMP
  Moderate or High. This is not a ranking and not an exhaustive
  catalog; it is a starting point for a contractor building a
  tool-evaluation short-list.

Read alongside `references/fedramp-gap.md` (FedRAMP program
framework, CSP SRG reciprocity, DFARS 7012 equivalence mechanics)
and `references/contractor-profiles.md` (tooling investment
sequencing per contractor size).

**The supply-side reality.** FedRAMP High supply is constrained.
Per industry reporting through 2025-2026, the pool of FedRAMP
High authorized vendors across some capability categories is
thin, creating procurement pressure on federal customers and
DIB contractors. This file notes where the gaps are so
contractors can plan realistic alternatives rather than assume
a FedRAMP-authorized option exists for every category they
need.

---

## Scope of this file

Covered:

- Search patterns and filters for marketplace.fedramp.gov.
- Curated category short-lists for ~10 capability areas where
  DIB contractors commonly need tooling: email security, file
  collaboration, SIEM, EDR/endpoint, vulnerability management,
  IAM/PAM, DLP, network security/SASE, backup and recovery, GRC.
- Coverage-gap analysis: categories where FedRAMP High supply is
  constrained and the industry is still building options.
- Sequencing recommendations: how to order tooling investment
  against CMMC assessment readiness.

Not covered:

- Specific vendor rankings. This file names representative
  vendors per category without claiming any vendor is the best
  or worst choice. Specific vendor selection depends on
  contractor-specific factors (existing architecture,
  operational capacity, price negotiation, feature requirements)
  outside this file's scope.
- Productivity-suite tooling. Microsoft 365 GCC High, Google
  Workspace Assured Controls Plus, Atlassian Government Cloud,
  ServiceNow GCC, Box for Government, GitHub Enterprise Cloud
  live in `references/modern-it/productivity/` per Phase 5d.
- AI service tooling. Bedrock GovCloud, Azure OpenAI Government,
  Vertex AI Assured Workloads, AI dev tools live in
  `references/modern-it/ai-services/` per Phase 5.
- Cloud IaaS/PaaS platforms. AWS GovCloud, Azure Government,
  Google Cloud Assured Workloads live in
  `references/modern-it/cloud-platforms/` per Phase 5c.
- Non-FedRAMP compliance frameworks (SOC 2, ISO 27001, HITRUST,
  StateRAMP, GovRAMP). A vendor may hold multiple
  authorizations; this file treats FedRAMP only and notes where
  StateRAMP or GovRAMP fill gaps FedRAMP does not.
- Point-in-time vendor pricing or feature specifics. These decay
  faster than this file can track.

---

## How to search the FedRAMP Marketplace

The Marketplace at marketplace.fedramp.gov is the authoritative
source. The page is a single-page application (SPA); browse
rather than deep-link for specific searches. Four practical
search patterns:

**1. Status filter.** Products carry one of several statuses.
Understanding the status progression prevents citing an
In-Process product as if it were authorized:

- **Authorized** — the product holds a current authorization
  (JAB P-ATO or Agency ATO) at the listed impact level. Safe to
  cite in an SSP.
- **In Process** — the product is actively pursuing
  authorization. Not authorized yet; not cite-safe.
- **Ready** — the product has completed the FedRAMP Ready
  milestone (meets technical readiness to pursue authorization)
  but does not yet have an authorization. Not cite-safe.
- **Retired** or **Not Authorized** — the product has exited
  the authorization track. Verify current status before any
  SSP reference.

Filter to Authorized only when building an SSP-cite-safe
short-list. Include In Process when building a
forward-looking roadmap aware of vendors expected to reach
Authorized within 6-18 months.

**2. Impact level filter.** Filter by Low, Moderate, High, or
Low-Impact SaaS (LI-SaaS, also called Tailored). For DIB
CUI work, Moderate is the floor per DFARS 7012 equivalence;
High is preferred for IL5 workloads. LI-SaaS is appropriate
only for low-risk SaaS where the data itself is low-risk (see
`references/modern-it/productivity/legacy-dib-tools.md` GitHub
Enterprise Cloud treatment for a canonical LI-SaaS case).

**3. Authorization type filter.** JAB P-ATO vs Agency ATO. JAB
P-ATO expands to Joint Authorization Board Provisional Authority
to Operate. The two routes are operationally equivalent for
contract-accepting purposes but reflect different authorization
paths:

- JAB P-ATO — the Joint Authorization Board (DoD, DHS, GSA CIOs)
  issues a provisional authorization that any federal agency
  can leverage.
- Agency ATO — a specific federal agency issues the ATO; other
  agencies may leverage under reciprocity or re-authorize for
  their own use.

**4. Keyword search.** The Marketplace search box handles
vendor name, product name, and some capability keywords. Search
is exact-ish, not fuzzy; "Splunk" returns Splunk packages but
"log analytics" returns fewer results than a Marketplace
browse-by-category approach would.

**Verification discipline for SSP citation.**

- Always cite the specific package entry (for example,
  "Splunk Cloud Platform - FedRAMP High P-ATO" rather than
  "Splunk FedRAMP") and include the dated verification stamp.
- The Marketplace lists authorization boundaries per package,
  not per feature. A vendor's umbrella FedRAMP authorization
  may not cover every feature in the product; verify the
  specific capability the contractor intends to use against the
  package scope documented in the CSP's System Security Plan or
  the Marketplace package entry.
- Authorization status changes on a weeks-to-months cadence.
  Re-verify before any SSP citation; do not cite authorization
  status from memory or from an older market-intel document.

---

## Curated category short-lists

Ten capability categories where DIB contractors commonly need
tooling. Each category lists representative FedRAMP-authorized
or widely-known-to-be-in-scope vendors as of 2026-04-21. These
are starting points for a tool-evaluation short-list; specific
selection depends on contractor architecture and operational
constraints.

**Verification note.** Every vendor entry below should be
verified against marketplace.fedramp.gov for current package
scope before SSP citation. Authorization status, impact level,
and covered features can change between this file's
verification date and the contractor's procurement decision.

### Email and messaging security

**In scope for this category.** Email security gateway (spam and
phishing filtering beyond the productivity suite's native
capability); email encryption for external exchange; secure
messaging for cross-organization CUI-containing communications.

**Representative vendors.**

- Microsoft Defender for Office 365 (bundled with M365 GCC High;
  inherits GCC High FedRAMP High + IL5 authorization).
- Google Workspace native security (Gmail spam/phishing
  protection inherits Workspace Assured Controls Plus
  FedRAMP High authorization).
- Proofpoint for Government — FedRAMP authorized per vendor
  trust page; verify current impact level and package scope.
- Mimecast for Government — FedRAMP authorization roadmap has
  shifted over the years; verify current status at
  marketplace.fedramp.gov.

**Gap note.** Third-party email security for CUI-carrying
contractors beyond the primary suite's native tooling is a
thin market at FedRAMP High. Contractors routinely use the
primary suite's native capability and layer third-party only
where specific capability (advanced phishing simulation,
BEC-specific detection) requires it.

### File collaboration and transfer

**In scope.** File collaboration beyond the primary productivity
suite; managed file transfer for external CUI exchange.

**Representative vendors.**

- Box for Government — FedRAMP High authorized per
  `references/modern-it/productivity/legacy-dib-tools.md`.
- Egnyte for Government — FedRAMP authorization status varies
  by package; verify current scope.
- Axway / Globalscape / Kiteworks — MFT (Managed File Transfer)
  platforms with FedRAMP packages; verify specific package
  scope for CUI-handling workflows.
- Accellion / KiteworksLegacy — retired or transitioned
  offerings; verify current status before citing.

**Gap note.** File collaboration is well-covered at FedRAMP
Moderate; High is thinner. Primary-suite-native file storage
(SharePoint Online in GCC High, Drive in Workspace ACP) plus
Box for Government covers most DIB contractor needs.

### SIEM and log analytics

**In scope.** Security Information and Event Management
platforms; log aggregation and analytics; UEBA.

**Representative vendors.**

- Microsoft Sentinel — inherits Azure Government authorization;
  FedRAMP High + IL4/IL5 in Azure Government scope.
- Splunk Cloud Platform — FedRAMP High P-ATO achieved 2024 per
  Splunk press release (splunk.com/en_us/newsroom/press-
  releases/2024/splunk-cloud-platform-attains-fedramp-high-
  authorization.html). Verify current package scope.
- Google Chronicle / Google SecOps — inherits Google Cloud
  Assured Workloads; verify specific FedRAMP package scope.
- Elastic — FedRAMP authorization via Elastic Cloud on AWS
  GovCloud; verify current package.
- Rapid7 InsightIDR — FedRAMP authorization; verify current
  impact level.
- LogRhythm — FedRAMP authorization package; verify current
  status.

**Gap note.** SIEM at FedRAMP High is better-supplied than some
adjacent categories; the constraint is often integration
complexity rather than authorization availability.

### Endpoint protection (EDR / XDR)

**In scope.** Endpoint Detection and Response; Extended
Detection and Response; endpoint antivirus and antimalware
deployed on CUI-adjacent endpoints.

**Representative vendors.**

- Microsoft Defender for Endpoint — bundled with M365 GCC High
  and Azure Government; inherits FedRAMP High + IL5.
- CrowdStrike Falcon — FedRAMP authorization per CrowdStrike
  government trust documentation; verify current package scope
  (FedRAMP Moderate and High variants exist for different
  products in the Falcon suite).
- SentinelOne — FedRAMP authorized; verify current package and
  impact level at marketplace.fedramp.gov.
- Palo Alto Networks Cortex XDR — FedRAMP authorization
  coverage is partial across the Cortex product family;
  verify per-product scope.
- Trellix (formerly McAfee Enterprise + FireEye) — FedRAMP
  authorization on specific products; verify current.
- Tanium — FedRAMP authorized per vendor documentation;
  verify current scope.

**Gap note.** EDR at FedRAMP High is a known supply-constrained
category. Several major EDR vendors hold Moderate but not High;
contractors needing High EDR may find the market narrower than
expected.

### Vulnerability management

**In scope.** Vulnerability scanning (credentialed and
network); configuration-drift detection; asset inventory.

**Representative vendors.**

- Tenable (Tenable.io, Tenable.sc) — FedRAMP authorization per
  Tenable government pages; verify current package scope.
- Qualys — FedRAMP authorization via Qualys Cloud Platform;
  verify current impact level.
- Rapid7 (InsightVM, InsightAppSec) — FedRAMP authorization
  per vendor documentation.

**Gap note.** Core three vendors (Tenable, Qualys, Rapid7)
dominate the FedRAMP vulnerability management market.
Specialized tooling (cloud workload scanning, container
scanning) has a narrower FedRAMP-authorized supply.

### Identity and access management (IAM / PAM)

**In scope.** Workforce identity (workforce IdP, federation);
privileged access management; multi-factor authentication;
identity governance.

**Representative vendors.**

- Microsoft Entra ID Government — bundled with Azure Government
  and M365 GCC High; FedRAMP High + IL5.
- Google Cloud Identity (Workspace ACP) — inherits Workspace
  Assured Controls Plus authorization.
- Okta for US Government — FedRAMP Moderate and High variants
  at different package scopes; verify current.
- Ping Identity for Government — FedRAMP authorization per
  vendor page; verify current.
- CyberArk — FedRAMP authorization on the Privilege Cloud
  product; verify current scope.
- BeyondTrust — FedRAMP authorization on multiple products
  including the October 2025 Identity Security Insights
  extension (beyondtrust.com/press/fedramp-identity-security-
  insights).
- Saviynt — FedRAMP authorization; verify current package.

**Gap note.** IAM/PAM at FedRAMP High is generally
well-supplied, but specific feature gaps exist (for example,
specific IGA automation workflows, specific PAM just-in-time
patterns) that the major vendors handle differently per
authorization scope.

### DLP and data governance

**In scope.** Data Loss Prevention beyond the primary
productivity suite's native DLP; data classification and
labeling; data governance for CUI-marked content.

**Representative vendors.**

- Microsoft Purview — bundled with M365 GCC High; inherits GCC
  High authorization.
- Google Workspace DLP / Drive DLP — inherits Workspace ACP
  authorization.
- Proofpoint DLP — FedRAMP authorization via Proofpoint for
  Government; verify current package.
- Forcepoint DLP — FedRAMP authorization; verify current.
- Symantec / Broadcom DLP — FedRAMP authorization on specific
  products; verify current scope.
- Netskope Cloud Firewall + DLP — FedRAMP authorization via
  Netskope Federal; verify current package.

**Gap note.** Primary-suite-native DLP (Purview, Workspace DLP)
covers most DIB contractor scenarios. Third-party DLP is
typically layered for specific capability (endpoint-DLP on
mixed-OS fleets, network-DLP for cross-suite exfiltration
detection) where the native tooling is insufficient.

### Network security, SASE, and ZTNA

**In scope.** Secure Access Service Edge; Zero Trust Network
Access; cloud firewall; secure web gateway; CASB.

**Representative vendors.**

- Zscaler for Government — FedRAMP High authorization;
  verify current package scope at marketplace.fedramp.gov.
- Netskope Federal — FedRAMP authorization; verify current
  impact level.
- Palo Alto Networks Prisma Access — FedRAMP authorization on
  specific products; verify current.
- Cisco Umbrella for Government — FedRAMP authorization.
- Cloudflare Zero Trust for US Government — FedRAMP
  authorization; verify current package scope.
- Microsoft Entra Private Access / Internet Access — bundled
  with Azure Government for certain configurations; verify
  current availability in the government tenancy.

**Gap note.** SASE/ZTNA at FedRAMP High is a growing-but-
constrained supply. Contractors standing up zero-trust
architecture routinely combine FedRAMP-authorized SASE with
the primary suite's native identity-plane rather than
single-vendor sourcing.

### Backup and recovery

**In scope.** Backup platforms for CUI-containing systems;
immutable backup; disaster recovery orchestration.

**Representative vendors.**

- AWS Backup / Azure Backup / Google Cloud Backup — inherit
  their respective cloud platform authorizations.
- Rubrik — FedRAMP authorization on specific products; verify
  current package.
- Cohesity — FedRAMP authorization; verify current scope.
- Veeam — FedRAMP authorization status varies; verify current.
- Commvault — FedRAMP authorization; verify current package.

**Gap note.** Cloud-native backup (AWS/Azure/GCP) dominates
FedRAMP-authorized backup for cloud workloads. Third-party
backup adds value for hybrid or on-premises workloads where
cloud-native backup does not reach.

### GRC and compliance automation

**In scope.** Governance, Risk, Compliance platforms; policy
management; control assessment automation; evidence
collection.

**Representative vendors.**

- ServiceNow GRC on ServiceNow GCC — inherits ServiceNow GCC
  FedRAMP High + IL4 authorization (see
  `references/modern-it/productivity/legacy-dib-tools.md`).
- RSA Archer — FedRAMP authorization on RSA Archer on the
  RSA-managed government platform; verify current.
- MetricStream — FedRAMP authorization; verify current scope.
- Vanta, Drata, Secureframe, Hyperproof — SOC 2 / ISO 27001
  focused platforms with varying FedRAMP authorization
  coverage; verify current status at marketplace.fedramp.gov
  for each.

**Gap note.** GRC at FedRAMP High is supplied primarily through
the ServiceNow GCC / RSA Archer / MetricStream enterprise
tier. Automation-first platforms (Vanta, Drata, Secureframe,
Hyperproof) have historically targeted SOC 2 and ISO 27001
compliance; FedRAMP authorization coverage is case-by-case.

### Secure file transfer and data exchange

**In scope.** Managed File Transfer; secure drop-box-style
external exchange; data-exchange workflows with government
customers.

**Representative vendors.**

- Box for Government — file exchange use case (covered under
  File collaboration above).
- AWS Transfer Family in AWS GovCloud — inherits GovCloud
  authorization.
- Axway SecureTransport — FedRAMP authorization; verify
  current.
- IBM Sterling Secure File Transfer — FedRAMP authorization
  per specific package; verify current.
- Kiteworks (successor offering to Accellion) — FedRAMP
  authorization status has evolved; verify current.

**Gap note.** Legacy MFT products (Accellion, legacy Ipswitch)
have retired or transitioned; current-generation vendors
(Kiteworks, Axway, IBM Sterling) hold active packages but
coverage at High is narrower than at Moderate.

---

## Coverage-gap analysis

FedRAMP coverage is uneven across capability categories. A
contractor planning tooling investment should understand where
the market is thin so alternative strategies (dual-vendor
sourcing, in-house augmentation, acceptance of Moderate where
High is unavailable) can be built into the plan rather than
discovered mid-procurement.

**High-supply categories (FedRAMP Authorized vendors are
plentiful).**

- Cloud IaaS (AWS GovCloud, Azure Government, Google Cloud
  Assured Workloads)
- Primary productivity suite (M365 GCC High, Workspace ACP)
- SIEM at Moderate (Sentinel, Splunk, Chronicle, Elastic)
- Vulnerability management (Tenable, Qualys, Rapid7)
- Identity at Moderate (Okta, Ping, Entra)

**Medium-supply categories (multiple vendors, authorization
coverage uneven across features).**

- EDR / XDR — mid-tier vendors carry Moderate, fewer carry High.
- DLP — primary-suite-native dominates; third-party DLP
  authorization coverage is uneven.
- GRC — ServiceNow GCC plus a handful of enterprise platforms;
  mid-market GRC tooling is thinner.
- SASE / ZTNA — a growing but still-constrained market.

**Thin-supply categories (contractors routinely accept
Moderate or layer tooling rather than single-source High).**

- EDR at FedRAMP High — known constraint; major EDR vendors
  hold Moderate, fewer hold High. MeriTalk and industry
  analysis through 2025-2026 framed this as the "FedRAMP High
  supply crisis."
- Secure file transfer at High — Kiteworks and a few others;
  legacy MFT retired without equal-tier replacement.
- Specialized categories — cloud workload scanning, container
  runtime security, API security, data-in-motion encryption
  for specific protocols — often have no FedRAMP High option;
  contractors use Moderate or self-hosted.

**Categories with no FedRAMP coverage (contractors self-host
or accept the gap).**

- AI developer tools at the tool-vendor service layer —
  covered in `references/modern-it/ai-services/ai-dev-tools.md`;
  most dev tools are not FedRAMP-authorized at the control-
  plane layer even when the model backend is.
- Specialized compliance-automation tooling — some
  FedRAMP-authorized, others only SOC 2 or StateRAMP.
- Developer-experience tooling (Gitpod, Codespaces commercial,
  many CI/CD SaaS) — covered in modern-IT files; gap is
  architectural, not imminent.

**What the gap story means for the contractor.**

- Build tooling investment plans against FedRAMP reality, not
  against a wished-for catalog. A category with no FedRAMP High
  option requires a different architecture decision
  (self-hosting, acceptance at Moderate with agency agreement,
  feature substitution).
- StateRAMP and GovRAMP (formerly StateRAMP) fill some gaps for
  state government work but do not substitute for FedRAMP in
  DFARS 7012 equivalence. Do not cite StateRAMP as FedRAMP
  equivalent in a CMMC SSP.
- Vendor claims of "FedRAMP compliance" without a Marketplace
  package entry are marketing, not authorization. Verify
  against marketplace.fedramp.gov; accept no substitute.

---

## Compliance coverage recommendations

Tooling investment sequencing for CMMC assessment readiness.
Ordering below is a practitioner-typical sequence; specific
contractor architecture may reorder.

**First investment: scoping and inheritance.**

- CUI scope determination via `references/scoping-and-cui.md`.
- Inheritance map: which FedRAMP-authorized cloud platform and
  primary productivity tenancy the contractor will rely on.
  The platform and primary-suite tenancy establish the
  authorization baseline that subsequent tooling rides on.

**Second investment: identity and audit.**

- Primary-suite identity plane (Entra ID Government, Cloud
  Identity) provides MFA, conditional access, and federation.
- SIEM or log analytics platform inherits audit logs from
  every other tool. Investing here early pays compounding
  returns.

**Third investment: endpoint and vulnerability.**

- EDR on CUI-adjacent endpoints (primary-suite-native or
  FedRAMP-authorized third party per category availability).
- Vulnerability management for CUI systems.

**Fourth investment: DLP and data governance.**

- Primary-suite-native DLP (Purview, Workspace DLP) first;
  add third-party DLP only where gaps appear.
- Sensitivity labels / classification framework aligned to
  `references/scoping-and-cui.md` CUI categories.

**Fifth investment: backup, GRC, and specialized tooling.**

- Backup per contractor architecture (cloud-native or
  hybrid).
- GRC platform investment scales with contractor size; see
  `references/contractor-profiles.md` for sizing guidance.
- Specialized tooling (SASE/ZTNA, MFT, IAM/PAM extensions) as
  CUI architecture demands.

**Do not.**

- Invest in tooling before CUI scope is determined. Tooling
  follows scope, not the other way around.
- Single-source GRC automation as a substitute for CMMC
  preparation. GRC tooling accelerates evidence collection
  and control tracking; it does not substitute for
  understanding the control requirements.
- Cite a vendor's FedRAMP authorization in an SSP without
  verifying the specific package scope at
  marketplace.fedramp.gov.

---

## Cross-domain anchors

Marketplace navigation composes with corpus cross-cutting
files:

- **FedRAMP program framing.** `references/fedramp-gap.md` for
  FedRAMP program context, CSP SRG v1r1 reciprocity, DFARS 7012
  equivalence mechanics, and FedRAMP-to-IL crosswalk.
- **CUI scoping.** `references/scoping-and-cui.md` for the
  upstream determination that drives tooling requirements.
- **Levels and assessment.** `references/levels-and-assessment.md`
  for L1 vs L2 determination that scopes tooling depth.
- **SSP authoring.** `references/ssp-guidance.md` for citing
  FedRAMP-authorized tooling in the SSP.
- **POA&M management.** `references/poam-management.md` for
  Conditional Certification tooling-gap handling.
- **Contractor profiles.** `references/contractor-profiles.md`
  for sizing tooling investment by contractor profile.
- **Modern IT: productivity.**
  `references/modern-it/productivity/README.md` for the primary-
  suite layer that dominates contractor tooling.
- **Modern IT: cloud platforms.**
  `references/modern-it/cloud-platforms/cloud-selection.md` for
  the IaaS/PaaS authorization underlying all third-party
  tooling.
- **Modern IT: AI services.**
  `references/modern-it/ai-services/README.md` for AI-service
  tooling (out of this file's scope but referenced for
  completeness).

Domain practice files at `references/domains/` reference
FedRAMP-authorized tooling for specific control implementation
guidance; this guide is the cross-reference directory for
category-level selection.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/fedramp-gap.md`,
`references/modern-it/cloud-platforms/cloud-selection.md`, or
previous Phase 5 slices are not repeated here.

**BEC (Business Email Compromise).** A category of email-based
attack where a threat actor impersonates a business principal
to induce wire transfers or sensitive-data disclosure. Used in
evaluating email-security tooling capabilities.

**CASB (Cloud Access Security Broker).** A SaaS-access
security control point typically colocated with SASE or ZTNA
tooling.

**EDR (Endpoint Detection and Response).** Endpoint security
tooling that detects and responds to threats beyond
traditional antivirus.

**IGA (Identity Governance and Administration).** The
discipline and tooling around lifecycle management,
access-review cycles, and entitlement governance. Typically
overlaps with IAM but emphasizes governance rather than
authentication.

**LI-SaaS (Low-Impact SaaS).** FedRAMP Tailored baseline for
low-risk SaaS systems; see `references/modern-it/productivity/legacy-dib-tools.md`
GitHub Enterprise Cloud section for the canonical case.

**MFT (Managed File Transfer).** Secure, auditable
file-exchange platforms for cross-organization file transfer.
Distinct from ad-hoc file-share tools.

**PAM (Privileged Access Management).** Identity tooling
focused on privileged-account credential management, session
recording, and just-in-time access.

**SASE (Secure Access Service Edge).** A cloud-delivered
security service combining network security, zero-trust
access, and SaaS security into an integrated service.

**StateRAMP / GovRAMP.** A state-government-focused
authorization framework inspired by FedRAMP but distinct from
it. Rebranded circa 2023-2024 (stateramp.org now redirects to
govramp.org; StateRAMP retained as the dba). Not a FedRAMP
substitute for DFARS 7012 equivalence in CMMC SSPs.

**UEBA (User and Entity Behavior Analytics).** Machine-
learning-driven anomaly detection typically layered on SIEM
telemetry.

**XDR (Extended Detection and Response).** A category
evolving from EDR that integrates endpoint, network, and
cloud telemetry into a unified detection-and-response
capability.

**ZTNA (Zero Trust Network Access).** Identity- and context-
aware access control replacing perimeter-based VPN for
workforce access to internal applications.

---

## Versioning and drift

FedRAMP Marketplace content drifts faster than any other
content in this corpus outside AI services. Vendor
authorization status changes weekly; new packages land, old
packages retire, impact-level upgrades happen, and the
Marketplace UI itself updates.

Per hub Versioning discipline:

- Vendor-specific claims in this file carry dated verification
  (2026-04-21). Re-verify against marketplace.fedramp.gov
  before citing in an SSP.
- Category-level supply analysis (which categories are
  well-supplied, which are thin) is more stable than specific
  vendor claims but still updates quarterly; re-verify at the
  corpus review cycle.
- FedRAMP program structural changes (FedRAMP 20x / Revision
  process updates, new impact levels, process changes) shift
  the framework below this guide. Monitor fedramp.gov for
  program-level announcements.
- Vendor rebranding and acquisitions happen on a months cadence
  (Accellion to Kiteworks; McAfee Enterprise + FireEye to
  Trellix; others ongoing). Specific vendor names in this file
  reflect 2026-04 state; the category framing survives
  rebrands.

A deeper automated approach for tracking Marketplace state is
tracked as a follow-up (`dev-w1ez` FedRAMP Marketplace snapshot
+ refresh, P3 backlog) — a JSON data file plus refresh script
for the Phase 5d/5 corpus's named vendors with dated
verification stamps. When it ships, this file's vendor-specific
claims migrate to cite the snapshot as the stable reference.

Content verified 2026-04-21 against the cited primary sources.
Next full re-verification at the corpus review cycle or when
FedRAMP program structure changes materially.
