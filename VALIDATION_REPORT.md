# Content Validation Report

**Date**: April 2026
**Scope**: Full review of all content files in the repository for hallucinations, factual accuracy, academic credibility, rigour, and truthfulness.

---

## Executive Summary

This repository is a markdown-based curriculum for quantitative finance, attributed to Prof Barry Quinn at Ulster University Business School. Overall, the content is **substantive, well-structured, and pedagogically sound**. The recommended textbooks and papers are genuine, well-regarded works. The curriculum's philosophy — emphasising rigour, reproducibility, and scepticism of fads — is commendable and appropriate for its target audience.

However, the review identified **multiple factual errors** (incorrect book chapter descriptions, wrong journal attributions, an inaccurate centre name, and a misleadingly titled supplementary book), **several structural inconsistencies** (phantom directories listed in STATUS.md, broken internal references), and a handful of issues affecting **academic credibility** (missing DOIs, an unverifiable citation, and some overstatements). None are catastrophic, but collectively they risk undermining the repo's emphasis on rigour.

Action points are ranked:
- **[CRITICAL]** — Factual errors or hallucinations that would mislead students
- **[IMPORTANT]** — Issues affecting credibility, accuracy, or usability
- **[MINOR]** — Polish items or suggestions for improvement

---

## 1. Hallucinations and Factual Errors

### 1.1 [CRITICAL] O'Hara chapter descriptions are fabricated

**File**: `resources/market-microstructure.md` (lines 28–63), `CURRICULUM.md` (lines 139–147)

The repo describes O'Hara's *Market Microstructure Theory* as having chapters titled: (1) Market Microstructure: An Overview, (2) Inventory Models, (3) Information-Based Models, (4) Strategic Trader Models, (5) Market Structures, (6) Empirical Evidence.

The actual chapter structure of O'Hara (1995) is:
1. Markets and Market-Making
2. Inventory Models
3. Information-Based Models
4. Strategic Trader Models I: Informed Traders
5. Strategic Trader Models II: Uninformed Traders
6. Information and the Price Process
7. Market Viability and Stability
8. Liquidity and the Relationships between Markets
9. Issues in Market Performance

The repo collapses 9 chapters into 6, invents chapter titles ("Market Structures", "Empirical Evidence", "Market Microstructure: An Overview"), and omits Chapters 6–9 entirely. The claim "Chapters 1–5" in CURRICULUM.md is particularly problematic because Chapters 4 and 5 in the real book split strategic trader models into informed vs. uninformed traders, which is a substantively different framing from what the repo describes.

**Action**: Rewrite the O'Hara chapter descriptions to match the actual table of contents. Update the recommended chapter range.

---

### 1.2 [CRITICAL] Hasbrouck chapter descriptions are fabricated

**File**: `resources/market-microstructure.md` (lines 76–116)

The repo describes Hasbrouck's *Empirical Market Microstructure* as having chapters: (2) The Bid-Ask Spread, (3) Measuring Information in Prices, (4) The Information Content of Trades, (5) Liquidity and Trading Costs, (6) Market Depth, (7) High-Frequency Data Analysis.

The actual table of contents (Oxford University Press, 2007) is:
1. Introduction
2. Trading Mechanisms
3. The Roll Model of Trade Prices
4. Univariate Time Series Analysis
5. Sequential Trade Models
6. Order Flow And The Probability of Informed Trading (PIN)
7. Strategic Trade Models
8. A Generalized Roll Model of Trade Prices
9. Multivariate Linear Microstructure Models
10. Multiple Securities and Multiple Prices
11. Dealers and Their Inventories
12. Limit Order Markets
13. Depth
14. Trading Costs: Retrospective and Comparative
15. Prospective Trading Costs and Execution Strategies

The repo's chapter numbering and titles bear no resemblance to the actual book. This is a clear hallucination.

**Action**: Completely rewrite the Hasbrouck chapter guide to reflect the actual 15-chapter structure. Identify the correct chapters covering the topics described.

---

### 1.3 [CRITICAL] Resnick chapter descriptions are partially incorrect

**File**: `resources/mathematical-foundations.md` (lines 64–77), `CURRICULUM.md` (lines 41–48)

The repo describes Resnick's *A Probability Path* Chapters 1–5 as covering: (1) Sets and Events, (2) Random Variables and Distributions, (3) Transforms and Convergence, (4) Sums and Symmetry (LLN, CLT), (5) Conditioning and Martingales.

The actual chapter structure is:
1. Sets and Events
2. Probability Spaces
3. Random Variables, Elements and Measurable Maps
4. Independence
5. Integration and Expectation
6. Convergence Concepts
7. Laws of Large Numbers and Sums of Independent Random Variables
8. Convergence in Distribution
9. Characteristic Functions and the Central Limit Theorem
10. Martingales

The repo conflates and re-orders topics substantially. The LLN and CLT are in Chapters 7–9, not 4. Martingales are Chapter 10, not 5. Convergence concepts are Chapter 6, not 3. Saying "focus on Chapters 1–5" would actually give students only foundational set theory, probability spaces, random variables, independence, and integration — not the convergence theory and martingales the curriculum claims they will cover.

**Action**: Correct the chapter descriptions. Update the recommended chapter range to cover the topics actually described (likely Chapters 1–10, or at minimum 1–7 for convergence, with 10 for martingales).

---

### 1.4 [CRITICAL] Hasbrouck (2002) journal attribution is wrong

**File**: `papers/essential-readings.md` (line 141)

The repo states:
> **Hasbrouck, J. (2002).** *Stalking the "Efficient" Price in Market Microstructure Specifications*. **Journal of Finance**.

This paper was published in the **Journal of Financial Markets** (Vol. 5, Issue 3, pp. 329–339), not the Journal of Finance.

**Action**: Correct the journal to "Journal of Financial Markets".

---

### 1.5 [CRITICAL] Cartea et al. chapter descriptions are inaccurate

**File**: `resources/market-microstructure.md` (lines 126–158), `CURRICULUM.md` (lines 163–173)

The repo describes Cartea et al.'s *Algorithmic and High-Frequency Trading* as having: Chapter 2 (Statistical Properties of Trading Processes), Chapter 3 (Optimal Execution), Chapter 4 (Market Making), Chapter 5 (Optimal Liquidation), Chapter 6 (HFT Strategies), and the CURRICULUM.md says "Chapters 1–7".

The actual structure is:
- Part I: Chapters 1–4 (Microstructure and Empirical Facts)
- Part II: Chapter 5 (Stochastic Optimal Control — mathematical tools)
- Part III: Chapters 6–12 (Algorithmic and HFT Strategies)

Optimal execution is Chapters 6–8, not Chapter 3. Market making is Chapter 10, not Chapter 4. The repo's chapter numbering is entirely wrong.

**Action**: Rewrite to reflect the actual 12-chapter structure. Update recommended chapter ranges.

---

### 1.6 [CRITICAL] Tsay chapter descriptions conflate and re-order chapters

**File**: `resources/econometric-methods.md` (lines 28–60), `CURRICULUM.md` (lines 85–94)

The CURRICULUM.md states:
> Tsay Chapters 1-5: Linear time series models, Volatility models, Unit roots and cointegration, State space models and Kalman filtering.

The actual Tsay (3rd ed.) structure:
- Ch 1: Financial Time Series Characteristics
- Ch 2: Linear Time Series
- Ch 3: Conditional Heteroscedastic Models
- Ch 4: Nonlinear Models
- Ch 5: High-Frequency Data Analysis

Unit roots and cointegration are **not** in Chapters 1–5; they appear in Chapter 8 (Multivariate Time Series). State space models and Kalman filtering are in **Chapter 11**, not Chapter 5.

The `econometric-methods.md` file correctly describes the actual content of Chapters 1–6 but then the CURRICULUM.md contradicts it by attributing wrong topics to the "Chapters 1–5" range.

**Action**: Fix the CURRICULUM.md to accurately state what Tsay Chapters 1–5 cover. Move references to unit roots/cointegration and state-space models to the correct chapter numbers.

---

### 1.7 [IMPORTANT] Jurczenko book title and editorship misattributed

**File**: `CURRICULUM.md` (line 215), `resources/advanced-topics.md` (line 167)

The repo cites: **"Big Data and Machine Learning in Quantitative Investment" (Jurczenko)**

The actual book is edited by **Tony Guida**, not Jurczenko. It was published by Wiley in 2019. There is no evidence that Jurczenko edited this volume. A different book by Jurczenko exists (*Machine Learning for Asset Management*), so confusing the two is plausible but still incorrect.

**Action**: Correct the editor attribution. Verify which book is actually intended and cite it accurately.

---

### 1.8 [IMPORTANT] Causal Inference: The Mixtape — incorrect language claim

**File**: `resources/econometric-methods.md` (line 99)

The repo states:
> *Causal Inference: The Mixtape* (Cunningham) provides **extensive Python code examples** for causal inference methods.

The book's primary code examples are in **R and Stata**, not Python. The GitHub repository contains only 6.7% Python code. The book website explicitly advertises R and Stata.

**Action**: Correct to state the book provides R and Stata code examples. Note that Python translations exist in the community but are not the primary offering.

---

### 1.9 [IMPORTANT] Hasbrouck website URL is wrong

**File**: `resources/market-microstructure.md` (line 118)

The repo gives: `http://people.stern.nyu.edu/jhasbrou/`

The correct URL is: `https://pages.stern.nyu.edu/~jhasbrou/`

The `people.stern.nyu.edu` URL format may redirect, but the canonical and currently working address uses `pages.stern.nyu.edu/~jhasbrou/`.

**Action**: Update the URL.

---

### 1.10 [IMPORTANT] Centre name is incorrect

**Files**: README.md, CURRICULUM.md, STATUS.md, and all `resources/*.md` footers

The repo consistently refers to the **"Centre for Finance and Responsible Technology"**.

According to Ulster University's official profile for Prof Barry Quinn, the actual name is the **"Centre for Financial and Regulatory Technology"**.

**Action**: Correct the centre name throughout the repository.

---

### 1.11 [IMPORTANT] Title inconsistency: "Dr" vs "Prof"

**File**: `LICENSE` (line 2) says "Dr Barry Quinn"; `README.md` (line 9) and `STATUS.md` (line 280) say "Prof Barry Quinn".

According to Ulster University's website, Quinn holds the title **Professor**. The LICENSE should be updated to be consistent.

**Action**: Standardise to "Prof Barry Quinn" or "Professor Barry Quinn" throughout.

---

### 1.12 [IMPORTANT] Lyons book title is incorrect

**File**: `resources/market-microstructure.md` (line 177)

The repo refers to: **"The Microstructure of Foreign Exchange Markets" (Richard Lyons)**

The actual book title is: **"The Microstructure Approach to Exchange Rates"** (MIT Press, 2001).

**Action**: Correct the title.

---

### 1.13 [IMPORTANT] Percival book title is slightly wrong

**File**: `resources/programming-practices.md` (line 158)

The repo refers to: **"Test-Driven Development in Python" (Harry Percival)**

The actual title is: **"Test-Driven Development with Python"** (O'Reilly).

**Action**: Correct the title.

---

### 1.14 [IMPORTANT] Bayesian Econometric Methods — incomplete author list

**File**: `resources/econometric-methods.md` (line 183)

The repo cites: **"Bayesian Econometric Methods (Chan & Koop)"**

The book has four authors: **Joshua Chan, Gary Koop, Dale J. Poirier, and Justin L. Tobias** (Cambridge University Press, 2nd ed. 2019). Omitting two of four authors is a notable bibliographic error.

**Action**: Cite all four authors, or use "Chan et al." if brevity is needed.

---

### 1.15 [IMPORTANT] Strang book — edition ambiguity

**File**: `resources/mathematical-foundations.md`, `CURRICULUM.md`

The repo recommends **"Linear Algebra and Its Applications" (Gilbert Strang)**. Strang has two distinct and commonly used textbooks:
- *Linear Algebra and Its Applications* (4th ed., 2005) — older edition, 4 chapters + supplements
- *Introduction to Linear Algebra* (6th ed., 2023) — the more current and widely recommended text

The chapter numbers cited (Chapters 1, 2, 3, 6, 7 including SVD) more closely match *Introduction to Linear Algebra* or his MIT OCW lecture structure than *Linear Algebra and Its Applications*, which has a different chapter layout. The repo also mentions "Introduction to Linear Algebra" as a "gentler" alternative, but for many readers they may actually be describing the same progression.

**Action**: Clarify which specific Strang text and edition is intended. Verify chapter numbers against the chosen edition.

---

## 2. Structural and Internal Consistency Issues

### 2.1 [IMPORTANT] STATUS.md lists directories that do not exist

**File**: `STATUS.md` (lines 70–86)

STATUS.md lists subdirectories under `implementations/`, `papers/`, and `exercises/` (e.g., `implementations/foundations/`, `papers/asset-pricing/`, `exercises/task-01-portfolio-returns/`, etc.). These directories **do not exist** in the repository. Only the parent directories with their README files are present.

This creates a misleading impression of the repository's state. The STATUS.md claims "Directory Structure ✅" and "All required directories created with README files" — this is false.

**Action**: Either create the listed subdirectories (even if empty, with `.gitkeep` files), or update STATUS.md to accurately reflect what exists. The current state is misleading.

---

### 2.2 [IMPORTANT] resources/README.md says "Planned Resource Documents" but they all exist

**File**: `resources/README.md` (line 12)

The file says "## Planned Resource Documents" and lists the five resource documents. All five documents exist and are complete. The heading should reflect reality.

**Action**: Change "Planned Resource Documents" to "Resource Documents" or "Available Resource Documents".

---

### 2.3 [MINOR] Date inconsistency

**File**: `README.md` (line 128) says "Last Updated: November 2024"; `STATUS.md` (line 286) says "Last Updated: November 13, 2024"; `LICENSE` (line 2) says "Copyright (c) 2024".

The citation block in README.md (line 108) says "Quinn, B. (2025)." — this is inconsistent with the "Last Updated November 2024" date.

**Action**: Reconcile dates. If the citation year is 2025, the last-updated date should reflect that.

---

### 2.4 [MINOR] Effective Python item numbering may be edition-dependent

**File**: `CURRICULUM.md` (line 62)

The repo says "Items 1–30" and specifically mentions "Item 27–30" for comprehensions. The 2nd edition (90 items) and 3rd edition (125 items) have different item numbering. Items 27–30 do relate to comprehensions in the 2nd edition, but students picking up the 3rd edition (published November 2024) will find different numbering.

**Action**: Specify the edition (2nd edition recommended, or update references for 3rd edition).

---

### 2.5 [MINOR] Missing bibliography.csv

**File**: `scripts/find_dois.py` (line 9)

The script references `papers/bibliography.csv` which does not exist in the repository. The script is unusable without this file.

**Action**: Either create a bibliography.csv with the papers from `essential-readings.md`, or document that the file needs to be created by the user.

---

## 3. Academic Credibility and Rigour

### 3.1 [IMPORTANT] No DOIs or links for any cited paper

**File**: `papers/essential-readings.md`

None of the 25+ cited papers include DOIs or links to the actual publications. For a curriculum emphasising rigour and reproducibility, this is a significant gap. Students would need to search for every paper individually.

**Action**: Add DOIs for all cited papers. The `scripts/find_dois.py` utility appears designed for this purpose but has no input data. Prioritise adding DOIs to `essential-readings.md`.

---

### 3.2 [IMPORTANT] Unverifiable GitHub URL in citation block

**File**: `README.md` (line 111)

The citation block includes: `https://github.com/quinfer/quantitative-finance-foundations`

This URL has not been verified to exist. If the repo lives at a different URL, the citation is misleading.

**Action**: Verify the URL and update if needed, or remove if the repo is not publicly hosted at that address.

---

### 3.3 [IMPORTANT] No peer review or external validation claimed

The repo states it was "maintained by" Prof Barry Quinn and reflects "teaching experience" — but there is no mention of whether the curriculum has been used in an actual course, reviewed by external academics, or validated through student outcomes. For a resource claiming authority, some evidence of adoption or review would strengthen credibility.

**Action**: Consider adding a note about where/when this curriculum has been used, or acknowledge it as a proposed curriculum. This is a soft recommendation.

---

### 3.4 [MINOR] Overstatement: "over 3,000 lines of detailed guidance"

**File**: `STATUS.md` (line 93)

The claim "5 comprehensive resource documents (over 3,000 lines of detailed guidance)" and "Total lines of documentation: 3,200+" (line 252) is plausible but unverified. More importantly, line count is a poor metric of quality and its prominence feels like padding.

**Action**: Consider removing or de-emphasising line counts as a quality metric. Let the content speak for itself.

---

### 3.5 [MINOR] Missing discussion of key limitations in ML-for-finance literature

**File**: `resources/advanced-topics.md`, `papers/essential-readings.md`

The curriculum appropriately warns about overfitting and multiple testing, but does not cite or discuss some important critical works:
- McLean & Pontiff (2016), "Does Academic Research Destroy Stock Return Predictability?" — shows published anomalies decay after publication
- Hou, Xue & Zhang (2020), "Replicating Anomalies" — shows most anomalies fail to replicate

The Harvey, Liu & Zhu (2016) paper on multiple testing is included, which is good, but the replication crisis in asset pricing deserves more attention given the curriculum's emphasis on rigour.

**Action**: Consider adding McLean & Pontiff (2016) and/or Hou, Xue & Zhang (2020) replication study to the essential readings, given their importance to the curriculum's critical stance.

---

### 3.6 [MINOR] López de Prado (2013/2018) citation is vague

**File**: `papers/essential-readings.md` (line 235)

The citation:
> **López de Prado, M. (2013/2018).** *Backtest Overfitting in Financial Machine Learning* (various versions).

This is imprecise. There are multiple distinct papers. If the intent is to cite the *Journal of Computational Finance* paper (Bailey et al., 2014, already cited separately) or his book chapters, this should be specified. "Various versions" is not an acceptable academic citation.

**Action**: Replace with a specific paper citation, or remove if the content is already covered by Bailey et al. (2014).

---

### 3.7 [MINOR] `pbo` R package reference appears twice

**Files**: `papers/essential-readings.md` (line 241), `resources/advanced-topics.md` (line 69)

The reference to the CRAN `pbo` package for Probability of Backtest Overfitting appears in both files. This is minor duplication but also feels somewhat promotional or out of place in a Python-oriented curriculum.

**Action**: Consolidate to one mention, or note that this is an R package in a curriculum that otherwise recommends Python.

---

## 4. Summary of Action Points

### Critical (fix immediately — these are factual errors that would mislead students)

| # | File(s) | Issue |
|---|---------|-------|
| 1.1 | `resources/market-microstructure.md`, `CURRICULUM.md` | O'Hara chapter descriptions are fabricated; real book has 9 chapters, not 6 |
| 1.2 | `resources/market-microstructure.md` | Hasbrouck chapter descriptions are fabricated; real book has 15 chapters |
| 1.3 | `resources/mathematical-foundations.md`, `CURRICULUM.md` | Resnick chapter descriptions wrong; LLN/CLT are Ch 7–9, Martingales Ch 10 |
| 1.4 | `papers/essential-readings.md` | Hasbrouck (2002) published in J. Financial Markets, not J. Finance |
| 1.5 | `resources/market-microstructure.md`, `CURRICULUM.md` | Cartea et al. chapter descriptions wrong; book has 12 chapters in 3 parts |
| 1.6 | `CURRICULUM.md` | Tsay Ch 1–5 descriptions wrong; unit roots/cointegration in Ch 8, Kalman filter in Ch 11 |

### Important (fix soon — these affect credibility and accuracy)

| # | File(s) | Issue |
|---|---------|-------|
| 1.7 | `CURRICULUM.md`, `resources/advanced-topics.md` | Jurczenko book is actually edited by Tony Guida |
| 1.8 | `resources/econometric-methods.md` | Mixtape provides R/Stata code, not Python |
| 1.9 | `resources/market-microstructure.md` | Hasbrouck URL should be `pages.stern.nyu.edu/~jhasbrou/` |
| 1.10 | Multiple files | Centre name should be "Financial and Regulatory Technology" |
| 1.11 | `LICENSE` | "Dr" should be "Prof" for consistency |
| 1.12 | `resources/market-microstructure.md` | Lyons book title is "The Microstructure Approach to Exchange Rates" |
| 1.13 | `resources/programming-practices.md` | Percival book title is "Test-Driven Development *with* Python" |
| 1.14 | `resources/econometric-methods.md` | Bayesian Econometric Methods has 4 authors, not 2 |
| 1.15 | `resources/mathematical-foundations.md`, `CURRICULUM.md` | Strang book edition ambiguity; chapter numbers may not match cited edition |
| 2.1 | `STATUS.md` | Lists directories that do not exist in the repo |
| 2.2 | `resources/README.md` | Says "Planned" but documents exist |
| 3.1 | `papers/essential-readings.md` | No DOIs or URLs for any cited paper |
| 3.2 | `README.md` | Unverifiable GitHub URL in citation block |
| 3.3 | General | No evidence of actual course use or external review |

### Minor (improve when convenient)

| # | File(s) | Issue |
|---|---------|-------|
| 2.3 | `README.md`, `STATUS.md` | Date inconsistencies (2024 vs 2025) |
| 2.4 | `CURRICULUM.md` | Effective Python edition not specified; item numbers are edition-dependent |
| 2.5 | `scripts/find_dois.py` | References non-existent `bibliography.csv` |
| 3.4 | `STATUS.md` | Line-count metrics feel like padding |
| 3.5 | `resources/advanced-topics.md` | Missing key replication-crisis papers |
| 3.6 | `papers/essential-readings.md` | López de Prado (2013/2018) citation is vague |
| 3.7 | `papers/essential-readings.md`, `resources/advanced-topics.md` | Duplicate `pbo` package reference |

---

## 5. What the Repo Gets Right

To be balanced: the core content is genuinely useful and well-conceived.

- **Textbook selection** is excellent. Shreve, Tsay, Angrist & Pischke, Hastie et al., O'Hara, Hasbrouck, Cartea et al., López de Prado, and Ang are all standard, well-regarded references in their fields.
- **Paper selection** in `essential-readings.md` is solid — the canon of Fama-French, Kyle, Glosten-Milgrom, Roll, Engle, Bollerslev, Harvey et al., and Gu-Kelly-Xiu represents the genuine intellectual core of quantitative finance.
- **Pedagogical philosophy** — emphasising implementation alongside theory, warning against common pitfalls, insisting on proper cross-validation — is sound and reflects real teaching experience.
- **Curriculum progression** is well-thought-out and appropriate for the target audience.
- **Code examples** (skeleton functions, testing examples, project structure) are genuinely helpful and follow good practices.
- **Critical stance** toward trends, buzzwords, and overfitting is appropriate and valuable.

The issues identified are primarily errors of **detail** (wrong chapter numbers, wrong journal names, wrong book titles) rather than errors of **substance**. The curriculum recommends the right books and papers — it just sometimes describes their contents inaccurately, which is the hallmark of content generated with an LLM that confabulates structural details.

---

*Report generated by automated content validation review, April 2026.*
