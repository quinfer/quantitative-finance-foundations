# Contributing Guidelines

Thank you for your interest in contributing to the Quantitative Finance Foundations curriculum. This resource aims to provide rigorous, validated guidance for students developing quantitative capabilities in finance.

## Contribution Standards

All contributions must meet these criteria:

### 1. Rigour and Validation

- Resources must demonstrate mathematical rigour and empirical validation
- Methods should have proven value through application to real problems
- Avoid trendy but untested approaches
- Include evidence of quality (citations, adoption, empirical validation)

### 2. Pedagogical Value

- Explain how the contribution fits within the curriculum progression
- Identify prerequisites and learning objectives
- Provide implementation guidance where applicable
- Consider the target audience (motivated finance students with solid undergraduate preparation)

### 3. Reproducibility

- All code must be documented, tested, and reproducible
- Include requirements files with pinned dependencies
- Provide clear instructions for running examples
- Document data sources and preprocessing steps

## Types of Contributions

### Resource Recommendations

To suggest a new book, paper, or learning resource:

1. Open an issue with the title "Resource Suggestion: [Resource Name]"
2. Include:
   - Full citation
   - Why this adds value beyond existing recommendations
   - Evidence of quality and validation
   - How it fits within curriculum progression
   - Specific chapters or sections to prioritise

### Implementation Examples

To contribute code examples:

1. Follow Python best practices (PEP 8, type hints, docstrings)
2. Include comprehensive comments explaining methodology
3. Provide test cases demonstrating correctness
4. Document all assumptions and limitations
5. Include requirements file with specific versions
6. Ensure reproducibility on standard environments

### Paper Annotations

To add research paper summaries:

1. Create directory under appropriate theme in `papers/`
2. Include `notes.md` with:
   - Key contributions and methodology
   - Main findings and their robustness
   - Limitations and caveats
   - Relevance to curriculum
3. Link to publicly available versions (working papers, author websites)
4. Do NOT include copyrighted PDFs without permission

### Exercise Development

To contribute new exercises:

1. Specify clear learning objectives
2. Provide detailed task description
3. Suggest data sources and expected outputs
4. Include validation criteria
5. Offer extension opportunities
6. Create sample solution (in separate branch)

## Submission Process

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/your-contribution`)
3. **Make your changes** following the standards above
4. **Test thoroughly** ensuring reproducibility
5. **Commit with clear messages** explaining the contribution
6. **Submit a pull request** with:
   - Description of changes
   - Justification for inclusion
   - Evidence of quality
   - Any relevant context

## What We DON'T Accept

- Promotional material for commercial products or services
- Resources lacking rigorous methodology or validation
- Trendy topics without proven value in quantitative finance
- Code without proper documentation and testing
- Contributions that duplicate existing material without adding value
- Material focused on superficial tool familiarity over deep understanding

## Review Process

All contributions undergo review for:

1. **Alignment with curriculum philosophy**: Does it emphasise rigour, validation, and implementation?
2. **Quality standards**: Does it meet criteria for documentation, testing, and reproducibility?
3. **Pedagogical value**: Does it help students develop genuine capabilities?
4. **Maintenance burden**: Can we maintain this long-term?

Reviews may take time. We prioritise quality over speed.

## Code of Conduct

- Engage respectfully with maintainers and other contributors
- Accept constructive criticism professionally
- Focus on improving the resource, not promoting specific approaches
- Acknowledge limitations and alternative perspectives

## Questions?

Open an issue with the "question" label. We're happy to discuss:

- Whether a potential contribution would fit
- How to structure a contribution
- Clarification on standards and criteria
- Feedback on work in progress

## Attribution

Contributors are acknowledged in:

- Pull request comments
- Commit history
- Optional CONTRIBUTORS.md file (for substantial contributions)

## License

By contributing, you agree that your contributions will be licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license, matching the repository license.

---

**Thank you for helping build rigorous quantitative finance education resources.**

