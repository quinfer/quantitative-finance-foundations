# Curriculum Overview

This document provides detailed progression through quantitative finance foundations, explaining how different components fit together and why particular sequencing matters.

## Learning Objectives

By working through this curriculum systematically, students will develop capability to:

1. **Formulate research questions** precisely and identify appropriate methods for addressing them

2. **Implement econometric and statistical methods** correctly, understanding assumptions and limitations

3. **Build reproducible research pipelines** from data acquisition through analysis to results

4. **Evaluate empirical evidence** critically, distinguishing robust findings from spurious patterns

5. **Communicate quantitative findings** clearly to technical and non-technical audiences

6. **Apply methods to real problems** in systematic trading, risk management, and financial research

These objectives require integrated development across mathematical foundations, statistical methods, computational implementation, and domain knowledge.

## Phase 1: Foundations (Months 1-3)

**Objective**: Build mathematical and computational infrastructure for subsequent work.

### Mathematical Foundations

Begin with **Stochastic Calculus for Finance II** (Shreve), working through Chapters 1-4 on probability spaces, random variables, and conditional expectation. Don't attempt comprehensive mastery—focus on developing intuition for measure-theoretic probability whilst accepting some formalism remains opaque initially.

Concurrently review **Introduction to Linear Algebra** (Strang, 6th ed.), particularly:

- Matrix decompositions (eigenvalue, singular value)

- Projection and least squares

- Positive definite matrices and quadratic forms

These concepts appear constantly in portfolio optimisation, principal component analysis, and covariance estimation.

For probability theory specifically, **A Probability Path** (Resnick) develops rigorous treatment without excessive measure theory. Core chapters 1–5 cover probability spaces, random variables, independence, and integration. Then focus on:

- Convergence concepts — in probability, almost surely, in distribution (Chapter 6)

- Law of large numbers (Chapter 7) and central limit theorem (Chapters 8–9)

- Martingale theory and conditional expectation (Chapter 10)

### Python Implementation

Simultaneously begin **Python for Data Analysis** (McKinney), implementing every example. Focus on:

- Data structures (Series, DataFrame) and manipulation

- GroupBy operations and aggregation

- Time series functionality specific to pandas

Then move to **Effective Python** (Slatkin, 2nd edition), implementing Items 1-30 which cover core language features and best practices. Pay particular attention to:

- Comprehensions vs. loops (Items 27-30 in 2nd ed.)

- Generator expressions for large datasets

- Proper exception handling

*Note*: The 3rd edition (2024) expands to 125 items with different numbering. Item references here follow the 2nd edition.

### First Implementations

By end of Month 3, you should implement:

**Task 1**: Download daily returns for S&P 500 constituents, compute equal-weighted and value-weighted portfolio returns, calculate rolling volatility and Sharpe ratios. Document data sources, handle survivorship bias, plot results.

**Task 2**: Implement mean-variance optimisation following Markowitz, including constraints (long-only, leverage limits). Compare efficient frontiers under different assumptions. Document numerical stability issues encountered.

**Task 3**: Estimate simple GARCH(1,1) model for equity index returns using maximum likelihood. Compare your implementation to established library. Investigate where results diverge.

These tasks force engagement with real data issues (missing values, corporate actions, survivorship bias) whilst building implementation skills.

## Phase 2: Econometric Methods (Months 4-6)

**Objective**: Develop rigorous statistical inference capabilities for financial time series.

### Time Series Analysis

Work through **Analysis of Financial Time Series** (Tsay, 3rd ed.):

- Financial time series characteristics (Chapter 1)

- Linear time series models — AR, MA, ARMA (Chapter 2)

- Volatility models — ARCH, GARCH, extensions (Chapter 3)

- Nonlinear models (Chapter 4)

- Multivariate time series, unit roots, and cointegration (Chapter 8)

- State space models and Kalman filtering (Chapter 11)

Implement every major example using recent data. Compare results to Tsay's findings. When results differ, investigate why—data period, market regime, implementation details all matter.

### Causal Inference

Study **Mostly Harmless Econometrics** (Angrist & Pischke) Chapters 3-6:

- Instrumental variables and two-stage least squares

- Regression discontinuity designs

- Differences-in-differences

- Panel data methods

Whilst examples come from labour economics, identification strategies apply directly to finance questions: Do circuit breakers affect volatility? How do regulatory changes impact market quality? What are causal effects of corporate governance on firm value?

### Statistical Learning Foundations

Begin **The Elements of Statistical Learning** (Hastie et al.), focusing on:

- Chapter 3: Linear methods for regression (particularly Ridge and Lasso)

- Chapter 7: Model assessment and selection (cross-validation, bootstrap)

- Chapters 9-10: Additive models and boosting

- Chapter 15: Random forests

Don't attempt comprehensive coverage—focus on methods demonstrably useful in finance applications. Implement each method from scratch for simple cases before using libraries.

### Intermediate Implementations

**Task 4**: Estimate and compare volatility models (GARCH, EGARCH, GJR-GARCH) for multiple assets. Test for asymmetric effects. Evaluate out-of-sample forecast accuracy using proper scoring rules (not just MSE).

**Task 5**: Identify and test a cointegration relationship between related securities (e.g., spot and futures, or closely-related equities). Implement pairs trading strategy with proper risk controls. Backtest carefully, documenting transaction costs and implementation assumptions.

**Task 6**: Apply regularisation methods (Ridge, Lasso, Elastic Net) to predicting equity returns from characteristics. Implement proper cross-validation. Compare to OLS. Investigate which characteristics receive non-zero weights and why.

## Phase 3: Market Microstructure (Months 7-9)

**Objective**: Understand how markets actually function and implications for quantitative strategies.

### Microstructure Theory

Study **Market Microstructure Theory** (O'Hara) Chapters 1-6:

- Markets and market-making (Chapter 1)

- Inventory models of dealer behaviour (Chapter 2)

- Information-based models (Chapter 3)

- Strategic trader models — informed and uninformed (Chapters 4-5)

- Information and the price process (Chapter 6)

Then **Empirical Market Microstructure** (Hasbrouck):

- Roll model and spread estimation (Chapter 3)

- Sequential trade models and order flow (Chapters 5-7)

- Multivariate models and price discovery (Chapters 9-10)

- Transaction costs and execution strategies (Chapters 14-15)

Understanding microstructure proves essential for realistic strategy implementation. Transaction costs, market impact, and adverse selection often dominate returns in high-turnover strategies.

### Algorithmic Trading

Work through **Algorithmic and High-Frequency Trading** (Cartea et al.):

- Microstructure and empirical facts (Part I, Chapters 1–4)

- Optimal execution — Almgren-Chriss framework and extensions (Part III, Chapters 6–8)

- Market making models (Chapter 10)

- Pairs trading, statistical arbitrage, and order imbalance (Chapters 11–12)

Implement optimal execution strategies. Compare theoretical predictions to empirical execution costs. Identify when theory breaks down and why.

### Advanced Implementations

**Task 7**: Obtain tick data (TAQ, Thomson Reuters Tick History, or similar) for liquid equities. Calculate bid-ask spreads, effective spreads, and realised spreads following Hasbrouck. Investigate intraday patterns and determinants of liquidity.

**Task 8**: Implement Almgren-Chriss optimal execution for realistic position sizes. Compare to simpler strategies (TWAP, VWAP). Estimate transaction cost functions from data. Assess sensitivity to model parameters.

**Task 9**: Build limit order book simulator. Test simple market-making strategies. Identify adverse selection costs. Investigate inventory risk management approaches.

## Phase 4: Advanced Applications (Months 10-12)

**Objective**: Apply integrated capabilities to research questions and systematic strategies.

### Factor Models and Asset Pricing

Study **Asset Management: A Systematic Approach to Factor Investing** (Ang):

- Foundations of factor investing

- Equity factors (value, momentum, quality)

- Fixed income and alternative risk premia

- Portfolio construction with factors

Understand both theoretical foundations (why factors might command risk premia) and empirical evidence (what actually works, with proper adjustments for multiple testing).

### Machine Learning in Finance

Work through **Advances in Financial Machine Learning** (López de Prado):

- Feature engineering for financial data

- Cross-validation under dependence

- Backtesting without overfitting

- Portfolio construction from predictions

Pay particular attention to Chapters 4 (sample weights), 7 (cross-validation), 11 (bet sizing), and 12 (backtesting). These chapters address implementation realities often ignored in academic treatments.

Study **Big Data and Machine Learning in Quantitative Investment** (Guida, ed., Wiley, 2019) selected chapters on:

- Alternative data sources and preprocessing

- Dimension reduction for high-dimensional predictors

- Ensemble methods and stacking

- Walk-forward analysis

### Synthesis Projects

**Project 1**: Develop and test a systematic equity strategy based on established factors. Implement proper portfolio construction (accounting for transaction costs, diversification, risk controls). Conduct comprehensive backtest following López de Prado's recommendations. Document assumptions, limitations, and sensitivity to parameters.

**Project 2**: Investigate a specific market microstructure question using proprietary or academic data. Formulate hypothesis clearly, identify appropriate econometric method, implement analysis, present results with proper uncertainty quantification. Write up as research paper or technical report.

**Project 3**: Build production-quality research pipeline from data acquisition through strategy backtesting to reporting. Implement version control, testing, documentation. Demonstrate reproducibility by having collaborator replicate results independently.

## Ongoing Development

Beyond this 12-month foundation, continued development requires:

### Reading Research

Follow leading journals systematically:

- *Journal of Finance*, *Journal of Financial Economics*, *Review of Financial Studies* (top-tier finance)

- *Journal of Financial and Quantitative Analysis*, *Journal of Financial Markets* (quantitative focus)

- *Journal of Econometrics*, *Econometrica* (methods development)

- *Quantitative Finance*, *Journal of Portfolio Management* (practitioner-oriented)

Maintain reading list of papers addressing methods or applications relevant to your research questions.

### Method Development

As new methods emerge (deep learning, reinforcement learning, causal machine learning), evaluate critically:

- What problem does this solve that existing methods don't?

- What are theoretical foundations?

- What is empirical evidence of value-added in finance specifically?

- What are implementation requirements and limitations?

Avoid chasing trends. Most "innovations" represent repackaging of established ideas.

### Building Track Record

Maintain portfolio of completed projects demonstrating capabilities:

- Research papers or technical reports

- Open-source implementations of methods

- Contributions to established projects

- Reproducible analysis supporting empirical claims

Quality over quantity. One rigorous, well-documented project demonstrates more than multiple superficial implementations.

## Common Pitfalls and How to Avoid Them

**Pitfall 1: Mathematical preparation without implementation**

*Symptom*: Can derive Black-Scholes PDE but can't price actual options from market data.

*Solution*: Implement methods immediately upon learning them. Theory and practice develop together.

**Pitfall 2: Implementation without understanding**

*Symptom*: Uses libraries without knowing what they actually compute or why.

*Solution*: Implement simple versions from scratch before using sophisticated libraries. Compare results, understand differences.

**Pitfall 3: Backtesting without rigour**

*Symptom*: Impressive historical performance that fails immediately in live trading.

*Solution*: Study López de Prado's work on backtest overfitting carefully. Implement proper cross-validation, account for transaction costs realistically, test robustness systematically.

**Pitfall 4: Ignoring market microstructure**

*Symptom*: Strategies that look profitable tick-by-tick but fail when accounting for realistic execution.

*Solution*: Always model transaction costs, market impact, and adverse selection explicitly. Test sensitivity to execution assumptions.

**Pitfall 5: Confusing statistical significance with economic significance**

*Symptom*: Publishing papers about "significant" predictors that explain 0.1% of variance.

*Solution*: Always report economic magnitudes alongside statistical tests. Ask whether findings matter in practice.

**Pitfall 6: Data snooping and multiple testing**

*Symptom*: Testing hundreds of strategies, reporting the best performers without adjustment.

*Solution*: Pre-register hypotheses where possible. Apply multiple testing corrections (Harvey et al. 2016). Maintain "researcher degrees of freedom" tracker.

## Assessment and Progress Tracking

Track progress through:

**Implementation portfolio**: Maintain Git repository of completed tasks and projects with documentation.

**Research journal**: Document what you've learned, what confused you, what worked and what didn't. This metacognitive practice proves invaluable.

**Code review**: Have peers review your implementations. Nothing reveals gaps in understanding like explaining code to others.

**Replication exercises**: Reproduce published results. When you can't replicate findings, investigate why—data differences, methodology details, or publication bias all provide learning opportunities.

**Substantive projects**: Complete non-trivial research questions requiring integration of methods. Can you formulate question precisely, identify appropriate methods, implement correctly, and interpret results appropriately?

## Next Steps

Upon completing this foundation:

**Research path**: Pursue PhD focusing on empirical asset pricing, market microstructure, or quantitative methods development. Attend conferences (AFA, WFA, SFS, FMA). Publish in peer-reviewed journals.

**Industry path**: Seek systematic trading, quantitative research, or risk management roles at investment firms. Build track record through open-source contributions and Kaggle-style competitions (with appropriate scepticism about their realism).

**Teaching path**: Develop courses teaching these methods to next generation. Teaching forces crystallisation of knowledge and reveals gaps in understanding.

All paths require continuous learning. Quantitative finance evolves as markets change, data becomes available, and methods develop. Foundations here enable adaptation and continued growth rather than providing final answers.

---

*This curriculum reflects methods taught at Ulster University Business School's Centre for Financial and Regulatory Technology and builds on experience teaching quantitative finance to masters and PhD students.*

