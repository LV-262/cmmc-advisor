# CUI Scoping and Boundary Definition

> Source: 32 CFR Part 170, NIST SP 800-171 Rev 2, CMMC Scoping Guidance
> (dodcio.defense.gov)

## Overview

Scoping is the single most impactful decision in your CMMC journey. A
well-defined boundary reduces the number of systems you must protect,
the evidence you must collect, and the cost of your assessment. A poorly
defined boundary expands your compliance surface unnecessarily or — worse —
leaves CUI unprotected in systems you thought were out of scope.

Get scoping right first. Everything else follows from it.

**FedRAMP interaction.** If CUI lives in an external cloud service, the
Defense Federal Acquisition Regulation Supplement (DFARS)
252.204-7012(b)(2)(ii)(D) requires the cloud service provider (CSP) to meet
Federal Risk and Authorization Management Program (FedRAMP) Moderate (or
equivalent) security requirements. See `references/fedramp-gap.md` "The
CUI Baseline Decision" for the clause text and the equivalency mechanics.
The CUI boundary and the CSP's FedRAMP authorization boundary are distinct
artifacts; see `references/fedramp-gap.md` "Boundary documentation depth"
for the two-boundary pattern. For platform-selection decisions across
AWS GovCloud, Azure Government, and Google Cloud Assured Workloads, see
`references/modern-it/cloud-platforms/cloud-selection.md`.

---

## FCI vs CUI

Understanding the difference between Federal Contract Information (FCI)
and Controlled Unclassified Information (CUI) determines which CMMC level
you need.

### Federal Contract Information (FCI)

Information provided by or generated for the Government under a contract
that is not intended for public release. FCI does not include information
provided by the Government to the public or simple transactional information.

**Examples:**
- Contract performance data
- Deliverable drafts
- Project schedules shared with the Government
- Technical drawings not marked as CUI

**CMMC requirement:** Level 1 (17 practices, self-assessment)

### Controlled Unclassified Information (CUI)

Information the Government creates or possesses that requires safeguarding
or dissemination controls consistent with applicable laws, regulations, and
government-wide policies. CUI is marked or designated as such by the
Government.

**Examples:**
- Technical data marked as CUI
- Export-controlled information (ITAR, EAR)
- Critical infrastructure information
- Personally identifiable information (PII) in Government records
- Law enforcement sensitive information

**CMMC requirement:** Level 2 (110 practices) or Level 3 (134 practices)

### The Critical Distinction

FCI is broadly defined — almost any non-public contract information qualifies.
CUI is specifically designated by the Government and carries marking
requirements. If your contract specifies DFARS 252.204-7012, you are handling
CUI and need at least Level 2.

**Common mistake:** Assuming you only handle FCI when your contract actually
involves CUI. Review your contract clauses carefully. If DFARS 7012 is
present, plan for Level 2.

> Source: 32 CFR 2002 (CUI Registry); FAR 52.204-21 (FCI safeguarding)

---

## Asset Categories for Scoping

CMMC 2.0 defines five categories of assets for scoping purposes. Understanding
these categories determines what falls inside your assessment boundary.

### 1. CUI Assets

Systems that process, store, or transmit CUI. These are always in scope
for your CMMC assessment.

**Examples:**
- File servers storing CUI documents
- Email systems transmitting CUI
- Development environments processing CUI data
- Databases containing CUI records

### 2. Security Protection Assets

Systems that provide security functions for CUI assets, even if they do
not process CUI directly.

**Examples:**
- Firewalls protecting the CUI network segment
- SIEM systems collecting logs from CUI assets
- Identity providers authenticating users to CUI systems
- Endpoint protection platforms managing CUI endpoints

**Key point:** These assets are in scope because a compromise of a security
protection asset could expose CUI. You cannot exclude your firewall from
scope just because it does not store CUI.

### 3. Contractor Risk Managed Assets

Assets that can — but are not intended to — process, store, or transmit CUI.
The contractor manages the risk of CUI exposure on these assets.

**Examples:**
- A general-purpose laptop that could access CUI systems but is not
  designated for CUI work
- A shared printer on the same network as CUI systems
- Conference room equipment connected to the CUI network

**Key point:** These assets are in scope but may have reduced assessment
requirements. Document how you manage the risk of CUI exposure on each.

### 4. Specialized Assets

Government property, IoT devices, operational technology, and test equipment
that may interact with CUI but cannot implement standard security controls.

**Examples:**
- Government-furnished equipment (GFE)
- Industrial control systems
- Laboratory test equipment
- IoT sensors in a manufacturing environment

**Key point:** These assets require specialized handling. Document what
controls can and cannot be applied, and what compensating measures are in place.

### 5. Out-of-Scope Assets

Assets that do not process, store, or transmit CUI and do not provide
security functions for CUI assets.

**Examples:**
- Public-facing marketing website
- HR system with no CUI
- Personal devices that never access CUI systems
- Guest Wi-Fi network fully isolated from CUI infrastructure

**Key point:** Properly isolating assets as out-of-scope reduces your
assessment surface. This is where enclave design becomes critical.

> Source: CMMC Assessment Guide, Level 2 Scoping (dodcio.defense.gov)

---

## Enclave Strategies

An enclave is a defined network segment or computing environment that
contains all CUI processing. Everything outside the enclave is out of scope
for CMMC assessment.

### When to Use an Enclave

**Use an enclave when:**
- Less than 60% of your systems handle CUI
- You have a small number of employees who work with CUI
- You want to minimize the cost and scope of your assessment
- You are a small contractor with limited IT resources

**Consider full-enterprise compliance when:**
- More than 60% of your systems handle CUI
- The cost of maintaining enclave boundaries exceeds the cost of
  enterprise-wide compliance
- Your business model requires most employees to access CUI regularly

> Source: Pivot Point Security, "CUI and FCI: Should We Keep Them Separate
> for CMMC Level 2 Compliance?"
> https://www.pivotpointsecurity.com/cui-and-fci-should-you-keep-them-separate-for-cmmc-level-2-compliance/

### Enclave Architecture Patterns

#### Pattern 1: Cloud VDI Enclave

All CUI processing occurs in virtual desktops hosted in a FedRAMP-authorized
cloud environment. Local endpoints are access terminals only.

**How it works:**
- CUI stays in the cloud (AWS GovCloud, Azure Government, or GCP Assured)
- Users access CUI through virtual desktop sessions
- Local devices never store CUI
- The enclave boundary is the cloud environment + VDI access controls

**Best for:** Small contractors, remote workforces, organizations with
limited on-premises infrastructure.

**Trade-offs:** Requires reliable internet connectivity. VDI licensing
adds cost. User experience may differ from native desktop.

#### Pattern 2: Dedicated Physical Enclave

A physically and logically separated network segment for CUI processing.

**How it works:**
- Dedicated hardware (computers, network equipment) for CUI work
- Separate network segment with its own firewall boundary
- Users switch between CUI and non-CUI systems
- Physical access controls on the CUI workspace

**Best for:** Organizations with on-premises infrastructure, manufacturing
environments, or situations where cloud VDI is not practical.

**Trade-offs:** Higher hardware costs. Dual-system workflow inconvenience.
Physical security requirements for the enclave space.

#### Pattern 3: Hybrid Enclave

Combines cloud-based CUI processing with enterprise non-CUI infrastructure.

**How it works:**
- Non-CUI work runs in commercial cloud (standard AWS, Azure, or GCP)
- CUI work runs in a FedRAMP-authorized environment (GovCloud, GCC High, Assured Workloads)
- Clear network boundaries between the two environments
- Users authenticated differently for each environment

**Best for:** Medium contractors who want cost-efficient non-CUI operations
while maintaining compliance for CUI work. Enables the broadest set of
commercial tools for non-CUI activities.

**Trade-offs:** More complex architecture. Boundary management requires
ongoing attention. Users must understand which environment to use for
which work.

---

## Scoping Best Practices

### 1. Start with Data Flow

Before defining your boundary, map where CUI flows:
- Where does CUI enter your organization? (email, file transfer, portal)
- Where is CUI stored? (file servers, databases, email archives, backups)
- Where is CUI processed? (workstations, development environments, applications)
- Where does CUI leave your organization? (deliverables, email, collaboration tools)
- Who touches CUI? (which roles, which teams)

This data flow map becomes the foundation of your SSP and your scoping decision.

### 2. Minimize Before You Protect

Reduce the number of systems that touch CUI before you start applying controls:
- Can you consolidate CUI storage to fewer systems?
- Can you limit CUI access to fewer people?
- Can you replace CUI email with a secure collaboration portal?
- Can you use an enclave to isolate CUI from your general network?

Every system removed from scope is a system you do not need to protect,
monitor, document, or include in your assessment.

### 3. Document Your Boundary

Your SSP must clearly describe:
- What is in scope (CUI assets, security protection assets, contractor risk managed assets)
- What is out of scope and why
- The boundary between in-scope and out-of-scope systems
- Network diagrams showing the enclave boundary
- Data flow diagrams showing CUI movement

Assessors will ask for this. If your boundary is unclear or undocumented,
expect scoping questions that expand your assessment.

### 4. Account for Backups and Archives

CUI in backups is still CUI. If your backup system captures CUI data,
the backup infrastructure is in scope. Consider:
- Do your backups include CUI? If so, the backup system is a CUI asset.
- Are backup tapes or cloud backup archives encrypted?
- Can you exclude CUI from general backups and create a separate, scoped
  backup process within the enclave?

### 5. Account for Email

Email is the most common vector for CUI scope expansion. If any employee
receives CUI via email, the entire email system may be in scope.

**Mitigation strategies:**
- Use a separate email system for CUI (e.g., GCC High for CUI, commercial
  for everything else)
- Implement DLP policies that flag CUI in commercial email
- Train users to redirect CUI received in commercial email to the
  compliant system
- Document your email handling procedures in the SSP

---

## Common Scoping Mistakes

1. **Assuming cloud = compliant.** Using AWS or Azure does not make you
   CMMC compliant. The cloud environment must be specifically configured
   for CMMC (GovCloud, GCC High, Assured Workloads) and you must implement
   your own controls on top of the cloud provider's shared responsibility.

2. **Forgetting security protection assets.** Your firewall, SIEM, and
   identity provider are in scope even if they never touch CUI directly.

3. **Ignoring personal devices.** If employees access CUI from personal
   devices (phones, tablets, home computers), those devices may be in scope.
   VDI is the cleanest solution — the device becomes an access terminal,
   not a CUI asset.

4. **Leaving CUI in commercial email.** One CUI-marked document in a
   commercial email inbox can bring the entire email infrastructure into
   scope.

5. **Scope creep from collaboration tools.** Slack, Teams, or shared drives
   used for both CUI and non-CUI work expand scope unnecessarily. Separate
   collaboration environments for CUI and non-CUI work.

6. **Not documenting out-of-scope decisions.** Assessors will ask why
   certain systems are out of scope. If you cannot explain and document the
   isolation, the assessor may consider them in scope.
