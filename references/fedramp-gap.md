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
252.204-7012 (the 72-hour DIBNet incident reporting obligation,
the DC3 malware-submission path, the DFARS 252.204-7019 and
252.204-7020 Supplier Performance Risk System (SPRS) scoring
assessment, the DFARS 252.204-7021 CMMC certification requirement)
are treated in the "CMMC and DFARS Excesses Over FedRAMP" section
below once that section lands.

---

## CMMC to FedRAMP Moderate Overlap Crosswalk

The baseline decision above says Moderate is the floor for CUI.
This section maps each of the 110 CMMC practices to the NIST SP
800-53 controls that implement the same intent. A contractor
working with a FedRAMP Moderate CSP can point to the CSP's
implementation of these controls as inherited implementation
evidence for the corresponding CMMC practices, subject to the
inheritance caveats below.

### How to read this crosswalk

**Source of record.** The per-practice mappings below come from
NIST SP 800-171 Revision 2, Appendix D (Mapping Tables D-1 through
D-14). Appendix D is the canonical 171-to-53 mapping published by
NIST. Its cross-references target NIST SP 800-53 Revision 4, per
the Appendix D cautionary footnote: "The security controls in
Tables D-1 through D-14 are taken from NIST Special Publication
800-53, Revision 4." This file reproduces the Appendix D mapping.

**Note on the withdrawn parent document.** NIST SP 800-171 Rev 2
was withdrawn on May 14, 2024, and superseded by Rev 3. It
remains enforceable for CMMC because DoD's class deviation keeps
Rev 2 as the operative standard for DFARS contracts. See
`references/rev3-transition.md` for the transition status and the
conditions under which Rev 3 would become enforceable.

**Rev 4 to Rev 5 translation.** FedRAMP moved to Rev 5 in May 2023;
contractors evaluating a FedRAMP Moderate CSP today are reading a
Rev 5 package. Control identifiers (AC-2, SC-7, IA-2, and so on)
persist between Rev 4 and Rev 5 in nearly all cases for the
families cited in this crosswalk. Specific deltas that affect the
crosswalk are flagged in the tables and in the "Rev 4 baseline and
Rev 5 translation notes" section at the end.

**What "maps to" means.** A mapping says the 800-53 control
addresses the same protection objective as the CMMC practice. It
does not guarantee the control as implemented in a given CSP
satisfies the CMMC practice word-for-word. Assessment still
requires checking that the CSP's implementation covers the CMMC
requirement's scope, not just shares a control number. Inheritance
treatment is discussed below.

**What "no direct mapping" means in Appendix D's ISO column.** Some
cells in Appendix D show "No direct mapping" under the ISO/IEC
27001 column. This crosswalk focuses on the 800-53 side only.
ISO/IEC 27001 mappings are preserved in the Appendix D source for
contractors with an Information Security Management System (ISMS)
already in place; they are out of scope here.

**Pre-existing paraphrase drift.** Some CMMC practice text in this
corpus uses Rev 1 "information system" phrasing where Rev 2
canonical uses "system." Those drifts are tracked as bd follow-ups
and do not affect the cross-practice control mapping, which is
authoritative regardless of paraphrase wording.

### The 110-practice crosswalk

#### Access Control (AC) — 22 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| AC.L1-3.1.1 | AC-2, AC-3, AC-17 | Authorized access control |
| AC.L1-3.1.2 | AC-2, AC-3, AC-17 | Transaction and function control (shares AC-2/3/17 with 3.1.1) |
| AC.L2-3.1.3 | AC-4 | Information flow enforcement (CUI flow) |
| AC.L2-3.1.4 | AC-5 | Separation of duties |
| AC.L2-3.1.5 | AC-6, AC-6(1), AC-6(5) | Least privilege |
| AC.L2-3.1.6 | AC-6(2) | Non-privileged account use |
| AC.L2-3.1.7 | AC-6(9), AC-6(10) | Privileged function logging and prohibition |
| AC.L2-3.1.8 | AC-7 | Unsuccessful logon attempts |
| AC.L2-3.1.9 | AC-8 | System use notification |
| AC.L2-3.1.10 | AC-11, AC-11(1) | Session lock with pattern-hiding |
| AC.L2-3.1.11 | AC-12 | Session termination |
| AC.L2-3.1.12 | AC-17(1) | Remote access monitoring |
| AC.L2-3.1.13 | AC-17(2) | Remote access encryption |
| AC.L2-3.1.14 | AC-17(3) | Remote access routing |
| AC.L2-3.1.15 | AC-17(4) | Privileged remote access |
| AC.L2-3.1.16 | AC-18 | Wireless access authorization |
| AC.L2-3.1.17 | AC-18(1) | Wireless authentication and encryption |
| AC.L2-3.1.18 | AC-19 | Mobile device connection control |
| AC.L2-3.1.19 | AC-19(5) | Mobile device encryption |
| AC.L1-3.1.20 | AC-20, AC-20(1) | External system connections |
| AC.L2-3.1.21 | AC-20(2) | Portable storage on external systems |
| AC.L1-3.1.22 | AC-22 | Publicly accessible content |

#### Awareness and Training (AT) — 3 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| AT.L2-3.2.1 | AT-2, AT-3 | General security awareness |
| AT.L2-3.2.2 | AT-2, AT-3 | Role-based training (shares AT-2/3 with 3.2.1) |
| AT.L2-3.2.3 | AT-2(2) | Insider-threat training |

#### Audit and Accountability (AU) — 9 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| AU.L2-3.3.1 | AU-2, AU-3, AU-3(1), AU-6, AU-11, AU-12 | Audit log creation and retention |
| AU.L2-3.3.2 | AU-2, AU-3, AU-3(1), AU-6, AU-11, AU-12 | User traceability (shares anchors with 3.3.1) |
| AU.L2-3.3.3 | AU-2(3) | Event review and update |
| AU.L2-3.3.4 | AU-5 | Audit logging failure alerting |
| AU.L2-3.3.5 | AU-6(3) | Audit correlation |
| AU.L2-3.3.6 | AU-7 | Audit reduction and reporting |
| AU.L2-3.3.7 | AU-8, AU-8(1) | Time stamps with authoritative source |
| AU.L2-3.3.8 | AU-9 | Audit information protection |
| AU.L2-3.3.9 | AU-9(4) | Audit management by privileged users |

#### Security Assessment (CA) — 4 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| CA.L2-3.12.1 | CA-2 | Periodic security assessment |
| CA.L2-3.12.2 | CA-5 | Plan of action and milestones |
| CA.L2-3.12.3 | CA-7 | Continuous monitoring |
| CA.L2-3.12.4 | PL-2 | System security plan (mapped from PL family) |

#### Configuration Management (CM) — 9 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| CM.L2-3.4.1 | CM-2, CM-6, CM-8, CM-8(1) | Baseline configuration and inventory |
| CM.L2-3.4.2 | CM-2, CM-6, CM-8, CM-8(1) | Configuration enforcement (shares anchors) |
| CM.L2-3.4.3 | CM-3 | Change control |
| CM.L2-3.4.4 | CM-4 | Security impact analysis |
| CM.L2-3.4.5 | CM-5 | Access restrictions for change |
| CM.L2-3.4.6 | CM-7 | Least functionality |
| CM.L2-3.4.7 | CM-7(1), CM-7(2) | Nonessential function restriction |
| CM.L2-3.4.8 | CM-7(4), CM-7(5) | Application execution policy |
| CM.L2-3.4.9 | CM-11 | User-installed software |

#### Identification and Authentication (IA) — 11 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| IA.L1-3.5.1 | IA-2, IA-3, IA-5 | Identify system users |
| IA.L1-3.5.2 | IA-2, IA-3, IA-5 | Authenticate users (shares anchors) |
| IA.L2-3.5.3 | IA-2(1), IA-2(2), IA-2(3) | Multi-factor authentication |
| IA.L2-3.5.4 | IA-2(8), IA-2(9) | Replay-resistant authentication. See Rev 5 notes. |
| IA.L2-3.5.5 | IA-4 | Identifier reuse prevention |
| IA.L2-3.5.6 | IA-4 | Identifier disabling |
| IA.L2-3.5.7 | IA-5(1) | Password complexity |
| IA.L2-3.5.8 | IA-5(1) | Password reuse prevention (shares IA-5(1)) |
| IA.L2-3.5.9 | IA-5(1) | Temporary passwords (shares IA-5(1)) |
| IA.L2-3.5.10 | IA-5(1) | Cryptographic password protection (shares IA-5(1)) |
| IA.L2-3.5.11 | IA-6 | Obscured feedback |

#### Incident Response (IR) — 3 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| IR.L2-3.6.1 | IR-2, IR-4, IR-5, IR-6, IR-7 | Incident handling capability |
| IR.L2-3.6.2 | IR-2, IR-4, IR-5, IR-6, IR-7 | Incident tracking (shares anchors) |
| IR.L2-3.6.3 | IR-3 | Incident response testing |

#### Maintenance (MA) — 6 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| MA.L2-3.7.1 | MA-2, MA-3, MA-3(1), MA-3(2) | Perform maintenance |
| MA.L2-3.7.2 | MA-2, MA-3, MA-3(1), MA-3(2) | Maintenance controls (shares anchors) |
| MA.L2-3.7.3 | MA-2 | Sanitize equipment before off-site maintenance |
| MA.L2-3.7.4 | MA-3(2) | Check diagnostic media for malicious code |
| MA.L2-3.7.5 | MA-4 | MFA for nonlocal maintenance |
| MA.L2-3.7.6 | MA-5 | Supervise maintenance personnel |

#### Media Protection (MP) — 9 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| MP.L2-3.8.1 | MP-2, MP-4, MP-6 | Protect system media |
| MP.L2-3.8.2 | MP-2, MP-4, MP-6 | Limit media access (shares anchors) |
| MP.L1-3.8.3 | MP-2, MP-4, MP-6 | Sanitize before disposal (shares anchors) |
| MP.L2-3.8.4 | MP-3 | Media marking |
| MP.L2-3.8.5 | MP-5 | Media transport |
| MP.L2-3.8.6 | MP-5(4) | Cryptographic protection in transport |
| MP.L2-3.8.7 | MP-7 | Removable media use |
| MP.L2-3.8.8 | MP-7(1) | Prohibit unowned portable storage |
| MP.L2-3.8.9 | CP-9 | Backup CUI confidentiality. CP-9 is the Contingency Planning family control folded into MP in Appendix D. |

#### Personnel Security (PS) — 2 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| PS.L2-3.9.1 | PS-3, PS-4, PS-5 | Screen individuals before access |
| PS.L2-3.9.2 | PS-3, PS-4, PS-5 | Personnel actions protection (shares anchors) |

#### Physical Protection (PE) — 6 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| PE.L1-3.10.1 | PE-2, PE-4, PE-5, PE-6 | Limit physical access |
| PE.L2-3.10.2 | PE-2, PE-4, PE-5, PE-6 | Monitor physical facility (shares anchors) |
| PE.L1-3.10.3 | PE-3 | Escort visitors |
| PE.L1-3.10.4 | PE-3 | Physical access logs (shares PE-3) |
| PE.L1-3.10.5 | PE-3 | Physical access devices (shares PE-3) |
| PE.L2-3.10.6 | PE-17 | Alternate work site safeguards |

#### Risk Assessment (RA) — 3 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| RA.L2-3.11.1 | RA-3 | Periodic risk assessment |
| RA.L2-3.11.2 | RA-5, RA-5(5) | Vulnerability scanning with privileged access |
| RA.L2-3.11.3 | RA-5 | Vulnerability remediation |

#### System and Communications Protection (SC) — 16 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| SC.L1-3.13.1 | SC-7 | Boundary protection |
| SC.L2-3.13.2 | SA-8 | Security engineering principles. SA-8 is the System and Services Acquisition family control folded into SC in Appendix D. |
| SC.L2-3.13.3 | SC-2 | Application partitioning |
| SC.L2-3.13.4 | SC-4 | Shared resource information protection |
| SC.L1-3.13.5 | SC-7 | Public access system separation (shares SC-7) |
| SC.L2-3.13.6 | SC-7(5) | Deny by default, allow by exception |
| SC.L2-3.13.7 | SC-7(7) | Split tunneling prevention |
| SC.L2-3.13.8 | SC-8, SC-8(1) | Transmission confidentiality and integrity |
| SC.L2-3.13.9 | SC-10 | Network disconnect |
| SC.L2-3.13.10 | SC-12 | Cryptographic key management |
| SC.L2-3.13.11 | SC-13 | FIPS-validated cryptography |
| SC.L2-3.13.12 | SC-15 | Collaborative computing device control |
| SC.L2-3.13.13 | SC-18 | Mobile code control |
| SC.L2-3.13.14 | SC-19 | Voice over IP (VoIP) control |
| SC.L2-3.13.15 | SC-23 | Session authenticity |
| SC.L2-3.13.16 | SC-28 | Protection of information at rest |

#### System and Information Integrity (SI) — 7 practices

| CMMC Practice | 800-53 Controls | Notes |
|---------------|------------------|-------|
| SI.L1-3.14.1 | SI-2, SI-3, SI-5 | Flaw remediation |
| SI.L1-3.14.2 | SI-2, SI-3, SI-5 | Malicious code protection (shares anchors) |
| SI.L2-3.14.3 | SI-2, SI-3, SI-5 | Security alerts and advisories (shares anchors) |
| SI.L1-3.14.4 | SI-3 | Update malicious code mechanisms |
| SI.L1-3.14.5 | SI-3 | Periodic and real-time scanning (shares SI-3) |
| SI.L2-3.14.6 | SI-4, SI-4(4) | System monitoring inbound and outbound |
| SI.L2-3.14.7 | SI-4 | Unauthorized use detection |

### Where the mapping is tightest

Six families concentrate the highest-value overlap between CMMC and
FedRAMP Moderate. A contractor choosing a FedRAMP Moderate CSP gets
the tightest inheritance coverage in these areas, and an assessor
reviewing inherited-control evidence spends the most time here.

#### FIPS-validated cryptography

**CMMC anchor.** SC.L2-3.13.11 requires FIPS-validated cryptography
when used to protect CUI confidentiality. Related practices:
SC.L2-3.13.8 (transmission confidentiality and integrity),
SC.L2-3.13.10 (cryptographic key management), SC.L2-3.13.16
(protection of information at rest).

**FedRAMP anchor.** SC-13 (Cryptographic Protection) is the direct
FedRAMP Moderate control. SC-8 and SC-8(1) cover the transmission
side; SC-28 covers at-rest protection; SC-12 covers key management.

**What the contractor inherits.** A FedRAMP Moderate CSP running on
FIPS-validated cryptographic modules, authorizing against SC-13
with a CMVP (Cryptographic Module Validation Program) certificate
referenced in their SSP, gives a contractor most of what
SC.L2-3.13.11 demands. The remaining responsibility is contractor-
side: use only the approved modules (avoid configuring the CSP to
operate in a non-FIPS mode), document which CSP SKU or edition
provides the FIPS boundary (commercial editions often lack it),
and verify module certificate status on the NIST CMVP validated
modules list rather than trusting marketing claims.

**Where it gets missed.** The most common gap is configuration
drift. A CSP tenant is spun up in a mode that falls back to
non-validated cryptography for interoperability with legacy
clients. The FedRAMP authorization still stands, but the tenant
is outside the FIPS boundary. The "FedRAMP Excesses Over CMMC"
section treats the ConMon cadence that catches this class of
drift once that section lands.

#### Multi-factor authentication

**CMMC anchor.** IA.L2-3.5.3 requires MFA for local and network
access to privileged accounts and for network access to non-
privileged accounts. IA.L2-3.5.4 requires replay-resistant
authentication for the same scopes.

**FedRAMP anchor.** IA-2(1), IA-2(2), IA-2(3) cover MFA for
privileged and non-privileged network and local access. IA-2(8)
and IA-2(9) cover replay resistance.

**Rev 4 to Rev 5 delta.** IA-2(8) was not in the Rev 4 Moderate
baseline. NIST SP 800-171 Rev 2 Appendix D flags this explicitly
(footnote 33, page 70): "IA-2(8) is not currently in the NIST
Special Publication 800-53 moderate security control baseline
although it will be added to the baseline in the next update.
Employing multifactor authentication without a replay-resistant
capability for non-privileged accounts creates a significant
vulnerability for systems transmitting CUI." Rev 5 closed this
gap: IA-2(8) is in the Rev 5 Moderate baseline. A FedRAMP Moderate
CSP authorized under Rev 5 inherits replay resistance for privileged
accounts directly; the contractor verifies the equivalent on the
non-privileged side.

**Where it gets missed.** SMS-based second factors. NIST SP
800-63B deprecates one-time passwords sent over SMS for
Authenticator Assurance Level 2 (AAL2) and above, because of
SIM-swap and SS7-intercept attacks. A FedRAMP Moderate CSP that
offers SMS as an MFA option is not out of compliance with IA-2
per se, but a contractor using SMS exclusively to satisfy
IA.L2-3.5.3 is making an assessor's objection hunt easy. Prefer
phishing-resistant factors: FIDO2 or WebAuthn security keys,
derived-credential Personal Identity Verification (PIV-D) tokens,
or authenticator apps.

#### Boundary protection

**CMMC anchor.** SC.L1-3.13.1 requires monitoring, controlling, and
protecting communications at the external boundaries and key
internal boundaries. SC.L1-3.13.5 requires subnet separation for
publicly accessible components. SC.L2-3.13.6 (deny by default)
and SC.L2-3.13.7 (split tunneling prevention) extend the boundary
controls.

**FedRAMP anchor.** SC-7 (Boundary Protection) is the core control,
with SC-7(5) for deny-by-default and SC-7(7) for split-tunneling
prevention.

**What the contractor inherits.** A FedRAMP Moderate CSP
implements SC-7 at the cloud infrastructure boundary (the tenant
or Virtual Private Cloud (VPC) edge). The contractor's
responsibility is the boundary they define around their system
footprint inside the tenancy: which subnets are public, which are
CUI-bearing, how ingress and egress are controlled, how split
tunneling is prevented on endpoint VPNs connecting into the
tenancy. The CSP's SC-7 implementation is necessary but not
sufficient.

**Where it gets missed.** Assuming the CSP's VPC or tenancy
boundary is the CUI boundary. For most architectures it is not.
The CUI boundary is wherever CUI lives, which may be a subset of
the cloud footprint (an enclave) or a superset (if CUI also sits
on-prem or on endpoints). The FedRAMP authorization boundary is
the CSP's concern; the CUI boundary is the contractor's and must
be separately documented in the SSP.

#### Audit and accountability

**CMMC anchor.** AU.L2-3.3.1 and AU.L2-3.3.2 require creating,
retaining, and reviewing audit logs that make user activity
traceable. AU.L2-3.3.5 requires correlating audit-review processes
to support investigation of indications of unlawful, unauthorized,
suspicious, or unusual activity.

**FedRAMP anchor.** AU-2 (event selection), AU-3 (content of audit
records), AU-3(1) (additional audit information), AU-6 (audit
review and analysis), AU-6(3) (correlation), AU-11 (retention),
AU-12 (generation).

**What the contractor inherits.** FedRAMP Moderate CSPs ship with a
well-instrumented audit-logging substrate at the infrastructure
level: control-plane API calls, authentication events, resource
changes. The contractor responsibility is application-level and
user-level audit inside the tenancy: who logged into the CUI
application, what they accessed, what changes they made. Neither
substrate is optional.

**Where it gets missed.** Log exports that decorrelate. The CSP
keeps audit logs in its own storage under its retention policy.
Contractors typically export selected logs to a
Security Information and Event Management (SIEM) platform. Between
export frequency, filtering decisions, and time-sync drift, the
contractor's view of user activity may diverge from what the CSP
actually recorded. AU.L2-3.3.5 correlation requires these to
reconcile. See `references/domains/au-audit.md` for the
AU-family domain details.

#### Access control

**CMMC anchor.** AC.L1-3.1.1 and AC.L1-3.1.2 require limiting
system access and transaction types to authorized users. AC.L1-3.1.20
addresses external system connections; AC.L1-3.1.22 addresses
publicly accessible content. The L2 practices cover the full
depth: least privilege, session management, remote access,
wireless, mobile.

**FedRAMP anchor.** AC-2 (Account Management), AC-3 (Access
Enforcement), AC-17 (Remote Access) are the three workhorse
controls shared by AC.L1-3.1.1 and AC.L1-3.1.2.

**What the contractor inherits.** FedRAMP Moderate CSPs operate AC-2
identity lifecycle tooling and AC-3 policy enforcement points at
the cloud-control-plane level. For a contractor using the CSP's
identity provider (IdP) as the primary IdP, AC-2 inheritance is
substantial. For a contractor federating a separate corporate IdP,
inheritance is thinner and the contractor owns more of the AC-2
implementation evidence.

**Where it gets missed.** Privileged-access accounts. The CSP's
AC-2 covers tenant-level accounts, but many contractors still run
privileged operations through shared break-glass accounts that the
CSP does not see. AC.L2-3.1.5 (least privilege) and AC.L2-3.1.7
(privileged function logging) live on the contractor side almost
entirely for these accounts.

#### Incident response

**CMMC anchor.** IR.L2-3.6.1 requires an operational incident-
handling capability covering preparation, detection, analysis,
containment, recovery, and user response. IR.L2-3.6.2 requires
tracking, documenting, and reporting incidents to designated
officials and authorities. IR.L2-3.6.3 requires testing the IR
capability.

**FedRAMP anchor.** IR-2 (training), IR-4 (handling), IR-5
(monitoring), IR-6 (reporting), IR-7 (assistance), IR-3 (testing).

**What the contractor inherits.** FedRAMP Moderate CSPs maintain their
own IR programs for incidents at the infrastructure layer and
coordinate with customers for tenant-affecting events. Contractors
inherit the CSP's incident-detection capability for underlying
platform events and layer their own IR on top for tenant-level
and application-level events. The contractor's IR program must
ingest CSP notifications and integrate them into the contractor's
own IR workflow.

**Where it gets missed.** Reporting destinations and timelines. A
FedRAMP CSP reports certain classes of incidents to the agency
authorizing official and to US-CERT per FedRAMP IR guidance. A CMMC
contractor under DFARS 252.204-7012 reports cyber incidents to DoD
via DIBNet within 72 hours, and separately submits any isolated
malware samples to DC3 under paragraph (d). These are different
destinations with different triggers. A joint incident may require
reporting on both tracks with different content requirements. The
"FedRAMP Excesses Over CMMC" section below treats the ConMon and
US-CERT reporting cadence; the "CMMC and DFARS Excesses Over
FedRAMP" section treats the 7012 reporting mechanics. Contractors
should pre-map the reporting destinations by incident class, not
improvise during an incident.

### Inherited vs shared-responsibility controls

**Scope note.** The taxonomy below is FedRAMP-specific: it covers
how a CMMC contractor inherits controls from a FedRAMP-authorized
CSP. General SSP narrative patterns for documenting any inherited
or shared control (FedRAMP or otherwise) live in
`references/ssp-guidance.md`. This section names the categories;
that file owns the "how to write it in the SSP" guidance.

A FedRAMP Moderate CSP does not relieve a contractor of
responsibility for every control above. The inheritance model has
three categories:

**Fully inherited.** The CSP operates the control; the contractor
points to the CSP's ATO and uses it as implementing evidence. Most
physical protection (PE), environmental, and infrastructure
controls fall here. A contractor hosting exclusively on a FedRAMP
Moderate CSP typically inherits PE.L1-3.10.1 and PE.L1-3.10.3
through PE.L1-3.10.5 fully (the CSP operates the data center).
PE.L2-3.10.6 (alternate work site) is contractor-side because the
alternate work site is the contractor's office.

**Shared responsibility.** The CSP provides the capability; the
contractor configures and uses it. AC-2, AC-3, AU-2, AU-3, SC-7,
SC-13 are all shared. The CSP builds the tooling; the contractor
decides which accounts to provision, what to audit, what the
boundary looks like, which cryptographic modules to enable. An
assessor asks both sides: "Is the CSP capability authorized at
Moderate?" (check the FedRAMP Marketplace) and "Does the
contractor's configuration meet the CMMC practice?" (check the
contractor's SSP).

**Contractor responsibility.** The CSP does not operate the
control in any meaningful sense. Personnel security (PS), awareness
training (AT), incident response on the contractor side (IR), and
much of risk assessment (RA) are contractor-owned regardless of
cloud posture. A FedRAMP Moderate CSP does not screen the
contractor's employees, does not train them on CUI handling, and
does not write the contractor's POA&M.

**Documenting inheritance in the SSP.** Every CMMC practice the
contractor claims as inherited must point to the specific CSP
service, the specific FedRAMP control(s) being inherited, and the
date of the CSP's current ATO. "Our cloud provider has FedRAMP" is
not a substitute for naming the control and evidencing the scope.
See `references/ssp-guidance.md` for SSP narrative patterns.

### Rev 4 baseline and Rev 5 translation notes

Appendix D of NIST SP 800-171 Rev 2 maps to NIST SP 800-53 Rev 4
(per its cautionary footnote cited above). FedRAMP moved to Rev 5
in 2023. The practical consequences:

**Control ID continuity.** AC-2, AC-3, AC-17, AU-2, AU-3, CM-6,
IA-2, IA-5, IR-4, IR-6, MP-6, PE-2, PE-3, PS-3, PS-4, PS-5, RA-5,
SC-7, SC-8, SC-12, SC-13, SI-2, SI-3, SI-4, and most other
controls cited in the tables retain their identifiers between Rev
4 and Rev 5. A Rev 5 FedRAMP Moderate package cites the same
control numbers.

**Specific deltas that matter.** IA-2(8) replay resistance for
non-privileged accounts was not in Rev 4 Moderate (Appendix D
footnote 33); Rev 5 Moderate includes it. CM-7(5) allowlisting
was restricted to High in Rev 4 (Appendix D footnote 32); Rev 5
treats allowlisting more permissively across baselines, and
contractors using CM-7(5) should confirm the CSP's Rev 5
authorization reflects this.

**New Rev 5 families.** Two new families appear in Rev 5:
SR (Supply Chain Risk Management) and
PT (Personally Identifiable Information Processing and Transparency).
Neither appears in the 171-to-53 crosswalk because 171 predates
them. Both become relevant in the "FedRAMP Excesses Over CMMC"
section below.

**Authoritative Rev 4 to Rev 5 translation.** The authoritative
mapping lives in NIST SP 800-53 Revision 5, Appendix C ("Mapping
Tables") and in the csrc.nist.gov Control Catalog spreadsheet. A
contractor tracking specific Rev 4 to Rev 5 deltas should consult
those sources directly; this file presents the 171-to-53 mapping
at the level FedRAMP assessors typically evaluate.

**CMMC Rev 3 durability.** If CMMC adopts NIST SP 800-171 Revision
3 and the DoD class deviation ends (see
`references/rev3-transition.md` for current status), this
crosswalk requires full reauthoring rather than delta patches. Rev
3 restructures the 171-to-53 relationship substantially: dropped
practices, renumbered practices, the elimination of the Basic
versus Derived distinction. Readers tracking that transition
should treat this crosswalk as a snapshot of the Rev 2 era.

---

## FedRAMP Excesses Over CMMC

The crosswalk above shows where CMMC and FedRAMP Moderate align. A
contractor using a FedRAMP Moderate CSP inherits substantial control
coverage. But alignment is not equivalence: FedRAMP carries several
obligations that go meaningfully beyond what CMMC Level 2 requires.

This section names those excesses. A contractor reading an inherited
FedRAMP Moderate control as satisfying a CMMC practice is usually
correct; a contractor reading the same control as equivalent to the
full FedRAMP program is not. The CSP's FedRAMP package carries
monthly scan reports, 1-hour incident reporting obligations to the
Cybersecurity and Infrastructure Security Agency (CISA), a system
security plan format with seventeen-plus appendices, and (in Rev 5)
new control families the contractor's 800-171 baseline does not name
at all. None of these flow down to the contractor automatically, but
all of them shape how the CSP operates the infrastructure the
contractor relies on.

### Continuous monitoring cadence

CMMC Level 2 assessments are conducted on a **three-year cycle**
under 32 CFR Part 170. A certified CMMC assessment runs every three
years, with annual self-affirmations between assessments. Between
formal assessments, the contractor maintains their program through
internal reviews, POA&M maintenance, and ongoing evidence collection.
The cadence floor is annual; the external validation floor is
triennial.

FedRAMP continuous monitoring (ConMon) runs on a **monthly cycle**
with an **annual 3PAO subset assessment**. This cadence reflects
the Rev 5 Agency Authorization pathway. FedRAMP 20x (in staged
pilot as of April 2026, per the "FedRAMP at a Glance" section
above) may alter the ConMon cadence for CSPs on that pathway;
verify against the CSP's specific authorization package. For
Rev 5 Agency Authorization specifically:

**Monthly.** CSPs submit an updated POA&M, an up-to-date inventory,
and raw vulnerability scan files (when required by agency
agreement) to the FedRAMP secure repository. Vulnerability scans
cover operating systems, web applications, and databases for all
externally accessible components; FedRAMP recommends 100% coverage
of externally accessible system components, with any sampling
methodology requiring strong justification.

**Monthly vulnerability scanning.** The 30-day scan window is
anchored to NIST SP 800-53 control RA-5, with FedRAMP-specific
guidance in the FedRAMP Vulnerability Scanning Requirements. For
containerized components, the 30-day window begins at production
registry deployment; only images scanned within the window are
actively deployed.

**Annual.** A FedRAMP-accredited 3PAO performs an assessment of a
subset of the overall controls implemented on the system. This is
not a full reassessment (that happens on the three-year FedRAMP
reauthorization cycle), but it is a substantive independent check
on a rotating subset of controls each year.

> Source: FedRAMP Documentation, "Continuous Monitoring Overview"
> (fedramp.gov/docs/rev5/playbook/csp/continuous-monitoring/) and
> "Vulnerability Scanning"
> (fedramp.gov/docs/rev5/playbook/csp/continuous-monitoring/vulnerability-scanning/).

**What this means for the contractor.** A contractor using a
FedRAMP Moderate CSP inherits the CSP's ConMon program for the
infrastructure layer: monthly scanning of the CSP's operating
systems, web apps, and databases is happening regardless of the
contractor's own cadence. What the contractor still owes, and what
CMMC still requires, is vulnerability scanning of the contractor's
own layer: applications the contractor builds on top of the CSP,
endpoints connecting into the tenancy, on-premises components of
the CUI boundary. CMMC practice RA.L2-3.11.2 (vulnerability
scanning) does not specify a cadence; FedRAMP ConMon effectively
sets a monthly floor for the CSP's portion of the stack, but the
contractor-side cadence is a scoping decision.

### Incident reporting cadence

This is where the two regimes diverge most sharply. CMMC and DFARS
route incident reports to DoD; FedRAMP routes to CISA. The triggers,
timing, and destinations are different, and a contractor whose CSP
is FedRAMP-authorized and who is subject to DFARS 252.204-7012 owes
**both** sets of reports when a single incident affects both
surfaces.

**FedRAMP CSP reporting to CISA: 1 hour.** A CSP must report to the
Cybersecurity and Infrastructure Security Agency (CISA) within 1
hour of incident identification when the incident is confirmed,
suspected, or yet-to-be-confirmed as stemming from an attack vector
listed in CISA's Federal Incident Notification Guidelines. The
report goes through the CISA Incident Reporting System.

**FedRAMP CSP reporting to customers, FedRAMP, and agency AO: 1
hour.** The same 1-hour window applies to notifying affected agency
customers via the FedRAMP Secure Repository, notifying FedRAMP at
the fedramp_security@gsa.gov address, and notifying the agency
Authorizing Official's designated points of contact.

**Daily updates.** After initial notification, CSPs provide daily
updates to all parties (FedRAMP, CISA when applicable, all agency
customers) until recovery is complete.

**Final post-incident report.** After completing the Post-Incident
Activity phase, the CSP provides a comprehensive report describing
what occurred, root cause, response actions, lessons learned, and
required changes. The Agency AO reviews this report and may
establish corrective action plans.

> Source: FedRAMP Documentation, "Incident Communication"
> (fedramp.gov/docs/rev5/playbook/csp/continuous-monitoring/incident-communication/).
> CISA trigger list: Federal Incident Notification Guidelines
> (cisa.gov/federal-incident-notification-guidelines).

**CMMC contractor reporting via DIBNet: 72 hours.** DFARS
252.204-7012 paragraph (c)(1)(ii) requires the contractor to
rapidly report cyber incidents affecting covered defense
information to DoD through the
DIBNet (Defense Industrial Base Network) portal at dibnet.dod.mil.
"Rapidly report" is defined in paragraph (a) as within 72 hours
of discovery.

**DC3 is a separate recipient for malware samples.** Per DFARS
252.204-7012 paragraph (d), contractors who discover and isolate
malicious software during a reported incident submit the malware
to the DC3 (DoD Cyber Crime Center). This is a separate submission
from the (c)(1)(ii) incident report. The clause states explicitly:
"Do not send the malicious software to the Contracting Officer."
See `references/domains/ir-incident-response.md` for the full
IR.L2-3.6.2 narrative and `references/evidence-collection.md` for
evidence preservation requirements.

**Joint-reporting scenarios.** An incident affecting both a FedRAMP
CSP and a DoD contractor using that CSP for CUI may trigger all of:
the CSP's 1-hour CISA report, the CSP's 1-hour notifications to the
contractor and agency AO, and the contractor's 72-hour DIBNet
filing. These are independent obligations with independent content
requirements. A CSP's CISA filing does not discharge the
contractor's DIBNet filing, and the contractor's DIBNet filing does
not discharge the CSP's CISA obligation. Both tracks must run.

**Pre-mapping is the mitigation.** Neither clock is friendly to
improvisation. Contractors with any FedRAMP-authorized CSP handling
CUI should have the reporting decision tree written down, with
named owners for each track, before an incident. The "CMMC and
DFARS Excesses Over FedRAMP" section below treats the DFARS
reporting mechanics in more depth.

### System Security Plan depth

The FedRAMP SSP is a substantially more elaborate document than
what CMMC requires for the nonfederal side.

**FedRAMP SSP structure.** The template uses a single document
shared across impact levels with a baseline-specific appendix. The
body covers FIPS 199 categorization, service model, deployment
model, system function description, system architecture,
authorization boundary, data flows, interconnections, leveraged
external services, and cryptographic module use. As of the Rev 5
SSP template (April 2026), the template includes Section 8
"Illustrated Architecture and Narratives" and appendices labeled
A through Q (seventeen appendices total). Template structure is
subject to change; verify against the current template on
fedramp.gov/rev5/documents-templates/.

**Per-control depth.** Every control cited in the baseline has
three required sections in the SSP appendix: Control Requirement,
Control Summary Information, and Control Implementation Statement.
The Moderate baseline carries 300-plus controls. The per-control
depth multiplied across the baseline is the reason FedRAMP SSPs run
to hundreds of pages.

**CMMC SSP guidance.** The skill's `references/ssp-guidance.md`
treats the contractor-side SSP: per-practice implementation
narrative, boundary documentation, evidence pointers. The CMMC SSP
is lighter than the FedRAMP SSP in both per-control depth and
structural framing, reflecting 800-171's role as a tailored subset
rather than a full federal catalog. This is not a gap in CMMC; it
is a deliberate scope choice that matches the 110-practice
safeguarding baseline.

**What this means for the contractor.** A contractor whose CSP
carries a FedRAMP Moderate SSP does not inherit a completed SSP.
The contractor must still write their own SSP for the contractor's
system boundary, and the contractor's SSP references (but does not
reproduce) the CSP's FedRAMP package via inherited-control
attribution. See
`references/ssp-guidance.md` for the CMMC SSP pattern and the
"Inherited vs shared-responsibility controls" section above for
the attribution model.

> Source: FedRAMP Documentation, "System Security Plan (SSP)"
> (fedramp.gov/docs/rev5/playbook/csp/authorization/ssp/); FedRAMP
> Rev 5 Documents and Templates (fedramp.gov/rev5/documents-templates/).

### Supply chain (SR family) — new in Rev 5

NIST SP 800-53 Revision 5 added the
SR (Supply Chain Risk Management) family as a new control family,
integrating SCRM concepts throughout the catalog. The SR family
did not exist in Rev 4. FedRAMP Rev 5 Moderate includes a subset
of SR controls.

**What the SR family covers.** Controls in the SR family address
supply-chain risk across the system lifecycle: supply-chain risk
management planning, supplier assessments, tamper resistance,
component authenticity, software integrity, and provenance. These
cover the kinds of risks that surface in high-profile supply-chain
incidents (compromised software updates, counterfeit hardware,
insider threats at upstream vendors).

**Gap against CMMC Level 2.** NIST SP 800-171 Rev 2 does not have a
dedicated supply-chain family. Some supply-chain risk considerations
appear implicitly through CM (configuration management) and AT
(awareness and training), but there is no 800-171 equivalent to the
800-53 SR family. A CMMC Level 2 contractor implements no
dedicated SR controls under the 171 baseline.

**What this means for the contractor.** A contractor using a
FedRAMP Moderate CSP inherits the CSP's SR-family implementation
for the CSP's own supply chain: the CSP has documented its
suppliers, its software-integrity processes, its firmware-update
channels, and so on. The contractor's own supply chain, including
software the contractor uses beyond the CSP, remains outside the
CMMC 110-practice scope. Contractors evaluating supply-chain
exposure should read the CSP's SR implementation as a starting
point, not as the contractor's own SCRM program. If DoD requires
dedicated SCRM (some DFARS clauses and specific contract flowdowns
do), the contractor provides that separately.

### Privacy overlay (PT family) — new in Rev 5

NIST SP 800-53 Rev 5 introduced the
PT (Personally Identifiable Information Processing and Transparency)
family as a new privacy-focused control family, replacing and
expanding the privacy appendix from Rev 4. FedRAMP Rev 5 includes
PT controls in the Moderate baseline when a system processes
PII (Personally Identifiable Information).

**What the PT family covers.** Authority to collect and process
PII, purpose specification, consent mechanisms, specific PII
categories handled, and transparency obligations including system
of records notices and privacy notices.

**Gap against CMMC Level 2.** NIST SP 800-171 Rev 2 is scoped to
CUI confidentiality. It does not treat privacy or PII handling as
a distinct regime. A contractor whose system processes only CUI
and no PII sees no PT-family gap. A contractor whose system
processes PII along with CUI sees a gap: PT controls at the
FedRAMP Moderate level cover considerations that CMMC 800-171 Rev
2 does not.

**When this matters.** Government contractors handling personnel
records, health information (under Health Insurance Portability
and Accountability Act (HIPAA) overlays), or broader constituent
data typically have PII obligations layered on top of or alongside
CUI obligations. In those cases, the FedRAMP Moderate PT-family
inheritance is substantive. Read the CSP's privacy documentation
separately from the security documentation.

### Boundary documentation depth

FedRAMP requires a formal authorization boundary with explicit
documentation, diagrams, and data-flow artifacts. CMMC boundary
definition is looser in 800-171 Rev 2 text and tightened in the
CMMC Assessment Guide and scoping guidance.

**FedRAMP boundary artifacts.** The SSP includes the authorization
boundary diagram, data flow diagrams, and a narrative of what is
inside the boundary versus what is out. Leveraged external services
are documented with their own FedRAMP authorization status.
Interconnections are enumerated. The boundary is the unit of
authorization; changing the boundary is a formal event that may
require a Significant Change Request and an impact review.

**CMMC boundary.** Defined in 800-171 §3.12.4 and the CMMC Scoping
Guidance. The CMMC boundary is "the CUI boundary," the set of
systems, components, and processes where CUI is stored, processed,
or transmitted. Less formal than FedRAMP; practical and
contractor-scoped rather than architectural-first. See
`references/scoping-and-cui.md` for the CUI boundary pattern.

**Two-boundary problem.** The CUI boundary and the FedRAMP
authorization boundary may not be the same boundary. The CSP's
FedRAMP boundary is what the CSP authorized; the contractor's CUI
boundary is where CUI lives. If the contractor uses a small
fraction of the CSP's capabilities, the contractor's CUI boundary
is a subset of the CSP's authorization boundary. If the contractor
processes CUI across multiple CSPs plus on-premises systems, the
CUI boundary spans multiple authorization boundaries. The CUI
boundary sits in the contractor's SSP per
`references/scoping-and-cui.md`; the FedRAMP authorization
boundary sits in the CSP's SSP. They are distinct artifacts and
should not be conflated.

### Summary of the inheritance gap

The six areas above share a common pattern. FedRAMP sets a higher
floor for the CSP's operation of the infrastructure the contractor
relies on. CMMC sets the floor for the contractor's own operation
of their CUI boundary. A contractor with a FedRAMP Moderate CSP
inherits the CSP's implementation of the overlapping technical
controls (cryptography, boundary protection, audit logging, and
so on per the crosswalk above). The contractor does not inherit
the CSP's ConMon cadence, the CSP's CISA reporting obligation, or
the CSP's SR or PT control implementations as discharge of the
contractor's own obligations.

The inheritance model from the crosswalk section above applies:
**fully inherited** controls shift to the CSP, **shared**
controls require both the CSP's capability and the contractor's
configuration, **contractor-owned** controls stay with the
contractor regardless of CSP posture. The FedRAMP excesses in
this section affect the first two categories (what the CSP does
goes further than CMMC demands) but not the third (contractor-
owned controls are not affected by the CSP's cadence or reporting
obligations).

---

## CMMC and DFARS Excesses Over FedRAMP

The "Inherited vs shared-responsibility controls" framing in the
crosswalk section explains what a contractor inherits from a
FedRAMP Moderate CSP. That model addresses **control
implementation** for the overlapping technical surface. It does
not address the CMMC/DFARS-specific obligations that sit on the
contractor regardless of CSP posture.

This section covers those contractor-side obligations. It is not
about what the CSP does; it is about what the contractor must do
even with a fully FedRAMP-inheriting cloud stack. The distinction
matters because a C3PAO (CMMC Third-Party Assessment Organization)
assesses the contractor's implementation of CMMC, not the CSP's
FedRAMP authorization. A contractor cannot cite "we use a FedRAMP
Moderate CSP" as a substitute for CMMC certification. The CSP's
FedRAMP ATO and the contractor's CMMC certification are different
artifacts, from different assessors, covering different scopes.

### DFARS 252.204-7012 — the safeguarding clause in full

The crosswalk section above cited DFARS 252.204-7012(b)(2)(ii)(D)
for the FedRAMP Moderate CSP requirement, and the FedRAMP Excesses
section above cited (c)(1)(ii) and (d) for the 72-hour DIBNet
reporting and DC3 malware submission. The clause carries further
obligations that shape contractor behavior before and after an
incident.

**(a) Definitions.** The clause defines four key terms used
throughout the rest of the clause:
CDI (covered defense information), "cyber incident," "covered
contractor information system," and "rapidly report" (which means
within 72 hours). CDI includes CUI identified in the contract
plus certain categories defined in the clause. A contractor
uncertain about scope should read (a) first.

**(b)(1) IT services operated on behalf of the Government.** For
covered contractor information systems that are part of an IT
service or system operated on behalf of the Government, the
clause directs the contractor to cloud computing security
requirements in DFARS 252.239-7010 or to other contract-specified
security requirements, not to NIST SP 800-171. The 800-171 path
in (b)(2) applies to everything else.

**(b)(2)(i) NIST SP 800-171 baseline.** Except as provided in
(b)(2)(ii), the covered contractor information system shall
implement NIST SP 800-171. This is the primary CUI safeguarding
requirement.

**(b)(2)(ii) Subparagraphs A through D.** Four specific provisions
modify the (b)(2)(i) baseline: (A) sets the original December 31,
2017 implementation deadline for NIST SP 800-171. (B) directs the
contractor to submit variance requests in writing to the
contracting officer for DoD CIO consideration. (C) allows
recognition of prior DoD CIO adjudications on inapplicable
requirements or equivalent security measures. (D) is the FedRAMP
Moderate CSP path for external cloud services (see the CUI
Baseline Decision section above).

**(c)(1) Cyber incident reporting.** Paragraph (c)(1) requires
the contractor to conduct a review for evidence of compromise and
rapidly report cyber incidents to DoD through DIBNet at
dibnet.dod.mil. See the FedRAMP Excesses section above for the
72-hour window and the DIBNet destination. (c)(1)(i) through (iv)
detail the review activities, the reporting destination, the
medium access token requirement, and the submission of malicious
software under (d).

**(d) Malicious software.** When the contractor discovers and
isolates malicious software during a reported incident, submit
the malware to the DC3 (DoD Cyber Crime Center). The clause
states explicitly: "Do not send the malicious software to the
Contracting Officer." DC3 submission is separate from the (c)(1)
DIBNet incident report.

**(e) Media preservation and protection.** Preserve and protect
images of all known affected information systems and all relevant
monitoring and packet-capture data for **at least 90 days** from
the submission of the cyber incident report. This gives DoD a
90-day window to request the media or decline interest. Practical
implication: if a contractor rolls over logs or wipes images on
anything shorter than 90 days post-incident-report, the contract
is out of compliance.

**(f) Access for forensic analysis.** Upon request by DoD, the
contractor provides access to additional information and equipment
necessary to conduct a forensic analysis of the incident.

**(g) Cyber incident damage assessment activities.** If DoD elects
to conduct a damage assessment, the contracting officer will
request that the contractor provide the damage assessment
information gathered in accordance with paragraph (e).

**(m) Subcontracts.** The clause flows down to subcontracts
"without alteration" for subcontracts involving operationally
critical support or covered defense information. Subcontractors
must notify the prime when requesting NIST SP 800-171 variances
under (b)(2)(ii)(B) and must provide incident report numbers when
they report cyber incidents to DoD.

> Source: DFARS 252.204-7012, effective DFARS Change 2025-11-10,
> at acquisition.gov/dfars/252.204-7012.

### FedRAMP Moderate Equivalency — the detail path

The CUI Baseline Decision section introduced equivalency as an
alternate path to a full FedRAMP Moderate authorization. This
subsection treats the equivalency mechanics.

**DoD CIO Memorandum, December 2023.** The memorandum narrows
(b)(2)(ii)(D)'s "equivalent to" language: equivalence requires a
complete body of evidence equivalent to a FedRAMP Moderate
authorization package, including a 3PAO-assessed attestation
against the full Moderate baseline. The contracting officer
evaluates the equivalency claim and accepts or rejects it.

**What this means in practice.** A CSP pursuing equivalency
submits to the same 3PAO assessment rigor as a CSP pursuing full
FedRAMP authorization. The difference is the absence of an agency
sponsor and the absence of an Agency ATO; the contracting officer
takes the role the agency AO would have taken. Equivalency is not
a lower bar; it is a parallel path with a different acceptance
structure.

**Where contractors get this wrong.** A CSP's marketing claim of
"FedRAMP Moderate equivalent" is not, by itself, sufficient. The
contractor must verify: (1) a current 3PAO attestation letter
exists, (2) a complete body of evidence mirroring a FedRAMP
package is available for contracting officer review, (3) the
specific contracting officer has accepted the equivalency claim
for the specific contract. Absent all three, the equivalency path
is unsubstantiated and a DFARS 252.204-7012(b)(2)(ii)(D) finding
is available to any assessor or auditor who looks.

### DFARS 252.204-7019 and 252.204-7020 — SPRS assessment

These two DFARS provisions establish the self-assessment and
flowdown framework that sits underneath CMMC. Both apply
contract-by-contract based on NIST SP 800-171 implementation
requirements.

**DFARS 252.204-7019 (Notice of NIST SP 800-171 DoD Assessment
Requirements).** A solicitation provision. Offerors must have a
current NIST SP 800-171 DoD Assessment posted in the Supplier
Performance Risk System (SPRS) for each covered contractor
information system relevant to the offer. "Current" means not
more than 3 years old unless the solicitation specifies a shorter
window. Offerors without a current assessment may conduct and
submit a Basic Assessment for SPRS posting before the solicitation
closes.

**DFARS 252.204-7020 (NIST SP 800-171 DoD Assessment
Requirements).** A contract clause. Defines three assessment
levels.

**Basic Assessment.** Contractor self-assessment against NIST
SP 800-171 using the DoD Assessment Methodology. Confidence
level: Low. Contractor submits the summary score to SPRS via
encrypted email.

**Medium Assessment.** Government-conducted evaluation including
review of the contractor's Basic Assessment, a thorough document
review, and discussions with the contractor. Confidence level:
Medium.

**High Assessment.** Government-conducted evaluation using NIST
SP 800-171A, including verification, examination, and
demonstration of implementation. Typically performed by
DCMA (Defense Contract Management Agency), specifically the
Defense Industrial Base Cybersecurity Assessment Center (DIBCAC).
Confidence level: High.

**SPRS summary scores.** SPRS posts summary scores in the form
"95 out of 110," not individual practice scores. DoD posts Medium
and High Assessment results within 30 days of assessment, giving
the contractor 14 business days for rebuttal before the score
appears in SPRS.

**Flowdown under 7020.** The clause flows down "without
alteration" to subcontracts involving NIST SP 800-171
implementation. Primes cannot award such subcontracts unless the
subcontractor has completed a Basic Assessment (or higher) within
the last 3 years and posted the score in SPRS.

### The DoD Assessment Methodology scoring rules

The DoD Assessment Methodology (currently Version 1.2.1, June 24,
2020) defines how the 110-point scoring works.

**Maximum score is 110.** A contractor implementing all 110
practices correctly scores 110. A contractor missing a practice
loses the weighted point value of that practice, subtracted from
110. Scores can go negative (a contractor missing many 5-point
practices can end up well below zero).

**Weighted deductions: 1, 3, or 5 points per missed practice.**
Each practice is weighted according to its security impact. A
missed 5-point practice is worth 5 points subtracted from 110; a
missed 3-point practice is worth 3; a missed 1-point practice is
worth 1.

**Partial credit exists only on two practices.** IA.L2-3.5.3
(multi-factor authentication) and SC.L2-3.13.11 (FIPS-validated
cryptography) permit partial credit. IA.L2-3.5.3 scores 5 points
off if MFA is not implemented at all, 3 points off if MFA is
implemented only for privileged or remote users (not general
users). SC.L2-3.13.11 has an analogous partial-credit structure.

**No partial credit on the other 108 practices.** A practice is
either implemented (full weighted score) or not implemented (full
weighted deduction). "Mostly implemented" earns zero points.

**Why this matters for FedRAMP comparison.** FedRAMP Moderate
does not use a 110-point scoring system. FedRAMP is pass-fail at
the authorization level, with POA&M accepting time-bound
remediation of specific findings. The DoD Assessment Methodology
is additive and weighted; a contractor can still hold a valid
contract with a 58 out of 110 score as long as the gaps are
captured in an SSP and POA&M. CMMC Level 2 raises the bar to
requiring all 110 (subject to POA&M allowances for specific
items; see `references/poam-management.md`).

> Source: NIST SP 800-171 DoD Assessment Methodology, Version
> 1.2.1 (2020-06-24), operative as of April 2026, published at
> acq.osd.mil/asda/dpc/cp/cyber/docs/safeguarding/. DoD may revise
> the Methodology; verify current version before relying on
> specific point values.

### DFARS 252.204-7021 — CMMC certification requirement

**Effective date.** 2025-11-10 (DFARS Change). The clause is now
in force for contracts with the required CMMC level specified by
the contracting officer.

**What the clause requires.** The contractor must have and
maintain, for the duration of the contract, a current CMMC status
at the level specified in the solicitation. Levels are Level 1
(Self), Level 2 (Self), Level 2 (C3PAO), and Level 3 (DIBCAC),
with the CMMC status type determined by the contracting officer.

**CMMC status validity.** Per 32 CFR 170.17 and the clause:

- Conditional certification: not older than 180 days. Conditional
  status allows a contractor to hold the contract while closing
  out specific POA&M items, but the 180-day clock converts
  Conditional to Final or expires.
- Final Level 1 (Self): not older than 1 year. Level 1 is
  self-assessed and annually reaffirmed.
- Final Level 2 (Self or C3PAO) and Level 3 (DIBCAC): not older
  than 3 years, with annual affirmations between assessments.

**Annual affirmations.** A senior official of the contractor's
OSA (Organization Seeking Assessment) affirms annually that the
contractor remains in compliance with the CMMC requirements. The
affirmation is posted in SPRS.

**Flowdown under 7021.** The clause flows down to subcontracts
involving FCI or CUI. Primes must ensure the subcontractor holds
a current CMMC status at the appropriate level for the
subcontract scope.

### C3PAO versus FedRAMP 3PAO — what gets assessed by whom

This distinction is load-bearing. The crosswalk section's
inheritance taxonomy addresses what a FedRAMP 3PAO assessed about
the CSP's cloud offering. The C3PAO assessment is a different
event, against a different scope, with a different certification
outcome.

**FedRAMP 3PAO.** A Third-Party Assessment Organization
accredited by the FedRAMP PMO. Assesses the CSP's cloud offering
against the 800-53 Rev 5 baseline selected for the authorization
(Low, Moderate, or High). The 3PAO produces a Security Assessment
Report. The sponsoring agency's Authorizing Official grants the
ATO to the CSP. The CSP is the entity with the authorization;
the authorization covers the CSP's defined authorization
boundary.

**C3PAO.** A CMMC Third-Party Assessment Organization
authorized, and eventually accredited (ISO/IEC 17020:2012
compliance required), by the CyberAB (the Accreditation Body
defined in 32 CFR 170.8). Assesses the OSA's implementation of
CMMC Level 2 practices against NIST SP 800-171 Rev 2 per the DoD
Assessment Methodology and the CMMC Assessment Guide. The C3PAO
issues a Certificate of CMMC Status to the OSA if the assessment
passes (possibly Conditional, with POA&M items to close out).
The OSA is the
entity with the certification; the certification covers the OSA's
CMMC Assessment Scope.

**Why the distinction matters.** A contractor cannot point to a
CSP's FedRAMP 3PAO assessment as evidence for the contractor's
own CMMC certification. The FedRAMP 3PAO assessed the CSP; the
C3PAO assesses the contractor. Inheritance of *controls* happens
through the SSP attribution pattern (per the crosswalk
inheritance section); certification of *the contractor* happens
through the C3PAO assessment of the contractor's environment.

**DCMA DIBCAC's role.** For Level 3 assessments, DCMA DIBCAC
conducts the certification assessment directly. For Level 2
(C3PAO), DCMA DIBCAC audits the C3PAOs themselves, including
assessing the C3PAO's own information systems for CMMC Level 2
compliance. The C3PAO's certificate-issuing authority rides on
the C3PAO being certified at the same level the C3PAO is
certifying others to.

> Source: 32 CFR Part 170 Subpart C (§170.8 Accreditation Body,
> §170.9 C3PAOs, §170.10 CAICO, §170.11 CCA) in effect as of
> April 2026, at
> ecfr.gov/current/title-32/chapter-I/subchapter-G/part-170.

### CUI-specific handling not covered by FedRAMP

CUI has categorical markings, dissemination controls, and
handling requirements defined by the National Archives CUI
Registry and 32 CFR Part 2002. FedRAMP addresses the security of
federal information systems generally; it does not cover the
markings and handling layer that CUI-specific compliance demands.

**CUI markings.** Each piece of CUI carries a category marking
(Controlled Technical Information, Law Enforcement Sensitive,
Export Controlled, etc.) and may carry dissemination controls
(NOFORN, REL TO, FEDCON, etc.). Contractors processing CUI must
apply and preserve these markings through the data lifecycle.
FedRAMP provides no marking guidance; it presumes the agency
owning the data applies and enforces markings.

**CUI dissemination controls.** Controls like NOFORN ("No Foreign
Dissemination") and FEDCON ("Federal Contractors Only") shape who
can receive the data regardless of technical access. A FedRAMP
Moderate CSP does not implement dissemination-control awareness;
the contractor's own access-control policies implement these
marking-based restrictions.

**CUI Registry categories.** The National Archives CUI Registry
enumerates the CUI categories (roughly 100+ subcategories under
20+ categories). Contractor SSPs typically scope which categories
apply to their contract. FedRAMP inherits nothing about which CUI
categories the contractor handles; that scoping is contractor-
side.

**Where this lives in this skill.** See
`references/scoping-and-cui.md` for the full CUI scoping treatment
including category enumeration, dissemination-control rules, and
boundary implications. This section establishes only that CUI
markings and dissemination controls are contractor-owned work
that FedRAMP does not address.

### Summary

The contractor's CMMC and DFARS obligations form a stack that a
FedRAMP Moderate CSP cannot discharge. The stack, read from the
bottom up:

1. CUI handling (markings, dissemination, categories).
   Contractor-only, outside FedRAMP scope entirely.
2. 800-171 implementation on the contractor's covered information
   systems. This is the baseline CMMC evaluates against.
3. SPRS Basic Assessment score (current within 3 years) posted by
   the contractor per DFARS 7019/7020.
4. CMMC Level 2 (or 3) certification issued by a C3PAO (or DCMA
   DIBCAC for Level 3) against the OSA's environment per DFARS
   7021.
5. Annual affirmations by a senior official of the OSA attesting
   continued compliance.
6. Incident reporting via DIBNet within 72 hours per DFARS
   7012(c)(1)(ii) when an incident affects CDI, with malware
   samples to DC3 per (d) and 90-day image preservation per (e).

The FedRAMP Moderate CSP inheritance supports the 800-171
implementation layer for the infrastructure the contractor runs
on. It does not supply the other layers. A contractor building
a CMMC program who treats the FedRAMP CSP's ATO as "CMMC
compliance" will fail a C3PAO assessment; the C3PAO assesses the
contractor's environment, not the CSP's.

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

