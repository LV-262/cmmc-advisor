# FedRAMP-Authorized AI Services Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2
> (DoD CIO); DFARS 252.204-7012; FedRAMP Marketplace
> (marketplace.fedramp.gov); AWS Bedrock FedRAMP authorization
> status
> (aws.amazon.com/compliance/services-in-scope/FedRAMP/amazon-bedrock-models/);
> AWS GovCloud Bedrock documentation
> (docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-bedrock.html);
> Azure Government OpenAI announcement
> (devblogs.microsoft.com/azuregov/azure-openai-fedramp-high-for-government/);
> Azure Government Foundry Models documentation
> (learn.microsoft.com/en-us/azure/ai-foundry/openai/azure-government);
> Claude on Vertex AI announcement
> (claude.com/blog/claude-on-google-cloud-fedramp-high); Google
> Cloud Assured Workloads documentation
> (cloud.google.com/assured-workloads); DoD CSP SRG v1r1
> (public.cyber.mil); NIST CMVP validated modules registry
> (csrc.nist.gov).

## Overview

This file maps the three FedRAMP-authorized managed AI services
available to defense contractors handling CUI or FCI: Amazon
Bedrock in AWS GovCloud, Azure OpenAI Service in Azure
Government, and Vertex AI via Google Cloud Assured Workloads. It
is the authoritative source in this corpus for per-model
authorization detail per Phase 5 hub Decision 2.

Three providers serve three distinct model ecosystems:

- **Amazon Bedrock (AWS GovCloud).** FedRAMP High plus DoD
  IL4/IL5 authorization covering a subset of Anthropic, Amazon,
  and Meta models. The authorization route via AWS GovCloud
  gives Claude access at IL5 without committing to Azure or
  Google Cloud.
- **Azure OpenAI Service (Azure Government).** FedRAMP High
  plus DoD IL4/IL5 authorization covering OpenAI models (GPT-
  4o, GPT-4.1 series, GPT-5.1, o-series, embeddings). Natural
  pair for M365 GCC High contractors. Also holds a Top Secret
  authorization (out of CMMC L2 scope).
- **Vertex AI (Google Cloud Assured Workloads).** FedRAMP High
  plus DoD IL2 authorization at the AI layer. Covers Claude
  models plus Google's Gemini family when configured in an
  Assured Workloads environment. IL5 is roadmap.

Read this file alongside the Phase 5 hub at
`references/modern-it/ai-services/README.md` (seven conventions;
this file implements Decision 2's FedRAMP-primary-with-IL-overlay
pattern) and the Phase 5c cloud-platforms files
(`aws-govcloud.md`, `azure-government.md`, `gcp-assured.md`) for
the underlying platform authorizations that each AI service rides
on.

---

## Scope of this file

Covered:

- Amazon Bedrock in AWS GovCloud (US-East and US-West) with the
  FedRAMP High + IL4/IL5 authorization boundary and the
  specific model subset in scope.
- Azure OpenAI Service in Azure Government (the usgovarizona
  and usgovvirginia regions of Microsoft's sovereign Government
  cloud) with the FedRAMP High + IL4/IL5 authorization boundary
  and the specific model subset in scope.
- Vertex AI via Google Cloud Assured Workloads (FedRAMP High
  configuration) with Claude and Gemini model availability.
- Per-model dated authorization stamps sourced from each
  provider's primary compliance documentation.
- Tenancy Selection, capability coverage, common mistakes
  specific to each service's government offering.

Not covered:

- Commercial AWS Bedrock, commercial Azure OpenAI, commercial
  Vertex AI. These are out of scope for CUI; migration paths
  noted inline per-service.
- Self-hosted AI inference patterns (Llama on contractor GPUs,
  open-weight models on GovCloud EC2, air-gapped deployments),
  covered in `self-hosted-ai.md`.
- AI developer tools (Claude Code, Copilot, Cursor), covered
  in `ai-dev-tools.md`.
- Top Secret / IL6 cloud AI (Azure OpenAI in Azure Government
  Top Secret, January 2025 authorization). Out of CMMC L2
  scope.
- Generative-AI features bundled into productivity suites
  (Microsoft 365 Copilot, Gemini for Workspace). Covered under
  productivity files where they embed in the primary suite's
  tenancy.

---

## Tenancy Selection

Per hub Decision 3, this section answers three questions in
order. Symmetric structure across the three providers; different
answers reflect each provider's architecture. (Slices V and W
substitute Fit Assessment for Tenancy Selection per hub
Decision 3; the tenancy axis does not apply to self-hosted or
dev-tool scopes.)

**1. Is the commercial tier ever acceptable for CUI?** No, across
all three providers. Commercial Bedrock (in non-GovCloud regions)
holds FedRAMP High on the AWS commercial boundary but does not
meet DoD IL4/IL5 operator-access restrictions for CUI. Commercial
Azure OpenAI sits on Azure commercial's FedRAMP High boundary
with IL2 only. Commercial Vertex AI sits on Google Cloud
commercial with FedRAMP Moderate on specific services. A
contractor running CUI on any of these has a scope problem, not
a configuration issue.

**2. Which government boundary applies to the contractor's
workload?**

- **AWS GovCloud Bedrock** for DoD IL4 or IL5 Claude or Llama
  workloads, or for contractors already committed to AWS
  GovCloud IaaS.
- **Azure Government OpenAI Service** for DoD IL4 or IL5 OpenAI-
  model workloads, or for contractors running Microsoft 365 GCC
  High who want identity and audit federation from the primary
  suite.
- **Vertex AI via Assured Workloads** for FedRAMP High Claude or
  Gemini workloads at IL2, or for contractors running Google
  Workspace Assured Controls Plus.

Cross-boundary combinations exist (Bedrock GovCloud plus M365
GCC High for contractors who need Claude specifically while on
Microsoft productivity). The tradeoff is operational complexity
(two cloud-tenancy relationships, dual SIEM, cross-cloud identity
federation) versus model choice.

**3. What workload-location and personnel boundaries apply?**

- **AWS GovCloud Bedrock.** Vetted US-person operator access;
  GovCloud data plane physically and logically separated from
  commercial AWS; FedRAMP High + IL5 per CSP SRG v1r1
  reciprocity.
- **Azure Government OpenAI.** Same vetted US-person operator
  commitment as Azure Government broadly; Azure Government data
  plane separated from commercial Azure; FedRAMP High + IL4/IL5.
- **Vertex AI Assured Workloads.** Vertex AI inference runs
  inside the Assured Workloads FedRAMP High regional boundary
  with data-residency plus personnel-access controls per
  Assured Workloads' FedRAMP High configuration.

---

## Amazon Bedrock in AWS GovCloud

Amazon Bedrock provides managed foundation-model inference across
multiple model families (Anthropic Claude, Meta Llama, Amazon
Titan, plus commercial-only Cohere, Mistral AI, Stability AI,
AI2I Labs). In AWS GovCloud (US), a subset of Bedrock models
holds FedRAMP High + DoD IL4/IL5 authorization.

**FedRAMP authorization and DoD IL coverage (verified 2026-04-21).**
Amazon Bedrock models in AWS GovCloud (US-East and US-West) hold
**FedRAMP High plus DoD IL4/IL5 authorization** per
docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-bedrock.html.
The authorization was announced May 2025 per AWS Public Sector
blog
(aws.amazon.com/blogs/publicsector/accelerating-government-innovation-amazon-bedrock-models-get-fedramp-high-and-dod-il-4-5-approval-in-aws-govcloud-us/).
Commercial AWS Bedrock (non-GovCloud) carries FedRAMP High on
the AWS commercial boundary with IL2 reciprocity, not
appropriate for DFARS 7012 CUI work.

**Models in GovCloud scope (verified 2026-04-21 via AWS GovCloud
UserGuide).**

- All Amazon Titan models.
- Anthropic Claude Sonnet 4.5.
- Anthropic Claude 3.7 Sonnet.
- Anthropic Claude 3.5 Sonnet v1.
- Anthropic Claude 3 Haiku.
- Meta Llama 3 70B.
- Meta Llama 3 8B.

**Models NOT in GovCloud (as of 2026-04-21).** Claude 3.5 Haiku,
Claude 3.5 Sonnet v2, Claude 4.0 Sonnet, Claude 4.1 Opus, Claude
4.5 Haiku, all Cohere models, all Mistral AI models, all
Stability AI models, all AI2I Labs models, and most Meta Llama
variants beyond 3 70B and 3 8B.

A contractor requiring a model not in GovCloud scope has three
options: (a) use a GovCloud-scoped model substitute at the same
capability tier (Claude Sonnet 4.5 is the current frontier in
GovCloud); (b) wait for expanded authorization (AWS extends
GovCloud model coverage on a months-to-quarters cadence); (c)
evaluate alternative providers (Azure OpenAI Government,
Vertex AI) if the specific model is more important than the
AWS commitment.

**Implementation notes.**

- Inference endpoints: Bedrock in GovCloud is accessed through
  GovCloud-specific Bedrock endpoints; cross-region inference
  between GovCloud East and West is supported within the
  GovCloud boundary.
- Export-controlled content: AWS documents that Bedrock custom-
  model metadata and provisioned-throughput metadata may leave
  the GovCloud Regions only when the customer requests AWS
  investigation support. Model evaluation metadata must not
  contain export-controlled data (configuration, IAM role ARNs,
  S3 bucket names, tags).
- Guardrails and Knowledge Bases: Bedrock Guardrails, Bedrock
  Knowledge Bases, and Bedrock Data Automation are available in
  GovCloud; verify current feature-availability at
  `docs.aws.amazon.com/bedrock/latest/userguide/features-regions.html`
  before citing specific features in the SSP.

**Prompt-surface CUI exposure (per hub Decision 5).** Bedrock
inference on GovCloud covers the prompt-in-flight and the
response-in-flight; contractor-attached context exposes CUI
through separate paths that each must be evaluated:

- RAG retrieval sources (S3 buckets, OpenSearch indexes) for
  Bedrock Knowledge Bases must be inside the GovCloud
  authorization boundary when they hold CUI.
- Agent tool-call destinations must be FedRAMP-scoped when the
  tool-call may return CUI to the agent's context; Bedrock
  Agents running in GovCloud inherit the platform boundary but
  contractor-authored tools operate under the contractor's own
  CUI discipline.
- Fine-tuning training data: a custom model fine-tuned on CUI
  data becomes a CUI-derived asset; document the fine-tune
  artifact and its storage location in the SSP.
- Model invocation logs in CloudWatch Logs retain prompt and
  response content when logging is enabled; verify the log
  retention and access posture matches the contractor's CUI
  handling requirements.

**Common mistakes.**

- Using Claude 3.5 Haiku (not in GovCloud scope) assuming it is
  covered because other Claude 3.5 models are; Haiku 3.5
  specifically is not in GovCloud at this verification date.
- Routing from a GCC High or AWS GovCloud workload to
  Anthropic's direct API for Claude access rather than through
  Bedrock GovCloud; direct-API routing is not FedRAMP-authorized
  and constitutes a scope breach for CUI workloads.
- Assuming commercial Bedrock's FedRAMP High authorization
  covers CUI workloads; commercial Bedrock is on the commercial
  AWS boundary at IL2 reciprocity, not GovCloud.

---

## Azure OpenAI Service in Azure Government

Azure OpenAI Service is Microsoft's managed OpenAI-model
inference on Azure. In Azure Government (usgovarizona and
usgovvirginia regions), Azure OpenAI holds FedRAMP High + DoD
IL4/IL5 authorization covering the OpenAI model family
(GPT-5.1, GPT-4.1 series, o-series reasoning models, GPT-4o,
and embeddings).

**FedRAMP authorization and DoD IL coverage (verified 2026-04-21).**
Azure OpenAI Service was approved as a service within the
**FedRAMP High Authorization for Azure Government** in August 2024
per devblogs.microsoft.com/azuregov/azure-openai-fedramp-high-for-government/.
It was also approved as a service within the **DoD IL4 and IL5
Provisional Authorization** by the Defense Information Systems
Agency (DISA) in September 2024 per the same blog's editor's
note. Commercial Azure OpenAI (on Azure commercial) carries
FedRAMP High on the Azure commercial boundary with IL2
reciprocity, not appropriate for DFARS 7012 CUI.

Azure OpenAI (including GPT-4o) also received a
Top Secret authorization for use in Azure Government Top Secret
as of January 2025 per Defense Scoop reporting. Top Secret / IL6
is outside CMMC L2 scope; contractors with TS workloads work
with Microsoft government sales directly.

**Models in Azure Government scope (verified 2026-04-21 via
learn.microsoft.com/en-us/azure/ai-foundry/openai/azure-government).**

- **GPT-5.1 series**: `gpt-5.1` (version 2025-11-13). Reasoning
  model with 400K-token context (272K input, 128K output) and
  training data through September 30, 2024.
- **GPT-4.1 series**: `gpt-4.1` and `gpt-4.1-mini` (both
  version 2025-04-14). Multimodal text + image input, 128K
  context (standard and provisioned managed deployments),
  300K context (batch deployments), 32K output tokens.
- **o-series reasoning**: `o3-mini` (version 2025-01-31).
  Reasoning model; 200K input, 100K output.
- **GPT-4o**: `gpt-4o` (version 2024-11-20). Multimodal;
  128K input, 16K output. Training data through October 2023.
- **Embeddings**: `text-embedding-3-large` (3,072 dimensions),
  `text-embedding-3-small` (1,536 dimensions),
  `text-embedding-ada-002` versions 1 and 2.

**Regional availability as of 2026-04-21.**

- **usgovarizona**: GPT-5.1 (Data Zone Standard and Provisioned),
  GPT-4.1 / GPT-4.1-mini (all deployment types), o3-mini (Data
  Zone deployments), GPT-4o (all deployment types), all
  embedding models (Standard deployment).
- **usgovvirginia**: GPT-5.1 (Data Zone Standard only), GPT-4.1 /
  GPT-4.1-mini (all deployment types), o3-mini (Data Zone Standard
  and Provisioned), GPT-4o (all deployment types). Embedding
  models less broadly available.

**Model retirements in Azure Government (verified 2026-04-21).**

- `gpt-4o` version 0513: retirement 3/31/2026 across all
  deployment types (earlier than the commercial retirement plan).
- `gpt-4o-mini` version 0718: retirement 3/31/2026 across all
  deployment types.

Contractors running retiring model versions must plan migration
to supported versions (gpt-4o 2024-11-20, gpt-4.1, GPT-5.1) with
SSP update reflecting the model-version transition.

**Implementation notes.**

- Deployment types: Data Zone Standard (an Azure Government
  deployment option that routes traffic within the Government
  data boundary for higher throughput); Data Zone Provisioned
  managed (purchases PTUs, Provisioned Throughput Units, across
  Azure Government infrastructure); Standard and Provisioned
  managed (regional deployment patterns). Per-model deployment-
  type availability varies; see the deployment-types guide at
  `learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types-gov`.
- Identity: Entra ID Government federation from M365 GCC High or
  contractor-primary IdP into Azure OpenAI Service. No commercial
  Entra ID interaction from the Government boundary.
- Abuse monitoring: Azure OpenAI's default commercial abuse-
  monitoring retention (30 days of prompt/response logging) is
  managed differently in Azure Government per the government-
  package configuration. Verify current tenant-level
  configuration against Microsoft Learn Azure Government
  Foundry Models guidance before loading CUI.
- Content Safety: Azure AI Content Safety is available in Azure
  Government and integrates with Azure OpenAI Service.

**Common mistakes.**

- Running CUI through commercial Azure OpenAI (commercial Azure
  boundary at IL2) instead of Azure Government OpenAI. Scope
  problem, not configuration.
- Citing a retired model version in an SSP (gpt-4o 0513 beyond
  3/31/2026) without a migration plan to a supported version.
- Assuming Azure Government Top Secret / IL6 is accessible
  without a separate contract vehicle. IL6 is DoD mission-
  specific; CMMC L2 contractor paths end at IL5.
- Conflating "Azure Government" and "GCC High". Azure Government
  is Microsoft's sovereign IaaS/PaaS boundary; GCC High is the
  M365 productivity tenancy that rides on Azure Government
  infrastructure. Azure OpenAI Service lives on Azure
  Government, not on M365 GCC High; federation between the two
  is via Entra ID Government.

---

## Vertex AI via Google Cloud Assured Workloads

Vertex AI is Google Cloud's managed AI platform providing
foundation-model inference, RAG, agent orchestration, and MLOps
tooling. When deployed inside a Google Cloud Assured Workloads
FedRAMP High configuration, Vertex AI supports CUI workflows at
FedRAMP High plus DoD IL2 at the AI layer.

**FedRAMP authorization and DoD IL coverage (verified 2026-04-21).**
Claude on Google Cloud's Vertex AI holds **FedRAMP High and DoD
IL2 authorization** per Anthropic's announcement at
claude.com/blog/claude-on-google-cloud-fedramp-high dated April 2,
2025. Access is via Google Cloud Assured Workloads environments
configured for FedRAMP High or IL2. The underlying Google Cloud
Assured Workloads product provides the platform boundary;
Vertex AI rides inside that boundary for the AI-layer
authorization.

IL5 authorization at the AI layer is on the roadmap per the
Claude-on-Vertex announcement ("lays groundwork toward future
IL5 compatibility") and is not current authorization at
2026-04-21. A contractor whose contract requires IL5 at the AI
plane uses Bedrock GovCloud or Azure Government OpenAI until
Vertex AI IL5 becomes available.

**Models in Vertex AI Assured Workloads FedRAMP High scope
(verified 2026-04-21).**

- **Anthropic Claude.** Claude 3.7 Sonnet at the April 2025
  announcement ("Access the complete Claude model family,
  including Claude 3.7 Sonnet"). Claude 4, 4.5 Sonnet and
  related newer Claude models on Vertex AI: verify current
  availability at the Vertex AI Model Garden and Google Cloud
  Assured Workloads release notes before citing in an SSP.
- **Google Gemini family.** Gemini models are accessible on
  Vertex AI; per-model Assured Workloads FedRAMP High coverage
  updates run through the Google Cloud Assured Workloads
  release notes at `cloud.google.com/assured-workloads/docs/release-notes`.
  Verify specific Gemini model coverage and Assured Workloads
  data-boundary status before citing.
- **Google open-weight models** (Gemma family) and partner
  models (Mistral, Meta Llama via Model Garden) are on the
  Vertex AI surface with per-model coverage that varies; verify
  each against the Assured Workloads release notes.

**Implementation notes.**

- Assured Workloads configuration: create the Vertex AI
  environment inside an Assured Workloads folder configured for
  FedRAMP High or IL2. The Assured Workloads package enforces
  data-residency, personnel-access, and encryption posture at
  the folder level; Vertex AI inherits those controls.
- Access via Model Garden (Google Cloud's catalog of
  foundation models on Vertex AI): contractor applications
  route to Claude or Gemini through Vertex AI Model Garden
  endpoints specific to the Assured Workloads region. Cross-
  region inference between FedRAMP High regions is supported
  within Assured Workloads.
- Identity: Cloud Identity federation from Google Workspace
  Assured Controls Plus (natural pairing) or SAML federation
  from a contractor-primary IdP. No commercial Cloud Identity
  interaction from the Assured Workloads boundary.
- Agent Engine: Vertex AI Agent Engine is available in Preview
  on Assured Workloads as of 2026-04; verify current preview-
  vs-GA status per hub Decision 6 (drift-tracking policy)
  before citing agent-orchestration features in the SSP.

**Prompt-surface CUI exposure (per hub Decision 5).** Vertex AI
inference inside Assured Workloads covers the prompt-in-flight
and response-in-flight at FedRAMP High + IL2; contractor-attached
context exposes CUI through separate paths:

- RAG retrieval sources (Vertex AI Search indexes, Cloud
  Storage buckets, BigQuery tables feeding RAG Engine) must
  sit inside the Assured Workloads data boundary when they
  hold CUI.
- Agent Engine tool-call destinations (Preview at 2026-04)
  must be FedRAMP-scoped when the tool-call may return CUI.
- Fine-tuning training data via Vertex AI Tuning: the tuned
  model becomes a CUI-derived asset inside Assured Workloads.
- Cloud Audit Logs and Vertex AI monitoring: verify the log
  retention and access posture matches the CUI handling
  requirements in the SSP.

**Common mistakes.**

- Using Vertex AI on Google Cloud commercial (non-Assured
  Workloads) for CUI. Scope problem; commercial Vertex AI does
  not meet DFARS 7012 equivalence for CUI.
- Assuming Vertex AI Assured Workloads covers IL5. At 2026-04-
  21, IL5 is roadmap. IL4 workloads work; IL5 workloads route
  through Bedrock GovCloud or Azure Government OpenAI.
- Routing Claude traffic from Assured Workloads to Anthropic's
  direct API rather than through Vertex AI Model Garden. Direct-
  API routing is not FedRAMP-authorized.
- Confusing Assured Workloads (Google Cloud IaaS/PaaS + AI
  compliance overlay) with Assured Controls Plus (Google
  Workspace productivity compliance overlay). Different
  packages, authorized independently, federated via identity.

---

## Cross-provider considerations

**Identity federation and operator access.** Each provider
federates identity from the contractor's primary IdP; the
operator-access commitment differs:

- AWS GovCloud: vetted US-person access per GovCloud's standing
  personnel commitment.
- Azure Government: vetted US-person access per Azure
  Government's standing personnel commitment.
- Google Cloud Assured Workloads: US-person access per the
  Assured Workloads package configuration.

All three are US-person-vetted but with slightly different
contractual framings. A contractor whose program-specific
requirements reference a named personnel-screening regime (for
example, a specific Tier-level background investigation for
operators) should verify the current commitment letter against
the provider's compliance documentation.

**Export-controlled content (ITAR / EAR).** None of the three
provider authorizations name ITAR as an in-scope overlay on the
FedRAMP High + IL5 package. A contractor handling ITAR-controlled
technical data through an AI service evaluates the specific
operator-access commitment against the ITAR requirement; the
typical path for ITAR-in-AI is self-hosted inference inside a
contractor-authored boundary (see `self-hosted-ai.md`).

**Prompt-surface CUI boundary per hub Decision 5.** All three
providers expose the prompt as a CUI-carrying surface. The
authorization boundary covers the inference service; it does not
automatically cover contractor-attached context (RAG retrieval
sources, agent tool-call destinations, fine-tuning training
data). Document the CUI-boundary for each attached surface
separately in the SSP; do not assume FedRAMP authorization on
the model service covers arbitrary context attachment.

**Model-version drift cadence.** Per hub Versioning section,
foundation-model releases run monthly-to-weekly; per-model
authorization lag is days-to-weeks on each provider. Dated
verification is the only defensible SSP citation. Rebrand and
version transitions (Claude 3.5 Sonnet v1 → v2 → 3.7 → 4 → 4.5;
GPT-4 → GPT-4o → GPT-4.1 → GPT-5.1) happen on a months-to-
quarters cadence; the underlying authorization typically
survives the version transition while specific model identifiers
shift.

---

## Capability appendix — CMMC capability to FedRAMP AI service

Per hub Decision 1 canonical format. Row order matches the
hub's three-column crosswalk.

| AI capability | FedRAMP-authorized service |
|---|---|
| Frontier-capability text generation | Claude Sonnet 4.5 (Bedrock GovCloud); GPT-5.1 (Azure OpenAI Government); Claude 3.7 Sonnet + Gemini frontier tier (Vertex AI Assured Workloads) |
| Small-model text generation | Claude 3 Haiku (Bedrock GovCloud); GPT-4.1-mini (Azure OpenAI Government); Gemini Flash tier (Vertex AI Assured Workloads) |
| Code generation | Claude Sonnet 4.5 (Bedrock GovCloud); GPT-5.1 + GPT-4.1 (Azure OpenAI Government); Claude 3.7 Sonnet (Vertex AI Assured Workloads) |
| Text embedding | Amazon Titan Text Embeddings V2 (Bedrock GovCloud); text-embedding-3-large, text-embedding-3-small, text-embedding-ada-002 (Azure OpenAI Government); Vertex AI embedding models (Assured Workloads) |
| Multimodal (text + image) | Claude 3.7 Sonnet, Sonnet 4.5 (Bedrock GovCloud); GPT-4o, GPT-4.1 (Azure OpenAI Government); Claude 3.7 + Gemini multimodal (Vertex AI Assured Workloads) |
| Reasoning models | Claude Sonnet 4.5 (Bedrock GovCloud); o3-mini, GPT-5.1 (Azure OpenAI Government); Claude via Vertex AI (Assured Workloads) |
| Structured output and tool-use | Claude (Bedrock); GPT-4o / GPT-4.1 / GPT-5.1 (Azure OpenAI Government); Claude + Gemini (Vertex AI Assured Workloads) |
| Fine-tuning | Bedrock Custom Models (GovCloud; verify current per-model fine-tuning availability); Azure OpenAI fine-tuning (Government; verify current scope); Vertex AI Tuning (Assured Workloads) |
| Retrieval-augmented generation (RAG) | Bedrock Knowledge Bases (GovCloud); Azure AI Search + Azure OpenAI (Government); Vertex AI Search + RAG Engine (Assured Workloads) |
| Agent orchestration | Bedrock Agents (GovCloud); Azure AI Agent Service (Government); Vertex AI Agent Engine (Assured Workloads, Preview at 2026-04) |
| Content safety and guardrails | Bedrock Guardrails (GovCloud); Azure AI Content Safety (Government); Vertex AI Safety (Assured Workloads) |
| Audit and logging | AWS CloudTrail + Bedrock model invocation logs (GovCloud); Azure Monitor + Azure OpenAI logs (Government); Vertex AI monitoring + Cloud Audit Logs (Assured Workloads) |

**Reading the appendix.** The right-hand column names the
provider plus the specific service plus the tenancy context.
Rows map capability to provider options; model-specific
authorization caveats live in the structural sections above.

---

## Cross-domain anchors

FedRAMP AI service posture composes with corpus cross-cutting
files and domain practice files:

- **Phase 5 AI hub.** `references/modern-it/ai-services/README.md`
  for the six Decisions including the prompt-surface CUI
  boundary (Decision 5) and dev-tools CUI layer (Decision 6).
- **Phase 5c cloud-platforms.**
  `references/modern-it/cloud-platforms/aws-govcloud.md` for
  AWS GovCloud platform authorization that Bedrock GovCloud
  rides on; `azure-government.md` for Azure Government platform
  authorization that Azure OpenAI rides on; `gcp-assured.md`
  for Google Cloud Assured Workloads that Vertex AI rides on.
- **Phase 5d productivity.**
  `references/modern-it/productivity/microsoft-365-gcc.md` for
  the M365 GCC High productivity tenancy that pairs naturally
  with Azure OpenAI Government; `google-workspace.md` for the
  Workspace Assured Controls Plus tenancy that pairs naturally
  with Vertex AI Assured Workloads.
- **FedRAMP framing.** `references/fedramp-gap.md` for the
  FedRAMP program context, CSP SRG v1r1 reciprocity, and DFARS
  7012 CSP-equivalence mechanics.
- **CUI scoping.** `references/scoping-and-cui.md`.
- **SSP authoring.** `references/ssp-guidance.md` for
  documenting AI-service inheritance in the SSP.

Domain practice files used for requirement text and evidence
lists:

- Access Control (AC). `references/domains/ac-access-control.md`
  for account management on AI-service surfaces and identity
  federation.
- System and Communications Protection (SC).
  `references/domains/sc-system-comms.md` for encryption in
  transit to AI endpoints and at rest in prompt caches.
- Configuration Management (CM).
  `references/domains/cm-configuration-mgmt.md` for change
  control on model-version transitions and service feature
  additions.
- Audit and Accountability (AU).
  `references/domains/au-audit.md` for model invocation logs.
- System and Information Integrity (SI).
  `references/domains/si-system-information-integrity.md` for
  guardrail and content-safety monitoring.

---

## Examples as of 2026-04

> **Examples as of 2026-04:** The three FedRAMP-authorized
> provider families named in this file are the hub Decision 1
> scope for the FedRAMP-AI track. Third-party managed AI services
> outside these three (providers offering FedRAMP-authorized AI
> inference through other routes) would require a deliberate
> scope expansion rather than an author's judgment call. This
> skill does not rank model providers. Verify current FedRAMP
> Marketplace status and the current vendor authorization letter
> before selecting any managed AI service for CUI workloads.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/ai-services/README.md`,
`references/modern-it/cloud-platforms/cloud-selection.md`,
`references/modern-it/productivity/README.md`, or previous Phase
5 slices are not repeated here.

**Data Zone (Azure OpenAI).** An Azure Government deployment
option that routes inference traffic within the Azure Government
data boundary for higher throughput. Distinct from Standard
and Provisioned managed deployment types.

**Model Garden (Vertex AI).** Google Cloud's catalog of
foundation models, first-party (Gemini, Gemma) and partner
(Claude, Mistral, Meta Llama), accessible through Vertex AI.

**MSO365MT.** Defined in
`references/modern-it/productivity/microsoft-365-gcc.md`. Not
directly relevant to Azure OpenAI Service but useful framing for
contractors routing AI from M365 GCC High.

**PTU (Provisioned Throughput Unit).** The Azure OpenAI
provisioned-deployment billing unit. Data Zone Provisioned and
Standard Provisioned deployments purchase PTUs rather than
pay-per-inference.

**usgovarizona, usgovvirginia.** The two Azure Government
regions hosting Azure OpenAI Service at FedRAMP High + IL4/IL5.

---

## Versioning and drift

Per hub Versioning policy: service-level claims are stable
anchors; per-model claims decay on a weekly-to-monthly cadence;
feature-level claims decay faster. All authorization claims in
this file are verified 2026-04-21 against the primary sources
named at top.

Near-term drift risks for this file:

- AWS may add or remove models from Bedrock GovCloud scope on a
  months-to-quarters cadence. Re-verify against
  `docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-bedrock.html`
  before citing in an SSP.
- Azure OpenAI will retire gpt-4o 0513 and gpt-4o-mini 0718 on
  3/31/2026. Contractors citing these versions in an SSP after
  that date have a correctness problem.
- Vertex AI Assured Workloads will add model families and
  potentially new Assured Workloads data boundaries. Re-verify
  against
  `cloud.google.com/assured-workloads/docs/release-notes`.
- Vertex AI IL5 authorization is roadmap at 2026-04-21. When
  it lands, update the hub tier-snapshot and this file's Vertex
  AI section to reflect the new IL tier.
- Model version transitions within each provider (Claude 4 →
  4.5 → future; GPT-5.1 → future; Gemini version transitions)
  follow a months-to-quarters cadence. Underlying authorization
  typically survives version transitions; specific model
  identifiers shift.

Next full re-verification pass is scheduled for the corpus
review cycle or when any AI service provider announces a tier-
level authorization change (new IL coverage, new Assured
Workloads tier, new GovCloud region).
