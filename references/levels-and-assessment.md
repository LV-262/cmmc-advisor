# CMMC 2.0 Levels and Assessment

> Source: 32 CFR Part 170 (CMMC Program Final Rule), CMMC Assessment Guide
> (dodcio.defense.gov), NIST SP 800-171 Rev 2

## Overview

The Cybersecurity Maturity Model Certification (CMMC) 2.0 program establishes
three certification levels for organizations in the Defense Industrial Base
(DIB). The level required depends on the type of information the contractor
handles and the sensitivity of the contract.

CMMC does not create new cybersecurity requirements. It verifies that
contractors have implemented requirements that have been in place since
DFARS 252.204-7012 was published in 2017. As Summit 7 puts it:
"CMMC isn't making you do the requirements; it's making sure you did the
requirements."

> Source: Summit 7 Blog, "CMMC is Published: What Now?"
> https://www.summit7.us/blog/cmmc-is-published-what-now

---

## The Three Levels

### Level 1 — Foundational

| Attribute | Detail |
|-----------|--------|
| **Information type** | Federal Contract Information (FCI) |
| **Practice count** | 17 practices |
| **Source standard** | FAR 52.204-21 (Basic Safeguarding) |
| **Assessment type** | Annual self-assessment |
| **Assessment body** | Organization itself |
| **Applies to** | All DoD contractors handling FCI |

Level 1 represents basic cyber hygiene. These 17 practices are the minimum
safeguards that any organization handling federal contract information should
have in place. Examples include using passwords, limiting physical access
to systems, and updating software.

**Key point for contractors:** If your contract involves only FCI (not CUI),
Level 1 is sufficient. Self-assessment means no third-party audit. You
assess yourself annually and submit results to the Supplier Performance
Risk System (SPRS).

> Source: 32 CFR 170.14, Level 1 Self-Assessment

---

### Level 2 — Advanced

| Attribute | Detail |
|-----------|--------|
| **Information type** | Controlled Unclassified Information (CUI) |
| **Practice count** | 110 practices |
| **Source standard** | NIST SP 800-171 Rev 2 |
| **Assessment type** | Self-assessment OR C3PAO third-party assessment |
| **Assessment body** | Organization (self) or Certified Third-Party Assessment Organization (C3PAO) |
| **Applies to** | DoD contractors handling CUI |

Level 2 is the most common certification target for DIB contractors. It
requires implementation of all 110 security requirements from NIST SP
800-171 Revision 2, organized across 14 domains.

**Self-assessment vs. C3PAO:**
- **Non-prioritized CUI contracts:** Annual self-assessment permitted
- **Prioritized CUI contracts:** Third-party C3PAO assessment required every three years

The distinction between prioritized and non-prioritized is made by the
DoD program manager in the contract solicitation. DoD has stated that
Level 2 self-assessments are the exception, not the rule; most CUI
contracts will require C3PAO assessment.

> Source: Summit 7 Blog, "DoD Says CMMC Level 2 Self-Assessments Are the
> Exception, Not the Rule"
> https://www.summit7.us/blog/cmmc-l2-self-assessments

**Cost context:**
- Level 2 self-assessment: approximately $37,000–$49,000
- Level 2 C3PAO assessment: approximately $105,000–$118,000

These estimates include preparation, remediation, and assessment fees.
Actual costs vary by organization size, complexity, and current posture.

> Source: Secureframe, "CMMC for Small Business: A Practical Guide to
> Compliance & Cost," https://secureframe.com/blog/cmmc-small-business

---

### Level 3 — Expert

| Attribute | Detail |
|-----------|--------|
| **Information type** | CUI for highest-sensitivity programs |
| **Practice count** | 134 practices (110 from 800-171r2 + 24 from 800-172) |
| **Source standard** | NIST SP 800-171 Rev 2 + NIST SP 800-172 |
| **Assessment type** | Government-led assessment |
| **Assessment body** | Defense Industrial Base Cybersecurity Assessment Center (DIBCAC) |
| **Applies to** | Contractors on the most sensitive DoD programs |

Level 3 adds 24 enhanced requirements from NIST SP 800-172 on top of the
110 Level 2 requirements. These address advanced persistent threats and
require capabilities like threat hunting, redundancy, and advanced
monitoring.

**Key point:** Level 3 is government-assessed. There is no self-assessment
or third-party option. DIBCAC conducts the assessment directly. This level
applies to a small subset of DIB contractors working on the most sensitive
programs.

> Source: 32 CFR 170.16, Level 3 Certification Assessment

---

## The 14 Domains

All 110 Level 2 practices are organized into 14 domains. Each domain
corresponds to a requirement family in NIST SP 800-171 Rev 2:

| Domain | ID | L1 Practices | L2 Practices | Total |
|--------|----|-------------|-------------|-------|
| Access Control | AC | 4 | 18 | 22 |
| Awareness and Training | AT | 0 | 3 | 3 |
| Audit and Accountability | AU | 0 | 9 | 9 |
| Configuration Management | CM | 0 | 9 | 9 |
| Identification and Authentication | IA | 2 | 9 | 11 |
| Incident Response | IR | 0 | 3 | 3 |
| Maintenance | MA | 0 | 6 | 6 |
| Media Protection | MP | 1 | 8 | 9 |
| Personnel Security | PS | 0 | 2 | 2 |
| Physical Protection | PE | 4 | 2 | 6 |
| Risk Assessment | RA | 0 | 3 | 3 |
| Security Assessment | CA | 0 | 4 | 4 |
| System and Communications Protection | SC | 2 | 14 | 16 |
| System and Information Integrity | SI | 4 | 3 | 7 |
| **Total** | | **17** | **93** | **110** |

> Source: CMMC Model Overview v2.0, dodcio.defense.gov

**Note:** The 17 Level 1 practices are a subset of the 110 Level 2 practices.
A Level 2 certification covers all Level 1 requirements automatically.

---

## Scoring Methodology

### How Scoring Works

Each of the 110 Level 2 practices is assessed as either **MET** or **NOT MET**.

The scoring system assigns point values to each practice. The maximum score
is 110 points (one point per practice in the simplest case). However, some
practices carry higher point values when they have multiple assessment
objectives, so a practice that is partially implemented may lose more than
one point.

**SPRS scoring:** Organizations calculate their SPRS (Supplier Performance
Risk System) score by starting at 110 and subtracting points for practices
that are NOT MET. The score is submitted to SPRS and is visible to DoD
contracting officers.

### Passing Threshold

- **Full certification:** All 110 practices MET (score of 110)
- **Conditional certification:** Minimum score of 80% with all critical
  practices met and unmet items documented in a POA&M

### Conditional Certification

If an organization achieves at least 80% but does not meet all 110 practices:

1. All practices scored as NOT MET must be **non-critical** (1-point items only) per 32 CFR 170.21
2. One exception per 32 CFR 170.21/170.23: SC.L2-3.13.11 (CUI encryption)
   can be on a POA&M when encryption exists but is not FIPS-validated (the
   3-point-deduction state of a 5-point practice per the DoD Assessment
   Methodology v1.2.1 partial-credit structure)
3. All NOT MET items must be documented in a Plan of Action & Milestones (POA&M)
4. All POA&M items must be closed within **180 days** per 32 CFR 170.21
5. A closeout assessment by the C3PAO must verify remediation

**If the 180-day deadline is missed:** Conditional status expires. The
organization loses its certification and must re-assess.

> Source: 32 CFR 170.21, POA&M Closeout; ISI Defense, "CMMC POA&Ms
> Explained: What You Can and Cannot Defer"
> https://isidefense.com/blog/cmmc-poams-explained-what-you-can-and-cannot-defer

### Practices That Cannot Be on a POA&M

Certain practices are designated as critical and must be fully implemented
at the time of assessment. These cannot be deferred to a POA&M. The specific
list is defined in the CMMC Assessment Guide, but the general principle is:
practices that represent fundamental security capabilities (such as those
protecting the confidentiality of CUI at rest and in transit) must be in
place before certification.

---

## Assessment Process

### Level 1 Self-Assessment

1. Organization reviews all 17 Level 1 practices
2. Assesses each practice as MET or NOT MET
3. Documents results
4. Submits SPRS score
5. Senior official affirms the assessment with a signed affirmation
6. Repeat annually

**Important:** The affirmation carries legal weight. A senior official is
attesting under penalty of law that the assessment is accurate. This is
not a checkbox exercise.

### Level 2 C3PAO Assessment

1. Organization prepares by implementing all 110 practices and documenting
   them in a System Security Plan (SSP)
2. Organization selects a C3PAO from The Cyber AB (formerly the CMMC Accreditation Body; rebranded 2022)
   marketplace
3. C3PAO conducts assessment:
   - Reviews SSP and supporting documentation
   - Examines evidence of practice implementation
   - Interviews personnel
   - Observes controls in operation
4. C3PAO issues assessment report
5. Results submitted to CMMC eMASS (Enterprise Mission Assurance Support Service)
6. Certification valid for three years (if fully certified) or 180 days
   (if conditional)

### Level 3 DIBCAC Assessment

1. Organization must first hold a Level 2 C3PAO certification
2. DIBCAC conducts the Level 3 assessment directly
3. Assesses the 24 additional practices from NIST SP 800-172
4. Government-led process with no third-party option

---

## Phased Rollout Timeline

CMMC implementation follows a four-phase rollout:

| Phase | Date | What Happens |
|-------|------|-------------|
| Phase 1 | December 16, 2024 | CMMC program rule effective. C3PAOs can begin L2 assessments. L1 self-assessments and L2 self-assessments may appear in contracts. |
| Phase 2 | November 10, 2025 | 48 CFR acquisition rule effective. CMMC requirements begin appearing in new DoD solicitations and contracts. L2 C3PAO assessments required for prioritized CUI. |
| Phase 3 | November 10, 2026 | L2 C3PAO assessments required more broadly. L3 DIBCAC assessments begin. |
| Phase 4 | November 10, 2027 | Full CMMC inclusion in all applicable DoD contracts (excluding COTS). |

> Source: Secureframe, "CMMC 2.0 Timeline: Key Dates & Deadlines Explained"
> https://secureframe.com/hub/cmmc/proposed-final-rule

**Current status (April 2026):** We are in Phase 2. CMMC requirements are
actively appearing in new DoD solicitations. Phase 3 enforcement begins
November 2026.

---

## Key Takeaways for Contractors

1. **Determine your level now.** Review your contracts and solicitations for
   CMMC level requirements. If you handle CUI, plan for Level 2.

2. **Start with scoping.** Define your CUI boundary before implementing
   controls. See `scoping-and-cui.md` for guidance.

3. **Self-assessment scores matter today.** Even before C3PAO assessment,
   your SPRS score is visible to contracting officers and affects contract
   eligibility.

4. **Budget for the assessment.** C3PAO assessments are a significant cost.
   Build this into your contract pricing and business planning.

5. **The 180-day clock is real.** If you pursue conditional certification,
   you must close all POA&M items within 180 days or lose certification.
   See `poam-management.md` for strategies.

6. **Primes set the pace.** Your prime contractor's CMMC requirements flow
   down to you. Engage early with your prime to understand their timeline
   and expectations.
