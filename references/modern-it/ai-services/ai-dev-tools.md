# AI Developer Tools Compliance

> Source: NIST SP 800-171 Rev 2; CMMC Assessment Guide Level 2
> (DoD CIO); DFARS 252.204-7012; Anthropic Claude Code
> documentation (code.claude.com/docs); GitHub Copilot FedRAMP
> compliance (docs.github.com/en/copilot); GitHub Enterprise
> Cloud FedRAMP FAQ (government.github.com/fedramp-faq); Cursor
> Security page (cursor.com/security) and Cursor Trust Center
> (trust.cursor.com); Windsurf / Codeium documentation
> (codeium.com); Continue project documentation (continue.dev);
> DoD CSP SRG v1r1 (public.cyber.mil); NIST CMVP validated
> modules registry (csrc.nist.gov).

## Overview

This file covers AI developer tools — IDE-integrated AI coding
assistants — scoped against the CUI boundary question at the
dev-tool layer, distinct from the model-service authorization
covered in `fedramp-ai-services.md` and `self-hosted-ai.md`. Per
hub Decision 6, AI dev tools sit one layer above the prompt-
surface Decision 5: a dev tool backed by a FedRAMP-authorized
model service still has a separate CUI question at the workspace-
context collection, telemetry, and cache layer.

Five tools in scope per hub Decision 7:

- **Claude Code** (Anthropic) — agentic coding system. Configurable
  backend: direct Anthropic API, Amazon Bedrock (including
  GovCloud), or Google Vertex AI. Dev-tool CUI boundary depends
  on which backend the contractor configures.
- **GitHub Copilot Enterprise** (Microsoft/GitHub) — IDE
  assistant. Rides on GitHub Enterprise Cloud authorization
  (FedRAMP Tailored) with Azure OpenAI Government as the
  federal-customer model backend option.
- **Cursor** (Anysphere) — IDE (VS Code fork) with server-side
  prompt building. SOC 2 Type II, not FedRAMP-authorized. Cannot
  direct-route to enterprise backends; Cursor's servers are
  always in the prompt path.
- **Windsurf** (Codeium) — IDE assistant with cloud-hosted
  control plane. Enterprise offerings exist but FedRAMP
  authorization is not established.
- **Continue** (Continue Dev) — open-source AI coding assistant.
  Self-hostable control plane; backend is contractor-configured.

**The distinguishing axis is not model capability.** All five tools
route to similar models (Claude, GPT, Gemini, open-weight). The
distinguishing axis is the dev-tool's own data flow: does the
tool's control plane see prompt content; does the tool persist
code-embeddings; does the tool emit telemetry containing
workspace data; can the tool be configured to direct-route to a
contractor's FedRAMP-authorized backend without the tool vendor's
servers in the path.

Read this file alongside the Phase 5 AI hub at
`references/modern-it/ai-services/README.md` (Decisions 5 and 6
define the two-layer CUI boundary),
`fedramp-ai-services.md` (Slice U — the backend options for
FedRAMP-authorized model routing), and
`self-hosted-ai.md` (Slice V — Coder as a workspace containment
adjacency and on-prem LLM as a backend option).

---

## Scope of this file

Covered:

- Claude Code, GitHub Copilot Enterprise, Cursor, Windsurf,
  Continue: the five AI dev tools per hub Decision 7.
- Dev-tool-specific CUI-exposure paths: workspace-context
  collection, codebase indexing and embedding, telemetry export,
  prompt cache retention.
- Backend routing options per tool (which tools can route to
  FedRAMP-authorized model backends without the tool vendor's
  infrastructure in the path).
- Configuration recommendations for each tool when the tool's
  fit permits CUI use with discipline.

Not covered:

- Consumer AI coding assistants for CUI workflow: GitHub Copilot
  Individual (commercial consumer tier), public ChatGPT web
  interface, public Claude.ai web interface. These are
  commercial-SaaS tiers not appropriate for CUI regardless of
  configuration.
- Model backend authorization (covered in
  `fedramp-ai-services.md`).
- Self-hosted model inference that a dev tool may route to
  (covered in `self-hosted-ai.md`).
- Productivity-embedded AI (Microsoft 365 Copilot, Gemini for
  Workspace). These are productivity-suite AI rather than dev
  tools; their CUI boundary is documented in the productivity
  files where applicable.
- Augment, Tabnine, Amazon CodeWhisperer, Sourcegraph Cody, and
  other dev tools not in the hub Decision 7 named scope. A
  contractor considering an unlisted dev tool applies the same
  framework: evaluate the tool's control-plane data flow,
  backend routing options, and CUI-exposure paths against the
  contractor's CUI boundary.

---

## Fit Assessment — four-question structure

Each tool below answers the same four questions in the same
order. Per hub Decision 3, Fit Assessment replaces Tenancy
Selection (dev tools have no tenancy axis; the question is
whether the tool's control-plane plus backend-routing combination
fits inside the contractor's CUI boundary).

1. Is the tool's control plane FedRAMP-authorized, and at what
   level?
2. Can the tool route to a FedRAMP-authorized model backend, and
   does that routing bypass the tool vendor's servers?
3. What is the CUI-handling story for the dev-tool layer
   (workspace context, indexing, telemetry, cache)?
4. What is the migration path if the tool cannot fit the
   contractor's CUI workflow directly?

The critical axis for AI dev tools is often question 2: even
when a model backend is FedRAMP-authorized, a dev tool whose
servers sit in the prompt path introduces the tool-vendor
infrastructure as a separate CUI-exposure layer.

---

## Claude Code

**Claude Code** is Anthropic's agentic coding system, installable
as a CLI and as IDE extensions. Configurable to route inference
through the Anthropic direct API, Amazon Bedrock (including
GovCloud), or Google Vertex AI.

**1. Control-plane FedRAMP authorization.** None at the Claude
Code dev-tool layer. Anthropic does not publish a FedRAMP
authorization package covering the Claude Code client binary and
its telemetry plane. The client runs on the developer's endpoint;
telemetry and diagnostic reporting (crash reports, usage
analytics) route to Anthropic-controlled endpoints by default.

**2. FedRAMP-authorized backend routing.** Yes, via Bedrock or
Vertex AI. Per code.claude.com/docs/en/amazon-bedrock, Claude
Code can be configured to route inference to Amazon Bedrock;
when configured against a Bedrock GovCloud account, inference
rides on the Bedrock GovCloud FedRAMP High + DoD IL4/IL5
authorization boundary (see `fedramp-ai-services.md`). Vertex AI
configuration routes inference through Vertex AI Assured
Workloads when the contractor configures Assured Workloads
properly.

The direct Anthropic API (api.anthropic.com) is NOT FedRAMP-
authorized at the direct-API surface. A contractor running CUI
code through Claude Code with the direct-API backend has a
scope breach regardless of the tool's local configuration.

**3. CUI-handling story at the dev-tool layer.** With backend
routed to Bedrock GovCloud or Vertex AI Assured Workloads, the
inference path is authorized. Remaining dev-tool layer concerns:

- **Workspace context collection.** Claude Code reads files in
  the current workspace as context for prompts. Developers
  working on CUI code must ensure the workspace scope matches
  the CUI boundary; mixing CUI and non-CUI files in one workspace
  without discipline risks CUI leaking into prompts that a
  developer believes are non-CUI.
- **Telemetry and diagnostics.** Claude Code emits telemetry by
  default (tool usage metrics, session identifiers, crash
  reports). Disable telemetry at the enterprise level or route
  telemetry to a contractor-operated collector where available.
  Verify current telemetry configuration options at
  code.claude.com/docs before CUI deployment.
- **Prompt cache.** Claude Code maintains local prompt cache on
  the developer's endpoint. The endpoint becomes a CUI asset when
  CUI flows through the cache; treat the endpoint under the
  contractor's CUI endpoint controls per
  `references/modern-it/endpoints/windows-fleet.md` or
  `macos-fleet.md`.
- **Tool-use and agent operations.** Claude Code operates as an
  agent with tool-use (file read, shell execution, web fetch).
  Each tool-use destination is a separate CUI-egress path; a
  shell command that uploads a file to a non-authorized
  destination is an exfiltration event. Agent tool-use
  discipline is the developer's responsibility and the
  contractor's enforcement.

**4. Migration path when fit is no.** If the direct-API backend
is the default and the contractor cannot transition to Bedrock
GovCloud or Vertex AI Assured Workloads, use a different dev
tool that either runs fully inside the contractor's boundary
(Continue; see below) or routes through an established FedRAMP
backend by architecture (GitHub Copilot Enterprise with Azure
OpenAI Government).

**Configuration recommendations for CUI use.**

- Route backend to Bedrock GovCloud (for Claude model access at
  IL5) or Vertex AI Assured Workloads (for IL2; IL5 is
  roadmap).
- Configure at the enterprise level so individual developers
  cannot silently switch to direct-API routing.
- Disable or redirect telemetry to a contractor-operated
  collector; audit telemetry egress periodically.
- Treat the developer endpoint as a CUI asset with full
  endpoint-management controls.
- Define workspace-scope discipline: one CUI workspace per
  program, separate from non-CUI workspaces.

---

## GitHub Copilot Enterprise

**GitHub Copilot Enterprise** is Microsoft/GitHub's IDE AI
assistant available to GitHub Enterprise Cloud customers. In
October 2025, GitHub announced that Copilot supports US/EU data
residency and is FedRAMP-compliant within the GHEC parent
FedRAMP Tailored scope for federal workloads.

**1. Control-plane FedRAMP authorization.** Copilot rides on
GitHub Enterprise Cloud's authorization. GHEC holds FedRAMP
Tailored (LI-SaaS) at the parent-service level per
government.github.com/fedramp-faq (see
`references/modern-it/productivity/legacy-dib-tools.md` for the
GHEC treatment). The October 2025 data-residency and FedRAMP
announcement (LinkedIn / GitHub blog) indicates Copilot is
covered under the GHEC parent authorization when used in an
Enterprise Cloud configuration with appropriate data residency.
Verify the current scope against the FedRAMP Marketplace package
before citing in an SSP.

**2. FedRAMP-authorized backend routing.** Yes, via Azure OpenAI
Government for Copilot models routed through Microsoft's
FedRAMP-High Azure Government environment. This is the federal-
customer pairing: Microsoft runs both the GHEC control plane
and the Azure OpenAI Government backend, which simplifies the
data-flow boundary.

**3. CUI-handling story at the dev-tool layer.**

- **Workspace context.** Copilot uses open-file content plus
  repository context as inference input. Repository scope is
  governed by GHEC permissions; file scope follows the
  developer's IDE session.
- **Codebase indexing.** Copilot indexing scope depends on
  configuration; verify the indexing extent aligns with the
  CUI-repo boundary.
- **Telemetry.** Copilot emits usage telemetry to the GitHub
  control plane. Enterprise configuration controls telemetry
  scope and retention. Refer to docs.github.com/en/copilot for
  current telemetry settings.
- **FedRAMP Tailored scope limits.** The GHEC parent FedRAMP
  Tailored authorization is scoped around source code as the
  low-risk data type. CUI beyond source code (attachments,
  issue descriptions, PR bodies) sits outside Tailored's
  design intent per
  `references/modern-it/productivity/legacy-dib-tools.md`
  GitHub Enterprise Cloud section. Copilot inherits this scope
  limit; prompt content is CUI-scoped source code, not
  arbitrary CUI context.

**4. Migration path when fit is no.** For contractors whose CUI
scope exceeds Tailored's source-code-only intent, route source
control through GitHub Enterprise Server (self-hosted per
legacy-dib-tools.md) with a self-hosted model backend; Copilot
Enterprise-in-GHEC is not the right tool for CUI-beyond-source-
code workflows.

**Configuration recommendations for CUI use.**

- Ensure Copilot is configured to use the Azure OpenAI
  Government backend for federal workloads.
- Verify data residency configuration matches the contractor's
  regional requirement.
- Scope Copilot indexing to CUI-appropriate repositories only;
  exclude non-FedRAMP-scope content from Copilot context.
- Exclude CUI-containing issue descriptions and PR bodies from
  the contractor's Copilot workflow per the Tailored scope
  discipline.
- Treat Copilot telemetry as an egress channel; verify scope.

---

## Cursor

**Cursor** is an AI-first IDE (fork of Visual Studio Code) from
Anysphere, with server-side prompt building and server-side AI
request routing. Current compliance posture is **SOC 2 Type II
only**; Cursor is NOT FedRAMP-authorized.

**1. Control-plane FedRAMP authorization.** None. Per
cursor.com/security (verified 2026-04-21), Cursor is SOC 2 Type
II certified. Cursor's infrastructure runs primarily on AWS
commercial (US primary, with some latency-critical services in
Europe and Singapore). Secondary infrastructure on Microsoft
Azure (commercial) and Google Cloud Platform (commercial).

**2. FedRAMP-authorized backend routing.** No, not in the way a
DIB contractor needs. Per cursor.com/security: "We currently do
not have the ability to direct-route from the Cursor app to
your enterprise deployment of OpenAI/Azure/Anthropic, as our
prompt-building happens on our server, and our custom models on
Fireworks are critical in providing a good user experience. We
do not yet have a self-hosted server deployment option."

This is the architectural constraint that disqualifies Cursor
for CUI: even if the contractor pays for Azure OpenAI
Government, prompts and code context still flow through
Cursor's AWS commercial servers first, which is a scope breach
for DFARS 7012 CUI. Privacy Mode (Cursor's zero-data-retention
agreement with model providers) does not solve the
authorization-boundary problem; it addresses a different
question (training-data use).

**3. CUI-handling story at the dev-tool layer.** Not appropriate
for CUI workflow at the 2026-04-21 verification date. Detailed
concerns:

- **Server-side prompt building.** All prompts originate at
  Cursor's AWS commercial servers even when the configured
  model is on the contractor's FedRAMP-authorized backend.
- **Codebase indexing.** Cursor indexes the workspace into
  Turbopuffer (on Google Cloud commercial); file paths are
  obfuscated but embeddings-of-code are stored. For CUI code,
  this is data-at-rest on commercial infrastructure.
- **Subprocessor chain.** Cursor's documented subprocessors
  (AWS commercial, Cloudflare, Microsoft Azure commercial,
  Google Cloud commercial, Fireworks, Baseten, Together,
  OpenAI, Anthropic, Vertex commercial, xAI) are commercial
  services; none are in a FedRAMP-authorized boundary for DIB
  CUI use.
- **Privacy Mode.** Cursor states that its Privacy Mode ensures
  model providers do not store code data or use it for training
  (per cursor.com/security). That is a contractual commitment,
  not a FedRAMP authorization; it does not satisfy DFARS 7012
  equivalence.

**4. Migration path when fit is no (current state).** A contractor
using Cursor for CUI work has a scope problem, not a
configuration issue. Options: (a) switch to a dev tool that
supports FedRAMP-authorized backend routing without vendor
servers in the path (Claude Code routed to Bedrock GovCloud;
GitHub Copilot Enterprise with Azure OpenAI Government;
Continue self-hosted); (b) use Cursor for non-CUI work only
with rigorous scope-separation between CUI and non-CUI
development environments.

Cursor's roadmap may include a self-hosted deployment option
(noted on their security page as "do not yet have"). When and
if that ships, re-evaluate.

**Configuration recommendations.** For non-CUI development only.
Enable Privacy Mode. Use .cursorignore to exclude any
CUI-adjacent files. Do not use Cursor for CUI workflow at
2026-04-21.

---

## Windsurf

**Windsurf** is Codeium's IDE assistant (also distributed under
the Codeium brand for earlier generations). Cloud-hosted control
plane; enterprise tier exists with additional controls.

**1. Control-plane FedRAMP authorization.** Not established at
2026-04-21. Codeium markets SOC 2 Type II compliance and
enterprise features (self-hosted enterprise tier for some
configurations) but no public FedRAMP authorization package.
Verify current status at codeium.com or trust.codeium.com
before citing.

**2. FedRAMP-authorized backend routing.** Codeium's architecture
is similar to Cursor's: server-side prompt building on the
Codeium-hosted control plane. Enterprise configurations may
support self-hosted inference (check current availability); the
default cloud configuration routes through Codeium's commercial
infrastructure.

**3. CUI-handling story at the dev-tool layer.** Same
architectural concern as Cursor: when the dev-tool's control
plane is in the prompt path, and the control plane is not
FedRAMP-authorized, the tool does not fit CUI workflow
regardless of backend configuration. Verify current enterprise-
tier capabilities; if Codeium Enterprise offers a self-hosted
control plane option inside a contractor-authored boundary,
re-evaluate against the contractor's authorization package.

**4. Migration path when fit is no.** Same as Cursor: use a
different dev tool for CUI workflow (Claude Code with Bedrock
GovCloud; GitHub Copilot Enterprise with Azure OpenAI
Government; Continue self-hosted).

**Configuration recommendations.** Verify current compliance
posture and enterprise-tier capabilities at codeium.com trust
center before any CUI-adjacent use. Default posture: not
appropriate for CUI workflow pending primary-source
verification of FedRAMP-compatible architecture.

---

## Continue

**Continue** is an open-source AI coding assistant (CLI and VS
Code / JetBrains extensions). Control plane is self-hostable;
backend is contractor-configured (any model provider or self-
hosted LLM).

**1. Control-plane FedRAMP authorization.** Not applicable.
Continue is self-hosted software; there is no vendor cloud in
the prompt path unless the contractor configures an external
backend. When Continue runs entirely inside the contractor's
infrastructure with a self-hosted backend (see
`self-hosted-ai.md`), the entire data flow is inside the
contractor-authored authorization boundary.

**2. FedRAMP-authorized backend routing.** Yes, by design.
Continue can be configured to route inference to any backend
the contractor chooses: Bedrock GovCloud, Azure OpenAI
Government, Vertex AI Assured Workloads, or a self-hosted model
server. The Continue client runs on the developer's endpoint
and routes directly to the configured backend without an
intermediate vendor control plane.

**3. CUI-handling story at the dev-tool layer.** Appropriate for
CUI workflow when:

- Backend is FedRAMP-authorized (Bedrock GovCloud, Azure OpenAI
  Government, Vertex AI Assured Workloads) or self-hosted
  inside a contractor-authored boundary.
- Continue client runs on an endpoint that is a CUI asset per
  the contractor's endpoint-management controls.
- Continue's context indexing scope is defined via .continueignore
  or equivalent workspace-scope mechanisms.
- Telemetry is disabled or routed to a contractor-operated
  collector (Continue's open-source nature permits full
  telemetry control, including no-telemetry builds).

**4. Migration path when fit is no.** Continue's flexibility
means the tool fits most CUI workflows; the migration question
is usually about backend choice (Slice U or Slice V) rather than
the dev tool.

**Configuration recommendations for CUI use.**

- Self-host any backend infrastructure the contractor manages;
  route to Bedrock GovCloud, Azure OpenAI Government, or Vertex
  AI Assured Workloads for managed-service backends.
- Configure workspace-scope discipline via .continueignore to
  exclude non-CUI-scope files or CUI-scope files from indexing
  as the situation requires.
- Disable telemetry or verify telemetry destination matches the
  contractor's CUI boundary.
- Treat the developer endpoint as a CUI asset.
- Document the full data-flow path (client -> backend) in the
  SSP, referencing the chosen backend's authorization package.

---

## Two-layer CUI boundary summary

Per hub Decision 6, the dev-tool CUI boundary is a two-layer
problem. The following table applies the hub's framework to the
five tools:

| Tool | Control-plane layer | Backend-routing layer | CUI-appropriate at 2026-04-21? |
|---|---|---|---|
| Claude Code | Not FedRAMP-authorized; endpoint-local with vendor telemetry by default | Bedrock (incl. GovCloud) or Vertex AI supported | Yes, when configured with FedRAMP-authorized backend and telemetry scoped |
| GitHub Copilot Enterprise | FedRAMP Tailored via GHEC parent (October 2025 scope update) | Azure OpenAI Government natural pairing | Yes, for Tailored-scope source code; not for CUI-beyond-source-code |
| Cursor | SOC 2 Type II; NOT FedRAMP | Cannot direct-route; Cursor server in prompt path | No — architectural blocker at 2026-04-21 |
| Windsurf (Codeium) | SOC 2 Type II; not FedRAMP-authorized at 2026-04-21 | Cloud-hosted control plane; enterprise options vary | Default: no — verify current enterprise-tier posture |
| Continue | Self-hosted; no vendor control plane in prompt path | Contractor-configured (any backend) | Yes, with FedRAMP-authorized or self-hosted backend |

**Reading the summary.** Three tools can fit CUI workflow at
2026-04-21: Claude Code (with backend discipline), Copilot
Enterprise (within Tailored scope), and Continue. Two tools
cannot fit DIB CUI workflow at the verification date: Cursor
(architectural blocker) and Windsurf (pending enterprise-
architecture verification). This is a snapshot, not a ranking;
vendor postures shift and re-verification is required before
SSP citation.

---

## Capability appendix — CMMC capability to AI dev tool

Per hub Decision 1 canonical format. Dev tools consume model
backends rather than providing capabilities directly; the
appendix maps capability clusters to dev-tool choices that
deliver each capability under CUI-appropriate configuration.

| AI capability | AI dev tool |
|---|---|
| Code generation (inline) | Claude Code (Bedrock GovCloud backend); GitHub Copilot Enterprise (Azure OpenAI Gov backend); Continue (any FedRAMP or self-hosted backend) |
| Code explanation and Q&A | Claude Code; Copilot Enterprise; Continue |
| Agent-based refactoring / multi-file edits | Claude Code (agentic); Continue (agentic support varies by version) |
| PR review assistance | Copilot Enterprise (first-party); Claude Code or Continue via custom workflow |
| Codebase semantic search | Continue (self-hosted indexing); Copilot Enterprise (within GHEC Tailored scope) |
| CUI-appropriate workspace context | Claude Code with workspace-scope discipline; Continue with .continueignore |
| Telemetry-disabled deployment | Continue (open-source, no-telemetry builds possible); Claude Code (with enterprise configuration); Copilot Enterprise (enterprise telemetry controls) |
| Self-hosted control plane | Continue (by design); Coder + Continue hybrid for workspace-plus-dev-tool containment |

**Reading the appendix.** Cursor and Windsurf do not appear in
the appendix because neither is CUI-appropriate at 2026-04-21
per the two-layer analysis above. When those postures change,
re-verify and update.

---

## Hybrid patterns — dev tools with Coder workspaces

A natural hybrid per hub Pattern C (dev tools routed through
FedRAMP backend): run Coder workspaces (see `self-hosted-ai.md`)
to contain developer environments inside the contractor's
boundary, and install Claude Code, Copilot Enterprise, or
Continue inside the workspace rather than on developer laptops.
Benefits:

- Workspace containment: developer laptops are not CUI assets;
  the workspace holds CUI code and runs the dev tool.
- Centralized configuration: enterprise-level dev-tool
  configuration applies to all workspaces uniformly, preventing
  individual-developer configuration drift.
- Egress control: Coder workspaces sit in a contractor-managed
  network subnet with egress restricted to FedRAMP-authorized
  backends.
- Telemetry consolidation: dev-tool telemetry from workspaces
  routes through the contractor's SIEM rather than individual
  endpoints.

Fails when:

- The contractor lacks operational capacity for both Coder and
  a dev-tool fleet.
- Developer experience degrades (latency, display responsiveness)
  to the point that developers work around the workspace (for
  example, copying code to a local laptop to edit locally).

---

## Cross-domain anchors

AI dev tool posture composes with corpus cross-cutting files and
domain practice files:

- **Phase 5 AI hub.** `references/modern-it/ai-services/README.md`
  for the six Decisions including Decision 6 (AI dev tools as a
  distinct layer).
- **FedRAMP AI services.**
  `references/modern-it/ai-services/fedramp-ai-services.md` for
  the backend options (Bedrock GovCloud, Azure OpenAI
  Government, Vertex AI Assured Workloads).
- **Self-hosted AI.**
  `references/modern-it/ai-services/self-hosted-ai.md` for Coder
  as a workspace-containment adjacency (Hybrid C above) and on-
  prem LLM as a backend option for Continue.
- **Endpoint posture.** `references/modern-it/endpoints/windows-fleet.md`
  and `macos-fleet.md` for the developer-endpoint controls that
  treat the endpoint as a CUI asset when dev tools run locally.
- **Productivity adjacency.**
  `references/modern-it/productivity/legacy-dib-tools.md` GitHub
  Enterprise Cloud section for the GHEC parent authorization
  underlying Copilot Enterprise.
- **CUI scoping.** `references/scoping-and-cui.md`.
- **SSP authoring.** `references/ssp-guidance.md`.

Domain practice files used for requirement text and evidence
lists:

- Access Control (AC) — `references/domains/ac-access-control.md`
  for dev-tool session and workspace-scope access control.
- System and Communications Protection (SC) —
  `references/domains/sc-system-comms.md` for encryption-in-
  transit from dev tool to backend.
- Configuration Management (CM) —
  `references/domains/cm-configuration-mgmt.md` for change
  control on dev-tool version and configuration updates.
- Audit and Accountability (AU) —
  `references/domains/au-audit.md` for dev-tool telemetry and
  workspace audit export to SIEM.
- System and Information Integrity (SI) —
  `references/domains/si-system-information-integrity.md` for
  dev-tool vulnerability management and supply-chain discipline
  (open-source dependencies, extension marketplace exposure).
- Awareness and Training (AT) —
  `references/domains/at-awareness-training.md` for developer
  training on CUI-boundary discipline when using AI dev tools
  (prompt content, workspace scope, tool-use operations).

---

## Examples as of 2026-04

> **Examples as of 2026-04:** The five AI dev tools named in
> this file are the hub Decision 7 scope (Claude Code, GitHub
> Copilot Enterprise, Cursor, Windsurf, Continue). Unnamed dev
> tools (Augment, Tabnine, Amazon CodeWhisperer, Sourcegraph
> Cody, Codestream, others) would require a deliberate scope
> expansion rather than an author's judgment call. A contractor
> evaluating an unlisted dev tool applies the same four-question
> Fit Assessment: is the control plane FedRAMP-authorized; does
> the tool support FedRAMP-authorized backend routing without
> vendor servers in the prompt path; what is the CUI-handling
> story at the dev-tool layer; what is the migration path. This
> skill does not rank AI dev tools. Verify current FedRAMP
> authorization and architectural posture at the vendor's trust
> center before SSP citation.

---

## Terminology

Acronyms used in this file. Terms defined in
`references/modern-it/ai-services/README.md`,
`references/modern-it/ai-services/fedramp-ai-services.md`,
`references/modern-it/ai-services/self-hosted-ai.md`, or
previous Phase 5 slices are not repeated here.

**Claude Code.** Anthropic's agentic coding system; the named
AI dev tool covered in the Claude Code section.

**Continue.** The open-source AI coding assistant from Continue
Dev; the named tool covered in the Continue section.

**Copilot Enterprise.** GitHub Copilot at the Enterprise license
tier, distinct from Copilot Individual (consumer) and Copilot
Business (SMB). Federal path rides on GHEC parent authorization.

**Cursor.** The AI-first IDE from Anysphere; the named tool
covered in the Cursor section.

**IDE (Integrated Development Environment).** The developer-
facing editor and tooling shell (VS Code, JetBrains IDEs,
Vim/Neovim, Emacs) inside which AI dev tools run as extensions
or adjacent CLIs.

**Privacy Mode (Cursor-specific).** Cursor's zero-data-retention
agreement with model providers, enabling users to configure
model-provider access so code data is not stored or used for
training. Distinct from FedRAMP authorization; does not satisfy
DFARS 7012 equivalence for CUI.

**Workspace context.** The set of files, file contents, and
related metadata that an AI dev tool sends as context with each
prompt. Workspace context is the dev-tool-layer CUI-exposure
path distinct from the model-service authorization.

**Workspace Trust (VS Code feature).** A Visual Studio Code
feature that restricts certain operations in untrusted
workspaces. Cursor disables Workspace Trust by default per
cursor.com/security; this is a security-configuration choice
relevant to dev-tool evaluation.

**Windsurf.** The IDE assistant from Codeium; the named tool
covered in the Windsurf section.

---

## Versioning and drift

AI dev tools drift faster than any other category in this
directory. Vendor products rebrand, change architectures, add
enterprise tiers, and re-scope compliance on weeks-to-months
cadence. Per hub Versioning policy:

- Tool-level compliance claims (Cursor SOC 2 Type II, Copilot
  FedRAMP via GHEC Tailored, Continue self-hosted) are the
  stable anchors at 2026-04-21. Re-verify at the next slice
  review.
- Backend-routing capability per tool (Claude Code via Bedrock
  or Vertex; Copilot via Azure OpenAI Gov; Continue arbitrary)
  is the load-bearing compliance claim; verify against vendor
  documentation before SSP citation.
- Feature-level claims (Cursor Privacy Mode mechanics, Copilot
  indexing scope, Continue configuration options) decay on a
  weeks-to-months cadence and are labeled "as of 2026-04, verify
  current vendor documentation before implementing."
- Architectural shifts (a vendor adding a self-hosted control
  plane, a vendor losing SOC 2 coverage, a vendor entering
  FedRAMP certification) are material changes that shift the
  two-layer CUI-boundary summary. Re-verify whenever a vendor
  announces an architectural change.

Known near-term drift risks:

- Cursor self-hosted deployment is marketed as roadmap at
  2026-04-21. When and if it ships, re-evaluate the two-layer
  summary.
- Windsurf/Codeium enterprise architecture continues to evolve;
  current verification found no FedRAMP authorization at the
  control plane.
- GitHub Copilot FedRAMP scope extended in October 2025; the
  specific FedRAMP tier and package scope should be verified
  against the FedRAMP Marketplace before SSP citation.
- Anthropic's enterprise posture around Claude Code telemetry
  is evolving; verify current enterprise configuration options
  at code.claude.com/docs.

Content verified 2026-04-21. Next full re-verification at the
corpus review cycle or when any dev tool vendor announces a
material compliance-posture change.
