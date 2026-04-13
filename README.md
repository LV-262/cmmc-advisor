# CMMC Advisor

A Claude Code skill for navigating CMMC 2.0 (Cybersecurity Maturity Model Certification) compliance. Built for defense contractors who deliver services to the U.S. Government and need clear, actionable guidance on cybersecurity certification requirements.

## Philosophy

This skill exists to help businesses succeed in delivering great services to the U.S. Government in a compliant way. It is not a tool to say no — it is a tool to say **how**.

When a compliant path exists, the skill maps it clearly. When no compliant option exists today, the skill identifies the gap, describes who in the industry is working on closing it, and estimates when options may become available. Legitimate gaps in the market deserve honest answers, not dead ends.

## What This Covers

- **All 3 CMMC levels** — Level 1 (Foundational), Level 2 (Advanced), Level 3 (Expert)
- **14 domains, 110 practices** — Full implementation guidance mapped from NIST SP 800-171 Rev 2
- **Assessment preparation** — Self-assessment, C3PAO, and DIBCAC assessment guidance
- **CUI scoping** — Boundary definition, FCI vs CUI, enclave strategies
- **SSP and POA&M** — System Security Plan guidance and Plan of Action & Milestones management
- **Modern IT mapping** — Compliance guidance for real-world technology stacks:
  - Cloud platforms (AWS GovCloud, Azure Government, GCP Assured Workloads, hybrid patterns)
  - Productivity suites (Microsoft 365 GCC/GCC High, Google Workspace)
  - AI services (Amazon Bedrock, Azure OpenAI, Vertex AI, self-hosted models)
  - Endpoint management (macOS, Windows STIG baselines, remote work)
  - Legacy DIB tools (Atlassian, ServiceNow, and others)
- **Contractor profiles** — Guidance tailored by company type and size (SDVOSB, 8(a), small/medium/large)
- **FedRAMP marketplace guide** — Curated compliant product recommendations by category
- **Rev 3 transition** — Current Rev 2 requirements with Rev 3 awareness and timeline context
- **Anti-patterns** — Common compliance mistakes and how to avoid them

## Installation

Copy the skill to your Claude Code skills directory:

```bash
# Personal installation
cp -r cmmc-advisor ~/.claude/skills/cmmc-advisor

# Project installation
cp -r cmmc-advisor .claude/skills/cmmc-advisor
```

Claude Code automatically discovers and loads skills from these locations.

## Usage Examples

```
"What CMMC level do I need for a DoD subcontract that handles CUI?"

"We use Google Workspace and macOS — can we achieve Level 2 compliance?"

"Design a CUI enclave for a 30-person company using AWS GovCloud."

"What evidence do I need to collect for the Access Control domain?"

"We want to use AI coding tools in our development workflow — what are the compliant options?"
```

## Sources

Every factual claim in this skill traces to a publicly available source. See [SOURCES.md](SOURCES.md) for the complete provenance list.

Primary sources include:
- NIST SP 800-171 Revision 2
- NIST SP 800-171A (Assessment Procedures)
- 32 CFR Part 170 (CMMC Program Final Rule)
- CMMC Assessment Guide (dodcio.defense.gov)
- FedRAMP Marketplace (fedramp.gov)
- Vendor public documentation (AWS, Microsoft, Google Cloud)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Key requirement: every factual claim must cite a public source.

## Disclaimer

This skill provides compliance guidance based on publicly available documentation. It is not legal advice, it is not a substitute for professional cybersecurity consultation, and it does not constitute an official assessment or certification. Always verify guidance against current authoritative sources and consult qualified professionals for your specific situation.

## License

This work is licensed under [CC BY-SA 4.0](LICENSE) — Creative Commons Attribution-ShareAlike 4.0 International.

You are free to share and adapt this material for any purpose, including commercial use, as long as you provide attribution and distribute contributions under the same license.
