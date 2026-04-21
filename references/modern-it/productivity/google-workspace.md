# Google Workspace Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); DFARS 252.204-7012; 32 CFR Part 170 CMMC Program Final
> Rule (effective 2024-12-16); 48 CFR Parts 204/212/217/252
> acquisition rule (effective 2025-11-10); FedRAMP Marketplace
> (marketplace.fedramp.gov); Google Cloud CMMC page
> (cloud.google.com/security/compliance/cmmc); Google Workspace
> CMMC Implementation Guide (published 2025); Assured Controls
> Plus documentation (support.google.com/a/answer/13880647);
> Google Workspace C3PAO CMMC attestation letter (2025); DoD
> CSP SRG v1r1 (public.cyber.mil); NIST CMVP validated modules
> registry (csrc.nist.gov).

## Overview

This file maps Google Workspace capability patterns to CMMC
practice requirements for defense contractors handling CUI or
FCI. Google Workspace is the authoritative owner in this corpus
of the Assured Controls Plus overlay-configuration decision per
Phase 5d hub Decision 6; Phase 5c's
`references/modern-it/cloud-platforms/gcp-assured.md` keeps a
terminology pointer rather than re-deriving the Workspace-side
story.

**The architectural distinction from M365 GCC High is
load-bearing.** Google Workspace Assured Controls Plus delivers
CUI-capable compliance through a *control-package overlay* on
commercial Google Workspace, not through a sovereign tenancy
partition. Microsoft 365 GCC High is a physically and logically
separate tenancy with its own partition, directories, and
operator staff; Workspace Assured Controls Plus is the
Enterprise Plus edition plus an add-on that configures
Organization Policy, data residency, personnel access, and
encryption controls inside the commercial Workspace
infrastructure. A contractor reading from
`microsoft-365-gcc.md` expects a sovereign-tenancy answer;
Workspace delivers the same compliance outcome via a different
mechanism that the contractor must understand before making the
vendor decision.

**FedRAMP authorization summary (verified 2026-04-21).** Google
Workspace holds FedRAMP High and FedRAMP Moderate
Provisional Authorities to Operate (P-ATOs) through the
FedRAMP Joint Authorization Board (JAB) on in-scope services. A contractor
using Google Workspace for CMMC Level 2 CUI work must use
FedRAMP High authorized services and enable Assured Controls
Plus for data-residency and personnel-access controls per
Google's published CMMC guidance at
cloud.google.com/security/compliance/cmmc. Per-service
authorization scope is documented at the Google Cloud
compliance pages and the FedRAMP Marketplace; verify the
current service-level scope before citing in an SSP.

**DoD Impact Level coverage (verified 2026-04-21).** Google
Workspace Assured Controls Plus supports IL4-aligned CUI
workloads. Google Workspace does not hold an IL5 Provisional
Authorization as of this slice's verification date; IL5 for the
productivity plane requires Microsoft 365 GCC High or an
alternative path. A contractor whose contract vehicle requires
IL5 at the productivity layer must consider M365 GCC High
rather than Workspace. See
`references/modern-it/cloud-platforms/cloud-selection.md`
"FedRAMP baseline to DoD Impact Level crosswalk" for the
IL-to-FedRAMP mapping.

**C3PAO attestation.** Google has produced a 2025-dated C3PAO
attestation letter for Google Workspace CMMC compliance
supporting DFARS 7012 contractors. The letter is available at
services.google.com/fh/files/misc/gwsattestation2025.pdf;
verify currency before citing.

---

## Scope of this file

Covered:

- Google Workspace editions (Business Starter, Business Standard,
  Business Plus, Enterprise Standard, Enterprise Plus) with the
  CMMC-relevant path through Enterprise Plus plus Assured
  Controls Plus.
- Per-service Workspace posture (Gmail, Drive, Meet, Chat,
  Calendar, Docs, Sheets, Slides, Keep, Forms, Sites, Admin
  Console).
- Cloud Identity posture for workforce identity.
- DLP, Vault for eDiscovery and retention, Context-Aware Access,
  Client-Side Encryption with external key management.
- ITAR posture via data-residency + personnel + contract
  overlay (distinct from M365 GCC High sovereign-tenancy ITAR
  story).
- Support and operator-access posture.

Not covered:

- Google Cloud platform services (Compute Engine, Cloud
  Storage, BigQuery, Cloud SQL, other IaaS/PaaS). Those live in
  `references/modern-it/cloud-platforms/gcp-assured.md` with
  the Assured Workloads compliance overlay, which is distinct
  from Assured Controls Plus.
- Google Workspace for Education variants, non-US Workspace
  editions, or sovereign-controls-by-partners configurations
  (EU Data Boundary, regional sovereignty packages). Scope is
  US federal contractor CUI work.
- Generative AI features (Gemini for Workspace). Generative AI
  scope considerations are covered under
  `references/modern-it/ai-services/`.
- Consumer Gmail and personal Google Accounts. Consumer-grade
  products are not CUI-capable.

---

## Tenancy Selection

Per hub Decision 3, this section answers three questions in
order. The three-question structure is symmetric with
`microsoft-365-gcc.md`; the answers differ because Workspace's
architecture is an overlay rather than a sovereign tenancy.

**1. Is Google Workspace Commercial (without Assured Controls
Plus) ever acceptable for CUI?** No. Commercial Workspace
without Assured Controls Plus carries FedRAMP Moderate or High
on in-scope services but does not enforce the US-only data
residency, US-person personnel access, and contractual ITAR
commitments that DFARS 7012 CUI posture requires. A contractor
running CUI in commercial Workspace without the Assured
Controls Plus overlay has a scope problem, not a tuning
problem; the fix is enabling Assured Controls Plus (subject to
Enterprise Plus edition licensing), not configuration
tightening.

**2. Which overlay or control-plane configuration is the
contractor path: base Assured Controls, Assured Controls Plus,
or neither?** For CMMC Level 2 CUI work under DFARS 7012, the
answer is **Assured Controls Plus**. Base Assured Controls
provides a lighter-weight overlay (some personnel and
data-residency assurances) for non-CUI federal and regulated
workloads but is insufficient for DFARS-scope CUI. Assured
Controls Plus delivers the US-only data storage, US-person
access controls, FIPS 140-validated encryption, and
contractual commitments that CMMC Level 2 contractors require.
Enterprise Plus edition is the licensing prerequisite for
Assured Controls Plus.

**Regulatory mechanics behind the Assured Controls Plus
requirement.** DFARS 252.204-7012(b)(2)(ii)(D) requires FedRAMP
Moderate equivalence for CSPs handling CUI; Google Workspace
commercial services with FedRAMP Moderate or High on specific
services satisfy the equivalence threshold at the authorization
layer. The Assured Controls Plus overlay adds the
data-residency, personnel-access, and contractual commitments
that DFARS 7012 imposes beyond the FedRAMP authorization
itself. The contractor enables Assured Controls Plus at the
Workspace organization level; controls cascade to all in-scope
Workspace services under the overlay.

**Management-plane consistency.** Workspace identity (Cloud
Identity or Workspace-native accounts) must run under the same
Assured Controls Plus overlay as the productivity services.
Federating Workspace CUI workloads against an external identity
provider that is not CUI-capable pulls the CUI boundary into
the external identity plane and undermines the overlay's
personnel-access commitment.

**3. What workload-location and support-personnel-citizenship
boundaries apply under Assured Controls Plus?** Assured
Controls Plus enforces US-only data storage for covered
services (customer content resides in US Google Cloud regions).
Google personnel access to customer data under Assured Controls
Plus is restricted to US-persons with enhanced background
checks, enforced at the control-package level rather than at a
tenancy-partition level. Support case handling runs with
US-person personnel when the case is raised against an Assured
Controls Plus-enabled organization.

The contractor-side personnel posture is distinct from the
Google-side posture. A non-US-person contractor employee
cannot serve as a Google support escalation contact in an
Assured Controls Plus organization, and may or may not be
permitted to administer the contractor's own Workspace
organization depending on the contract's export-control terms.
If ITAR-controlled or EAR-controlled technical data is present,
US-person-only staffing may apply to the contractor side as
well; consult export-control counsel before finalizing
personnel policy.

**Architectural-model choice note.** Contractors with IL4-scope
CUI can choose either Microsoft 365 GCC High (sovereign tenancy,
IL5-aligned, FedRAMP High) or Workspace Assured Controls Plus
(overlay on commercial Workspace, IL4-aligned, FedRAMP High on
in-scope services). This is a choice between architectural
models (sovereign partition versus control-package overlay)
as much as between vendors. The "ITAR posture under Assured
Controls Plus" section below carries the architectural
comparison in depth.

---

## Edition and organization model

**Capability.** Google Workspace licensing comes in editions
targeting different organizational needs. For CMMC Level 2 CUI
work, the relevant edition is Enterprise Plus, which is the
prerequisite for Assured Controls Plus. An organization's
Workspace account holds domains, users, groups, and Organization
Policies; Cloud Identity is the companion identity-only SKU for
organizations that separate identity licensing from productivity
licensing. Organizational Units (OUs) inside the Workspace
organization provide hierarchical scope for configuration
policies.

**CMMC practices implemented.** CM.L2-3.4.1 (baseline
configuration), CM.L2-3.4.2 (configuration enforcement),
AC.L2-3.1.3 (CUI flow control at the Workspace organization
boundary), and AC.L2-3.1.5 (least privilege through OU-based
administration delegation).

**Implementation notes.**

- Enterprise Plus edition is the licensing prerequisite for
  Assured Controls Plus. Lower editions do not have the
  overlay available. Enable Assured Controls Plus at the
  Workspace organization level through the Admin Console.
- A CUI-scope Workspace organization should not mix Enterprise
  Plus with lower-tier licenses within the same organization
  where CUI is present. Mixed-license organizations create
  ambiguity about which users have which capabilities.
- Organizational Units (OUs) apply configuration and service
  access at sub-organization scope. Use OUs to segment CUI
  users from non-CUI users if the organization mixes work
  types, with Assured Controls Plus applied at the
  organization level covering the CUI OU.
- Cross-organization collaboration with non-Assured-Controls-
  Plus Workspace tenants or commercial Workspace uses
  external-sharing policies. Default posture for CUI: disable
  external sharing beyond named domains; verify at every
  Workspace service (Drive, Calendar, Meet).

**Evidence to collect.**

- Workspace admin console export showing Assured Controls
  Plus enabled at the organization level.
- Enterprise Plus license inventory covering all users in
  CUI scope.
- Organizational Unit hierarchy documentation with
  CUI-scope designation.
- External sharing policy configuration per service.

**Common mistakes.**

- Purchasing Enterprise Plus licenses without enabling Assured
  Controls Plus. The overlay is separate; license alone does
  not deliver the compliance posture.
- Mixing Enterprise Plus and Business Plus licenses in a
  CUI-scope organization. The Business Plus users cannot use
  the features Assured Controls Plus enforces, creating
  compliance-boundary confusion.
- Allowing external sharing to any domain from a CUI-scope
  Workspace organization. External sharing should be
  restricted to named domains whose posture is verified.

---

## Identity and access management

**Capability.** Google Workspace identity is managed natively
through the Admin Console. Cloud Identity is the separate SKU
for organizations that want workforce identity without
Workspace productivity apps. Both support 2-Step Verification
(Google's MFA), Context-Aware Access (session-context-based
policy enforcement parallel to Microsoft Conditional Access),
SSO to SAML and OIDC identity providers, and SCIM-based
user provisioning from external identity systems. Admin roles
are assigned through the Admin Console with predefined roles
(Super Admin, User Management Admin, Groups Admin, and others)
plus custom roles for fine-grained permissions.

**CMMC practices implemented.** IA.L1-3.5.1 (user
identification), IA.L1-3.5.2 (user authentication), IA.L2-3.5.3
(MFA), AC.L2-3.1.1 (account management), AC.L2-3.1.5 (least
privilege through admin-role assignment), and AC.L2-3.1.8
(unsuccessful logon attempts through 2-Step Verification
lockout policies).

**Implementation notes.**

- Workforce identity for Workspace CUI workloads lives in the
  Workspace organization under Assured Controls Plus. A
  federated IdP delivering identity claims to Workspace is
  acceptable, but the federation must terminate in a
  CUI-capable control plane; federating from a commercial
  identity store of dubious compliance posture pulls the
  commercial plane into CUI scope.
- 2-Step Verification must be enforced for all users in CUI
  scope. Phishing-resistant factors (FIDO2 security keys,
  passkeys, or Google Authenticator with prompt-plus-number-
  matching) are the assessor-preferred path; SMS-based 2-Step
  Verification is deprecated by NIST SP 800-63B for
  Authenticator Assurance Level 2.
- Context-Aware Access enforces policy based on session
  context (user, device, location, risk). Build policies that
  require MFA, managed-device state, and US-geolocation for
  CUI-scope service access. Context-Aware Access is part of
  Enterprise Plus and works alongside Assured Controls Plus.
- Admin-role assignments should follow least-privilege
  principles. Super Admin access is the highest privilege and
  must be tightly controlled; prefer predefined roles scoped
  to specific functions over Super Admin for day-to-day
  administration.
- SSO federation: enforce SAML or OIDC for organization
  users; keep the Google-native password path only as a
  break-glass recovery mechanism with hardware MFA.

**Evidence to collect.**

- Admin Console configuration export showing 2-Step
  Verification enforcement policy for the CUI-scope OU.
- Context-Aware Access policy inventory with session-context
  rules applied to CUI-scope services.
- Admin role assignment inventory showing Super Admin scope
  and predefined-role distribution.
- SSO configuration (IdP federation, metadata, certificate
  rotation history).

**Common mistakes.**

- Leaving 2-Step Verification optional for any user in CUI
  scope. The assessor-typical finding is a user without MFA
  who retains CUI access.
- Using Super Admin for day-to-day operations. Common
  finding; PIM-equivalent discipline (just-in-time Super
  Admin) is not native to Workspace, so admin-role hygiene
  matters more.
- Federating Workspace identity from a commercial IdP for
  CUI users. The CUI boundary extends into the IdP; the IdP
  must be CUI-capable or the identity plane must live in
  Cloud Identity under Assured Controls Plus.

---

## Productivity core: Gmail, Drive, Meet, Chat, Docs

**Capability.** The productivity core of Workspace Enterprise
Plus comprises Gmail (email, including Gmail confidential mode
for ephemeral sharing), Drive (file storage and sharing,
Shared Drives for team ownership), Meet (video meetings, dial-
in, recording), Chat (persistent messaging, Spaces), Calendar,
and Docs/Sheets/Slides (real-time collaborative document
editing). Under Assured Controls Plus, each service operates
under the overlay's data-residency and personnel-access
controls.

**CMMC practices implemented.** AC.L2-3.1.3 (CUI flow control
between services), SC.L2-3.13.8 (transmission confidentiality
and integrity via TLS), SC.L2-3.13.11 (FIPS-validated
cryptography at rest), SC.L2-3.13.16 (data at rest
encryption), AU.L2-3.3.1 (audit event creation through
Workspace audit logs), and AU.L2-3.3.2 (user accountability).

**Implementation notes.**

- Gmail under Assured Controls Plus enforces US-only data
  storage for message content and attachments. Gmail
  Confidential Mode provides time-limited message delivery
  with additional authentication, useful for CUI-sensitive
  transmissions; it is not a substitute for DLP or sensitivity
  labeling for persistent CUI handling.
- Drive sharing defaults should restrict external sharing.
  Assured Controls Plus enforces US-only storage; sharing
  policies enforce which domains or users can receive Drive
  content. Shared Drives (formerly Team Drives) are owned by
  the organization rather than individual users and are the
  preferred container for CUI team documents; My Drive holds
  per-user content and is harder to govern.
- Meet recordings are stored in Drive with the sharing
  permissions of the recording user. CUI discussed in Meet
  can land in Drive as a recording; confirm recording
  retention policies treat the recorded CUI as persistent
  CUI.
- Chat messages and Spaces are subject to Workspace retention
  policies configured in Vault. CUI discussed in Chat is
  retained and discoverable per the Vault retention rules.
- Docs, Sheets, and Slides support real-time collaboration
  with fine-grained sharing. Use Organization-level sharing
  defaults to restrict collaborator invitations to approved
  domains or users; per-document sharing settings can
  override but must be documented as exceptions.
- Per-service FedRAMP High authorization status is
  documented at cloud.google.com/security/compliance/fedramp
  and the FedRAMP Marketplace. Turn off services that are
  not FedRAMP-authorized in the Workspace Admin Console if
  the contractor's posture requires it;
  support.google.com/a/answer/182442 documents the service-
  disable workflow.

**Evidence to collect.**

- Admin Console Sharing policies export per service (Drive,
  Calendar, Chat).
- Gmail message rules and confidential-mode policy
  configuration.
- Shared Drive inventory for CUI scope with ownership
  documentation.
- Meet recording retention policy export.
- Service enable/disable status showing which Workspace
  services are active in the CUI organization.

**Common mistakes.**

- Allowing external sharing to any domain from a CUI-scope
  Workspace. Default sharing should be restricted to named
  domains with verified posture.
- Storing CUI in My Drive rather than Shared Drives. On
  employee departure, My Drive content migration is messy;
  Shared Drives retain organization ownership.
- Recording Meet sessions discussing CUI without a
  retention-policy review. The recording inherits Drive
  sharing semantics and Vault retention; make the recording
  lifecycle deliberate, not incidental.

---

## Data Loss Prevention, Vault, and compliance tooling

**Capability.** Workspace DLP detects sensitive content in
Gmail, Drive, and Chat with predefined detectors (PII, PCI,
PHI, credit card, SSN) and custom detectors (regex,
dictionary, document-fingerprint). DLP actions block,
quarantine, warn, or audit. Workspace Vault provides
eDiscovery (holds, searches, exports) and retention policies
at the organization or OU level. Client-Side Encryption (CSE)
with external key management encrypts content before it
reaches Google's servers, giving the customer exclusive
control over the decryption keys.

**CMMC practices implemented.** AC.L2-3.1.3 (CUI flow control
through DLP), MP.L2-3.8.1 (media marking and access
restriction through CSE and sharing policies), AU.L2-3.3.1
(audit event creation), AU.L2-3.3.5 (audit correlation
through Vault eDiscovery), SC.L2-3.13.11 (FIPS-validated
cryptography, through CSE with FIPS-validated external KMS),
and SC.L2-3.13.16 (data at rest encryption with CSE).

**Implementation notes.**

- Build DLP rules for the CUI categories in the contractor's
  scope. Start with Google-provided templates for CUI-
  adjacent content (SSN, ITAR-adjacent patterns, export-
  controlled terminology); customize with the contractor's
  specific CUI markings.
- DLP actions for CUI-scope rules: block external sharing
  that matches CUI patterns, warn users composing emails
  with CUI to external recipients, audit all CUI detection
  events for review.
- Vault retention policies enforce the contractor's records-
  retention schedule. CUI typically has multi-year retention;
  configure retention scoped to CUI-labeled content or
  CUI-scope OUs.
- Vault eDiscovery supports legal-hold workflows. Verify
  license tier includes the required eDiscovery features
  before relying on them for CUI legal holds.
- Client-Side Encryption (CSE) encrypts Gmail messages,
  Drive files, Meet recordings, Chat messages, and Calendar
  events with customer-controlled keys through an external
  key manager (Cloud EKM with a customer-chosen external KMS
  partner, or a direct CSE integration). CSE is the strongest
  cryptographic posture available in Workspace for CUI; the
  customer holds the keys that encrypt/decrypt content, so
  Google operator access to content (already restricted
  under Assured Controls Plus) is further constrained
  cryptographically.
- CSE requires additional configuration: external IdP
  integration for key-release authentication, external KMS
  partner selection, user-enrollment workflow for
  CSE-enabled accounts. The operational overhead is
  non-trivial; use CSE when the workload's threat model
  requires customer-held key custody.

**Evidence to collect.**

- DLP rule inventory showing CUI-detection coverage.
- DLP action-outcome log sample showing blocked/quarantined
  items.
- Vault retention policy export scoped to CUI content.
- CSE configuration documentation if in use, including
  external KMS partner integration.
- Sample eDiscovery case record demonstrating the workflow.

**Common mistakes.**

- Configuring DLP rules in audit-only mode indefinitely.
  Audit mode provides visibility but not enforcement; CUI
  leaks still occur.
- Failing to configure Vault retention for CUI content.
  Default retention may not meet the contractor's records-
  retention schedule; configure explicitly.
- Assuming CSE protects data from every party. CSE protects
  from Google-operator access (beyond what Assured Controls
  Plus already restricts) but does not protect from a
  compromised external KMS, a compromised user, or an
  attacker with access to the customer's CSE identity
  provider.

---

## Context-Aware Access and Access Transparency

**Capability.** Context-Aware Access evaluates session context
(user, device posture, IP, geolocation, time) at access time
and enforces policy outcomes (allow, MFA-required, deny) for
Workspace services. Access Transparency logs Google-personnel
access to customer data with justifications and timestamps,
giving the contractor visibility into operator activity under
Assured Controls Plus. Access Approval (available with some
Workspace configurations) requires explicit customer approval
before Google personnel can access customer data in specific
circumstances.

**CMMC practices implemented.** AC.L2-3.1.12 (remote access
monitoring through Context-Aware Access session logging),
AC.L2-3.1.7 (privileged function logging), AU.L2-3.3.1 (audit
event creation, via Access Transparency logs), AU.L2-3.3.2
(user accountability), and SI.L2-3.14.6 (system monitoring).

**Implementation notes.**

- Context-Aware Access policies should require managed-device
  state (Endpoint Verification installed), MFA, and US
  geolocation for CUI-scope services. Build the policies at
  the Workspace organization or OU level; apply to the
  CUI-scope OU.
- Endpoint Verification is Google's companion agent that
  reports device posture to Context-Aware Access. Deploy
  Endpoint Verification to managed endpoints in the CUI
  fleet; unenrolled devices cannot satisfy the device-posture
  condition in Context-Aware Access policies.
- Access Transparency logs ship to Workspace Admin Console
  and can be exported to a SIEM for correlation. Review
  Access Transparency logs on a cadence to verify
  Google-operator activity aligns with Assured Controls Plus
  personnel commitments.
- Access Approval workflows require more operational
  investment than Access Transparency alone. Use Access
  Approval when the contractor's workload requires
  customer-gate operator access for specific high-sensitivity
  scenarios.

**Evidence to collect.**

- Context-Aware Access policy inventory showing device,
  location, and MFA rules applied to CUI scope.
- Endpoint Verification deployment status across the fleet.
- Access Transparency log sample showing Google-operator
  activity on CUI data.
- Access Approval configuration if in use.

**Common mistakes.**

- Building Context-Aware Access policies without Endpoint
  Verification deployed. Device-posture conditions fail
  open (or deny every unverified device); either way, the
  intended policy does not operate.
- Ignoring Access Transparency logs. The capability exists
  specifically to let the contractor verify the inherited
  personnel-access posture under Assured Controls Plus; not
  reviewing is a missed-inheritance-evidence pattern.

---

## ITAR posture under Assured Controls Plus

**Capability.** Google Workspace Assured Controls Plus supports
ITAR-controlled technical data through a residency + personnel
+ contract overlay: US-only data storage enforced at the
control-package level, US-person Google personnel access
under the overlay's personnel commitments, and contractual
language in the Workspace Enterprise Plus plus Assured
Controls Plus agreement naming ITAR support. This is
architecturally distinct from M365 GCC High's sovereign-
tenancy ITAR story, which relies on physical and logical
tenancy partition rather than control-package overlay.

**Workspace's ITAR scope is Google-side only.** Workspace
Assured Controls Plus commits to Google-operated controls
(data residency, Google personnel US-person access,
contractual language); it does not deliver contractor-side
ITAR personnel compliance. Contractor personnel posture
(US-person-only access to ITAR-scope data, US-person-only
administration of ITAR-scope Shared Drives) is a separate
export-control and contract question outside Workspace's
technical scope, owned by the contractor.

**CMMC practices implemented.** This posture does not map to
a specific CMMC practice; ITAR is a separate regulatory
regime. Practices affected by ITAR posture (access control,
encryption, audit, personnel screening) are the same ones
affected by CUI posture, but the ITAR overlay imposes
additional constraints on contractor personnel that interact
with PS.L2-3.9.1 and PS.L2-3.9.2.

**Implementation notes.**

- ITAR posture applies to the contractor's full ITAR exposure.
  ITAR-controlled data in Gmail, Drive documents, Meet
  recordings, Chat messages, and Calendar events all inherit
  the Assured Controls Plus ITAR story; the contractor does
  not get to scope ITAR to a subset of Workspace services
  while using the whole suite.
- The contractor-side personnel posture is distinct from the
  Google-side posture. Google's Assured Controls Plus
  commitment covers Google personnel with US-person access
  controls; the contractor must independently ensure
  contractor-side access is limited to US-persons where ITAR
  applies. A non-US-person contractor employee with access
  to an ITAR-scope Shared Drive represents a contractor-
  side violation regardless of Workspace's Assured Controls
  Plus configuration.
- ITAR training for contractor personnel is required; Google
  does not deliver this training. Integrate ITAR training
  into the contractor's AT program (see
  `references/domains/at-awareness-training.md`).
- Cross-organization collaboration with non-Assured-Controls-
  Plus Workspace tenants or commercial Workspace for
  ITAR-scope content requires explicit export-control review.
  Default posture: no cross-org sharing of ITAR data.
- ITAR is different from the EAR regime. If the workload
  carries EAR-controlled dual-use data, verify EAR posture
  separately with export-control counsel.

**Architectural comparison with M365 GCC High.** Both tenancies
support DFARS 7012 CUI under DoD IL4 reciprocity; both
accommodate ITAR data. They deliver the posture through
different mechanisms:

- **M365 GCC High:** sovereign tenancy partition, physical and
  logical separation from commercial M365, US-person Microsoft
  operator access enforced at the tenancy boundary, IL5-aligned
  authorization. Migration from commercial M365 to GCC High
  requires tenancy-level migration with distinct data-plane
  changes.
- **Workspace Assured Controls Plus:** overlay on commercial
  Workspace infrastructure, US-only data storage enforced at
  the control-package level, US-person Google operator access
  enforced via the overlay's personnel commitments, IL4-aligned
  authorization. Migration from commercial Workspace to
  Assured Controls Plus requires edition upgrade to Enterprise
  Plus and overlay activation, not a tenancy-level migration.

The choice between the two is a choice between architectural
models, not just vendors. Contractors with IL5 workload
requirements must choose M365 GCC High; contractors with
IL4-scope CUI workloads can choose either.

**Evidence to collect.**

- Google Workspace Enterprise Plus agreement plus Assured
  Controls Plus add-on documentation including ITAR language.
- Contractor ITAR policy document naming US-person staffing
  requirements for ITAR-scope work.
- Personnel screening records for contractor staff with
  ITAR-scope access.
- Cross-organization sharing restriction documentation.

**Common mistakes.**

- Assuming Assured Controls Plus's ITAR commitment extends to
  the contractor's personnel automatically. It does not; the
  contractor owns contractor-side ITAR personnel compliance.
- Treating ITAR and EAR as interchangeable regimes. They
  differ in scope and enforcement mechanism.
- Cross-organization collaboration on ITAR data without
  export-control review. A single external-share link to a
  non-Assured-Controls-Plus tenant can create a violation.

---

## Support and operator-access posture

**Capability.** Google Workspace Support for Assured Controls
Plus organizations handles cases with US-person personnel
under the overlay's personnel commitments. Support tiers
(Standard, Enhanced, Premium) apply to Workspace separately
from Google Cloud. For CUI workloads, Enhanced or Premium
support is the typical tier for incident-response SLAs.

**CMMC practices implemented.** PS.L2-3.9.1 (personnel
screening) and PS.L2-3.9.2 (personnel transfer) are inherited
from Google for the Google-operator side under Assured
Controls Plus; the contractor still owns these practices for
contractor personnel.

**Implementation notes.**

- Support cases must not include CUI data in case descriptions
  or attachments. Google support handles Assured-Controls-
  Plus-scope cases with US-person personnel, but case-data
  sanitization is the contractor's responsibility.
- Access Transparency logs (discussed above) are the primary
  evidence surface for verifying that Google operator
  activity matches Assured Controls Plus commitments.
- The Google US-person operator-access posture is distinct
  from the contractor's own personnel posture. A
  non-US-person contractor employee cannot serve as a Google
  support escalation contact in an Assured Controls Plus
  organization, and may or may not be permitted to administer
  the contractor's own Workspace organization depending on
  the contract's export-control terms. If ITAR-controlled or
  EAR-controlled technical data is present, US-person-only
  staffing may apply to the contractor side as well; consult
  export-control counsel before finalizing personnel policy.

**Evidence to collect.**

- Workspace support tier documentation per organization.
- Support case hygiene policy naming CUI-scrubbing
  requirement before submission.
- Access Transparency log sample covering the assessment
  window.
- C3PAO CMMC attestation letter (2025-dated) downloaded from
  services.google.com/fh/files/misc/gwsattestation2025.pdf.

**Common mistakes.**

- Attaching CUI logs or production data to Support cases
  without sanitization.
- Assuming commercial Workspace Support handling applies to
  Assured Controls Plus organizations. Different posture,
  different personnel; verify the organization is on the
  Assured Controls Plus support path.

---

## FedRAMP and Impact Level posture

**FedRAMP status (verified 2026-04-21).**

- Google Workspace holds FedRAMP High and FedRAMP Moderate
  Provisional Authorities to Operate (P-ATOs) on in-scope
  services through the JAB.
- For CMMC Level 2 CUI work under DFARS 7012, the contractor
  must use FedRAMP High authorized services and enable
  Assured Controls Plus at the organization level (per
  cloud.google.com/security/compliance/cmmc).
- Per-service authorization scope is documented at
  cloud.google.com/security/compliance/fedramp and the
  FedRAMP Marketplace. Verify current service-level scope
  before citing in an SSP.
- Non-FedRAMP-authorized services can be disabled in the
  Workspace Admin Console per
  support.google.com/a/answer/182442 if the contractor's
  posture requires it.

**DoD Impact Level posture (verified 2026-04-21).** Google
Workspace Assured Controls Plus supports DoD IL4-aligned CUI
workloads through the FedRAMP High baseline plus the overlay's
personnel and residency commitments. Google Workspace does
not hold an IL5 Provisional Authorization; IL5 for the
productivity plane requires Microsoft 365 GCC High. See
`references/modern-it/cloud-platforms/cloud-selection.md`
"FedRAMP baseline to DoD Impact Level crosswalk" for the
IL-to-FedRAMP mapping.

**Scope boundary for IL content in this file.** This section
names the authorization level and points at the hub crosswalk.
It does not implement IL4 end-to-end. Full IL4 implementation
detail (CNSSI 1253 Moderate Confidentiality and Integrity
overlays, NSS controls if applicable) is deferred to a future
DoD-specific reference per the forward-reference in
`references/fedramp-gap.md` "Relationship to DoD Cloud
Computing Security Requirements Guide."

---

## Capability appendix — CMMC capability to Google Workspace service

Per hub Decision 1 canonical format.

| Productivity capability | Google Workspace service (under Assured Controls Plus) |
|---|---|
| Email | Gmail (Enterprise Plus + Assured Controls Plus) |
| File storage and collaboration | Drive with Shared Drives and sharing policies |
| Real-time messaging and chat | Chat with Spaces; Vault retention |
| Calendaring and meetings | Calendar + Meet with recording retention through Drive |
| Document editing | Docs, Sheets, Slides with sharing policies |
| Identity and access | Cloud Identity or Workspace identity; Context-Aware Access; 2-Step Verification |
| Device posture evaluation | Endpoint Verification |
| DLP and sensitivity | Workspace DLP (Gmail, Drive, Chat) |
| Client-side encryption | Client-Side Encryption with Cloud EKM external key manager |
| Retention and records | Vault retention policies |
| eDiscovery | Vault eDiscovery (holds, searches, exports) |
| Operator-activity visibility | Access Transparency; Access Approval (where configured) |
| Audit and logging | Admin Console audit logs; Workspace audit log export to SIEM |

---

## Cross-domain anchors

Google Workspace Assured Controls Plus posture composes with
corpus cross-cutting files and domain practice files:

- **Phase 5d hub.** `references/modern-it/productivity/README.md`
  for the seven conventions, the GCC High versus Assured
  Controls Plus equivalence synthesis, and the canonical
  capability-appendix format.
- **Phase 5c cloud-platforms hub.** `references/modern-it/cloud-platforms/cloud-selection.md`
  for the FedRAMP-to-IL crosswalk.
- **GCP Assured Workloads (distinct from Assured Controls Plus).**
  `references/modern-it/cloud-platforms/gcp-assured.md` for
  the Google Cloud platform overlay (distinct from the
  Workspace overlay covered here).
- **Microsoft 365 GCC High counterpart.**
  `references/modern-it/productivity/microsoft-365-gcc.md`
  for the sovereign-tenancy model contractors may compare
  against when making the Workspace-vs-M365 productivity
  decision.
- **FedRAMP inheritance.** `references/fedramp-gap.md`
  "Inherited vs shared-responsibility controls."
- **CUI scoping.** `references/scoping-and-cui.md`.
- **SSP authoring.** `references/ssp-guidance.md`.

Domain practice files used for requirement text and evidence
lists:

- Access Control (AC): `references/domains/ac-access-control.md`
- System and Information Integrity (SI): `references/domains/si-system-information-integrity.md`
- System and Communications Protection (SC): `references/domains/sc-system-comms.md`
- Identification and Authentication (IA): `references/domains/ia-identification-auth.md`
- Configuration Management (CM): `references/domains/cm-configuration-mgmt.md`
- Audit and Accountability (AU): `references/domains/au-audit.md`
- Media Protection (MP): `references/domains/mp-media-protection.md`
- Awareness and Training (AT): `references/domains/at-awareness-training.md`
- Personnel Security (PS): `references/domains/ps-personnel-security.md`

---

## Examples as of 2026-04

> **Examples as of 2026-04:** Google Workspace services named
> in this file are platform-native and are not in scope for
> the ranked-examples convention. Where a contractor considers
> third-party alternatives for a specific capability (third-
> party SIEM for Workspace audit log ingestion, third-party
> key manager for Client-Side Encryption backend, third-party
> identity provider for SSO federation into Workspace), those
> vendors appear in a sidebar for the relevant capability with
> the dated Examples format from the hub's capability-versus-
> product convention. This skill does not rank vendors. Verify
> current FedRAMP Marketplace status before selecting any
> third-party service operating alongside Workspace Assured
> Controls Plus.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/productivity/README.md`,
`references/modern-it/cloud-platforms/cloud-selection.md`,
`references/modern-it/cloud-platforms/gcp-assured.md`, or
previous Phase 5 slices are not repeated here.

**Assured Controls Plus.** Defined in
`references/modern-it/productivity/README.md` Terminology;
this file carries the authoritative implementation detail per
hub Decision 6.

**CSE (Client-Side Encryption).** The Workspace feature that
encrypts customer content in the client before it reaches
Google servers, using customer-held keys managed through an
external key manager. Provides cryptographic isolation from
Google operator access beyond the Assured Controls Plus
personnel commitments.

**Endpoint Verification.** The Google companion agent that
reports device posture (managed state, encryption state,
operating system version) to Context-Aware Access for
session-context policy evaluation.

**Enterprise Plus.** The Google Workspace edition that is the
licensing prerequisite for Assured Controls Plus. Lower
editions do not have the Assured Controls Plus overlay
available.

**OU (Organizational Unit).** The Workspace hierarchical scope
primitive for applying configuration, service access, and
sharing policies at a sub-organization level.

**SSO.** Single Sign-On, typically via SAML 2.0 or OIDC,
federating workforce identity from an external identity
provider into Workspace authentication.

**Vault.** The Google Workspace eDiscovery and retention tool,
providing legal-hold workflows, search, export, and
organization-level or OU-level retention policies.

**2-Step Verification.** Google's MFA mechanism, supporting
hardware security keys (FIDO2), passkeys, Authenticator apps,
and SMS (deprecated for CUI-scope AAL2).
