# Essential Readings in Quantitative Finance

## Purpose and Scope

This document provides a curated set of core research papers that underpin the curriculum in `CURRICULUM.md` and the thematic guides in `resources/`. It is not an exhaustive bibliography but a **minimum viable canon** of papers that students should understand deeply by the end of the 12-month programme.

For each paper, you'll find:

- **Citation** (author, year, title, outlet, DOI)
- **Theme** and **curriculum phase** where it fits
- **Key contribution** and why it matters
- **Implementation / replication suggestions**

Use this document to prioritise reading and to structure replication projects in the `papers/` and `implementations/` directories.

## How to Use This Document

- **By phase**: At each curriculum phase, focus on the papers tagged for that phase.
- **By theme**: When working in a given area (e.g., microstructure, factors), read the papers in that theme systematically.
- **Actively, not passively**: For each paper:
  - Reproduce key tables/figures where data are available.
  - Implement core models in Python.
  - Compare results across time periods and markets.
  - Document deviations and potential reasons.

When filing papers in this repository:

- Store them under the appropriate thematic subdirectory in `papers/`.
- Create a `notes.md` in each paper folder summarising core insights, methodology, and replication status.
- Place replication code in a `replication/` subdirectory and cross-link from `implementations/`.

---

## 1. Asset Pricing and Factor Models

These papers support **Phase 2-4** (Econometric Methods and Advanced Applications) and live primarily under `papers/asset-pricing/`.

### 1.1 Cross-Section of Returns and Classic Factors

**Fama, E. F., & French, K. R. (1992).** *The Cross-Section of Expected Stock Returns*. Journal of Finance, 47(2), 427-465. [DOI: 10.2307/2329112](https://doi.org/10.2307/2329112)  
**Theme**: Asset pricing, size and value factors (Phase 2-4)  
**Key contribution**: Documents that firm size and book-to-market equity explain cross-sectional stock returns better than CAPM beta, motivating three-factor and multi-factor models.  
**Why it matters**: Foundation for equity factor investing and nearly all empirical asset pricing work since the 1990s.  
**Implementation ideas**:
- Construct size and value portfolios using CRSP/Compustat (or equivalent).
- Replicate Fama-French portfolio sorts and factor returns.
- Test CAPM vs. three-factor model on your own data.

**Fama, E. F., & French, K. R. (1993).** *Common Risk Factors in the Returns on Stocks and Bonds*. Journal of Financial Economics, 33(1), 3-56. [DOI: 10.1016/0304-405X(93)90023-5](https://doi.org/10.1016/0304-405X(93)90023-5)  
**Theme**: Multi-factor models (Phase 2-4)  
**Key contribution**: Introduces three-factor model (market, size, value) and bond factors, formalising factor structure.  
**Implementation ideas**:
- Estimate factor loadings for portfolios/stocks using OLS.
- Compare explanatory power of CAPM vs. three-factor model.
- Explore time variation in factor premia.

**Carhart, M. M. (1997).** *On Persistence in Mutual Fund Performance*. Journal of Finance, 52(1), 57-82. [DOI: 10.1111/j.1540-6261.1997.tb03808.x](https://doi.org/10.1111/j.1540-6261.1997.tb03808.x)  
**Theme**: Momentum factor, performance attribution (Phase 2-4)  
**Key contribution**: Adds a momentum factor to Fama-French, demonstrating that mutual fund "alpha" often reflects exposure to momentum.  
**Implementation ideas**:
- Build long-short momentum factor a la Carhart.
- Run four-factor regressions on fund or portfolio returns.
- Investigate how alpha estimates change when momentum is included.

### 1.2 Modern Factor and Mispricing Debates

**Fama, E. F., & French, K. R. (2015).** *A Five-Factor Asset Pricing Model*. Journal of Financial Economics, 116(1), 1-22. [DOI: 10.1016/j.jfineco.2014.10.010](https://doi.org/10.1016/j.jfineco.2014.10.010)  
**Theme**: Factor proliferation, profitability and investment factors (Phase 4)  
**Key contribution**: Extends three-factor model with profitability and investment, questioning value's independent role.  
**Implementation ideas**:
- Construct five-factor returns (or use published series).
- Test whether value adds explanatory power beyond five factors.
- Compare implications for factor-tilted portfolios.

**Hou, K., Xue, C., & Zhang, L. (2015).** *Digesting Anomalies: An Investment Approach*. Review of Financial Studies, 28(3), 650-705. [DOI: 10.1093/rfs/hhu068](https://doi.org/10.1093/rfs/hhu068)  
**Theme**: Alternative factor structures (Phase 4)  
**Key contribution**: Proposes q-factor model and reinterprets anomalies in terms of investment-based asset pricing.  
**Implementation ideas**:
- Implement q-factor definitions from paper.
- Compare performance vs. Fama-French models.
- Examine how conclusions about "anomalies" change under q-factors.

### 1.3 Multiple Testing, the "Factor Zoo", and Replication

**Harvey, C. R., Liu, Y., & Zhu, H. (2016).** *... and the Cross-Section of Expected Returns*. Review of Financial Studies, 29(1), 5-68. [DOI: 10.1093/rfs/hhv059](https://doi.org/10.1093/rfs/hhv059)  
**Theme**: Multiple testing, factor proliferation (Phase 2-4)  
**Key contribution**: Argues that standard 5% significance is too lax given hundreds of factors; proposes higher t-stat thresholds.  
**Why it matters**: Sets standards for distinguishing genuine factors from data-mined noise.  
**Implementation ideas**:
- Apply their adjusted significance thresholds to your own factor tests.
- Re-evaluate significance of popular factors in your sample.
- Document how many "discoveries" survive stricter criteria.

**McLean, R. D., & Pontiff, J. (2016).** *Does Academic Research Destroy Stock Return Predictability?* Journal of Finance, 71(1), 5-32. [DOI: 10.1111/jofi.12365](https://doi.org/10.1111/jofi.12365)  
**Theme**: Publication bias and anomaly decay (Phase 2-4)  
**Key contribution**: Shows that anomaly returns decline by roughly one-third after publication, consistent with both statistical bias and informed trading eroding mispricings.  
**Why it matters**: Essential reading for anyone building factor strategies — published anomalies are not guaranteed to persist.  
**Implementation ideas**:
- Select a set of published anomalies and compare pre- vs. post-publication returns.
- Investigate whether decay rates differ by anomaly type or market.

**Hou, K., Xue, C., & Zhang, L. (2020).** *Replicating Anomalies*. Review of Financial Studies, 33(5), 2019-2133. [DOI: 10.1093/rfs/hhy131](https://doi.org/10.1093/rfs/hhy131)  
**Theme**: Replication and robustness of anomalies (Phase 2-4)  
**Key contribution**: Attempts to replicate 452 published anomalies; finds that most fail to replicate with proper methodology and multiple-testing adjustments.  
**Why it matters**: Reinforces the curriculum's emphasis on rigour and scepticism toward published factors.  
**Implementation ideas**:
- Pick 5-10 well-known anomalies and test replicability in your sample.
- Compare results using original vs. updated methodology.
- Document which anomalies survive and which do not.

---

## 2. Market Microstructure and Liquidity

These papers support **Phase 3** (Market Microstructure) and belong in `papers/market-microstructure/` (some overlap with `asset-pricing/` for liquidity premia).

### 2.1 Spreads, Transaction Costs, and Impact

**Roll, R. (1984).** *A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market*. Journal of Finance, 39(4), 1127-1139. [DOI: 10.1111/j.1540-6261.1984.tb03897.x](https://doi.org/10.1111/j.1540-6261.1984.tb03897.x)  
**Theme**: Spread estimation from price series (Phase 3)  
**Key contribution**: Shows how to infer effective spread from serial covariance of price changes without direct quote data.  
**Implementation ideas**:
- Implement Roll's estimator on daily data for multiple stocks.
- Compare implied spreads to quoted spreads where available.
- Examine how estimates vary with volatility and turnover.

**Glosten, L. R., & Milgrom, P. R. (1985).** *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*. Journal of Financial Economics, 14(1), 71-100. [DOI: 10.1016/0304-405X(85)90044-3](https://doi.org/10.1016/0304-405X(85)90044-3)  
**Theme**: Adverse selection and information (Phase 3)  
**Key contribution**: Formal model where bid-ask spread compensates dealer for trading with informed investors.  
**Implementation ideas**:
- Simulate Glosten-Milgrom trade process and spreads under different information structures.
- Link theory to empirical spread decomposition (e.g., effective vs. realised spreads).

**Kyle, A. S. (1985).** *Continuous Auctions and Insider Trading*. Econometrica, 53(6), 1315-1335. [DOI: 10.2307/1913210](https://doi.org/10.2307/1913210)  
**Theme**: Strategic informed trading and price impact (Phase 3-4)  
**Key contribution**: Continuous-time model of informed trader, noise traders, and market maker; introduces "Kyle lambda" impact coefficient.  
**Implementation ideas**:
- Implement Kyle model simulation; estimate lambda from simulated data.
- Compare theoretical impact to empirical impact estimates from TAQ data.

**Amihud, Y. (2002).** *Illiquidity and Stock Returns: Cross-Section and Time-Series Effects*. Journal of Financial Markets, 5(1), 31-56. [DOI: 10.1016/S1386-4181(01)00024-6](https://doi.org/10.1016/S1386-4181(01)00024-6)  
**Theme**: Illiquidity measure and liquidity premium (Phase 3-4)  
**Key contribution**: Introduces Amihud illiquidity ratio and shows illiquid stocks earn higher returns.  
**Implementation ideas**:
- Compute Amihud measure across stocks and time.
- Test whether illiquidity predicts returns in your sample.
- Investigate interaction with size and value factors.

### 2.2 Information Content and Price Discovery

**Hasbrouck, J. (1991).** *Measuring the Information Content of Stock Trades*. Journal of Finance, 46(1), 179-207. [DOI: 10.1111/j.1540-6261.1991.tb03749.x](https://doi.org/10.1111/j.1540-6261.1991.tb03749.x)  
**Theme**: Trade informativeness and VAR decomposition (Phase 3)  
**Key contribution**: Uses VARs to decompose price changes into trade-related and public information components.  
**Implementation ideas**:
- Implement simplified VAR framework using trade and quote data.
- Estimate information shares for different trading venues or securities.

**Hasbrouck, J. (2002).** *Stalking the "Efficient Price" in Market Microstructure Specifications: An Overview*. Journal of Financial Markets, 5(3), 329-339. [DOI: 10.1016/S1386-4181(02)00029-0](https://doi.org/10.1016/S1386-4181(02)00029-0)  
**Theme**: Efficient price, microstructure noise, and volatility (Phase 3)  
**Key contribution**: Discusses methods for extracting efficient price from noisy quotes and trades.  
**Implementation ideas**:
- Implement simple efficient price estimators.
- Compare realised volatility from efficient vs. transaction prices.

---

## 3. Econometric Methods and Time Series

These papers support **Phase 2** and live under `papers/econometric-methods/`.

### 3.1 Volatility Modelling

**Engle, R. F. (1982).** *Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of UK Inflation*. Econometrica, 50(4), 987-1007. [DOI: 10.2307/1912773](https://doi.org/10.2307/1912773)  
**Theme**: ARCH models (Phase 2)  
**Key contribution**: Introduces ARCH for modelling time-varying volatility.  
**Implementation ideas**:
- Implement ARCH(q) estimation via maximum likelihood.
- Compare to library implementations (e.g., `arch` package).

**Bollerslev, T. (1986).** *Generalized Autoregressive Conditional Heteroskedasticity*. Journal of Econometrics, 31(3), 307-327. [DOI: 10.1016/0304-4076(86)90063-1](https://doi.org/10.1016/0304-4076(86)90063-1)  
**Theme**: GARCH (Phase 2)  
**Key contribution**: Extends ARCH to GARCH, now standard for volatility modelling.  
**Implementation ideas**:
- Implement GARCH(1,1) from scratch and compare to Tsay examples.
- Test for remaining ARCH effects in standardised residuals.

### 3.2 Dependence, Cointegration, and Inference

**Dickey, D. A., & Fuller, W. A. (1979).** *Distribution of the Estimators for Autoregressive Time Series with a Unit Root*. Journal of the American Statistical Association, 74(366), 427-431. [DOI: 10.2307/2286348](https://doi.org/10.2307/2286348)  
**Theme**: Unit root testing (Phase 2)  
**Implementation ideas**:
- Implement simple ADF test and compare to `statsmodels`.
- Examine effect of lag length selection.

**Johansen, S. (1988).** *Statistical Analysis of Cointegration Vectors*. Journal of Economic Dynamics and Control, 12(2-3), 231-254. [DOI: 10.1016/0165-1889(88)90041-3](https://doi.org/10.1016/0165-1889(88)90041-3)  
**Theme**: Cointegration (Phase 2)  
**Implementation ideas**:
- Use Johansen procedure to test cointegration in pairs trading or term structure data.
- Compare to Engle-Granger two-step approach.

**Newey, W. K., & West, K. D. (1987).** *A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix*. Econometrica, 55(3), 703-708. [DOI: 10.2307/1913610](https://doi.org/10.2307/1913610)  
**Theme**: HAC standard errors (Phase 2)  
**Implementation ideas**:
- Implement simple Newey-West estimator.
- Compare OLS standard errors vs. HAC in return predictability regressions.

**White, H. (1980).** *A Heteroskedasticity-Consistent Covariance Matrix Estimator and a Direct Test for Heteroskedasticity*. Econometrica, 48(4), 817-838. [DOI: 10.2307/1912934](https://doi.org/10.2307/1912934)  
**Theme**: Robust inference (Phase 2)  
**Implementation ideas**:
- Implement White robust covariance matrix manually.
- Compare to package implementations.

### 3.3 GMM and Efficient Estimation

**Hansen, L. P. (1982).** *Large Sample Properties of Generalized Method of Moments Estimators*. Econometrica, 50(4), 1029-1054. [DOI: 10.2307/1912775](https://doi.org/10.2307/1912775)  
**Theme**: GMM (Phase 2-4)  
**Implementation ideas**:
- Implement simple GMM for a moment-based asset pricing model.
- Compare results to OLS and ML where applicable.

---

## 4. Machine Learning and Overfitting in Finance

These papers support **Phase 2-4** and belong under `papers/machine-learning/`.

### 4.1 ML for Asset Pricing

**Gu, S., Kelly, B., & Xiu, D. (2020).** *Empirical Asset Pricing via Machine Learning*. Review of Financial Studies, 33(5), 2223-2273. [DOI: 10.1093/rfs/hhaa009](https://doi.org/10.1093/rfs/hhaa009)  
**Theme**: ML for cross-sectional return prediction (Phase 4)  
**Key contribution**: Applies a range of ML methods (trees, neural networks, etc.) to predict returns from many characteristics; shows substantial improvements over linear models.  
**Implementation ideas**:
- Implement a subset of their methods on a reduced characteristic set.
- Compare OOS performance of linear vs. non-linear models.
- Examine feature importance and economic interpretability.

**Rasekhschaffe, K. C., & Jones, R. C. (2019).** *Machine Learning for Stock Selection*. Financial Analysts Journal, 75(3), 70-88. [DOI: 10.1080/0015198X.2019.1596678](https://doi.org/10.1080/0015198X.2019.1596678)  
**Theme**: Practitioner-oriented ML (Phase 4)  
**Implementation ideas**:
- Implement their ML pipeline on publicly available equity data.
- Compare performance and turnover to simpler factor models.

### 4.2 Backtest Overfitting and CV

**Bailey, D. H., Borwein, J., Lopez de Prado, M., & Zhu, Q. J. (2014).** *The Probability of Backtest Overfitting*. Journal of Computational Finance, 17(4), 1-31. [DOI: 10.21314/JCF.2014.285](https://doi.org/10.21314/JCF.2014.285)  
**Theme**: Backtest overfitting (Phase 4)  
**Key contribution**: Formalises notion of backtest overfitting and proposes procedures to estimate its probability.  
**Implementation ideas**:
- Replicate simple examples of overfitted strategies.
- Implement their probability-of-backtest-overfitting metric.

**Lopez de Prado, M. (2018).** *Advances in Financial Machine Learning*. Wiley. Chapters 7 and 12.  
**Theme**: Cross-validation and backtesting pitfalls in finance (Phase 4)  
**Key contribution**: Introduces purged and embargoed cross-validation and walk-forward backtesting methods addressing serial dependence and information leakage in financial ML.  
**Implementation ideas**:
- Implement purged and embargoed cross-validation.
- Compare naive CV vs. proper CV on your own strategies.
- Demonstrate information leakage using standard k-fold on time series data.

For R users, a reference implementation of the Probability of Backtest Overfitting methodology is available in the `pbo` package on CRAN: see [`https://CRAN.R-project.org/package=pbo`](https://CRAN.R-project.org/package=pbo) for documentation and examples.

---

## 5. Portfolio Construction and Risk

These papers support **Phase 1-4** and belong under `papers/portfolio-construction/`.

### 5.1 Foundations

**Markowitz, H. (1952).** *Portfolio Selection*. Journal of Finance, 7(1), 77-91. [DOI: 10.2307/2975974](https://doi.org/10.2307/2975974)  
**Theme**: Mean-variance optimisation (Phase 1)  
**Key contribution**: Formalises diversification and introduces efficient frontier.  
**Implementation ideas**:
- Implement mean-variance optimisation from the original formulation.
- Reproduce efficient frontiers for simple datasets.

**Black, F., & Litterman, R. (1992).** *Global Portfolio Optimization*. Financial Analysts Journal, 48(5), 28-43. [DOI: 10.2469/faj.v48.n5.28](https://doi.org/10.2469/faj.v48.n5.28)  
**Theme**: Incorporating views into optimisation (Phase 4)  
**Implementation ideas**:
- Implement a basic Black-Litterman model combining priors with investor views.
- Compare resulting portfolios to naive Markowitz and equal-weight.

### 5.2 Estimation Error and Robust Portfolio Choice

**DeMiguel, V., Garlappi, L., & Uppal, R. (2009).** *Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?* Review of Financial Studies, 22(5), 1915-1953. [DOI: 10.1093/rfs/hhm075](https://doi.org/10.1093/rfs/hhm075)  
**Theme**: Estimation risk and naive diversification (Phase 2-4)  
**Key contribution**: Shows that simple 1/N diversification often outperforms optimised portfolios out-of-sample due to estimation error.  
**Implementation ideas**:
- Reproduce their comparison between 1/N and optimised portfolios.
- Investigate impact of sample length and number of assets.

**Ledoit, O., & Wolf, M. (2004).** *A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices*. Journal of Multivariate Analysis, 88(2), 365-411. [DOI: 10.1016/S0047-259X(03)00096-4](https://doi.org/10.1016/S0047-259X(03)00096-4)  
**Theme**: Covariance shrinkage (Phase 2-4)  
**Implementation ideas**:
- Implement shrinkage estimator and compare eigenvalues to sample covariance.
- Test impact on portfolio performance vs. sample covariance.

---

## 6. Connecting Papers to Curriculum Phases

### Phase 1 (Foundations)

- Markowitz (1952) -- mean-variance foundations.
- Use Fama-French (1992, 1993) as motivation for why covariance and expected returns matter.

### Phase 2 (Econometric Methods)

- Engle (1982), Bollerslev (1986) -- volatility models.
- Dickey-Fuller, Johansen -- non-stationarity and cointegration.
- White (1980), Newey & West (1987) -- robust inference.
- Hansen (1982) -- GMM foundations.

### Phase 3 (Market Microstructure)

- Roll (1984), Glosten-Milgrom (1985), Kyle (1985) -- spreads and information.
- Hasbrouck (1991, 2002) -- information content and efficient price.
- Amihud (2002) -- illiquidity and returns.

### Phase 4 (Advanced Applications)

- Fama-French (2015), Hou-Xue-Zhang (2015) -- modern factor models.
- Harvey-Liu-Zhu (2016), McLean-Pontiff (2016), Hou-Xue-Zhang (2020) -- multiple testing, replication.
- Gu-Kelly-Xiu (2020), Rasekhschaffe-Jones (2019) -- ML for asset pricing.
- Bailey et al. (2014), Lopez de Prado (2018) -- backtest overfitting and CV.
- DeMiguel-Garlappi-Uppal (2009), Ledoit-Wolf (2004) -- robust portfolio choice.

---

## Implementation and Replication Strategy

To integrate these papers into your learning:

1. **Select a theme** (e.g., factor models, volatility, microstructure).  
2. **Pick 1-2 core papers** from that theme.  
3. **Create a folder** under the appropriate `papers/` subdirectory:
   - e.g., `papers/asset-pricing/fama-french-1992/notes.md`
4. **Write notes** summarising:
   - Research question, data, methodology, and main findings.
   - Strengths, limitations, and open questions.
5. **Implement replication code** in `replication/` and/or `implementations/`:
   - Strive to reproduce at least one core table or figure.
   - Document discrepancies with the original paper.
6. **Reflect in your journal** (see `QUICKSTART.md` and `CURRICULUM.md`):
   - What did you learn?
   - What was hard to reproduce, and why?
   - How does this paper connect to others?

Over time, this process builds a **personal library of deeply understood papers**, not just a list of PDFs.

---

*This reading list supports the curriculum at Ulster University Business School's Centre for Finance and Responsible Technology and is intended as a living document. Suggestions for additions or re-organisation are welcome via issues and pull requests (see `CONTRIBUTING.md`).*
