# Contributing to CMMC Advisor

Thank you for contributing to a resource that helps defense contractors
succeed in delivering compliant services to the U.S. Government.

## Provenance Requirement

**Every factual claim must cite a public source.**

This is non-negotiable. The CMMC Advisor skill is built entirely from
publicly available documentation. No proprietary, classified, or
access-restricted content is permitted.

When adding or modifying content:

1. Cite the specific source document (title, publisher, URL)
2. Add the source to `SOURCES.md` if it is not already listed
3. Include the access date for web sources
4. If citing a specific section, reference the section number or page

### Acceptable Sources

- NIST Special Publications (SP 800-171, 800-171A, 800-172, etc.)
- 32 CFR Part 170 (CMMC Program Final Rule)
- CMMC Assessment Guide (dodcio.defense.gov)
- FedRAMP documentation (fedramp.gov)
- DoD CIO publications (dodcio.defense.gov)
- Cloud provider public compliance documentation (AWS, Microsoft, Google)
- Published articles from recognized compliance practitioners
- Government Accountability Office (GAO) reports
- Congressional Research Service (CRS) reports

### Not Acceptable

- Proprietary compliance tools or platform content behind paywalls
- Classified or restricted government documents
- Internal organizational SSPs, POA&Ms, or assessment reports
- Content from competing compliance skills or proprietary knowledge bases

## Content Standards

### Practice Documentation Format

When documenting individual CMMC practices, use this consistent structure:

```markdown
### Practice ID — Practice Title

**Requirement:** One-sentence summary of what this practice requires.

**NIST Source:** The verbatim or closely paraphrased text from NIST SP
800-171 Rev 2, with section reference.

**Level:** L1 / L2 / L3

**Why it matters:** A brief explanation of the security objective this
practice serves, written for someone who may not have a compliance background.

**Implementation guidance:** Practical steps to implement this practice,
including specific tools, configurations, or processes.

**Evidence to collect:** What an assessor will ask to see to verify this
practice is implemented.

**Common mistakes:** What organizations frequently get wrong about this
practice, and how to avoid it.

**Modern IT notes:** (Optional) Specific guidance for cloud environments,
macOS, remote work, or other modern technology stacks.
```

### Voice and Tone

- **Enabler, not gatekeeper.** Frame guidance as "here is how" not "you cannot."
- **Practitioner register.** Write as one compliance professional to another.
  Skip the academic hedging. Be direct.
- **Audience-aware.** Remember that readers range from IT administrators to
  business owners. Use plain language where possible and define acronyms on
  first use within each file.
- **Date-stamp compliance claims.** FedRAMP authorization status and tool
  capabilities change. Include verification dates for product compliance claims.

### File Organization

- Keep reference files focused. One file per domain, one file per technology
  area, one file per topic.
- Use consistent heading levels across all reference files.
- Cross-reference related files using relative paths.

## Contribution Process

1. **Fork the repository** and create a feature branch.
2. **Make your changes** following the content standards above.
3. **Update SOURCES.md** with any new sources you referenced.
4. **Submit a pull request** with:
   - A clear description of what you added or changed
   - Which source documents support the changes
   - Whether this is a factual correction, new content, or content update
5. **Maintainer review** — A maintainer will review for:
   - Source provenance (every claim has a citation)
   - Accuracy (claims match the cited sources)
   - Consistency (format matches existing content)
   - Enabler tone (guidance helps, not blocks)

## Reporting Issues

If you find an error, outdated information, or a gap in coverage:

1. Open a GitHub issue
2. Describe what is incorrect or missing
3. If possible, cite the authoritative source that contradicts the current content
4. Label appropriately: `correction`, `gap`, `outdated`, `enhancement`

## Code of Conduct

Be professional, constructive, and respectful. This project serves defense
contractors building real compliance programs. Contributions should reflect
that seriousness.

## License

By contributing, you agree that your contributions will be licensed under
[CC BY-SA 4.0](LICENSE), the same license as the rest of this project.
