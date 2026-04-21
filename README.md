# CMMC Advisor

A Claude Code skill for working through CMMC 2.0 (Cybersecurity Maturity Model Certification) compliance. Built for defense contractors who deliver services to the U.S. Government and need clear, actionable guidance on cybersecurity certification requirements.

## Philosophy

This skill exists to help businesses succeed in delivering great services to the U.S. Government in a compliant way. It is not a tool to say no. It is a tool to say **how**.

When a compliant path exists, the skill maps it clearly. When no compliant option exists today, the skill identifies the gap, describes who in the industry is working on closing it, and estimates when options may become available. Legitimate gaps in the market deserve honest answers, not dead ends.

## What This Covers

All three CMMC levels: Level 1 (Foundational), Level 2 (Advanced), Level 3 (Expert). 14 domains, 110 practices with full implementation guidance mapped from NIST SP 800-171 Rev 2. Assessment preparation for self-assessment, C3PAO, and DIBCAC paths. CUI scoping covering boundary definition, FCI vs CUI, and enclave strategies. SSP guidance and POA&M management.

Modern IT compliance mapping for real-world stacks:

- Cloud platforms. AWS GovCloud, Azure Government, GCP Assured Workloads, and hybrid patterns.
- Productivity suites. Microsoft 365 GCC and GCC High, Google Workspace, Atlassian Government Cloud, ServiceNow GCC, GitHub Enterprise, Box for Government.
- AI services. FedRAMP-authorized (Amazon Bedrock GovCloud, Azure OpenAI Government, Vertex AI Assured Workloads), self-hosted (Coder, on-prem LLM, air-gapped), and AI dev tools (Claude Code, Copilot Enterprise, Cursor, Windsurf, Continue).
- Endpoint management. macOS, Windows STIG baselines, remote work.

Contractor-specific guidance by company size (small, medium, large) and socioeconomic set-aside (SDVOSB, 8(a), WOSB/EDWOSB, HUBZone).

FedRAMP Marketplace practitioner guide with curated category short-lists, search guidance, and coverage-gap analysis.

Rev 3 transition context (current Rev 2 requirements with Rev 3 awareness).

Anti-patterns catalog: sixteen named compliance-theater patterns across documentation, tool, scope, and assessment categories.

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

"We use Google Workspace and macOS. Can we achieve Level 2 compliance?"

"Design a CUI enclave for a 30-person company using AWS GovCloud."

"What evidence do I need to collect for the Access Control domain?"

"We want to use AI coding tools in our development workflow. What are the compliant options?"
```

## Sources

Every factual claim in this skill traces to a publicly available source. See [SOURCES.md](SOURCES.md) for the complete provenance list.

Primary sources include:
- NIST SP 800-171 Revision 2 and SP 800-171A (Assessment Procedures)
- 32 CFR Part 170 (CMMC Program Final Rule) and 48 CFR acquisition rule
- CMMC Assessment Guide Level 2 (dodcio.defense.gov)
- DoD CSP SRG v1r1 (public.cyber.mil) for DoD Impact Level reciprocity
- FedRAMP Marketplace (fedramp.gov) for authorization status
- NIST CMVP Validated Modules Registry (csrc.nist.gov) for FIPS validation
- SBA regulations (13 CFR Parts 121/124/126/127/128) for contractor profiles
- Cloud provider compliance documentation (AWS, Microsoft, Google Cloud)
- Vendor trust centers for each named product

Compliance facts that depend on current authorization state (per-service FedRAMP status, per-model availability, vendor product scope) carry dated verification stamps inline, typically "verified 2026-04-21 via [URL]." Re-verify at the primary source before citing in an SSP.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Key requirement: every factual claim must cite a public source.

## Disclaimer

This skill provides compliance guidance based on publicly available documentation. It is not legal advice, it is not a substitute for professional cybersecurity consultation, and it does not constitute an official assessment or certification. Always verify guidance against current authoritative sources and consult qualified professionals for your specific situation.

## License

This work is licensed under [CC BY-SA 4.0](LICENSE), Creative Commons Attribution-ShareAlike 4.0 International.

You are free to share and adapt this material for any purpose, including commercial use, as long as you provide attribution and distribute contributions under the same license.
