# Contractor Profiles

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2
> (DoD CIO); DFARS 252.204-7012; 32 CFR Part 170 CMMC Program
> Final Rule (effective 2024-12-16); 48 CFR Parts 204/212/217/252
> (effective 2025-11-10); SBA regulations at 13 CFR Parts 121,
> 124, 126, 127, 128 for small business size standards and
> socioeconomic set-aside programs; DoD CMMC Program regulatory
> impact analysis
> (federalregister.gov/documents/2023/12/26/2023-27280/
> cybersecurity-maturity-model-certification-cmmc-program); FAR
> Part 19 as revised; SBA certify.sba.gov for SDVOSB, 8(a),
> WOSB, HUBZone certifications.

## Overview

This file maps CMMC compliance patterns to contractor size and
socioeconomic profile. The same NIST 800-171 practices apply
across all profiles, but implementation paths, cost envelopes,
staffing approaches, and architectural patterns differ sharply
by organization size and by whether the contractor holds a
set-aside certification (SDVOSB, 8(a), WOSB, HUBZone).

Three size profiles:

- **Small** (fewer than 50 employees) — the most cost-sensitive
  segment. Enclave architectures, managed-service partnerships,
  and tax-credit leverage are common patterns. Primary risk is
  under-scoping CUI and running compliance on a spreadsheet.
- **Medium** (50-500 employees) — scaling compliance across
  multiple programs and contract vehicles. Typical segment for
  standing up dedicated compliance staff and maturing policy
  architecture.
- **Large** (500+ employees) — enterprise compliance programs
  with GRC tooling, dedicated teams, and multi-BU scope. Primary
  risk is scope sprawl and CUI-boundary drift across business
  units.

Four set-aside program considerations:

- **SDVOSB** (Service-Disabled Veteran-Owned Small Business) —
  SBA certification required since 2024-01-01 for federal
  set-aside eligibility.
- **8(a)** — the SBA's business development program for socially
  and economically disadvantaged small businesses. The Small
  Disadvantaged Business contracting goal reset to the statutory
  5% on 2025-01-24.
- **WOSB / EDWOSB** (Women-Owned Small Business / Economically
  Disadvantaged Women-Owned Small Business) — SBA certification
  via certify.sba.gov.
- **HUBZone** — Historically Underutilized Business Zone, SBA
  certification for firms in designated distressed areas.

Read this file alongside
`references/scoping-and-cui.md` (CUI scoping frames the cost
baseline), `references/levels-and-assessment.md` (L1 vs L2
determines the cost envelope), `references/ssp-guidance.md` (SSP
complexity scales with profile), and the modern-IT references
(tenancy and tooling choices interact with profile in ways the
profiles below call out).

---

## Scope of this file

Covered:

- Three size profiles (small, medium, large) mapped to CMMC
  compliance patterns.
- Four socioeconomic set-aside program considerations specific to
  CMMC posture.
- Cost framework covering CMMC Level 1 and Level 2 per profile,
  including DoD official cost projections and practitioner-
  typical preparation spend.
- Compliance coverage recommendations (which practices to
  prioritize, which to defer within Conditional Certification
  rules, which architectural patterns fit each profile).
- Common pitfalls specific to each profile.

Not covered:

- CMMC Level 3. Level 3 certification pathway is
  DoD-mission-specific and rare in the DIB; treated briefly in
  the cost framework but not in depth.
- International affiliates and foreign-ownership scenarios.
  Covered under `references/scoping-and-cui.md` and export-
  control counsel; this file stays on the domestic profile axis.
- Joint-venture-specific size determination. SBA has intricate
  rules for JV size treatment; consult SBA counsel before
  relying on JV small-business status for CMMC planning.
- Protests and appeals. Size protests, SDVOSB protests, and 8(a)
  appeals have their own regulatory track.
- Specific pricing from named MSPs, C3PAOs, or consultancies.
  Cost ranges are practitioner-typical; specific quotes require
  vendor engagement.

---

## Size profiles

### Small (fewer than 50 employees)

**Profile summary.** Few to no dedicated compliance staff.
Typically one person (CEO, CTO, or head of operations) wears
compliance as part of a broader role. CUI surface is often a
subset of the business (a program or contract rather than the
whole company). IT footprint may be Microsoft 365 commercial or
Google Workspace commercial with migration pressure to
government-tier tenancies on CUI-carrying contracts.

**Common architectural patterns.**

- **CUI enclave.** Keep the production IT footprint on
  commercial tenancies and carve out a CUI-specific enclave (a
  GCC High tenancy, a Workspace Assured Controls Plus tenancy,
  or a contractor-authored IaaS boundary) just for CUI-handling
  workflow. Smaller CUI boundary, smaller compliance footprint,
  lower cost. Downside: users manage two tenancies and the
  operational discipline to keep CUI inside the enclave.
- **MSP partnership.** Engage a managed service provider with
  CMMC expertise to handle tooling, monitoring, audit-log
  aggregation, and SSP drafting. The MSP absorbs the cost of
  specialist staff the small contractor cannot justify hiring
  directly. Verify the MSP itself has a documented CMMC-
  compliance-handling posture (MSPs with CUI access are within
  the contractor's CMMC scope).
- **L1-only where contract permits.** If the contract vehicle
  mandates only FCI-safeguarding (FAR 52.204-21) without DFARS
  252.204-7012, stay at Level 1 self-assessment rather than
  over-scoping to Level 2.

**Cost envelope.** DoD's official projection for a representative
small business is a three-year total of approximately $487,970
to achieve and maintain Level 2 compliance per the CMMC Program
regulatory impact analysis
(federalregister.gov/documents/2023/12/26/2023-27280/...).
Practitioner breakdowns land closer to $100,000-$200,000 for the
first-year push with smaller recurring amounts in years 2 and 3.
Level 1 is substantially cheaper (self-assessment under $10,000
all-in for most small contractors).

**Staffing approach.** No dedicated CISO at this scale. Fractional
vCISO engagement ($250-$400/hour, typically 10-40 hours per
month) is a common pattern. Compliance ownership sits on an
existing staff role (often CTO, COO, or head of operations).
Assessment-readiness work may engage a consultant for 2-6 months
on a scoped basis rather than hiring full-time compliance staff.

**Tax credit awareness.** Section 174 R&D capitalization changes
(2022 Tax Cuts and Jobs Act provisions that took effect 2022
and have been modified in subsequent legislation) affect how
contractors can treat cybersecurity software development
spending; consult tax counsel for current treatment. State and
federal cybersecurity-specific incentives may apply to
particular contractor circumstances (SBIR/STTR research
programs, state workforce-development credits); scope
eligibility case-by-case.

**Common pitfalls at this profile.**

- Under-scoping CUI to avoid cost, then failing assessment when
  the assessor finds CUI on out-of-scope systems.
- Over-scoping CUI to "be safe," driving compliance costs up
  unnecessarily when enclave architecture would have sufficed.
- Running compliance on a spreadsheet with policies that exist
  only in PDF form. Phase 4 assessment guides call this pattern
  out repeatedly; small contractors in particular fall into it.
- MSP partnership without written responsibility matrix. If the
  MSP is implementing controls, the SSP must name them and the
  contract must allocate responsibility explicitly.
- Assuming Level 1 covers a Level 2 contract. Contract clause
  review is the first step; DFARS 252.204-7012 presence in any
  clause means Level 2 is in play.

### Medium (50-500 employees)

**Profile summary.** One or more dedicated security staff
(security engineer, IT security analyst, sometimes a CISO in
title if not function). Multiple contracts and often multiple
programs with distinct CUI footprints. Business-unit variation
in CUI handling. More infrastructure complexity: existing AD
forests, hybrid cloud, on-premises plus SaaS mix.

**Intra-profile variance.** The 50-500 range spans substantial
operational variation. A 55-employee contractor close to the
small boundary behaves similarly to a small profile with a
single dedicated security hire; a 450-employee contractor close
to the large boundary carries enterprise GRC tooling, multiple
business units, and mature acquisition integration. Treat the
medium profile as a spectrum; pattern choices (tooling
investment, governance formality, tenancy migration completeness)
scale across the range rather than applying uniformly.

**Common architectural patterns.**

- **Tenancy migration.** Move from commercial Microsoft 365 or
  commercial Google Workspace to GCC High or Workspace Assured
  Controls Plus for CUI-handling users. Medium contractors
  typically cannot isolate CUI work cleanly into an enclave; the
  business is too integrated, so the whole CUI-carrying
  productivity plane migrates.
- **Dedicated GRC tooling.** ServiceNow GCC (for contractors
  already on ServiceNow commercial), Atlassian Government Cloud
  Jira for POA&M tracking, or a dedicated compliance platform
  (Vanta, Drata, Secureframe, Hyperproof). Tooling investment
  around $50K-$150K annually typical.
- **Formal governance.** Compliance committee meeting monthly or
  quarterly; annual internal assessment cycle; dedicated
  evidence repository; role-based compliance training.
- **SIEM consolidation.** Azure Sentinel (for Microsoft-
  committed shops), Google Chronicle/SecOps (for Workspace
  shops), Splunk, or Elastic with cloud government integration.

**Cost envelope.** Three-year total often in the $750K-$1.5M
range for contractors with 100-300 employees and moderate CUI
footprints. Annual recurring spend includes C3PAO assessments
(triennial), ongoing tooling licensing, dedicated compliance
staff, and periodic consultant engagement. Level 1-only
contractors at this size are rare; most carry DFARS 7012 on at
least some contracts.

**Staffing approach.** Dedicated security engineer or small
security team (1-3 people). CISO or VP Security role may be
combined with IT leadership. Compliance ownership typically sits
in the security function rather than on a business-role leader.
External consultants engage for specialized work (ATO prep,
C3PAO assessment readiness, incident-response planning) rather
than baseline compliance operations.

**Common pitfalls at this profile.**

- Scope drift across business units. CUI flows into a BU that
  was not in the original assessment scope; the SSP lags the
  actual CUI footprint by months.
- Tooling proliferation without integration. Three DLP tools,
  two SIEM instances, and four ticketing systems is the
  architectural anti-pattern.
- Policy pyramid (overarching policy + program-specific
  procedures + work-instruction templates) that looks complete
  on paper but does not reflect actual practice.
- Annual compliance cycle drift. The first annual assessment
  happens on schedule; the second slips to 13 months; the third
  to 18 months; by year five the organization is out of
  compliance rhythm.
- Under-investing in assessor experience. The contractor pays
  for a C3PAO whose assessor has limited CMMC experience; the
  assessment produces findings that a more experienced assessor
  would have resolved through dialogue rather than a written
  finding.

### Large (500+ employees)

**Profile summary.** Enterprise compliance program with
dedicated team (CISO, security architects, GRC analysts,
assessment readiness leads). Multiple business units with
distinct CUI footprints. Complex IT estate: legacy on-premises,
hybrid cloud, multiple SaaS platforms, subsidiaries and
acquisitions with their own compliance legacies.

**Common architectural patterns.**

- **Enterprise identity and tenancy consolidation.** Move to a
  single government-tenancy identity plane (Entra ID Government
  or Cloud Identity on Assured Controls Plus) with all CUI-
  carrying users federated through it. Legacy AD forests and
  subsidiary identity stores migrate to the consolidated plane
  or federate through specific trust relationships documented
  in the SSP.
- **GRC platform at enterprise scale.** ServiceNow GRC,
  RSA Archer, MetricStream, or similar enterprise compliance
  platform with dedicated administration team. Integration with
  ITSM, risk register, incident response, vendor management.
- **Dedicated CMMC program management.** CMMC program manager
  reporting to CISO or deputy CISO; assessment-readiness
  continuous cycle rather than point-in-time; multiple C3PAO
  relationships for different BUs or different assessment
  cycles.
- **Mergers and acquisitions compliance discipline.** Due
  diligence includes CMMC scope of acquisition target;
  integration plan names the CMMC migration cadence; 180-day to
  18-month integration timeline depending on target size.

**Cost envelope.** Total compliance spend in the multi-million
range annually across dedicated staff, enterprise GRC tooling,
assessment cycles, and remediation programs. C3PAO assessment
fees are a small fraction of total cost at this scale;
continuous-monitoring and dedicated-staff costs dominate.

**Staffing approach.** Dedicated CISO with reporting chain to
C-suite. GRC team of 5-20 depending on company size and CUI
footprint. Security engineering and security operations teams
separate from GRC. Legal and contracts teams have dedicated
CMMC/DFARS expertise. External counsel engaged for regulatory
interpretation and specific compliance decisions.

**Common pitfalls at this profile.**

- Scope sprawl across business units. Each BU has its own
  interpretation of CUI, its own SSP, its own operational
  approach; the enterprise loses visibility and consistent
  posture.
- Compliance theater. Enterprise organizations can maintain
  elaborate policy hierarchies, robust evidence repositories,
  and full-time compliance staff while the actual operational
  posture drifts from documented intent. Anti-pattern discussion
  beyond this file's scope is covered in a future corpus
  phase on compliance anti-patterns.
- Acquisition integration delay. An acquired company operates
  under its legacy compliance regime for years after
  acquisition; CUI moves between acquirer and acquired on
  informal paths that the enterprise SSP does not address.
- Over-automation before process maturity. Rolling out a GRC
  platform before the underlying compliance process is stable
  produces a system that automates chaos rather than order.
- Third-party assessor familiarity. Large contractors sometimes
  develop a preferred C3PAO relationship that becomes a point
  of organizational single-failure; C3PAO staff turnover or
  scope change forces a last-minute assessor switch.

---

## Set-aside program considerations

The four set-aside programs below interact with CMMC in a
specific way: set-aside status does not change CMMC requirements
but does affect contract eligibility, competitive positioning,
and (through SBA regulations) the size-standard rules that
determine whether a contractor is treated as small for a given
procurement.

### SDVOSB (Service-Disabled Veteran-Owned Small Business)

**Current state.** As of 2024-01-01 per
federalregister.gov/documents/2024/02/23/2024-02797, SBA is the
certifying authority for SDVOSB status (previously VA's CVE
handled VA-specific certifications; SBA's Veteran Small Business
Certification program now consolidates both VA and non-VA
set-asides). Self-certification is no longer valid for federal
set-asides; contractors must hold SBA certification obtained
through certify.sba.gov.

**CMMC intersection.** As a general rule, SDVOSB status
determines contract eligibility for set-aside procurements but
does not reduce or shift CMMC requirements; specific contract
clauses control. A small SDVOSB contractor handling CUI under
DFARS 7012 meets the same NIST 800-171 requirements as any other
contractor. The SDVOSB set-aside may make the contract
competitively accessible; the cybersecurity bar is the same.

**Practical implications.**

- Plan CMMC investment independently of SDVOSB certification
  timing. SDVOSB certification takes weeks to months; CMMC
  readiness takes months to a year or more.
- Track SBA certification renewal (typically triennial) alongside
  CMMC assessment cycle (also triennial at Level 2 with third-
  party); consolidating the calendars helps avoid lapsed-status
  gaps.
- VA contracts increasingly reference DFARS 7012 equivalents
  through contract-specific data-rights or CUI language; do not
  assume VA contracting paths are outside DFARS 7012 scope.

### 8(a) Business Development Program

**Current state.** SBA's 8(a) program supports socially and
economically disadvantaged small businesses. On 2025-01-24, the
SBA reset the Small Disadvantaged Business contracting goal to
the statutory 5% (previously 15%), affecting the volume of set-
aside opportunities. Further 2026 program changes have been
proposed; verify against the Federal Register and 13 CFR Part
124 before relying on specific eligibility or mentor-protege
mechanics.

**CMMC intersection.** 8(a) sole-source awards and competitive
8(a) set-asides carry DFARS 7012 when the contract handles CUI.
As a general rule, 8(a) certification does not exempt or reduce
CMMC requirements; specific contract clauses control. 8(a)
graduates (firms that have completed the nine-year 8(a) term)
carry CMMC requirements as they compete on open-market
contracts.

**Practical implications.**

- 8(a) mentor-protege relationships create joint-venture
  structures where the protege carries CMMC obligations for
  work under the JV's CUI contracts. The mentor's CMMC
  maturity does not automatically flow down to the protege; JV
  agreements should address compliance responsibility
  explicitly.
- 8(a) graduation timing and CMMC assessment cycles should be
  coordinated. A firm in year 8 of the 8(a) program competing
  for open-market work needs CMMC readiness before graduation,
  not after.
- The SDB goal reset affects contract volume rather than
  compliance requirements; CMMC investment remains necessary
  regardless of available 8(a) opportunities.

### WOSB / EDWOSB (Women-Owned Small Business)

**Current state.** SBA certification required via
certify.sba.gov for federal WOSB and EDWOSB set-asides.
Self-certification is no longer valid for WOSB set-asides under
FAR Part 19 as revised.

**CMMC intersection.** Same pattern as SDVOSB: set-aside status
determines contract eligibility; CMMC requirements apply based
on contract clauses (DFARS 7012 presence, data-handling scope).

**Practical implications.**

- Track certification renewal alongside CMMC assessment cycle.
- WOSB contracts in the DIB are often in program areas (IT
  services, professional services, research) where CUI is
  routinely present; plan CMMC readiness on the assumption that
  Level 2 will be required even for WOSB set-aside wins.

### HUBZone

**Current state.** SBA-certified HUBZone status requires the
contractor to be located in a Historically Underutilized
Business Zone and to employ a minimum percentage of HUBZone
residents. Certification is via certify.sba.gov with ongoing
compliance requirements.

**CMMC intersection.** Same pattern: HUBZone eligibility is a
competitive determinant; CMMC is determined by contract clauses.

**Practical implications.**

- HUBZone residency requirement interacts with CUI-handling
  workforce composition in a specific way: remote work for
  HUBZone-counted employees is permissible under SBA rules
  (subject to principal office location requirements), but
  DFARS 7012 and the contractor's SSP must address the CUI-
  handling posture for remote HUBZone employees.
- HUBZone annual-recertification and CMMC triennial assessment
  are separate cycles; track both.

---

## CMMC cost framework

Official DoD cost projections per the CMMC Program regulatory
impact analysis
(federalregister.gov/documents/2023/12/26/2023-27280):

| Assessment tier | Cost range |
|---|---|
| Level 1 self-assessment (annual) | $4,000-$6,000 |
| Level 2 self-assessment (triennial) | $37,000-$49,000 |
| Level 2 third-party (C3PAO) triennial + 2 annual affirmations | $105,000-$118,000 |
| Level 3 | Level 2 costs + ~$41,000 for additional requirements |

Preparation and ongoing spend outside the assessment fee
(practitioner-typical, not DoD official):

| Cost category | Range |
|---|---|
| Gap assessment | $3,500-$20,000 |
| Remediation and control implementation | $35,000-$250,000+ |
| Consultant / vCISO hourly | $250-$400/hour |
| Consultant / vCISO project total | $50,000-$300,000 |
| CUI enclave (managed) | $300-$400/user/month or $3,000-$4,000+/month flat |
| Required tooling annual (encryption, SIEM, endpoint, vulnerability scanning) | $10,000-$50,000+ |
| Staff time and lost productivity | Dozens to hundreds of hours |

**Cost by size profile, three-year total at Level 2 (practitioner-
typical ranges).**

| Profile | Three-year Level 2 total |
|---|---|
| Small (< 50 employees, narrow CUI footprint with enclave) | $150,000-$500,000 |
| Small (< 50 employees, broad CUI footprint without enclave) | $400,000-$800,000 |
| Medium (50-500 employees) | $750,000-$1,500,000 |
| Large (500+ employees) | $1,500,000+ (typically multi-million) |

These ranges are planning aids, not quotes. Specific C3PAO
engagement pricing and specific tooling costs vary; vendor
engagements produce the authoritative estimates.

---

## Compliance coverage recommendations by profile

All 110 NIST 800-171 practices apply at Level 2. Practices have
different implementation complexity and cost at different
profiles. The recommendations below are about prioritization
sequencing (which practices to invest in first for fastest
protection plus readiness) rather than scope (every Level 2
contract requires all 110). Priority timing framing below
("first-quarter" for small, "first-six-months" for medium) is
relative to when a contractor begins compliance investment;
with Phase 2 enforcement active since 2025-11-10 (per
`references/levels-and-assessment.md` phased-rollout
taxonomy), contractors
catching a DFARS 7012 clause on an active solicitation or
newly-awarded contract start the priority clock immediately and
compress the sequence as assessment deadlines dictate.

**Small profile — first-quarter priorities.**

1. Scope CUI accurately. Wrong scope dominates cost risk at
   small scale.
2. Deploy MFA everywhere (IA.L1-3.5.1, IA.L1-3.5.2, IA.L2-3.5.3).
   Cheap, high coverage, easy-to-evidence.
3. Stand up audit logging (AU.L2-3.3.1) with SIEM or log
   aggregation service.
4. Endpoint encryption (SC.L2-3.13.11 FIPS cryptography,
   SC.L2-3.13.16 data at rest) on all CUI-adjacent endpoints.
5. Draft SSP and POA&M (CA.L2-3.12.4, CA.L2-3.12.2) before
   investing in tooling. Scope drives tooling; tooling does
   not drive scope.

**Medium profile — first-six-months priorities.**

1. Tenancy migration to government-tier productivity (GCC High
   or Assured Controls Plus) if not already complete.
2. Formalize configuration management (CM domain) against a
   documented baseline.
3. Implement incident response plan (IR domain) with tabletop
   exercises.
4. Deploy dedicated GRC tooling or scale existing tooling to
   the compliance workload.
5. Establish assessment-readiness cycle separate from assessment
   delivery.

**Large profile — continuous priorities.**

1. Cross-BU consistency. Single SSP per assessment scope;
   consistent CUI-boundary definitions; consistent tooling.
2. Supply-chain discipline (SR domain not in L2 but
   increasingly in contract clauses). Vendor-access review
   cycles.
3. Red-team or purple-team adversarial assessments
   (SI.L2-3.14.7 unauthorized-use detection tested adversarially).
4. Acquisition integration discipline. CMMC migration plan for
   each acquisition; 18-month integration timeline with
   compliance milestones.
5. Continuous-monitoring technology maturity. UEBA, SOAR,
   case-management integration.

---

## Cross-domain anchors

Contractor-profile considerations compose with corpus cross-
cutting files and domain practice files:

- **CUI scoping.** `references/scoping-and-cui.md` — the most
  load-bearing upstream input to profile-driven compliance
  planning.
- **Levels and assessment.** `references/levels-and-assessment.md`
  — the L1 vs L2 determination that sets the cost envelope per
  profile.
- **SSP authoring.** `references/ssp-guidance.md` — SSP
  complexity scales with profile.
- **POA&M management.** `references/poam-management.md` —
  Conditional Certification deferral rules particularly
  relevant at small and medium profiles where resource
  constraints drive POA&M volume.
- **FedRAMP framing.** `references/fedramp-gap.md` —
  government-tenancy migration cost implications per profile.
- **Modern IT productivity.**
  `references/modern-it/productivity/README.md` and
  per-vendor files — tenancy-migration costs vary sharply by
  profile (enclave vs full migration).
- **Modern IT cloud platforms.**
  `references/modern-it/cloud-platforms/cloud-selection.md` —
  platform selection interacts with profile (single cloud
  commitment for small; multi-cloud for medium and large).
- **Modern IT AI services.**
  `references/modern-it/ai-services/README.md` — AI service
  adoption pattern varies by profile (managed services favored
  at small; self-hosted viable at medium and large).
- **Rev 3 transition.** `references/rev3-transition.md` —
  transition timing and cost impact varies by profile.

Domain practice files for requirement text and evidence lists:
all 14 CMMC domains at `references/domains/`.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/scoping-and-cui.md`,
`references/levels-and-assessment.md`, or previous references
are not repeated here.

**8(a).** SBA's business development program for socially and
economically disadvantaged small businesses. Regulations at 13
CFR Part 124.

**C3PAO (CMMC Third-Party Assessment Organization).** An
accredited assessor authorized to perform Level 2 and Level 3
certification assessments. Accreditation through The Cyber AB
(formerly the CMMC Accreditation Body; rebranded 2022).

**CISO (Chief Information Security Officer).** The executive
responsible for information-security program leadership.

**Enclave (CUI enclave).** An isolated IT environment scoped
to CUI workflow, architecturally separated from the
contractor's broader commercial IT footprint. Reduces
compliance scope at the cost of operational separation.

**GRC (Governance, Risk, Compliance).** The tooling and process
discipline covering policy management, risk register, control
assessment, and evidence collection. ServiceNow GRC, RSA
Archer, MetricStream, Vanta, Drata, Secureframe, Hyperproof are
common platforms.

**HUBZone (Historically Underutilized Business Zone).** SBA
set-aside program for firms in designated distressed areas.
Regulations at 13 CFR Part 126.

**MSP (Managed Service Provider).** A vendor that operates IT
services on the contractor's behalf. MSPs with CUI access are
within the contractor's CMMC scope.

**SBA (Small Business Administration).** The federal agency
administering small-business size standards, socioeconomic
set-aside certifications, and business-development programs.

**SBIR / STTR.** Small Business Innovation Research and Small
Business Technology Transfer — federal research programs that
sometimes intersect with CMMC when the research produces or
involves CUI.

**SDB (Small Disadvantaged Business).** SBA certification
(subset of 8(a)) for socially and economically disadvantaged
small businesses competing on SDB set-asides.

**SDVOSB (Service-Disabled Veteran-Owned Small Business).**
SBA-certified set-aside program per 13 CFR Part 128.

**Section 174.** US Internal Revenue Code Section 174 governing
R&D expense treatment; the 2022 Tax Cuts and Jobs Act
capitalization provisions affect contractor treatment of
cybersecurity-development spending.

**vCISO (virtual CISO).** A fractional CISO engagement where
the contractor retains CISO expertise on a part-time or
project basis rather than a full-time hire. Common pattern at
small and medium profiles.

**WOSB / EDWOSB (Women-Owned Small Business / Economically
Disadvantaged Women-Owned Small Business).** SBA-certified
set-aside programs per 13 CFR Part 127.

---

## Versioning and drift

Contractor-profile content drifts on several axes:

- **Cost projections.** DoD's 2023 regulatory impact analysis
  figures are stable anchors; practitioner-typical ranges
  shift with C3PAO availability, tooling market maturity, and
  wage inflation. Re-verify cost ranges against current market
  surveys before using in contract planning.
- **Set-aside regulations.** FAR Part 19 was overhauled in
  2025; 8(a) program changes were proposed in 2026. SBA
  regulations at 13 CFR Parts 121/124/126/127/128 update
  periodically. Verify current text at sba.gov/regulations
  before citing specific requirements.
- **CMMC enforcement timeline.** Per
  `references/levels-and-assessment.md`, Phase 1 is the
  2024-12-16 32 CFR program-rule effective date; Phase 2 is the
  2025-11-10 48 CFR acquisition-rule effective date; Phase 3
  begins 2026-11-10; Phase 4 begins 2027-11-10. Content below
  reflects the Phase 2 operating context.
- **SBA certification processes.** certify.sba.gov is the
  current authoritative portal for SDVOSB, WOSB, EDWOSB, 8(a),
  and HUBZone certifications. Process timing and documentation
  requirements update; verify current process before beginning
  a certification engagement.

Content verified 2026-04-21 against the cited primary sources.
Next full re-verification at the corpus review cycle or when
CMMC enforcement phase changes, when FAR Part 19 receives a
further update, or when SBA reorganizes certification
infrastructure.
