# System Security Plan (SSP) Guidance

> Source: NIST SP 800-171 Rev 2 (Section 3.12.4), NIST SP 800-171A,
> CMMC Assessment Guide Level 2, 32 CFR Part 170

## Overview

The System Security Plan is the single most important document in your
CMMC assessment. It describes your system, your CUI boundary, and how you
implement each of the 110 Level 2 security practices. Assessors use your
SSP as the roadmap for the entire assessment — if the SSP is incomplete
or inaccurate, the assessment stalls before it starts.

The SSP is not a compliance artifact to be written at the end. It is a
living document that reflects your actual security posture. Write it as
you build your controls, not after.

> Source: NIST SP 800-171 Rev 2, Practice 3.12.4: "Develop, document, and
> periodically update system security plans that describe system boundaries,
> system environments of operation, how security requirements are implemented,
> and the relationships with or connections to other systems."

---

## SSP Structure

A CMMC-ready SSP should contain the following sections. This structure
aligns with the NIST CUI SSP Template available at:
https://csrc.nist.gov/files/pubs/sp/800/171/r2/upd1/final/docs/cui-ssp-template-final.docx

### 1. System Identification

| Element | What to Document |
|---------|------------------|
| System name | The name used consistently across all documentation |
| System owner | The individual accountable for the system |
| System description | What the system does and its purpose |
| Information types | FCI, CUI, CUI categories handled |
| System environment | Cloud, on-premises, hybrid — the physical and logical environment |
| System status | Operational, under development, undergoing modification |

### 2. System Boundary

This is where scoping decisions are documented. Include:

- **Network diagram** showing all in-scope systems, network segments,
  and boundary points. Assessors expect this. A missing network diagram
  is one of the most common SSP gaps.
- **Data flow diagram** showing how CUI enters, moves through, and exits
  your environment. Include ingress points (email, file transfer, portals),
  processing locations, storage locations, and egress points (deliverables,
  collaboration tools).
- **Asset inventory** categorized by the five CMMC scoping categories:
  CUI Assets, Security Protection Assets, Contractor Risk Managed Assets,
  Specialized Assets, and Out-of-Scope Assets. See `scoping-and-cui.md`
  for definitions.
- **Boundary justification** explaining why out-of-scope assets are
  excluded and how isolation is maintained.

### 3. Security Personnel

| Role | What to Document |
|------|------------------|
| System Security Officer | Name, contact, responsibilities |
| System Administrator | Name, contact, responsibilities |
| Authorizing Official / Senior Leader | Name, contact — the person who signs the affirmation |
| IT Security Staff | Names, roles, training status |

**Common gap:** Listing generic role titles without named individuals.
Assessors want to know who is accountable, not what the org chart looks like.

### 4. Practice Implementation Statements

For each of the 110 Level 2 practices, document:

- **Practice ID and title** (e.g., AC.L2-3.1.1 — Authorized Access Control)
- **Implementation status:** Implemented, Partially Implemented, Planned, Not Applicable
- **Implementation description:** How your organization satisfies this
  practice in your specific environment. This is the core of the SSP.
- **Responsible role:** Who is responsible for maintaining this control
- **Tools or technologies used:** Specific products, configurations, or
  processes that implement the control
- **Evidence pointers:** Where the assessor can find proof of implementation

**Critical guidance on implementation descriptions:**

Write what you actually do, not what the requirement says. The NIST
requirement text says "limit system access to authorized users." Your
implementation description says: "Access to the CUI enclave is controlled
through Azure Active Directory with conditional access policies requiring
MFA. User provisioning follows the onboarding checklist in HR-SEC-001.
Terminated user accounts are disabled within 24 hours per procedure
IT-ACC-003."

The implementation description should be specific enough that a new
IT administrator could understand exactly how the control works by
reading it.

### 5. System Interconnections

Document connections between your in-scope system and any external systems:

| External System | Organization | Connection Type | Data Exchanged | Authorization |
|-----------------|-------------|-----------------|----------------|---------------|
| DoD SAFE | DISA | SFTP | CUI deliverables | DFARS 7012 |
| Prime portal | [Prime name] | HTTPS | CUI documents | Subcontract |
| Cloud provider | AWS/Azure/GCP | API/Console | CUI processing | FedRAMP auth |

### 6. Continuous Monitoring

Describe how you maintain your security posture over time:

- How often are controls assessed internally?
- What automated monitoring is in place? (SIEM, endpoint detection, log review)
- How are configuration changes tracked?
- How are new vulnerabilities identified and remediated?
- When is the SSP reviewed and updated?

---

## What Assessors Actually Look For

Based on publicly available C3PAO guidance and assessment preparation
materials:

### The Big Three

1. **Accuracy over polish.** Assessors care that the SSP reflects reality,
   not that it reads beautifully. A rough but accurate SSP is better than
   a polished but fictional one. If your implementation description says
   you do something and the assessor finds you don't, that is a finding.

2. **Specificity.** "We use firewalls" is not an implementation description.
   "Palo Alto PA-850 at the CUI enclave boundary, configured with rule set
   FW-CUI-2024-03, reviewed quarterly by the system administrator" is.

3. **Consistency across artifacts.** The SSP, the network diagram, the
   asset inventory, and the evidence must all tell the same story. If the
   SSP says you have 50 endpoints and the asset inventory lists 73, the
   assessor will ask which is correct.

### Practice-Level Assessment

For each practice, the assessor evaluates three things:

1. **Is the practice documented?** (SSP implementation description exists)
2. **Is the practice implemented?** (Evidence shows it works)
3. **Is the practice effective?** (It actually achieves the security objective)

A practice can be documented but not implemented (fiction). It can be
implemented but not documented (gap in the SSP). It can be implemented
and documented but not effective (security theater). All three must be
true for a MET determination.

### Evidence the Assessor Will Request

Assessors don't just read the SSP. They verify it against evidence:

- **Configuration screenshots** showing actual settings match SSP descriptions
- **Policy documents** referenced in the SSP
- **Procedure documents** for operational controls
- **Log samples** showing controls are active and monitored
- **Training records** showing personnel completed required training
- **Scan results** from vulnerability assessments
- **Incident response test results** showing IR plan has been exercised
- **Account management records** showing provisioning and deprovisioning
- **Personnel interviews** confirming staff understand their responsibilities

See `evidence-collection.md` for domain-specific evidence guidance.

---

## Common SSP Gaps

### 1. Missing Network Diagram

The most frequently cited gap. Every SSP needs a network diagram showing
the CUI boundary, network segments, key security devices, and
interconnections. It does not need to be a work of art — it needs to be
accurate and current.

**Fix:** Use any diagramming tool (draw.io, Visio, Lucidchart). Show
the CUI enclave boundary clearly. Label all in-scope network segments.
Show firewalls, switches, and key servers. Update it when the network
changes.

### 2. Missing Data Flow Diagram

Where does CUI enter? Where does it go? Where is it stored? Where does
it leave? If you cannot draw this, you do not understand your own
CUI boundary.

**Fix:** Trace the lifecycle of a single CUI document through your
environment. Map every system it touches. That is your data flow diagram.

### 3. Generic Implementation Descriptions

"Access is controlled" or "encryption is used" without specifics. These
descriptions tell the assessor nothing about your actual implementation.

**Fix:** Name the tool. Name the configuration. Name the procedure.
Name the responsible person. Be specific enough that someone unfamiliar
with your environment could understand exactly what you do.

### 4. Missing Asset Categories

The SSP lists CUI assets but omits Security Protection Assets or
Contractor Risk Managed Assets. This causes scoping errors that can
expand the assessment unexpectedly.

**Fix:** Use the five CMMC scoping categories. Document every in-scope
asset and justify every out-of-scope exclusion.

### 5. Stale Content

The SSP was written 18 months ago and hasn't been updated. The network
has changed, new tools have been deployed, and personnel have turned over.

**Fix:** Review the SSP quarterly at minimum. Update it whenever there
is a significant change (new system, new tool, new personnel, network
change). Date every update.

### 6. No Interconnection Documentation

External connections exist but are not documented. Cloud services,
prime contractor portals, and file transfer mechanisms all need to be
captured.

**Fix:** Audit all connections that enter or leave your CUI boundary.
Document each one with the external organization, connection type, data
exchanged, and authorization basis.

---

## SSP Maintenance

The SSP is not a one-time document. It requires ongoing maintenance:

| Activity | Frequency | Who |
|----------|-----------|-----|
| Full SSP review | Quarterly | System Security Officer |
| Update after significant change | Within 30 days of change | System Administrator + SSO |
| Asset inventory reconciliation | Monthly | IT Administrator |
| Network diagram verification | Quarterly | Network Administrator |
| Practice status review | Quarterly | System Security Officer |
| Pre-assessment SSP audit | 90 days before assessment | Entire security team |

**Tip:** Tie SSP updates to your change management process. If a change
request modifies the CUI environment, the SSP update is part of the
change — not a separate task to remember later.

---

## Tools for SSP Management

Several approaches exist for maintaining your SSP:

- **Document-based:** Word document or markdown files, version-controlled
  in git. Simple, low cost, works for small organizations. Risk: becomes
  unwieldy as the system grows.

- **GRC platforms:** Tools like RegScale, eMASS, or similar platforms
  provide structured SSP management with built-in templates, evidence
  linking, and assessment tracking. Cost: higher, but scales better.

- **OSCAL-based:** Machine-readable SSP using NIST's Open Security Controls
  Assessment Language. Enables automated validation and continuous
  monitoring integration. Emerging approach — not required but future-aligned.

Choose the approach that matches your organization's size, budget, and
technical capability. A well-maintained Word document beats a neglected
GRC platform.
