# Content Validation Report

**Date**: April 2026
**Scope**: Full review of all content files in the repository for hallucinations, factual accuracy, academic credibility, rigour, and truthfulness.

---

## Executive Summary

This repository is a markdown-based curriculum for quantitative finance, maintained by Prof Barry Quinn at Ulster University Business School. Overall, the content is **substantive, well-structured, and pedagogically sound**. The recommended textbooks and papers are genuine, well-regarded works. The curriculum's philosophy — emphasising rigour, reproducibility, and scepticism of fads — is commendable and appropriate for its target audience.

An initial review (April 2026) identified multiple factual errors, structural inconsistencies, and credibility issues. **All identified issues have been resolved.** This report documents what was found and how each item was addressed, for transparency and future maintenance.

---

## Issues Identified and Resolved

### 1. Hallucinations and Factual Errors (all fixed)

| # | Severity | File(s) | Issue | Resolution |
|---|----------|---------|-------|------------|
| 1.1 | CRITICAL | `resources/market-microstructure.md`, `CURRICULUM.md` | O'Hara chapter descriptions fabricated (6 fake chapters vs 9 real) | Rewritten to match actual 9-chapter structure |
| 1.2 | CRITICAL | `resources/market-microstructure.md` | Hasbrouck chapter descriptions fabricated (7 fake vs 15 real) | Rewritten to match actual 15-chapter structure |
| 1.3 | CRITICAL | `resources/mathematical-foundations.md`, `CURRICULUM.md` | Resnick chapter descriptions wrong (LLN/CLT attributed to Ch 4, Martingales to Ch 5; actually Ch 7-9 and Ch 10) | Corrected to actual 10-chapter structure |
| 1.4 | CRITICAL | `papers/essential-readings.md` | Hasbrouck (2002) attributed to Journal of Finance; actually Journal of Financial Markets | Corrected journal name |
| 1.5 | CRITICAL | `resources/market-microstructure.md`, `CURRICULUM.md` | Cartea et al. chapter descriptions wrong (book has 12 chapters in 3 parts, not 7 as described) | Rewritten to match actual 3-part/12-chapter structure |
| 1.6 | CRITICAL | `CURRICULUM.md` | Tsay Ch 1-5 described with wrong topics (unit roots in Ch 8, Kalman filter in Ch 11) | Corrected chapter-topic mapping |
| 1.7 | IMPORTANT | `CURRICULUM.md`, `resources/advanced-topics.md` | Book attributed to "Jurczenko"; actually edited by Tony Guida | Corrected to Guida |
| 1.8 | IMPORTANT | `resources/econometric-methods.md` | Mixtape described as having "extensive Python code"; actually R and Stata | Corrected to R/Stata |
| 1.9 | IMPORTANT | `resources/market-microstructure.md` | Hasbrouck URL wrong (`people.stern.nyu.edu`) | Fixed to `pages.stern.nyu.edu/~jhasbrou/` |
| 1.10 | IMPORTANT | Multiple files | "Centre for Finance and Responsible Technology" incorrect | Changed to "Centre for Financial and Regulatory Technology" everywhere |
| 1.11 | IMPORTANT | `LICENSE` | "Dr Barry Quinn" inconsistent with "Prof" elsewhere | Changed to "Prof Barry Quinn" |
| 1.12 | IMPORTANT | `resources/market-microstructure.md` | Lyons book title wrong ("The Microstructure of Foreign Exchange Markets") | Corrected to "The Microstructure Approach to Exchange Rates" |
| 1.13 | IMPORTANT | `resources/programming-practices.md` | Percival book title wrong ("Test-Driven Development in Python") | Corrected to "Test-Driven Development with Python" |
| 1.14 | IMPORTANT | `resources/econometric-methods.md` | Only 2 of 4 authors cited for Bayesian Econometric Methods | Corrected to "Chan, Koop, Poirier & Tobias" |
| 1.15 | IMPORTANT | `resources/mathematical-foundations.md`, `CURRICULUM.md` | Strang book edition ambiguous; chapter numbers didn't match cited edition | Clarified as "Introduction to Linear Algebra, 6th edition" |

### 2. Structural and Internal Consistency Issues (all fixed)

| # | Severity | File(s) | Issue | Resolution |
|---|----------|---------|-------|------------|
| 2.1 | IMPORTANT | `STATUS.md` | Listed subdirectories that did not exist | Created all missing subdirectories with `.gitkeep` files |
| 2.2 | IMPORTANT | `resources/README.md` | Heading said "Planned Resource Documents" but all exist | Changed to "Resource Documents" |
| 2.3 | MINOR | `README.md`, `STATUS.md` | Date inconsistencies (2024 vs 2025) | Reconciled all dates; citation year set to 2024, last-updated to April 2026 |
| 2.4 | MINOR | `CURRICULUM.md` | Effective Python edition not specified; item numbers edition-dependent | Specified 2nd edition; added note about 3rd edition differences |
| 2.5 | MINOR | `scripts/find_dois.py` | Referenced non-existent `bibliography.csv` | Created `papers/bibliography.csv` with all 28 papers; added .gitignore exception |

### 3. Academic Credibility and Rigour (all fixed)

| # | Severity | File(s) | Issue | Resolution |
|---|----------|---------|-------|------------|
| 3.1 | IMPORTANT | `papers/essential-readings.md` | No DOIs or links for any cited paper | Added DOIs and volume/page numbers for all 28 papers |
| 3.2 | IMPORTANT | `README.md` | Unverifiable GitHub URL in citation block | Removed URL from citation |
| 3.4 | MINOR | `STATUS.md` | Line-count metrics used as quality proxy | Removed line-count statistics |
| 3.5 | MINOR | `resources/advanced-topics.md`, `papers/essential-readings.md` | Missing key replication-crisis papers | Added McLean & Pontiff (2016) and Hou, Xue & Zhang (2020) |
| 3.6 | MINOR | `papers/essential-readings.md` | Lopez de Prado (2013/2018) citation vague | Replaced with specific citation to AFML (2018), Chapters 7 and 12 |
| 3.7 | MINOR | `papers/essential-readings.md`, `resources/advanced-topics.md` | Duplicate `pbo` R package reference | Consolidated to single mention in essential-readings.md |

### 4. Soft Recommendation (not actioned — for maintainer consideration)

| # | Issue | Note |
|---|-------|------|
| 3.3 | No evidence of actual course use or external review | Consider adding a note about where/when this curriculum has been used, or any external validation. This strengthens credibility but is a maintainer decision. |

---

## What the Repo Gets Right

The core content is genuinely useful and well-conceived:

- **Textbook selection** is excellent. Shreve, Tsay, Angrist & Pischke, Hastie et al., O'Hara, Hasbrouck, Cartea et al., Lopez de Prado, and Ang are all standard, well-regarded references.
- **Paper selection** in `essential-readings.md` is solid — Fama-French, Kyle, Glosten-Milgrom, Roll, Engle, Bollerslev, Harvey et al., and Gu-Kelly-Xiu represent the genuine intellectual core of quantitative finance.
- **Pedagogical philosophy** — emphasising implementation alongside theory, warning against common pitfalls, insisting on proper cross-validation — is sound and reflects real teaching experience.
- **Curriculum progression** is well-thought-out and appropriate for the target audience.
- **Code examples** (skeleton functions, testing examples, project structure) are genuinely helpful and follow good practices.
- **Critical stance** toward trends, buzzwords, and overfitting is appropriate and valuable.

---

## Methodology

All 15 markdown files, the Python script, `environment.yml`, and `LICENSE` were read in full. Key factual claims were cross-checked against published sources:

- Chapter structures verified against publisher tables of contents for O'Hara, Hasbrouck, Resnick, Shreve, Tsay, Cartea et al., and Strang
- Journal attributions verified via JSTOR, ScienceDirect, and publisher databases
- Book titles, editions, and author lists verified via publisher websites
- Institutional affiliations verified via Ulster University's official staff directory
- URLs tested for accessibility

---

*Report generated by automated content validation review, April 2026. Updated to reflect all corrections applied.*
