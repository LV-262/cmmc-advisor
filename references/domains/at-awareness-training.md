# Awareness and Training (AT)

> Source: NIST SP 800-171 Rev 2, Section 3.2; CMMC Assessment Guide Level 2

## Overview

Awareness and Training is the domain that turns policy into practice
in the heads of the people who operate the systems. The domain has 3
practices: AT.L2-3.2.1 (general awareness of security risks and
applicable policies), AT.L2-3.2.2 (role-based training for assigned
security duties), and AT.L2-3.2.3 (insider-threat recognition and
reporting). All three are at Level 2. No Level 1 AT practices exist,
so contractors handling only FCI have no awareness-and-training
requirement under this domain.

AT is the training hub for the rest of the skill.
Personnel Security (PS) establishes the pre-access screening gate
under PS.L2-3.9.1 before access authorization. Organizations may
also require completion of assigned training before granting access
as a separate internal policy. Personnel transfer under PS.L2-3.9.2
can prompt role-based training re-assignment.
Access Control (AC) content covers least-privilege and need-to-know
concepts. Identification and Authentication (IA) content covers
credential hygiene and multi-factor authentication.
Incident Response (IR) content covers insider-threat recognition and
tabletop participation under IR.L2-3.6.3.
Media Protection (MP) content covers CUI handling across physical
and digital forms.
Physical Protection (PE) content carries the alternate-work-site
safeguard training downstream from PE.L2-3.10.6.
AT.L2-3.2.1 is the locus for Phase 5 remote-work training content
referencing PE.L2-3.10.6 safeguards; AT.L2-3.2.2 is the locus for
role-based depth on IR team readiness and privileged-user training.

---

## Level 2 Practices

### AT.L2-3.2.1 — Awareness of Security Risks and Policies

**Requirement:** Ensure that managers, systems administrators, and
users of organizational systems are made aware of the security risks
associated with their activities and of the applicable policies,
standards, and procedures related to the security of those systems.

**Why it matters:** Users are the largest component of the attack
surface. Phishing, CUI mishandling, and careless credential disclosure
come from people, not from misconfigured systems. Awareness training
is the control that addresses the human layer; the other thirteen
domains assume it is working.

**Implementation guidance:**
- Differentiate content by audience. Managers need to understand risk
  acceptance, reporting obligations, and how security decisions affect
  their teams. Systems administrators need deeper coverage of
  privilege misuse, configuration drift, and incident triage. General
  users need practical content they can apply: phishing recognition,
  CUI handling, acceptable use, incident reporting, password hygiene
- Content must reference the actual SSP (System Security Plan) and
  site-specific procedures, not generic security-awareness material.
  Training that reads the same at any contractor site will fail the
  "applicable policies, standards, and procedures" portion of the
  requirement
- Required topics at a minimum: phishing recognition, CUI handling
  rules (marking, storage, transmission), incident reporting paths,
  acceptable-use boundaries, password hygiene, physical-security
  obligations (badge, visitor escort, device protection), mobile
  device and remote-work rules, social-engineering awareness
- Alternate-work-site safeguards from PE.L2-3.10.6 belong in the
  remote-work portion of base awareness training. Privacy filter use,
  locked storage, and household non-visibility are training-delivered
  controls that depend on user behavior; VPN routing is a technical
  control enforced by endpoint configuration that training must cover
  but does not substitute for those user-behavior safeguards.
- Cadence: at hire before access authorization, annually thereafter,
  and on material change to policy, threat environment, or
  organizational systems. The annual refresh is a floor, not a
  ceiling. Major policy changes or incident lessons-learned trigger
  interim training
- Delivery through an LMS (Learning Management System) or equivalent
  tracking system; paper sign-in sheets are acceptable for in-person
  briefings but completion evidence must aggregate per user
- Measure effectiveness, not just completion. Phishing-simulation
  click-through rates, knowledge-check scores, and incident-reporting
  rates are all measurable signals that training is producing behavior
  change

**Evidence to collect:**
- Awareness training policy defining scope, audience differentiation,
  and cadence
- Security awareness training curriculum and content (slides, video,
  interactive modules)
- LMS configuration showing enrollment and completion tracking
- Completion records per user with dates
- Sample training content demonstrating SSP and site-specific
  references
- Phishing-simulation results or equivalent effectiveness measures
- New-hire training completion records preceding access authorization

**Common mistakes:**
- Generic off-the-shelf awareness training that never references the
  actual SSP, site procedures, or role-specific risks
- Training at hire only, with no annual refresh; users operate on
  content that is three years stale
- Completion tracked in the LMS but effectiveness never measured;
  100% completion paired with high phishing-simulation click rates
- Alternate-work-site safeguards absent from the remote-work section,
  leaving PE.L2-3.10.6 requirements as paper-only controls
- Manager-specific content folded into general-user training rather
  than delivered as a distinct track

---

### AT.L2-3.2.2 — Role-Based Training

**Requirement:** Ensure that personnel are trained to carry out their
assigned information security-related duties and responsibilities.

**Why it matters:** Base awareness applies broadly. Role-based training
applies precisely. A systems administrator with general awareness but
no privileged-user training will misconfigure privilege boundaries; an
IR team member with no incident-handling training will fail the first
real incident. The practice requires specific training for specific
duties, not generic coverage.

**Implementation guidance:**
- Build a role-based training matrix mapping roles to required
  courses. Common role tracks: systems administrators (privileged-user
  responsibilities, baseline hardening, patch management), developers
  (secure coding, CUI handling in test environments, pre-commit
  controls), IR team members (incident handling per IR.L2-3.6.1,
  exercise participation per IR.L2-3.6.3), database administrators,
  cloud administrators, managers with security responsibilities
- Training content must be tied to specific duties in the role
  description. A title-based mapping ("all engineers take course X")
  misses duty-specific variance. A duty-based mapping ("anyone who
  makes production configuration changes takes course Y") matches the
  requirement
- Role-based training is re-assigned on transfer or role change. When
  PS.L2-3.9.2 fires a transfer, the role-based training curriculum for
  the new role is added; prior-role training does not carry forward
  automatically. The reciprocal link to PS.L2-3.9.2 is operational,
  not decorative
- External training is acceptable when tied to role duties: vendor
  courses on specific platforms, conference training sessions, formal
  certifications. Evidence must connect the external content to the
  role's security-related duties
- Frequency tied to role risk and change rate. Privileged-user
  training refreshes more frequently than manager-level training
  because the privilege surface changes faster. Annual is a reasonable
  floor for most roles; semiannual is appropriate where tooling
  changes that quickly
- Verify competency, not just completion. A completion record
  showing attendance does not demonstrate the person can execute the
  duty. Assessments, certifications, practical exercises, or supervisor
  sign-off close this gap

**Evidence to collect:**
- Role-based training matrix mapping each security-related role to
  required curriculum
- Per-role training content and delivery records
- Completion records broken out by role and course
- Competency verification artifacts: assessments, certifications,
  practical-exercise results, supervisor attestations
- Transfer records from HR showing training re-assignment triggered by
  PS.L2-3.9.2 personnel actions
- External-training evidence tied to specific role duties

**Common mistakes:**
- Role-based training in policy but universal content in practice;
  every role takes the same course
- Completion tracked but competency never verified; the training
  reduces to attendance
- IR team members trained to general-user level only; the team fails
  the first functional exercise under IR.L2-3.6.3
- Transfer via PS.L2-3.9.2 happens but training re-assignment does
  not; the employee in the new role operates on the prior role's
  training
- Privileged users trained identically to general users; the privilege
  risk surface is not addressed
- External-training certificates accepted as evidence without mapping
  to role duties

---

### AT.L2-3.2.3 — Insider-Threat Training

**Requirement:** Provide security awareness training on recognizing
and reporting potential indicators of insider threat.

**Why it matters:** Insider-threat incidents are the hardest to detect
with technical controls because the actor is already authorized. The
control that closes the detection gap is peer and manager recognition,
and the control that converts recognition into response is a reporting
path the reporter trusts.

**Implementation guidance:**
- Training content covers recognizable indicators. Common categories:
  job dissatisfaction expressed as explicit discontent with the
  organization, unauthorized access attempts or probing, unexplained
  access to resources outside stated duties, policy violations that
  cluster, behavioral changes correlated with stressors, attempts to
  acquire resources not tied to assigned work
- Training should include a reporting path that does not require
  routing through the suspected individual's management chain. The
  standard requires recognition and reporting; the chain-of-command
  bypass is a program design choice that closes a practical gap. A
  path through IR intake (IR.L2-3.6.2) or through a designated
  security contact avoids the single-point-of-failure where the person
  the reporter is worried about is also the person they would have to
  tell
- Reporter protection: training should state that good-faith reports
  are protected from retaliation and that reports are investigated
  before action is taken. Absent this assurance, the training teaches
  recognition without producing reports
- Manager-level content addresses a different audience: managers
  recognize indicators in reports from their teams, and know how to
  escalate without creating a hostile-environment claim. The general-
  user content teaches "what to notice"; the manager content teaches
  "what to do when your team notices"
- Tabletop participation under IR.L2-3.6.3 connects training to
  practice. Insider-threat scenarios in the exercise rotation validate
  that the reporting path is live and that the IR team can handle the
  intake

**Evidence to collect:**
- Insider-threat training content, both general-user and manager-level
- Completion records per audience tier
- Reporting-path documentation showing paths that avoid chain-of-
  command dependency
- Reporter-protection language in policy and training content
- IR intake capability for insider-threat reports (cross-reference to
  IR.L2-3.6.2 case management)
- Tabletop records showing insider-threat scenarios exercised under
  IR.L2-3.6.3

**Common mistakes:**
- Content lists indicators but never explains the reporting path
- Reporting path routes only up the chain of command, creating the
  single-point-of-failure scenario
- No manager-level content; managers receive the same training as
  general users and don't know how to handle reports that come up
- No reporter-protection language; employees trained to recognize but
  afraid to report
- Training never updated with lessons-learned from real insider-threat
  incidents or from exercise findings

---

## Domain Summary

| Practices | Level 1 | Level 2 | Total |
|-----------|---------|---------|-------|
| Count | 0 | 3 | 3 |

**Assessment priority:** Start with AT.L2-3.2.1. Base awareness is the
foundation on which AT.L2-3.2.2 role-based depth and AT.L2-3.2.3
insider-threat specifics build. A contractor with weak base awareness
will have role-based training that works in isolation but fails to
build on a shared security posture. Then focus on AT.L2-3.2.2 because
role-based training is the practice most likely to exist in policy
but collapse to universal content in implementation. AT.L2-3.2.3
passes or fails primarily on whether the reporting path is credible,
which is a design choice more than a content choice.

**Key relationships:**
- Personnel Security (PS) establishes the pre-access screening gate
  under PS.L2-3.9.1 that training completion must clear before access
  authorization; PS.L2-3.9.2 personnel actions trigger role-based
  training re-assignment on transfer
- Access Control (AC) provides the content backbone for
  least-privilege and need-to-know training in both base awareness and
  role-based tracks
- Identification and Authentication (IA) supplies credential-hygiene,
  multi-factor-authentication, and session-management content for
  training
- Incident Response (IR) is the audience for insider-threat reporting
  under AT.L2-3.2.3 and is where IR team role-based training lands
  under AT.L2-3.2.2, with tabletop participation satisfying
  IR.L2-3.6.3 exercises
- Media Protection (MP) training covers CUI handling across physical
  media, portable storage, and alternate-work-site artifacts
- Physical Protection (PE) supplies the alternate-work-site safeguard
  training that lands in AT.L2-3.2.1 base awareness, tied to
  PE.L2-3.10.6 remote-work requirements
