# Contributing to CMMC Advisor

Thank you for contributing to a resource that helps defense contractors
succeed in delivering compliant services to the U.S. Government.

## Provenance Requirement

**Every factual claim must cite a public source.**

This is non-negotiable. The CMMC Advisor skill is built entirely from
publicly available documentation. No proprietary, classified, or
access-restricted content is permitted.

### Zero-contamination rule

This skill is authored without reference to any private, proprietary,
or competitor compliance content. Contributors must not copy, adapt,
or paraphrase content from:

- Private client Systems Security Plans, POA&Ms, or assessment reports
- Internal contractor compliance documentation
- Competing compliance skills or proprietary knowledge bases behind
  paywalls or non-public agreements
- Classified or controlled-unclassified government documents outside
  the public domain

The test: if a contributor's employer or a past engagement is the
only place they could have seen the content, it does not belong here.
Public sources only, attributed in SOURCES.md.

Practitioner knowledge derived from applying public standards to
private work is welcome. A contributor who has implemented NIST SP
800-171A assessment objectives across twenty private engagements has
practitioner-level understanding of what those objectives look like
in practice; that understanding, expressed through the public
standards themselves, is the contribution this skill depends on. The
rule is about content provenance (do not copy private content), not
about contributor experience (experience from private work shapes
the framing without being the source).

### Primary-source verification with dated stamp

Compliance facts change. FedRAMP authorization status, DoD Impact
Level coverage, per-service model availability, and vendor product
scopes all shift on weeks-to-months cadences. For every claim that
depends on current authorization state:

1. Verify against the primary source (vendor compliance page,
   FedRAMP Marketplace package entry, Federal Register rule text,
   NIST CSRC publication) at the time of authoring.
2. Stamp the verification date inline in the content. The corpus
   convention is "verified YYYY-MM-DD via [URL]".
3. Label claims that decay faster than the stamp can track as
   "as of YYYY-MM, verify current [source] before implementing."
4. Do not cite a vendor's marketing claim of compliance without a
   Marketplace package entry or equivalent primary-source backing.

### Citation mechanics

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
5. **Maintainer review.** A maintainer will review for:
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
