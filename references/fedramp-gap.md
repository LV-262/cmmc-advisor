# FedRAMP Gap Analysis

> Source: Federal Risk and Authorization Management Program (FedRAMP)
> program documentation (fedramp.gov); NIST SP 800-53 Rev 5; DFARS
> 252.204-7012 (Safeguarding Covered Defense Information and Cyber
> Incident Reporting, DFARS Change 2025-11-10); FedRAMP Rev 5 transition
> materials; FedRAMP 2025 program update (fedramp.gov/2025-03-24).

## Overview

Defense contractors working through CMMC almost always hit a second
set of cybersecurity rules alongside it: FedRAMP authorization
requirements on the cloud services they use or provide. The two
regimes overlap heavily on technical controls (FIPS-validated
cryptography, multi-factor authentication, boundary protection, audit
logging) and diverge sharply on governance: continuous monitoring
cadence, incident reporting destinations, System Security Plan (SSP)
template depth, who issues the authorization, and what the
authorization actually means.

This file exists to make the relationship explicit. A contractor who
treats CMMC and FedRAMP as independent regimes ends up building two
compliance programs that share 70% of their technical controls but
never cite each other. A contractor who treats them as the same regime
misses the places where FedRAMP demands more than CMMC (and vice
versa).

**The one decision every contractor needs to make first.** If you
store, process, or transmit Controlled Unclassified Information (CUI)
in an external cloud service, the cloud service provider must hold a
FedRAMP Moderate authorization or be deemed "equivalent" to that
baseline by your contracting officer. This is the requirement set by
Defense Federal Acquisition Regulation Supplement (DFARS) clause
252.204-7012, paragraph (b)(2)(ii)(D). The clause text appears below.

This file is a hub. Detailed content lives in dedicated sections
authored incrementally: the CMMC-to-FedRAMP control crosswalk, the
places where FedRAMP exceeds CMMC, the places where CMMC plus DFARS
exceed FedRAMP, and the cross-references into individual practice
files. What appears here first is the baseline decision itself, the
terminology, and the scope boundary against the rest of the corpus.
See "Scope and Sections" near the end of this file for the full map.

---

## FedRAMP at a Glance

### What FedRAMP is

FedRAMP is the federal program that standardizes how cloud services
are assessed, authorized, and continuously monitored for use by
federal agencies. A cloud provider seeking to sell services to the
U.S. Government obtains a FedRAMP authorization once and can then
serve multiple agencies under that single authorization rather than
re-proving compliance per contract.

The program is operated by the FedRAMP Program Management Office
(PMO), housed at the General Services Administration. The PMO
maintains the baselines, the templates, the marketplace of authorized
services, and the transition plans between revisions.

### Current baseline (as of April 2026)

**NIST SP 800-53 Revision 5 is the FedRAMP baseline.** FedRAMP
baselines were approved for Rev 5 on May 29, 2023. All new FedRAMP
authorizations use Rev 5; existing Rev 4 authorizations have been
migrating under a phased transition plan. Rev 4 persists only for
legacy packages still in the transition window.

CMMC and FedRAMP cite different NIST documents. CMMC safeguarding is
built on NIST SP 800-171 Revision 2, a targeted subset adapted for
nonfederal systems handling CUI. FedRAMP is built on NIST SP 800-53
Revision 5, the full federal control catalog. Both families live
under the same NIST Risk Management Framework umbrella, but the
catalogs are not identical. A CMMC-to-FedRAMP crosswalk maps 171
practices to 53 controls and is therefore a subset-to-superset
mapping, not a one-to-one alignment. See `references/rev3-transition.md`
for the current CMMC safeguarding baseline status and the Rev 3
outlook.

> Source: FedRAMP, "Rev. 5 Baselines Have Been Approved and Released"
> (fedramp.gov/archive/2023-05-30-rev-5-baselines-have-been-approved-and-released/).

### Current authorization pathway

As of the March 2025 FedRAMP program update, **Agency Authorization is
the sole active path** to FedRAMP authorization. The Joint
Authorization Board (JAB) Provisional Authority to Operate (P-ATO)
pathway is no longer being issued for new authorizations. FedRAMP is
developing an additional authorization pathway called FedRAMP 20x for
cloud-native automated authorization. As of April 2026, FedRAMP 20x
remains in staged pilot development and does not replace the Rev 5
Agency Authorization process. Verify current status at fedramp.gov
before citing.

> Source: FedRAMP, "FedRAMP in 2025"
> (fedramp.gov/2025-03-24-FedRAMP-in-2025/), quoted: "The existing
> Agency Authorization path based on FedRAMP Rev. 5 baselines is the
> sole active path to FedRAMP authorization. No changes to this path
> are planned at this time."

A cloud service provider pursuing FedRAMP in 2026 finds a federal
agency willing to sponsor the authorization, engages a
FedRAMP-accredited Third-Party Assessment Organization (3PAO) to
perform the independent assessment, and receives from that sponsoring
agency an Authorization to Operate (ATO). The ATO is then published
in the FedRAMP Marketplace and becomes available for reuse by other
federal agencies.

### Key actors

**FedRAMP PMO.** The GSA-housed program office that maintains program
documentation, the Marketplace, and the Rev 5 baselines.

**3PAO.** Third-Party Assessment Organization, accredited to perform
independent FedRAMP security assessments. A 3PAO produces the Security
Assessment Report that feeds the agency authorization decision.

**Agency Authorizing Official (AO).** The sponsoring federal agency
official who reviews the 3PAO's assessment and issues the ATO.

**Cloud Service Provider (CSP).** The vendor whose offering is being
authorized. The CSP owns the System Security Plan, operates the
system, and performs ongoing continuous monitoring (ConMon).

---

## Impact Levels

FedRAMP categorizes authorizations by the impact of a confidentiality,
integrity, or availability compromise to the federal workload served.
Three impact levels exist: Low, Moderate, and High. **For CUI, the
operative level is Moderate.** Low is insufficient; High exceeds the
7012 requirement.

### FedRAMP Low

The Low baseline is designed for public-facing federal information
that has low confidentiality, integrity, and availability impact.
Public informational websites and similar low-sensitivity federal
workloads fit here.

**For CMMC contractors holding CUI, Low is not sufficient.** The
DFARS 252.204-7012(b)(2)(ii)(D) clause names Moderate specifically. A
CSP with only a Low ATO cannot be the cloud environment where CUI
flows.

### FedRAMP Moderate

The Moderate baseline is the operative target for most CUI workloads.
Federal agency systems that process sensitive-but-unclassified data
most commonly authorize at Moderate. Defense contractors hosting CUI
in an external cloud service must use a CSP at Moderate or higher, or
satisfy the "equivalent to Moderate" path described below.

### FedRAMP High

The High baseline covers federal workloads where a compromise would
cause severe or catastrophic harm. Law enforcement, emergency
services, financial systems, and some defense workloads authorize at
High. For most CMMC Level 2 contractor stacks, High is beyond what
DFARS 252.204-7012 requires, though some defense cloud environments
(for example, Microsoft Azure Government workloads designated Impact
Level 5 or Impact Level 6) run on High-authorized infrastructure. A
contractor who finds their CSP is authorized at High inherits stronger
controls than the 7012 baseline demands; this is not a compliance
problem but it does affect cost and operational complexity.

### Relationship to DoD Cloud Computing Security Requirements Guide

The DoD Cloud Computing Security Requirements Guide (CC SRG) defines
Impact Levels (IL2, IL4, IL5, IL6) that sit on top of FedRAMP impact
levels for DoD-specific workloads. IL4 and IL5 require FedRAMP
Moderate plus additional DoD controls; IL6 requires FedRAMP High plus
classified-adjacent handling. Most CMMC Level 2 contractors operate
against FedRAMP Moderate baselines; IL4/IL5 considerations arise for
contractors handling specific categories of defense CUI such as
Controlled Technical Information at certain distribution levels.

Detailed IL4/IL5 content is out of scope for this file and belongs
in a future DoD-specific reference not yet authored in this corpus.
This file treats FedRAMP as the authorization framework; the DoD
overlay is a separate layer.

---

## The CUI Baseline Decision

The core regulatory anchor for every CMMC contractor's FedRAMP
decision is a single clause in DFARS 252.204-7012.

### DFARS 252.204-7012(b)(2)(ii)(D), verbatim

> "If the Contractor intends to use an external cloud service provider
> to store, process, or transmit any covered defense information in
> performance of this contract, the Contractor shall require and ensure
> that the cloud service provider meets security requirements
> equivalent to those established by the Government for the Federal
> Risk and Authorization Management Program (FedRAMP) Moderate baseline
> (https://www.fedramp.gov/documents-templates/) and that the cloud
> service provider complies with requirements in paragraphs (c) through
> (g) of this clause for cyber incident reporting, malicious software,
> media preservation and protection, access to additional information
> and equipment necessary for forensic analysis, and cyber incident
> damage assessment."

> Source: DFARS 252.204-7012, paragraph (b)(2)(ii)(D), effective DFARS
> Change 2025-11-10. Available at acquisition.gov/dfars/252.204-7012.

### What this clause actually requires

1. **Scope trigger.** The clause applies when the contractor uses an
   external cloud service to store, process, or transmit covered
   defense information. "Covered defense information" is DFARS
   terminology for CUI under a DFARS contract, plus certain other
   controlled information categories defined in the clause at
   paragraph (a). See `references/scoping-and-cui.md` for the CUI
   definition and boundary implications.

2. **Baseline requirement.** The CSP must meet security requirements
   equivalent to FedRAMP Moderate. Two paths satisfy this:
   - The CSP holds a FedRAMP Moderate (or higher) authorization in
     the FedRAMP Marketplace.
   - The CSP is deemed by the contractor (and accepted by the
     contracting officer) to meet equivalent security requirements
     under DoD's published FedRAMP Moderate Equivalency guidance.

3. **Flowdown.** The contractor carries the obligation. If the CSP
   does not hold a FedRAMP ATO, the contractor must still ensure and
   document equivalence, including (per DoD guidance on
   equivalency) a 3PAO assessment against the FedRAMP Moderate
   baseline and a body of evidence equivalent to a FedRAMP package.

### FedRAMP Moderate Equivalency

The "equivalent to" phrase in (b)(2)(ii)(D) created a parallel path
that DoD has since narrowed through published guidance. As of the
DoD Chief Information Officer memorandum on FedRAMP Moderate
Equivalency (December 2023), equivalence means an independent
assessment against the same Moderate baseline and contracting
officer acceptance. It is not a lower bar.

Detailed equivalency mechanics (3PAO role, body of evidence,
contracting officer acceptance workflow) and the rest of DFARS
252.204-7012 (the 72-hour DoD Cyber Crime Center reporting
obligation, the DFARS 252.204-7019 and 252.204-7020 Supplier
Performance Risk System (SPRS) scoring assessment, the DFARS
252.204-7021 CMMC certification requirement) are treated in the
"CMMC and DFARS Excesses Over FedRAMP" section below once that
section lands.

---

## Scope and Sections

This file is a hub for FedRAMP-related content across the corpus.
Sections are authored incrementally; the project issue tracker carries
current status for sections still pending.

**Overview and Baseline Definitions.** This section. Defines FedRAMP,
names Rev 5 as the current baseline, and states the Moderate CUI
requirement.

**CMMC to FedRAMP Moderate Overlap Crosswalk.** Maps each of the 110
CMMC Level 2 practices (which includes the 17 CMMC Level 1 practices
as a subset) to its corresponding NIST SP 800-53 Rev 5 control or
control set, with substantive treatment of the families where the
mapping is tightest: FIPS-validated cryptography, multi-factor
authentication, boundary protection, audit logging, access control,
and incident response.

**FedRAMP Excesses Over CMMC.** Names the places where FedRAMP
demands more than CMMC: continuous monitoring cadence, US-CERT
(United States Computer Emergency Readiness Team, now operated
within the Cybersecurity and Infrastructure Security Agency)
incident reporting, SSP template depth, supply-chain controls added
in Rev 5, and the privacy overlay where applicable.

**CMMC and DFARS Excesses Over FedRAMP.** Treats DFARS 252.204-7012
full scope, DFARS 252.204-7019 and 252.204-7020 SPRS assessment
methodology, DFARS 252.204-7021 CMMC certification requirement, and
the C3PAO (CMMC Third-Party Assessment Organization) versus 3PAO
distinction.

**Cross-References into Domain Files.** Single-sentence pointers
from each relevant practice file back to this file. Wiring only; no
substantive content duplication.

Cross-file references from this hub into existing Phase 4 content:

- CUI definition and boundary: `references/scoping-and-cui.md`
- SSP structure and cadence: `references/ssp-guidance.md`
- POA&M mechanics and 180-day closeout: `references/poam-management.md`
- Assessment and certification levels: `references/levels-and-assessment.md`

Content that does not belong in this file:

- Detailed CUI handling rules. Those live in
  `references/scoping-and-cui.md`.
- Detailed SSP format. That lives in `references/ssp-guidance.md`,
  with the FedRAMP template-depth comparison added below in the
  "FedRAMP Excesses Over CMMC" section once that section lands.
- DoD Impact Level (IL4, IL5, IL6) content beyond the Moderate/High
  relationship. Belongs in future DoD-specific references.
- Product or vendor recommendations. The FedRAMP Marketplace is the
  authoritative product registry; this skill will not duplicate it.

---

## Terminology

Acronyms and terms used across this file and its dependent slices.
Grouped for orientation; all terms used above or in downstream slices
are glossed here for reference.

### Authorization

**ATO (Authorization to Operate).** The formal authorization decision
issued by a federal agency's Authorizing Official permitting a cloud
service to handle federal data at a given impact level.

**JAB P-ATO (Joint Authorization Board Provisional Authority to
Operate).** A legacy FedRAMP authorization pathway no longer being
issued for new authorizations as of the 2025 program update.

**3PAO (Third-Party Assessment Organization).** FedRAMP-accredited
independent assessor that produces the Security Assessment Report
feeding an Agency ATO decision.

**C3PAO (CMMC Third-Party Assessment Organization).** The CMMC
program's equivalent of a FedRAMP 3PAO. Treated in the "CMMC and
DFARS Excesses Over FedRAMP" section.

**PMO (Program Management Office).** The GSA-housed FedRAMP program
office.

### Programs and frameworks

**FedRAMP (Federal Risk and Authorization Management Program).** The
federal cloud authorization program.

**DFARS (Defense Federal Acquisition Regulation Supplement).** The
DoD supplement to the Federal Acquisition Regulation that carries the
cybersecurity clauses defense contractors operate under.

**SPRS (Supplier Performance Risk System).** The DoD system where
contractor 800-171 Basic Assessment scores are recorded under DFARS
252.204-7019 and 252.204-7020. Treated in the "CMMC and DFARS
Excesses Over FedRAMP" section.

### Information categories

**CUI (Controlled Unclassified Information).** The information
category that triggers CMMC Level 2 and DFARS 252.204-7012
safeguarding. Defined in `references/scoping-and-cui.md`.

**FCI (Federal Contract Information).** The broader information
category that triggers CMMC Level 1 obligations. Defined in
`references/scoping-and-cui.md`.

### Operational concepts

**CSP (Cloud Service Provider).** The vendor offering a cloud service
subject to FedRAMP authorization.

**ConMon (Continuous Monitoring).** The ongoing program of
vulnerability scanning, assessment, and POA&M maintenance that
FedRAMP requires post-ATO. Treated in the "FedRAMP Excesses Over
CMMC" section.

**SSP (System Security Plan).** The document describing how a system
implements each required control. See `references/ssp-guidance.md`.

**US-CERT (United States Computer Emergency Readiness Team).** The
historical federal incident-reporting channel, now operated within
the Cybersecurity and Infrastructure Security Agency. Referenced in
the "FedRAMP Excesses Over CMMC" section for incident-reporting
cadence.

