# AI Services Compliance (Overview)

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2 (DoD
> CIO); DFARS 252.204-7012; FedRAMP program documentation
> (fedramp.gov) and FedRAMP Marketplace (marketplace.fedramp.gov);
> AWS Bedrock FedRAMP authorization status
> (aws.amazon.com/compliance/services-in-scope/FedRAMP/amazon-bedrock-models/);
> Azure Government FedRAMP announcements
> (devblogs.microsoft.com/azuregov); Google Cloud Assured Workloads
> documentation (cloud.google.com/assured-workloads); Anthropic
> Trust Center (trust.anthropic.com) and Claude on Vertex AI
> announcement (claude.com/blog/claude-on-google-cloud-fedramp-high);
> Coder compliance documentation (coder.com); DoD CSP SRG v1r1
> (public.cyber.mil); NIST CMVP validated modules registry
> (csrc.nist.gov).

## Overview

This file is the hub for `references/modern-it/ai-services/`. A
defense contractor handling CUI or FCI under DFARS 252.204-7012
increasingly needs AI-service access for development, analytical,
and content-generation workflows. The compliance question splits
three ways: (1) which cloud AI services carry FedRAMP authorization
appropriate for CUI, (2) when a contractor must self-host (on-prem,
air-gapped, or IaaS-hosted under a contractor-authored boundary),
and (3) how AI developer tools (Claude Code, GitHub Copilot,
Cursor, similar) handle CUI exposure through prompt context even
when a model provider is FedRAMP-authorized.

Three per-vendor files live alongside this hub:

- **`fedramp-ai-services.md`.** Amazon Bedrock in AWS GovCloud
  (FedRAMP High + DoD IL4/IL5), Azure OpenAI Service in Azure
  Government (FedRAMP High + DoD IL4/IL5), Vertex AI via Google
  Cloud Assured Workloads (FedRAMP High + DoD IL2), with per-model
  authorization breakdowns per provider.
- **`self-hosted-ai.md`.** Coder as a self-hosted cloud
  development environment pattern, on-prem LLM inference, and
  air-gapped deployments. Contractor-authored compliance
  boundaries inheriting from the underlying IaaS or on-prem
  infrastructure.
- **`ai-dev-tools.md`.** Claude Code, GitHub Copilot, Cursor,
  and adjacent AI coding assistants. CUI-boundary scoping for
  the prompt-processing surface distinct from the underlying
  model authorization.

Read this file for the directory's conventions, the three-column
capability-orthogonal crosswalk, hybrid architectural patterns,
and the decision tree for selecting AI services. Read the
per-vendor files for model-level detail, per-service authorization
posture, and implementation guidance.

---

## Scope of this directory

Covered:

- Amazon Bedrock in AWS GovCloud (US) with the FedRAMP-High-scope
  Claude and Llama model subsets; Azure OpenAI Service in Azure
  Government with the FedRAMP-High-scope OpenAI model subset;
  Vertex AI via Google Cloud Assured Workloads with the FedRAMP-
  High-scope model subset including Claude.
- Anthropic direct API, OpenAI direct API, and Google Gemini
  direct API commercial surfaces, with migration paths to the
  FedRAMP-authorized routes above for CUI workloads. The direct
  APIs are appropriate for non-CUI development environments,
  synthetic-data workflows, and publicly-available-data tasks;
  they are not appropriate for CUI.
- Self-hosted AI patterns: Coder on FedRAMP-authorized IaaS, on-
  premises LLM inference (Llama, Mistral, open-weight models on
  contractor-owned GPUs), and fully air-gapped deployments for
  classified-adjacent CUI.
- AI developer tools (Claude Code, GitHub Copilot, Cursor,
  similar) scoped against CUI boundary through their prompt-
  processing and workspace-context-collection semantics.
- Hybrid architectures combining a primary suite (Microsoft 365
  GCC High or Google Workspace Assured Controls Plus) with AI
  adjacency.

Not covered:

- Commercial SaaS AI tiers of the three named providers outside
  their FedRAMP authorization boundary (commercial Bedrock, Azure
  OpenAI commercial, Vertex AI without Assured Workloads). These
  are scope problems for CUI work, not tuning problems; migration
  paths to the government-tier offerings are covered in
  `fedramp-ai-services.md`.
- ChatGPT, Claude.ai web, Gemini web, Perplexity, and similar
  consumer-grade AI products. These are not FedRAMP-authorized
  and are not appropriate for CUI regardless of workflow.
- Generic AI/ML frameworks (TensorFlow, PyTorch, scikit-learn,
  Hugging Face Transformers) as libraries. Framework compliance
  is inherited from the hosting platform; this directory treats
  managed AI services and dev tools, not library-level concerns.
- Classified AI deployments at IL6 and above beyond brief
  mention. Top Secret cloud AI (for example, Azure OpenAI in
  Azure Government Top Secret, announced January 2025) is
  workload-specific and outside CMMC L2 contractor scope.
- AI model training data provenance, foundation-model licensing,
  and bias-testing programs. Those are AI-governance concerns
  adjacent to but distinct from CMMC L2 compliance; consult
  NIST AI RMF and agency-specific AI policy guidance.

---

## The six conventions this directory follows

Four Decisions carry over from the Phase 5c cloud-platforms and
Phase 5d productivity hubs. Two Decisions are AI-services specific
(Decision 5 on the CUI boundary for the AI prompt surface, and
Decision 6 on the AI dev tools CUI boundary as a distinct layer).
The AI-specific drift posture (per-model authorization scope decay
runs faster than any other modern-IT category) is carried in the
Versioning and drift section rather than as a separate Decision,
since it is a drift-tracking policy rather than a structural
choice. Each Decision below is stated in prose with rationale.

### Decision 1: Provider-primary structural files with per-file capability appendix

**Per-vendor files are organized by that vendor's authorization
scope and model catalog.** Amazon Bedrock by GovCloud authorization
and per-model availability; Azure OpenAI Service by Government
authorization and per-model availability; Vertex AI by Assured
Workloads configuration and per-model availability. Each per-vendor
file carries a capability appendix (AI capability -> this provider's
service). This hub carries the three-column capability-orthogonal
crosswalk for multi-vendor readers.

**Rationale.** FedRAMP-authorized AI services differ architecturally
per provider in ways that capability-primary structure hides. Bedrock
exposes multiple model families (Claude, Llama, Titan, Cohere,
Mistral) under one authorization boundary; Azure OpenAI exposes only
OpenAI models; Vertex AI exposes Gemini plus Claude plus open-source
models. Per-model authorization status varies within each provider's
boundary (not every Bedrock model is in GovCloud). Provider-primary
mirrors the Phase 5c cloud-platforms and Phase 5d productivity
conventions where tenancy and per-service authorization are load-
bearing.

**Canonical capability-appendix format for per-vendor files.** Each
of `fedramp-ai-services.md`, `self-hosted-ai.md`, and
`ai-dev-tools.md` carries a two-column capability appendix with
this row shape:

| AI capability | This provider's service |
|---|---|
| Frontier-capability text generation | Claude 4.5 Sonnet on Bedrock (GovCloud) |
| Text embedding for retrieval | Amazon Titan Text Embeddings V2 on Bedrock (GovCloud) |

Row order matches the hub's three-column crosswalk below. The right
column names the specific service plus the model plus the
authorization tier. Per-vendor detail lives in structural
sections above the appendix; the appendix is a quick-reference
index, not a place for implementation depth.

### Decision 2: FedRAMP as primary axis; DoD Impact Level as overlay

**Every compliance claim in this directory uses FedRAMP
authorization as the primary axis and DoD Impact Level as a
declared overlay.** Service-level claims (Bedrock GovCloud is
FedRAMP High plus IL4/IL5, Azure OpenAI Government is FedRAMP
High plus IL4/IL5, Vertex AI via Assured Workloads is FedRAMP
High plus IL2) are the stable anchors; per-model authorization
claims (Claude 4.5 Sonnet is in GovCloud Bedrock scope as of
2026-04-21; GPT-5 is in Azure OpenAI Government scope; Gemini is
in Vertex AI Assured Workloads scope) carry dated verification
stamps inline.

**Rationale.** FedRAMP authorization is what CMMC L2 contractors
encounter directly under DFARS 252.204-7012. Per-provider per-model
authorization lag is severe: a model available in commercial Azure
OpenAI may be weeks or months away from Azure Government
availability; a Claude model version shipped on Bedrock commercial
may not be in GovCloud until a separate certification cycle
completes. FedRAMP as the primary axis keeps the prose legible at
service level while the per-model anchors sit in the per-vendor
files.

Full IL4 and IL5 implementation content remains deferred to a
future DoD-specific reference, consistent with the Phase 5c and
Phase 5d hub treatments (`references/modern-it/cloud-platforms/cloud-selection.md`
"FedRAMP baseline to DoD Impact Level crosswalk" and
`references/fedramp-gap.md` "Relationship to DoD Cloud Computing
Security Requirements Guide").

### Decision 3: Tenancy Selection for FedRAMP AI; Fit Assessment for self-hosted and dev tools

**`fedramp-ai-services.md` uses a Tenancy Selection section**
answering three questions in the same order as Phase 5c and 5d
(commercial acceptable for CUI? which government boundary or
Assured Workloads configuration? workload-location and personnel
boundaries?). This matches the established hub convention.

**`self-hosted-ai.md` and `ai-dev-tools.md` carry Fit Assessment
sections instead** because tenancy is not the relevant axis for
contractor-authored boundaries or for developer tools that
federate across multiple model providers. Each tool answers four
questions: is the underlying service FedRAMP-authorized, at what
level, what is the CUI-handling story for the prompt surface,
and what is the migration path if the tool cannot handle CUI
directly.

**Rationale.** FedRAMP AI service selection is first a tenancy
decision (Bedrock GovCloud vs commercial, Azure OpenAI Gov vs
commercial, Vertex AI Assured Workloads configuration) with
downstream model-availability implications. Self-hosted AI is a
contractor-boundary decision, not a tenancy decision. AI dev
tools are a prompt-surface decision where the model backend may
be FedRAMP-authorized but the dev-tool's workspace-context
collection creates a separate CUI exposure path.

### Decision 4: Hybrid patterns in this hub only

**Common hybrid architectures live here; per-vendor files forward-
reference rather than duplicate.** See "Hybrid patterns" below.

**Rationale.** Hybrid is a multi-vendor decision by definition.
Centralization prevents three divergent treatments from diverging
within months of authoring.

### Decision 5: CUI boundary for the AI prompt surface is load-bearing

**The prompt is CUI. The model context is CUI. The model output
may be CUI-derived.** Every section of this directory treats the
prompt surface as a first-class CUI asset, not as incidental input
to a compliance-elsewhere service. This contrasts with productivity
files where CUI lives in documents and attachments (stored state);
AI services process CUI as ephemeral inference input.

**Implications.**

- FedRAMP authorization on the model service means "the inference
  service can process CUI under the authorized boundary." It does
  not mean "any context the developer attaches to a prompt is in
  scope." Workspace-context collection by an AI coding assistant,
  RAG retrieval-augmentation context, and tool-use tool-call
  results are separate exposure paths; each must be evaluated
  against the contractor's CUI boundary.
- Output retention is a CUI exposure path. Azure OpenAI's default
  abuse-monitoring retention (30 days of prompt/response logging
  for safety review) is turned off for Azure Government at the
  package level; verify per-tenant configuration before loading
  CUI. Bedrock has a similar configuration surface. Retention
  configuration is part of the SSP, not an assumed default.
- Fine-tuning is a CUI exposure path. Fine-tuning a model on CUI
  data creates a derived artifact whose FedRAMP scope inherits
  from the training service; document the fine-tune artifact as
  a CUI asset and scope the retention and access posture
  accordingly.
- Agent tool-use is a CUI exposure path. An agent that calls
  tools (search, code execution, file read, external API) can
  exfiltrate CUI through tool-call destinations; each tool-use
  integration is a scope question separate from the model
  service's authorization.

**Rationale.** AI services are architecturally different from
storage or compute: the prompt-inference-output cycle crosses CUI
boundary surfaces that file-storage and compute-tenancy
decisions do not encounter. Treating the prompt as first-class
CUI avoids the common mistake of assuming "the service is FedRAMP
High, so my workflow is covered."

### Decision 6: AI dev tools carry distinct CUI-boundary treatment

**AI developer tools sit one layer above Decision 5.** Decision 5
names the prompt-surface CUI exposure generally; Decision 6
scopes the specific case of developer tools that process
workspace content as part of normal operation. A dev tool backed
by a FedRAMP-authorized model (Claude Code configured to hit
Bedrock GovCloud; GitHub Copilot Enterprise with Azure OpenAI
Government backend) has two distinct CUI-boundary questions: the
model-service authorization (Decision 5) and the dev-tool layer's
workspace-context-collection, telemetry, and cache semantics
(this Decision). Dev tools (Claude Code, GitHub Copilot, Cursor,
Windsurf, Continue, similar) each expose CUI through workspace
context and prompt content independently of the underlying model
service's authorization.

In scope:

- Claude Code configured against Anthropic direct API, Amazon
  Bedrock, or a self-hosted Claude deployment.
- GitHub Copilot Enterprise with federated access to underlying
  models.
- Cursor, Windsurf, Continue, and similar IDE-integrated AI
  coding assistants.

Out of scope (per Decision 6 scope boundary):

- Consumer AI coding assistants (Copilot Individual, public
  ChatGPT web interface, Claude.ai web interface) for CUI
  workflow. These are commercial-SaaS tiers not authorized for
  CUI; use the FedRAMP-authorized path.
- Model fine-tuning for specific dev-tool personalization
  (retention and authorization of the derived model is covered
  in `fedramp-ai-services.md`, not in the dev-tools file).
- Non-AI developer tools (IDEs, version control, CI/CD) covered
  elsewhere in `references/modern-it/productivity/legacy-dib-tools.md`
  and `references/modern-it/endpoints/windows-fleet.md`.

**Rationale.** The CUI-exposure question at the dev-tool surface
is architecturally different from the model-service question.
Treating them together flattens a real distinction; contractors
frequently deploy a dev tool against a FedRAMP-authorized model
backend while the dev tool itself still leaks workspace CUI
through context windows, telemetry, or crash reports. The
dev-tools file is the natural owner of that distinction.

---

## Tier-level authorization snapshot

All claims below verified 2026-04-21 via vendor compliance pages
named at top. Per-model authorization detail lives in the per-vendor
files; this snapshot is service-tier only.

| Provider / service | FedRAMP tier | DoD IL | CUI suitability |
|---|---|---|---|
| Amazon Bedrock (AWS GovCloud US) | FedRAMP High | IL4, IL5 | Appropriate for CUI under DFARS 7012; model-availability subset documented per-model |
| Amazon Bedrock (commercial AWS) | FedRAMP High (on AWS commercial boundary) | IL2 | Not appropriate for CUI; use GovCloud |
| Azure OpenAI Service (Azure Government) | FedRAMP High | IL4, IL5 | Appropriate for CUI; model-availability subset documented per-model |
| Azure OpenAI Service (Azure commercial) | FedRAMP High (on Azure commercial) | IL2 | Not appropriate for CUI; use Azure Government |
| Vertex AI (Google Cloud Assured Workloads FedRAMP High) | FedRAMP High | IL2 | Appropriate for CUI scenarios where IL2 boundary suffices; Claude and Gemini model availability documented per-model |
| Vertex AI (Google Cloud commercial) | FedRAMP Moderate (on specific services) | n/a directly | Not appropriate for CUI; use Assured Workloads |
| Self-hosted AI on Azure Government or AWS GovCloud | Contractor-authored | Inherited from platform | Contractor holds full compliance; FIPS and boundary posture depend on hosting |
| Self-hosted AI on-premises or air-gapped | Contractor-authored | Contractor-authored | Contractor holds full compliance including physical and operational |
| Anthropic direct API (commercial) | Not FedRAMP-authorized at direct-API surface | n/a | Not appropriate for CUI; use Bedrock GovCloud or Vertex AI Assured Workloads |
| OpenAI direct API (commercial) | Not FedRAMP-authorized at direct-API surface | n/a | Not appropriate for CUI; use Azure OpenAI Government |
| Claude Code (anthropic.com surface, direct-API backend) | Not FedRAMP-authorized | n/a | Backend configuration required: route Claude Code to Bedrock GovCloud for CUI workflow |
| GitHub Copilot (commercial) | Not FedRAMP-authorized at the Copilot service | n/a | Copilot Enterprise with Azure OpenAI Government backend is the federal path; verify current scope |

**Reading the snapshot.** This table is a directory-level map, not
an implementation guide. Per-vendor files carry the model-by-model
authorization breakdown (which Bedrock models are in GovCloud,
which OpenAI models are in Azure Government, which Vertex AI
models are in Assured Workloads FedRAMP High). A contractor
building an SSP cites the per-vendor file's dated per-model claims,
not this snapshot.

**Top Secret note.** Azure OpenAI (including GPT-4o) received an
authorization for use in Azure Government Top Secret as of January
2025. IL6 and Top Secret cloud AI are workload-specific and
outside CMMC L2 scope; contractors with IL6 or TS mission workloads
work with the cloud provider's government-sales team directly
rather than from a CMMC L2 reference.

**Direct-API surface note.** Anthropic and OpenAI both offer
commercial direct-API surfaces. Neither is FedRAMP-authorized at
the direct-API layer. Contractors needing programmatic access to
Claude or GPT models for CUI workloads route through Bedrock
GovCloud (Claude), Azure OpenAI Government (OpenAI models), or
Vertex AI Assured Workloads (Claude, Gemini). The direct-API
surfaces are appropriate for non-CUI work and for development
environments handling synthetic or publicly-available data.

---

## Capability-orthogonal crosswalk

The table below maps AI capabilities to the three categories a
reader chooses among: FedRAMP-authorized managed services (MaaS),
self-hosted patterns the contractor operates, and AI dev tools
that consume a model backend. Rows are capability clusters.
Columns are the three source categories; dev tools consume a
MaaS or self-hosted backend rather than providing capabilities
directly, so dev-tool rows are filled only where the tool's
prompt-surface is itself the distinguishing element. Per-vendor
files decompose each cell into specific service-to-model mapping.

| AI capability | FedRAMP-authorized cloud AI | Self-hosted AI | AI dev tools |
|---|---|---|---|
| Frontier-capability text generation | Claude 4.5 Sonnet (Bedrock GovCloud); GPT-5 family (Azure OpenAI Gov); Claude 3.7 Sonnet and Gemini (Vertex AI Assured Workloads) | Llama 3.3 70B or similar open-weight on contractor GPUs | Claude Code, GitHub Copilot Enterprise routed to the authorized backend |
| Small-model text generation | Claude Haiku 4.5 (Bedrock GovCloud); GPT-4o-mini (Azure OpenAI Gov); Gemini Flash (Vertex AI) | Llama 3 8B, Mistral 7B, Phi on contractor infrastructure | - |
| Code generation | Claude 4.5 Sonnet (Bedrock GovCloud); GPT-5 (Azure OpenAI Gov); Codestral or similar on Vertex AI | Code Llama, DeepSeek-Coder on contractor GPUs | Claude Code, Copilot, Cursor, Continue |
| Text embedding for retrieval | Amazon Titan Text Embeddings V2 (Bedrock GovCloud); Azure OpenAI ada-002 or text-embedding-3 (Gov); Gecko (Vertex AI) | Sentence-Transformers, BGE models on contractor infrastructure | - |
| Multimodal (vision plus text) | Claude 4.5 Sonnet (Bedrock); GPT-4o (Azure OpenAI Gov); Gemini 2.5 Pro (Vertex AI) | LLaVA, Llama Vision on contractor GPUs | IDE-integrated vision for screenshot analysis (dev-tool specific) |
| Structured output and tool-use | Claude (Bedrock); GPT-4o / GPT-5 (Azure OpenAI Gov); Gemini (Vertex AI) | Open-weight models with structured-output post-processing | Claude Code skills, Copilot extensions |
| Fine-tuning and customization | Bedrock Custom Models (GovCloud); Azure OpenAI fine-tuning (Gov); Vertex AI tuning | Full-weight fine-tuning on contractor GPUs (LoRA, full-parameter) | - |
| Retrieval-augmented generation (RAG) | Amazon Bedrock Knowledge Bases (GovCloud); Azure AI Search plus Azure OpenAI (Gov); Vertex AI Search plus RAG Engine | Open-source vector databases (pgvector, Qdrant, Weaviate) on contractor infrastructure | - |
| Agent orchestration | Amazon Bedrock Agents (GovCloud); Azure AI Agent Service (Gov); Vertex AI Agent Engine (Assured Workloads Preview) | LangChain, LlamaIndex, contractor-authored agent runtime | - |
| Prompt caching and context optimization | Bedrock prompt caching (GovCloud); Azure OpenAI prompt caching (Gov); Vertex AI context caching | Contractor-authored caching layer | Dev-tool-specific context strategies |
| Content safety and guardrails | Bedrock Guardrails (GovCloud); Azure AI Content Safety (Gov); Vertex AI Safety (Assured Workloads) | NeMo Guardrails, Llama Guard, contractor-authored filters | Dev-tool workspace-trust and telemetry configuration |
| Model inventory and monitoring | CloudTrail plus Bedrock model invocation logs (GovCloud); Azure Monitor plus Azure OpenAI logs (Gov); Vertex AI monitoring (Assured Workloads) | Contractor-authored telemetry, OpenTelemetry-instrumented inference servers | Dev-tool telemetry export to SIEM |

**Reading the crosswalk.** A hyphen in a cell means that column's
family does not provide the capability in a CUI-suitable way at
this writing. Where a capability spans multiple cells, the choice
is primarily cost and operational preference rather than
compliance posture (for example, frontier text generation is
available across all three FedRAMP-authorized families; pick the
one that matches the contractor's existing cloud commitment).

**What the crosswalk does not claim.** It does not claim model
parity across cells. Claude 4.5 Sonnet on Bedrock GovCloud and
GPT-5 on Azure OpenAI Government are not equivalent models; they
have different capabilities, different context windows, different
tool-use semantics, and different pricing. The crosswalk maps
which family offers a capability, not whether the specific model
serves a contractor's application.

---

## Hybrid patterns

AI architectures in the defense industrial base frequently combine
multiple of the above families. Four recurring patterns are named
here; per-vendor files forward-reference this section.

### Pattern A: Primary suite plus FedRAMP AI for model access

A contractor runs Microsoft 365 GCC High or Google Workspace
Assured Controls Plus for productivity and routes AI inference
through a FedRAMP-authorized managed service with identity
federation from the primary-suite IdP. The natural pairings are
M365 GCC High plus Azure OpenAI Government (same cloud tenancy,
Entra ID Government federation, shared SIEM) and Workspace
Assured Controls Plus plus Vertex AI Assured Workloads (same
cloud family, Cloud Identity federation).

Cross-cloud is also supported: a contractor whose workload
depends on a Claude-specific capability (agent tool-use,
extended context, specific model behaviors) can run M365 GCC
High and route AI traffic to Amazon Bedrock in AWS GovCloud
with identity federation from Entra ID Government to AWS IAM
Identity Center. The cross-cloud path adds operational
complexity (two government-tenancy relationships, SIEM
aggregation across clouds) but preserves model choice.

**When this works.** CUI document-generation, code-review, and
analytical workflows where the model output is drafted back into
the primary suite's document library or codebase. Compliance
posture inherits from both the primary suite and the AI service.

**When this fails.** Routing the AI service to a commercial
tenancy outside the primary suite's boundary. M365 GCC High
paired with Azure OpenAI commercial (not Government) is a scope
problem; so is GCC High paired with Anthropic's direct API for
Claude access rather than Bedrock GovCloud. The AI output is
CUI-derived and cannot legally cross the commercial boundary.

### Pattern B: Self-hosted AI for ITAR-controlled or air-gapped workflow

A contractor handling ITAR-controlled technical data, air-gapped
classified-adjacent workflow, or contract terms that prohibit
third-party AI service routing self-hosts inference on
contractor-owned GPUs. On-premises or inside Azure Government /
AWS GovCloud inside a contractor-authored boundary.

**When this works.** ITAR-controlled source code, aerospace
design data, or any CUI category where third-party cloud AI
service routing is contractually prohibited. Open-weight models
(Llama, Mistral, open-weight Claude variants where available)
inference on contractor-owned hardware gives full control over
prompt, context, and output surfaces.

**When this fails.** Small contractors without operations
capacity for inference infrastructure at production reliability.
Self-hosted AI is a real engineering commitment: GPU fleet
management, model versioning, safety and guardrail infrastructure,
monitoring, and cost at scale.

### Pattern C: AI dev tools routed through FedRAMP backend

A contractor runs Claude Code, GitHub Copilot, or Cursor against
a FedRAMP-authorized model backend (Bedrock GovCloud, Azure
OpenAI Government, Vertex AI Assured Workloads) rather than
against the dev-tool vendor's commercial direct API. Workspace-
trust configuration and telemetry-export discipline keep the
dev-tool layer's CUI exposure scoped.

**When this works.** Development work on CUI-containing code
where the model backend is routed through a FedRAMP-authorized
path. The dev-tool vendor may emit some telemetry; configuration
at the dev-tool layer limits what leaves the contractor's
boundary.

**When this fails.** Default-configuration deployment that routes
to the dev-tool vendor's commercial direct API. A developer
opening Claude Code against Anthropic's direct API while editing
CUI-containing code has a scope breach, not a configuration
issue.

---

## AI service selection decision tree

When selecting an AI service for a CUI workload, walk the
questions in this order. Store the answers in the SSP.

1. **Is CUI present in the prompt, context, or expected output?**
   If no, commercial AI services are available. If yes, continue.
2. **Which Cloud Computing Security Requirements Guide (CC SRG)
   Impact Level applies?** IL4 is the common DIB level; IL5 is
   mission-critical; IL6 is classified (out of CMMC L2 scope).
   Bedrock GovCloud and Azure OpenAI Government carry IL4 and
   IL5; Vertex AI via Assured Workloads carries IL2 at the AI
   layer (with IL4/IL5 roadmap for specific configurations).
   Route the decision accordingly.
3. **Is ITAR (International Traffic in Arms Regulations) or EAR
   (Export Administration Regulations) export-controlled data in
   the prompt or context?** If yes, the contractor needs
   sovereign or air-gapped assurance. Self-hosted AI (on-premises
   or inside a contractor-authored IaaS boundary) is the typical
   path. Consult export-control counsel before routing ITAR data
   through any third-party AI service.
4. **Which primary suite does the contractor run?** M365 GCC
   High pairs naturally with Azure OpenAI Government (identity
   federation, shared audit destination, shared operator-access
   posture). Workspace Assured Controls Plus pairs naturally
   with Vertex AI Assured Workloads. Bedrock GovCloud is cloud-
   agnostic at the identity layer but adds cross-cloud
   operational complexity.
5. **Which specific model capabilities does the workload need?**
   Claude-specific capabilities favor Bedrock or Vertex AI; GPT-
   specific capabilities favor Azure OpenAI; Gemini-specific
   capabilities favor Vertex AI. Model choice is primarily a
   capability question; the provider choice follows.
6. **Is the workload an AI developer tool (Claude Code, Copilot,
   Cursor, similar)?** If yes, the model backend question above
   is one layer; the dev-tool CUI-boundary question is a
   separate layer. See `ai-dev-tools.md` for the workspace-trust,
   telemetry-export, and prompt-context discipline specific to
   dev tools.
7. **Is an agent-orchestration or RAG pattern required?** Each
   FedRAMP-authorized provider exposes agent-orchestration
   tooling (Bedrock Agents, Azure AI Agent Service, Vertex AI
   Agent Engine) at slightly different maturity levels and
   different tool-use semantics. Per-vendor files cover the
   specifics.

This is a decision process, not a ranking. No AI service is
better for CUI in the abstract; each fits different contractor
circumstances, existing-infrastructure commitments, and model-
capability needs.

---

## Cross-domain anchors

AI-service posture composes with corpus cross-cutting files and
domain practice files:

- **FedRAMP framing.** `references/fedramp-gap.md` for FedRAMP
  program context, CSP SRG v1r1 reciprocity, and DFARS 7012
  CSP-equivalence mechanics.
- **Cloud-platform dependencies.** `references/modern-it/cloud-platforms/cloud-selection.md`
  for the cloud-platform selection under which AI services run
  (Bedrock GovCloud on AWS GovCloud; Azure OpenAI Government on
  Azure Government; Vertex AI on Google Cloud Assured Workloads).
- **Productivity-plane pairing.** `references/modern-it/productivity/README.md`
  for the primary suite that typically pairs with an AI service
  (M365 GCC High with Azure OpenAI Government; Workspace Assured
  Controls Plus with Vertex AI Assured Workloads).
- **Endpoint-plane interaction.** `references/modern-it/endpoints/windows-fleet.md`
  and `macos-fleet.md` for the endpoint posture of developers
  using AI dev tools on CUI-containing code.
- **CUI scoping.** `references/scoping-and-cui.md` for the
  decision of what sits in CUI scope across AI prompt and
  context surfaces.
- **SSP authoring.** `references/ssp-guidance.md` for how to
  document AI-service inheritance and dev-tool configuration in
  the SSP.

Domain practice files used for requirement text and evidence
lists:

- Access Control (AC). `references/domains/ac-access-control.md`
  for account management on AI-service surfaces and identity
  federation to the AI-service backend.
- System and Communications Protection (SC).
  `references/domains/sc-system-comms.md` for encryption in
  transit from dev tools to model backends and for data-at-rest
  on prompt caches and model artifacts.
- Configuration Management (CM).
  `references/domains/cm-configuration-mgmt.md` for change
  control on AI-service feature rollouts and model-version
  transitions.
- Audit and Accountability (AU).
  `references/domains/au-audit.md` for audit logging of AI-
  service invocations and dev-tool prompt-submission events.
- System and Information Integrity (SI).
  `references/domains/si-system-information-integrity.md` for
  guardrail and content-safety monitoring on AI outputs.
- Awareness and Training (AT).
  `references/domains/at-awareness-training.md` for training
  contractor personnel on AI-service CUI-boundary discipline
  (prompt content, context attachment, output retention).

---

## Terminology

Acronyms used in this directory. Terms defined in
`references/modern-it/cloud-platforms/cloud-selection.md`,
`references/modern-it/productivity/README.md`, or previous Phase
5 slices are not repeated here.

**Assured Workloads (Google Cloud).** The Google Cloud compliance
overlay for FedRAMP Moderate, FedRAMP High, and IL2 workloads.
Distinct from Google Workspace Assured Controls Plus; Assured
Workloads applies to Google Cloud infrastructure (compute,
storage, Vertex AI), while Assured Controls Plus applies to
Workspace productivity.

**Bedrock Guardrails.** Amazon Bedrock's content-safety filtering
and policy-enforcement feature, applied at inference time to
constrain model inputs and outputs.

**Bedrock Knowledge Bases.** Amazon Bedrock's managed retrieval-
augmented-generation (RAG) service providing vector-store-backed
context injection into prompts.

**CDE (Cloud Development Environment).** A managed developer
workspace running inside cloud infrastructure, accessed by
developers through web or thin-client. Coder is a self-hosted
CDE platform.

**Content Safety (Azure AI Content Safety).** Azure's content-
safety filtering service analogous in purpose to Bedrock
Guardrails and Vertex AI Safety.

**Direct API (in AI context).** The vendor's commercial-cloud
API surface for a model service (anthropic.com API for Claude,
api.openai.com for OpenAI models, generativelanguage.googleapis.com
for Gemini). Distinct from FedRAMP-authorized routes (Bedrock
GovCloud, Azure OpenAI Government, Vertex AI Assured Workloads).

**Fine-tuning (in AI context).** The process of adapting a
foundation model to a specific domain or task by further
training on contractor-owned data. The resulting fine-tuned
model inherits authorization from the training service; the
fine-tune artifact is a CUI asset when trained on CUI data.

**Foundation model.** A large pre-trained AI model (Claude, GPT,
Gemini, Llama) used as the base for downstream tasks. "Frontier
models" is the common marketing term for the highest-capability
foundation models; this file uses both interchangeably.

**Guardrails.** Content-safety, policy-enforcement, and PII-
detection mechanisms applied at inference time or in an adjacent
layer. Each FedRAMP-authorized AI provider exposes guardrail
tooling; self-hosted patterns require contractor-authored or
open-source guardrail layers.

**IL2 (DoD Impact Level 2).** Defined in
`references/modern-it/cloud-platforms/cloud-selection.md`. Vertex
AI Assured Workloads at FedRAMP High is IL2-authorized at the AI
layer as of 2026-04-21.

**Inference.** The forward-pass execution of a trained model on
an input prompt. Distinct from training and fine-tuning; most
AI-service workloads in this directory are inference-only.

**LoRA (Low-Rank Adaptation).** A parameter-efficient fine-tuning
technique that adapts a foundation model with a small number of
additional weights rather than retraining the full model. Common
for self-hosted fine-tuning on contractor GPUs.

**MaaS (Model-as-a-Service).** The FedRAMP-authorized cloud AI
pattern where the model runs as a managed service rather than
on contractor-owned inference infrastructure. Bedrock, Azure
OpenAI, and Vertex AI are all MaaS surfaces.

**Prompt caching.** A performance optimization where repeated
prefix content in prompts is cached server-side to reduce latency
and cost. Each FedRAMP-authorized provider exposes prompt-caching
with distinct cache-retention semantics.

**RAG (Retrieval-Augmented Generation).** The pattern of
augmenting a model's prompt with contextually-retrieved content
from a vector store or knowledge base. RAG context attached to a
prompt is a CUI exposure path if the retrieved content contains
CUI; see Decision 5.

**Structured output.** The capability of constraining a model's
response to a specific schema (JSON schema, function-call
signature). All three FedRAMP-authorized providers support
structured output at varying maturity.

**Titan (Amazon Titan).** Amazon's own-branded AI model family
available on Bedrock, including text-generation, embedding, and
image-generation variants. Titan Text Embeddings V2 is the
primary Titan model in Bedrock GovCloud scope as of 2026-04-21.

**Tool-use.** The capability of a model to invoke external tools
(search, code execution, file read, API call) as part of its
inference. Tool-use destinations are separate CUI-exposure paths
from the model service's authorization boundary; see Decision 5.

---

## Versioning and drift

AI-service content is the highest-drift content in this corpus.
Foundation-model families ship monthly; FedRAMP per-model
authorization updates run weekly-to-monthly in continuous
monitoring; managed-service feature additions (new Bedrock
Agents capability, new Azure OpenAI Assistants feature, new
Vertex AI Agent Engine maturity tier) ship faster than file-
level authoring can track.

Per the verify-at-source-with-dated-stamp pattern:

- Service-level claims (Bedrock GovCloud is FedRAMP High +
  IL4/IL5; Azure OpenAI Government is FedRAMP High + IL4/IL5;
  Vertex AI via Assured Workloads is FedRAMP High + IL2) are the
  stable anchors for this verification date. Re-verify at the
  next slice review or when any provider announces a new IL
  coverage level.
- Per-model authorization claims carry dated stamps inline in
  the per-vendor files. Each stamp reads "verified YYYY-MM-DD"
  with a pointer to the primary source.
- Feature-level claims (Bedrock Guardrails PII-detection
  capabilities, Azure OpenAI Assistants agent-orchestration
  maturity, Vertex AI Agent Engine preview-vs-GA status) are
  labeled "as of YYYY-MM, verify current vendor documentation
  before implementing."
- Model rebranding and version transitions (Claude 3.5 Sonnet v1
  -> v2 -> 3.7 Sonnet -> Claude 4 Sonnet -> Claude 4.5 Sonnet is
  a recent example; GPT-4 -> GPT-4o -> GPT-5 is another)
  happen on a months-to-quarters cadence. The underlying
  authorization typically survives the version transition;
  specific model identifiers shift. Verify names at the provider's
  current documentation when citing in SSP authoring.

This hub's content is verified 2026-04-21. Next full re-
verification pass is scheduled for the corpus review cycle or
when any AI-service provider announces a service-tier
restructuring (a new IL-level authorization, a new Assured
Workloads tier, a new GovCloud region offering).
