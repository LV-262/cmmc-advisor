# Self-Hosted AI Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2
> (DoD CIO); DFARS 252.204-7012; Coder documentation
> (coder.com/docs); Meta Llama 3 model card and license
> (llama.com); Mistral AI model licenses (mistral.ai); AWS
> GovCloud architecture guidance
> (docs.aws.amazon.com/govcloud-us/); Azure Government
> architecture guidance (learn.microsoft.com/en-us/azure/azure-
> government/); Google Cloud Assured Workloads documentation
> (cloud.google.com/assured-workloads); DoD CSP SRG v1r1
> (public.cyber.mil); NIST CMVP validated modules registry
> (csrc.nist.gov); 22 CFR Parts 120-130 (ITAR) and 15 CFR Parts
> 730-774 (EAR) for export-control framing.

## Overview

This file covers self-hosted AI patterns for defense contractors
where managed FedRAMP AI services (Bedrock GovCloud, Azure
OpenAI Government, Vertex AI Assured Workloads — see
`fedramp-ai-services.md`) do not fit the workload. Three patterns:
Coder as a self-hosted cloud development environment (CDE) for
AI-adjacent development workflow; on-premises or contractor-
authored-boundary LLM inference on open-weight models; and fully
air-gapped deployments for classified-adjacent or ITAR-scope
workloads.

Self-hosted AI differs architecturally from the FedRAMP AI
services in `fedramp-ai-services.md`: there is no vendor
authorization package covering the AI service itself. The
contractor authors the entire compliance boundary. Inheritance
flows from the underlying cloud platform (Azure Government, AWS
GovCloud) or from the contractor's on-premises infrastructure
when fully on-prem. The SSP carries the full authorization
burden; vendor software (Coder, Llama, Mistral, Qwen, open-source
inference servers) provides the building blocks but no
compliance cover.

Read this file alongside the Phase 5 AI hub at
`references/modern-it/ai-services/README.md` (six Decisions
including the Fit Assessment pattern for self-hosted per
Decision 3, and the prompt-surface CUI boundary per Decision 5)
and the Phase 5c cloud-platforms files
(`aws-govcloud.md`, `azure-government.md`) for the platform
authorization that contractor-authored boundaries inherit from.

---

## Scope of this file

Covered:

- **Coder** — the self-hosted Cloud Development Environment
  (CDE) platform deployed on FedRAMP-authorized IaaS or on-
  premises, providing managed workspaces for developers working
  on CUI-containing code or AI-augmented workflows.
- **On-premises LLM inference** — open-weight foundation models
  (Meta Llama, Mistral AI, Qwen, DeepSeek, Microsoft Phi,
  Google Gemma) deployed on contractor-owned GPUs (on-premises
  data center, colocated hardware, or contractor-authored
  IaaS boundary). Inference serving via vLLM, TGI, llama.cpp,
  Triton, or contractor-authored runtimes.
- **Air-gapped deployments** — fully disconnected-from-the-
  internet AI infrastructure for classified-adjacent CUI, ITAR-
  controlled technical data, or contract terms prohibiting any
  third-party cloud routing. On-premises GPU clusters with air-
  gap boundary enforcement.
- **Hybrid patterns** combining self-hosted AI with
  FedRAMP-authorized cloud AI (Slice U) or with AI dev tools
  (Slice W) where the dev tool routes to a self-hosted model
  backend.

Not covered:

- FedRAMP-authorized managed AI services (Bedrock GovCloud,
  Azure OpenAI Government, Vertex AI Assured Workloads).
  Covered in `fedramp-ai-services.md`. A contractor using one of
  these does not need self-hosted AI for the same capability.
- AI developer tools (Claude Code, GitHub Copilot Enterprise,
  Cursor, Windsurf, Continue). Covered in `ai-dev-tools.md`.
  When a dev tool routes to a self-hosted backend, that
  configuration is a hybrid pattern whose dev-tool layer lives
  in `ai-dev-tools.md`.
- GPU hardware selection (NVIDIA H100/H200/B200, AMD MI300X,
  Intel Gaudi). Hardware choice is an infrastructure question
  outside CMMC L2 scope; the compliance posture is about what
  runs on the hardware and how the boundary is enforced, not
  which accelerator family.
- Foundation-model pretraining. Contractor-authored pretraining
  of a frontier model is out of scope for this directory;
  fine-tuning open-weight models on contractor data is covered.
- Classified-system AI deployments at IL6 and above in
  implementation depth. Air-gapped patterns below address the
  architectural shape; IL6+ implementation is contract-
  specific and outside CMMC L2 scope.

---

## Fit Assessment — four-question structure

Each self-hosted pattern below answers the same four questions in
the same order. Per hub Decision 3, Fit Assessment replaces
Tenancy Selection here because tenancy is not the axis a
contractor-authored boundary turns on.

1. Is the tool FedRAMP-authorized, and at what level?
2. What DoD Impact Level does the pattern reach?
3. What is the CUI-handling story for the prompt surface?
4. What is the migration path if the pattern cannot deliver the
   contractor's workload at scale?

Answers differ across patterns because each addresses a
different contractor constraint: Coder solves the developer-
workspace-boundary problem; on-prem LLM solves the model-
ownership problem; air-gapped AI solves the boundary-separation
problem.

---

## Coder — self-hosted Cloud Development Environment

**Coder** is a self-hosted CDE platform. Developers connect to
managed workspaces (VM or container) running inside the
contractor's compliance boundary rather than working on local
laptops that themselves carry CUI. The contractor operates the
Coder control plane and the workspace infrastructure; Coder
Inc. provides the software and commercial support under license
but does not touch contractor instances except under explicit
engagement.

**1. FedRAMP authorization.** None at the Coder-software layer.
Coder is self-hosted; the compliance boundary belongs to the
contractor. When Coder runs on Azure Government or AWS GovCloud,
inheritance flows from the FedRAMP High platform boundary
beneath. When Coder runs on-premises, the contractor's own
authorization package carries the burden.

**2. DoD Impact Level.** Determined by hosting. Coder on Azure
Government IL5 boundary with IL5-appropriate configuration
operates inside a contractor-authored IL5 package. Coder on AWS
GovCloud with IL4/IL5 configuration operates inside a contractor-
authored IL4/IL5 package. Coder on-premises reaches whatever IL
the contractor's facility and operational posture support.

**3. CUI-handling story.** Coder is appropriate for development
workflow where CUI-containing code lives inside the workspace
rather than on developer laptops. Typical fit:

- Developers on loaner or BYOD laptops where the endpoint is
  not a CUI asset; the workspace inside the contractor's
  boundary holds all CUI source code, CUI-derived build
  artifacts, and CUI-touching configuration.
- Onboarding acceleration: a new developer gets a configured
  workspace in minutes rather than waiting for a compliance-
  grade laptop issue.
- Ephemeral workspaces for short-duration CUI projects:
  workspace torn down at project end rather than persisting
  CUI residue on endpoints.

When Coder is routed to AI inference (OpenAI, Anthropic, self-
hosted LLM) from inside the workspace, the AI service's own
CUI-boundary applies. Coder is a workspace container, not an AI
service; it inherits the AI-service question from whichever
model backend the developer chooses.

**Not appropriate for.** Contractors without operations capacity
for a self-hosted CDE at compliance-grade reliability. Coder's
value compounds at fleet scale; for small teams, the operational
overhead often exceeds the endpoint-discipline savings.

**4. Migration path when fit is no.** If Coder is operationally
too heavy, migrate to compliance-grade laptop issue with
contractor-approved endpoint controls (Intune on GCC High,
Workspace endpoint management) and treat the laptop as the CUI
asset. If the workspace-containment discipline is required but
Coder does not fit, evaluate alternatives (GitHub Codespaces
commercial is not FedRAMP-authorized for CUI; Azure DevTest Labs
on Azure Government is a more limited alternative).

**Implementation notes.**

- Workspace images: contractor-authored base images on FedRAMP-
  authorized IaaS marketplace images (Azure Government
  marketplace; AWS GovCloud marketplace) with FIPS-mode OS,
  FIPS-validated OpenSSL, and contractor-approved tooling.
- Identity: SAML or OIDC federation from the contractor's
  primary-suite IdP (Entra ID Government or Cloud Identity)
  into Coder's access-control plane.
- Network boundary: workspaces sit inside contractor VPC/VNet
  subnets with egress controls matching the contractor's CUI
  boundary. Coder control plane runs in a management subnet
  with its own access control.
- Audit: Coder audit logs export to the contractor's SIEM.
  Workspace activity (sessions, lifecycle events) flows through
  the same audit pipeline.

---

## On-premises LLM inference

Open-weight foundation models (Meta Llama 3 and Llama 4 families,
Mistral AI family, Qwen family, DeepSeek family, Microsoft Phi
family, Google Gemma family) deployed on contractor-owned GPU
infrastructure. Inference served via open-source runtimes (vLLM,
Text Generation Inference, llama.cpp, Triton Inference Server)
or contractor-authored inference servers.

**1. FedRAMP authorization.** None at the model or inference-
runtime layer. Open-weight models are released under permissive
licenses (Llama Community License, Mistral Apache 2.0, Qwen
license variants); the contractor hosts inference inside the
contractor's own authorization boundary. Platform inheritance
from Azure Government, AWS GovCloud, Google Cloud Assured
Workloads, or on-premises infrastructure carries the FedRAMP
coverage where applicable.

**2. DoD Impact Level.** Determined by infrastructure and
configuration. Open-weight inference on Azure Government IL5
boundary with IL5-appropriate configuration operates inside a
contractor-authored IL5 package. On-premises inference in a
facility meeting IL4/IL5 physical and operational controls
reaches the same IL level. Air-gapped on-premises infrastructure
can reach IL6 architecturally; IL6 authorization is contract-
specific and outside CMMC L2 scope.

**3. CUI-handling story.** On-prem LLM inference is appropriate
when:

- The specific model capability is not available in a FedRAMP-
  authorized managed service (a recent open-weight model
  released before provider authorization catches up; a fine-
  tuned model specific to the contractor's workload).
- ITAR-controlled technical data or EAR-controlled export-
  controlled data flows through the prompt surface and the
  contractor's export-control counsel requires boundary
  control beyond what managed-service operator-access
  commitments provide. This skill does not make ITAR or EAR
  determinations; consult export-control counsel before
  classifying a workload as ITAR-scope or EAR-scope.
- Contract terms prohibit third-party cloud AI routing even
  under FedRAMP authorization.
- Cost at inference volume makes managed-service pricing
  prohibitive and the contractor has GPU infrastructure
  already committed.
- Fine-tuning on CUI data where the fine-tune artifact must
  stay inside the contractor's boundary without being stored in
  a managed-service tenant.

Not appropriate for:

- Small contractors without operations capacity for GPU fleet
  management, model versioning, and inference-server SRE.
- Workloads needing frontier-capability models (Claude 4.5,
  GPT-5.1, Gemini frontier tier) where open-weight parity does
  not exist; the frontier gap between closed-model providers
  and open-weight releases is real for now.
- Multi-modal workloads beyond basic text where open-weight
  vision or audio support lags behind managed-service
  offerings.

**4. Migration path when fit is no.** Move to a FedRAMP-
authorized managed AI service (Bedrock GovCloud for Claude or
Llama access; Azure OpenAI Government for OpenAI models; Vertex
AI Assured Workloads for Claude or Gemini) when the operational
cost of self-hosting exceeds the value of model ownership. For
contractors who need both (ITAR-scope workloads plus non-ITAR
CUI), hybrid patterns below apply.

**Implementation notes.**

- Model licensing: verify the specific model's license permits
  the contractor's use case. Meta Llama 3 and 4 Community
  License has a 700 million monthly active user threshold;
  large contractors may not qualify under the free license
  terms. Mistral AI models under Apache 2.0 have the fewest
  restrictions. Some Qwen variants have commercial-use
  restrictions. Track licenses per-model in the SSP.
- Inference runtime choice: vLLM for high-throughput batched
  inference on large models; TGI (Hugging Face Text
  Generation Inference) for managed operational posture;
  llama.cpp for CPU-only or mixed-device deployment; Triton
  Inference Server for heterogeneous workloads. Runtime choice
  affects operational posture, not compliance posture.
- Fine-tuning: LoRA (Low-Rank Adaptation) fine-tuning on
  contractor-owned GPUs for efficiency; full-parameter fine-
  tuning for maximum customization. Fine-tune artifacts are
  CUI-derived assets when trained on CUI; document storage,
  access control, and retention in the SSP.
- Model updates: open-weight models release on weeks-to-months
  cadence. Contractor operations take over the model-update
  function that managed services handle automatically; plan
  for a documented model-refresh cadence.
- Guardrails: open-source guardrail layers (NeMo Guardrails,
  Llama Guard, Mistral's safety classifiers) or contractor-
  authored content-filter systems. Managed-service providers
  ship guardrails as a feature; self-hosted deployments author
  this layer.

**Prompt-surface CUI exposure (per hub Decision 5).** Self-
hosted inference gives the contractor full control over the
prompt surface. Exposure paths:

- RAG retrieval sources are contractor-controlled by default;
  document which vector stores and document sources feed
  inference contexts, and scope their access control to the
  CUI boundary.
- Agent tool-call destinations must be scoped to the
  contractor's CUI boundary; an agent that calls external APIs
  from a self-hosted inference server can exfiltrate CUI
  unless the tool-call egress is controlled.
- Fine-tuning training data: any CUI data used for fine-tuning
  creates a CUI-derived model artifact. Store and access-
  control the artifact as CUI.
- Inference logs: many inference runtimes log prompt and
  response content by default for debugging. Configure log
  verbosity to match the contractor's CUI retention policy;
  export logs to the contractor's SIEM for audit trail.

---

## Air-gapped deployments

Air-gapped AI infrastructure sits physically and logically
disconnected from any external network, including the internet
and unclassified contractor corporate networks. Model weights,
inference runtime, and operational tooling are loaded through
removable media or a one-way transfer boundary (diode or
equivalent). Patterns serve classified-adjacent CUI, ITAR-
controlled technical data where export-control counsel requires
maximal isolation, and contract terms that prohibit any network-
connected AI inference.

**1. FedRAMP authorization.** Not applicable directly. FedRAMP
assumes a continuous-monitoring posture incompatible with air-
gap operational constraints. The contractor's facility
authorization (typically tied to a classified-system
authorization or an IL6+ control package) carries the
authorization; FedRAMP-equivalence claims require contract-
specific negotiation with the agency.

**2. DoD Impact Level.** Reaches IL6 architecturally when the
facility and operational posture meet IL6 physical, personnel,
and operational controls. IL6 is outside CMMC L2 scope;
air-gapped AI for CUI (below classified level) operates inside
the contractor's own CUI boundary with physical separation as
an additional control layer beyond standard IL4/IL5.

**3. CUI-handling story.** Air-gapped AI is appropriate when:

- ITAR-controlled technical data must not transit any network
  that includes operator-access paths beyond the contractor's
  physical facility.
- Classified-adjacent CUI (CUI workflow feeding a classified
  system or CUI produced from a classified system) requires
  physical boundary separation per agency or program office
  direction.
- Contract or statement-of-work terms prohibit any network-
  connected AI inference, including FedRAMP-authorized cloud
  AI.

Not appropriate for:

- General CUI workloads where FedRAMP-authorized or contractor-
  authored-boundary cloud AI meets the contract requirement.
  Air-gap overhead is substantial; reserve for workloads where
  the isolation itself is load-bearing.
- Small contractors without classified-facility operational
  capacity.

**4. Migration path when fit is no.** Step down to contractor-
authored cloud boundary (on-prem LLM on Azure Government IL5 or
AWS GovCloud IL5) when the air-gap overhead exceeds the
workload's actual isolation requirement.

**Implementation notes.**

- Boundary enforcement: physical air-gap with monitored removable-
  media workflow for model weight updates and code deployment;
  one-way network transfer (data diode) where continuous data
  flow from an external source is required but no egress is
  permitted; SCIF (Sensitive Compartmented Information Facility)
  or equivalent controlled facility for the inference hardware.
- Model weight provenance: downloaded model weights verified
  against vendor-published hashes before transfer into the air-
  gap, with a documented chain of custody for each transfer.
  Weight files become part of the air-gapped authorization
  boundary after transfer.
- Update cadence: model updates, runtime updates, and OS
  security patches transit through a controlled workflow that
  preserves the air-gap. Typical cadence is slower than
  network-connected infrastructure; document the risk tradeoff
  in the SSP.
- Inference operators: physical access to the air-gapped
  facility is the primary access control; remote operation is
  by definition not available. Operator roster and access-log
  discipline match the facility's physical-security regime.
- Monitoring: telemetry export from the air-gapped system is
  constrained. One-way telemetry transfer (diode) to an
  external SIEM is a common pattern; alternatively,
  contractor-authored periodic-export workflow with manual
  review.

**Prompt-surface CUI exposure.** In an air-gapped deployment,
the prompt surface is fully under contractor control. External
exposure paths (cloud egress, telemetry to vendor, managed-
service operator access) do not exist by construction. The
exposure concern shifts to insider risk and physical-security
discipline, which are covered under PS (Personnel Security) and
PE (Physical Protection) domain practice files rather than
under AI-service compliance.

---

## Hybrid patterns (self-hosted adjacencies)

Self-hosted AI rarely operates in complete isolation. Three
recurring adjacencies:

### Hybrid A: Primary suite plus self-hosted LLM for ITAR workload

A contractor runs M365 GCC High or Google Workspace Assured
Controls Plus for productivity and runs self-hosted Llama or
Mistral inference on Azure Government IL5 GPU instances for
ITAR-controlled technical data that cannot route through
Bedrock GovCloud. Identity federation from Entra ID Government
or Cloud Identity into the self-hosted inference control plane.

Works when: the contractor has the operational capacity to run
inference at production reliability and the ITAR scope justifies
the overhead. Fails when: the contractor conflates "self-hosted"
with "our commercial cloud self-hosted" and lands inference in
a non-government boundary.

### Hybrid B: FedRAMP managed AI plus self-hosted fine-tuned model

A contractor uses Bedrock GovCloud or Azure OpenAI Government
for general inference and maintains a self-hosted fine-tuned
model (LoRA on Llama or similar) for contractor-specific tasks
where the fine-tune must stay inside the contractor's boundary.
The managed service handles frontier capability; self-hosted
handles specialized domain adaptation.

### Hybrid C: Coder workspaces plus managed AI inference

A contractor uses Coder to contain developer workstations inside
the compliance boundary and routes AI inference from inside
Coder workspaces to Bedrock GovCloud, Azure OpenAI Government,
or Vertex AI Assured Workloads. The workspace-containment and
AI-service authorization combine: CUI source code stays in the
workspace, AI inference rides on the FedRAMP-authorized route.

---

## Capability appendix — CMMC capability to self-hosted AI pattern

Per hub Decision 1 canonical format.

| AI capability | Self-hosted pattern |
|---|---|
| Frontier-capability text generation | Limited — open-weight frontier gap exists versus Claude 4.5, GPT-5.1, Gemini frontier. Llama 3.3 70B or Llama 4 70B is the practical self-hosted frontier as of 2026-04 |
| Small-model text generation | Llama 3 8B, Mistral 7B, Phi family, Gemma family on contractor GPUs or even CPUs for small workloads |
| Code generation | Code Llama, DeepSeek-Coder, StarCoder, Qwen-Coder on contractor GPUs |
| Text embedding | Sentence-Transformers (BAAI BGE, E5, Nomic Embed), Instructor models on contractor GPUs or CPUs |
| Multimodal (text + image) | LLaVA, Llama 3.2 Vision, Qwen-VL, open-weight vision models on contractor GPUs |
| Reasoning models | DeepSeek-R1, open-weight reasoning-trained models; lags closed-model reasoning (o-series, Claude extended thinking) at frontier |
| Structured output and tool-use | Open-weight models with outlines, guidance, or json-schema constrained decoding via vLLM or TGI |
| Fine-tuning | LoRA via PEFT, full-parameter fine-tuning via FSDP or DeepSpeed on contractor GPUs; contractor-owned fine-tune artifacts |
| Retrieval-augmented generation (RAG) | Open-source vector databases (pgvector, Qdrant, Weaviate, Milvus) on contractor infrastructure; contractor-authored retrieval pipelines |
| Agent orchestration | LangChain, LlamaIndex, contractor-authored agent runtime on contractor infrastructure |
| Content safety and guardrails | NeMo Guardrails, Llama Guard, contractor-authored filters; no managed-service guardrail inheritance |
| Audit and logging | Contractor-authored telemetry, OpenTelemetry-instrumented inference servers, SIEM export |
| Developer workspace containment | Coder on FedRAMP-authorized IaaS or on-premises |

**Reading the appendix.** Open-weight self-hosting parity tracks
closed-model frontier on a months-to-quarters lag; the gap
narrows for some capabilities (small-model text, embedding,
code generation) and persists for others (frontier reasoning,
multimodal). Workload fit decisions account for this drift.

---

## Cross-domain anchors

Self-hosted AI posture composes with corpus cross-cutting files
and domain practice files:

- **Phase 5 AI hub.** `references/modern-it/ai-services/README.md`
  for the six Decisions including Fit Assessment pattern
  (Decision 3) and prompt-surface CUI (Decision 5).
- **FedRAMP AI services.**
  `references/modern-it/ai-services/fedramp-ai-services.md` for
  the managed-service alternatives a contractor evaluates
  against before committing to self-hosted.
- **AI dev tools.** `references/modern-it/ai-services/ai-dev-tools.md`
  for dev tools that may route to self-hosted backends
  (Hybrid C above).
- **Phase 5c cloud-platforms.**
  `references/modern-it/cloud-platforms/azure-government.md` and
  `references/modern-it/cloud-platforms/aws-govcloud.md` for
  the platform authorizations that self-hosted patterns inherit
  from.
- **Productivity pairing.** `references/modern-it/productivity/README.md`
  for the primary suite that typically pairs with self-hosted
  AI inference (Hybrid A).
- **FedRAMP framing.** `references/fedramp-gap.md` for FedRAMP
  program context and DFARS 7012 equivalence.
- **CUI scoping.** `references/scoping-and-cui.md`.
- **SSP authoring.** `references/ssp-guidance.md`.

Domain practice files used for requirement text and evidence
lists:

- Access Control (AC) — `references/domains/ac-access-control.md`
  for workspace identity federation and inference-endpoint
  access control.
- System and Communications Protection (SC) —
  `references/domains/sc-system-comms.md` for encryption in
  transit (workspace connection, inference API) and at rest
  (model weights, fine-tune artifacts, prompt caches).
- Configuration Management (CM) —
  `references/domains/cm-configuration-mgmt.md` for change
  control on model updates, runtime updates, and workspace
  image revisions.
- Physical Protection (PE) —
  `references/domains/pe-physical-protection.md` for air-gapped
  facility controls.
- Personnel Security (PS) —
  `references/domains/ps-personnel-security.md` for air-gapped
  operator screening.
- Audit and Accountability (AU) —
  `references/domains/au-audit.md` for inference audit and
  workspace audit.
- Media Protection (MP) —
  `references/domains/mp-media-protection.md` for model-weight
  media handling during air-gap transfer.

---

## Examples as of 2026-04

> **Examples as of 2026-04:** Open-weight model names cited in
> this file (Llama 3/4 families, Mistral, Qwen, DeepSeek, Phi,
> Gemma) and inference-runtime names (vLLM, TGI, llama.cpp,
> Triton) reflect the 2026-04 state of the ecosystem. Both move
> fast. Coder is the named CDE platform in scope per hub
> Decision 7; other CDE platforms (Gitpod, GitHub Codespaces)
> either lack FedRAMP-compatible self-hosting or fall under
> different scope boundaries. This skill does not rank open-
> weight models or inference runtimes. Verify current vendor
> licensing, model cards, and operational posture before
> selecting any self-hosted AI component.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/ai-services/README.md`,
`references/modern-it/cloud-platforms/cloud-selection.md`, or
previous Phase 5 slices are not repeated here.

**Coder.** The self-hosted CDE platform covered in this file;
Coder Inc. is the vendor. Distinct from "Coder" as a role-
descriptor in the broader AI-dev-tools file.

**Data diode.** A one-way network transfer device that permits
data flow in a single direction; used in air-gapped
architectures to allow inbound data without permitting egress.

**DeepSeek.** An open-weight model family including general-
purpose (DeepSeek-V3) and reasoning (DeepSeek-R1) variants.

**FSDP (Fully Sharded Data Parallel).** A PyTorch distributed
training strategy for full-parameter fine-tuning of large
models across multiple GPUs.

**Gemma.** Google's open-weight model family, released under
the Gemma license; distinct from the Gemini closed-model family
on Vertex AI.

**llama.cpp.** An open-source inference runtime supporting
quantized open-weight models on CPU, GPU, and mixed-device
configurations.

**Llama (Meta Llama).** Meta's open-weight model family; Llama
3 and Llama 4 variants are the current generations. Released
under the Llama Community License with 700M MAU threshold
triggering commercial terms.

**LoRA (Low-Rank Adaptation).** A parameter-efficient fine-
tuning technique introducing a small number of adapter weights
rather than retraining the full model. Adapter weights can be
stored separately from the base model and loaded at inference
time.

**Mistral.** Mistral AI's open-weight model family, released
predominantly under Apache 2.0. Includes Mistral, Mixtral
(mixture-of-experts), and specialized variants.

**PEFT (Parameter-Efficient Fine-Tuning).** The Hugging Face
library implementing LoRA and related efficient fine-tuning
methods.

**Phi (Microsoft Phi).** Microsoft's small-language-model open-
weight family (Phi-3, Phi-4 variants); small enough for CPU or
single-GPU deployment.

**Qwen.** Alibaba's open-weight model family, including general-
purpose and specialized (Qwen-Coder, Qwen-VL) variants.

**SCIF (Sensitive Compartmented Information Facility).** A
physically secure facility meeting Intelligence Community
Directive 705 controls. Air-gapped AI deployments for
classified-adjacent CUI often sit inside a SCIF or SCIF-
equivalent controlled facility.

**TGI (Text Generation Inference).** Hugging Face's open-source
inference runtime, common for self-hosted deployment at
production reliability.

**Triton (Triton Inference Server).** NVIDIA's open-source
inference serving platform supporting heterogeneous hardware
and multiple runtime backends.

**vLLM.** An open-source inference runtime optimized for high-
throughput batched inference with paged-attention memory
management.

---

## Versioning and drift

Self-hosted AI content drifts along several axes. Per hub
Versioning policy:

- Model-family releases (Llama 3 → 3.1 → 3.2 → 3.3 → 4.x;
  Mistral → Mixtral → Pixtral → Mistral Large; Qwen → Qwen2 →
  Qwen2.5 → Qwen3) happen on a months-to-quarters cadence.
  Named model versions in this file reflect 2026-04 state;
  the pattern guidance survives version transitions.
- Inference-runtime releases (vLLM, TGI, llama.cpp) ship on a
  weeks-to-months cadence with feature additions (new
  quantization formats, new attention implementations, new
  hardware support). Feature-level claims decay fastest.
- Hardware acceleration vendor releases (NVIDIA, AMD, Intel)
  introduce new capabilities that self-hosted deployments can
  leverage. Hardware-specific guidance is deferred to the
  contractor's infrastructure team.
- Model licensing terms can change (Meta has updated the Llama
  license multiple times; Mistral adjusts commercial licensing
  for specific model variants). Verify current license terms at
  model card before citing license-permission claims in an SSP.
- Coder platform releases add features on a months cadence.
  Feature-level claims labeled "as of YYYY-MM, verify current
  Coder documentation before implementing."

Content verified 2026-04-21. Next full re-verification at the
corpus review cycle or when any self-hosted AI dependency
announces a tier-level change (model license restructure,
inference runtime major version, or Coder architectural
change).
