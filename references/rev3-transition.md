# NIST SP 800-171 Rev 3 Transition

> Source: NIST SP 800-171 Rev 3, ISI Defense Rev 2 vs Rev 3 analysis,
> Secureframe transition guidance, Summit 7 blog

## Current Status (April 2026)

**CMMC Level 2 is built on NIST SP 800-171 Revision 2.** This is the
current legal requirement. All assessments — self-assessment, C3PAO,
and DIBCAC — evaluate against Rev 2.

NIST published SP 800-171 Revision 3 in May 2024, but it has **not yet
been adopted by the CMMC program.** A DoD class deviation keeps Rev 2
as the enforceable standard, and this deviation has no published end date.

**Bottom line:** Build to Rev 2 now. Track Rev 3 changes. Do not spend
resources implementing Rev 3 requirements until DoD formally adopts it.

> Source: ISI Defense, "NIST 800-171 Rev. 2 vs Rev. 3: What Defense
> Contractors Need to Know"
> https://isidefense.com/blog/nist-800-171-rev-2-vs-rev-3-what-defense-contractors-need-to-know-now

---

## Transition Timeline

### What We Know

| Date | Event |
|------|-------|
| February 2020 | NIST SP 800-171 Rev 2 published |
| May 2024 | NIST SP 800-171 Rev 3 published |
| December 2024 | CMMC 2.0 program rule effective (based on Rev 2) |
| November 2025 | 48 CFR acquisition rule effective (Rev 2 baseline) |
| April 2026 | DoD class deviation still active — Rev 2 remains the standard |

### What We Expect

Industry consensus estimates the earliest realistic date for a formal
Rev 3 requirement is **H2 2027**, and even then a **12-18 month transition
period** before enforcement is expected. This means Rev 3 enforcement
is unlikely before 2029.

**Signals from DoD:**
- DoD has begun defining Organization-Defined Parameter (ODP) values for
  Rev 3 controls, signaling preparation for eventual adoption
- No formal rulemaking has been initiated to update CMMC from Rev 2 to Rev 3
- The class deviation has no published expiration date

---

## Key Changes in Rev 3

### Structural Changes

Rev 3 reorganizes the framework significantly:

| Aspect | Rev 2 | Rev 3 |
|--------|-------|-------|
| Requirement count | 110 | 97 (but many are consolidated, not removed) |
| Organization | 14 families | 17 control families (aligned with 800-53) |
| Tailoring | Pre-tailored from 800-53 | Organization-Defined Parameters (ODPs) |
| Assessment alignment | 800-171A | Integrated assessment procedures |

### What Changed Substantively

**New capabilities required in Rev 3:**
- Enhanced supply chain risk management requirements
- Expanded privacy controls
- More specific incident reporting requirements
- Stronger requirements for system and service acquisition

**Removed or consolidated:**
- Some requirements that were duplicative have been merged
- Requirements that map better to organizational policy (vs. technical
  controls) have been restructured

**Organization-Defined Parameters (ODPs):**
Rev 3 introduces ODPs — values that the organization must define for
certain requirements. For example, instead of prescribing a specific
password length, Rev 3 requires the organization to define and document
their minimum password length. DoD will define the specific ODP values
that apply to CMMC when they adopt Rev 3.

---

## Practical Guidance

### If You Have Not Started CMMC Compliance

**Start with Rev 2.** It is the current legal requirement and will remain
so for at least the next 1-2 years. Every practice you implement for Rev 2
will carry forward to Rev 3 — the security capabilities are the same,
even if the requirement numbering and structure change.

Do not wait for Rev 3 to begin your compliance journey. Contracts are
being awarded now with CMMC requirements based on Rev 2. Waiting means
losing contract eligibility.

### If You Are Currently Implementing Rev 2

**Continue with Rev 2.** Complete your current implementation and assessment.
A Rev 2 certification demonstrates compliance and satisfies current contract
requirements. When Rev 3 is adopted, you will have a solid security
foundation to map to the new structure.

**Start awareness activities:**
- Download and read NIST SP 800-171 Rev 3
- Identify the major structural differences
- Note new requirements that do not exist in Rev 2
- Track DoD announcements regarding Rev 3 adoption timeline

### If You Already Hold a Rev 2 Certification

**Your certification is valid for its full three-year period.** There is
no indication that existing Rev 2 certifications will be invalidated when
Rev 3 is adopted. Expect a transition period where both versions are
accepted.

When your certification comes up for renewal, it will likely be assessed
against whichever revision is in effect at that time. Plan your renewal
timeline accordingly.

---

## Mapping Rev 2 to Rev 3

A detailed mapping between Rev 2 and Rev 3 requirements is available from
NIST. The key insight: most Rev 2 requirements have direct equivalents in
Rev 3, though they may be numbered differently or organized into different
families.

Organizations that have fully implemented Rev 2 will find that the majority
of their controls satisfy Rev 3 requirements with minimal adjustment. The
primary work will be:

1. **Remapping documentation** — updating SSP practice references from
   Rev 2 numbering to Rev 3 numbering
2. **Defining ODPs** — establishing organization-defined parameter values
   per DoD guidance
3. **Addressing new requirements** — implementing any genuinely new
   capabilities required by Rev 3 that have no Rev 2 equivalent
4. **Updating evidence** — collecting evidence against the new assessment
   procedures

**This is documentation and tuning work, not a ground-up rebuild.** If
your Rev 2 implementation is solid, the Rev 3 transition should be
measured in weeks, not months.

> Source: NIST SP 800-171 Rev 3, Appendix C — Analysis of Changes;
> Secureframe, "NIST 800-171 Rev 2 vs Rev 3: What Changed and What It
> Means for CMMC"
> https://secureframe.com/blog/nist-800-171-rev2-vs-rev3

---

## What to Watch

Track these signals for Rev 3 adoption timing:

1. **DoD class deviation update** — When DoD rescinds or modifies the
   class deviation that keeps Rev 2 as the standard, the transition
   clock begins
2. **CMMC rulemaking** — A new proposed rule updating CMMC to Rev 3
   will go through the Federal Register process with a public comment
   period
3. **ODP publication** — DoD publication of specific ODP values for
   CMMC Rev 3 signals imminent adoption
4. **Cyber AB guidance** — The CMMC Accreditation Body will publish
   assessor guidance for Rev 3 assessments
5. **Summit 7 / Jacob Horne analysis** — Jacob Horne's Sum IT Up
   podcast and Summit 7 blog consistently provide early and accurate
   analysis of CMMC rulemaking developments:
   https://www.summit7.us/podcast
