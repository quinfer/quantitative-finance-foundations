# Essential Readings in Quantitative Finance

Start with a paper that addresses a question you are working on. In a factor study, for example, pick one table and identify the portfolio returns, the benchmark and the quantity the authors estimate. Then use the suggestions below to reproduce the comparison or ask a related question with data you can obtain.

Choose by topic when you have a research question, or follow the phase guide when you are working through the curriculum. [Curriculum](../CURRICULUM.md) · [Readings by phase](#6-connecting-papers-to-curriculum-phases) · [Replication strategy](#implementation-and-replication-strategy)

## 1. Asset Pricing and Factor Models

Use these papers to compare explanations for differences in average returns and to examine the evidence behind a proposed factor.

### 1.1 Cross-Section of Returns and Classic Factors

**Fama, E. F., & French, K. R. (1992).** *The Cross-Section of Expected Stock Returns*. Journal of Finance.  
**Theme**: Asset pricing, size and value factors (Phase 2–4)  
**Key contribution**: Documents that firm size and book‑to‑market equity explain cross-sectional stock returns better than CAPM beta, motivating three‑factor and multi‑factor models.  
**Why it matters**: Foundation for equity factor investing and nearly all empirical asset pricing work since the 1990s.  
**Implementation ideas**:
- Construct size and value portfolios using CRSP/Compustat (or equivalent).
- Replicate Fama‑French portfolio sorts and factor returns.
- Test CAPM vs. three‑factor model on your own data.

**Fama, E. F., & French, K. R. (1993).** *Common Risk Factors in the Returns on Stocks and Bonds*. Journal of Financial Economics.  
**Theme**: Multi‑factor models (Phase 2–4)  
**Key contribution**: Introduces three‑factor model (market, size, value) and bond factors, formalising factor structure.  
**Implementation ideas**:
- Estimate factor loadings for portfolios/stocks using OLS.
- Compare explanatory power of CAPM vs. three‑factor model.
- Explore time variation in factor premia.

**Carhart, M. M. (1997).** *On Persistence in Mutual Fund Performance*. Journal of Finance.  
**Theme**: Momentum factor, performance attribution (Phase 2–4)  
**Key contribution**: Adds a momentum factor to Fama‑French, demonstrating that mutual fund “alpha” often reflects exposure to momentum.  
**Implementation ideas**:
- Build long‑short momentum factor à la Carhart.
- Run four‑factor regressions on fund or portfolio returns.
- Investigate how alpha estimates change when momentum is included.

### 1.2 Modern Factor and Mispricing Debates

**Fama, E. F., & French, K. R. (2015).** *[A Five-Factor Asset Pricing Model](https://doi.org/10.1016/j.jfineco.2014.10.010)*. Journal of Financial Economics.\
**Theme**: Factor proliferation, profitability and investment factors (Phase 4)  
**Key contribution**: Adds profitability and investment to the three-factor model. The value factor appears redundant for describing average returns in the sample the authors examine.\
**Implementation ideas**:
- Construct five‑factor returns (or use published series).
- Compare the five-factor model with the same model excluding the value factor. State whether your result holds for the assets and period you test.
- Compare implications for factor‑tilted portfolios.

**Hou, K., Xue, C., & Zhang, L. (2015).** *Digesting Anomalies: An Investment Approach*. Review of Financial Studies.  
**Theme**: Alternative factor structures (Phase 4)  
**Key contribution**: Proposes q‑factor model and reinterprets anomalies in terms of investment‑based asset pricing.  
**Implementation ideas**:
- Implement q‑factor definitions from paper.
- Compare performance vs. Fama‑French models.
- Examine how conclusions about “anomalies” change under q‑factors.

### 1.3 Multiple Testing and the “Factor Zoo”

**Harvey, C. R., Liu, Y., & Zhu, H. (2016).** *… and the Cross-Section of Expected Returns*. Review of Financial Studies.  
**Theme**: Multiple testing, factor proliferation (Phase 2–4)  
**Key contribution**: Argues that standard 5% significance is too lax given hundreds of factors; proposes higher t‑stat thresholds.  
**Why it matters**: Shows why the evidence needed to propose a new factor depends on the wider history of tests.\
**Implementation ideas**:
- Apply their adjusted significance thresholds to your own factor tests.
- Re‑evaluate significance of popular factors in your sample.
- Document how many “discoveries” survive stricter criteria.

---

## 2. Market Microstructure and Liquidity

Read these papers alongside the spread and execution tasks. Start with how the authors turn trades and quotes into a measure of liquidity.

### 2.1 Spreads, Transaction Costs, and Impact

**Roll, R. (1984).** *A Simple Implicit Measure of the Effective Bid–Ask Spread in an Efficient Market*. Journal of Finance.  
**Theme**: Spread estimation from price series (Phase 3)  
**Key contribution**: Shows how to infer effective spread from serial covariance of price changes without direct quote data.  
**Implementation ideas**:
- Implement Roll’s estimator on daily data for multiple stocks.
- Compare implied spreads to quoted spreads where available.
- Examine how estimates vary with volatility and turnover.

**Glosten, L. R., & Milgrom, P. R. (1985).** *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders*. Journal of Financial Economics.  
**Theme**: Adverse selection and information (Phase 3)  
**Key contribution**: Formal model where bid‑ask spread compensates dealer for trading with informed investors.  
**Implementation ideas**:
- Simulate Glosten‑Milgrom trade process and spreads under different information structures.
- Link theory to empirical spread decomposition (e.g., effective vs. realised spreads).

**Kyle, A. S. (1985).** *Continuous Auctions and Insider Trading*. Econometrica.  
**Theme**: Strategic informed trading and price impact (Phase 3–4)  
**Key contribution**: Continuous‑time model of informed trader, noise traders, and market maker; introduces “Kyle lambda” impact coefficient.  
**Implementation ideas**:
- Implement Kyle model simulation; estimate lambda from simulated data.
- Compare theoretical impact to empirical impact estimates from TAQ data.

**Amihud, Y. (2002).** *Illiquidity and Stock Returns: Cross-Section and Time-Series Effects*. Journal of Financial Markets.  
**Theme**: Illiquidity measure and liquidity premium (Phase 3–4)  
**Key contribution**: Introduces Amihud illiquidity ratio and shows illiquid stocks earn higher returns.  
**Implementation ideas**:
- Compute Amihud measure across stocks and time.
- Test whether illiquidity predicts returns in your sample.
- Investigate interaction with size and value factors.

### 2.2 Information Content and Price Discovery

**Hasbrouck, J. (1991).** *Measuring the Information Content of Stock Trades*. Journal of Finance.  
**Theme**: Trade informativeness and VAR decomposition (Phase 3)  
**Key contribution**: Uses VARs to decompose price changes into trade‑related and public information components.  
**Implementation ideas**:
- Implement simplified VAR framework using trade and quote data.
- Estimate information shares for different trading venues or securities.

**Hasbrouck, J. (2002).** *Stalking the “Efficient” Price in Market Microstructure Specifications*. Journal of Finance.  
**Theme**: Efficient price, microstructure noise, and volatility (Phase 3)  
**Key contribution**: Discusses methods for extracting efficient price from noisy quotes and trades.  
**Implementation ideas**:
- Implement simple efficient price estimators.
- Compare realised volatility from efficient vs. transaction prices.

---

## 3. Econometric Methods and Time Series

Use these papers when an exercise asks you to model dependence, quantify uncertainty or choose an estimator.

### 3.1 Volatility Modelling

**Engle, R. F. (1982).** *Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of UK Inflation*. Econometrica.  
**Theme**: ARCH models (Phase 2)  
**Key contribution**: Introduces ARCH for modelling time‑varying volatility.  
**Implementation ideas**:
- Implement ARCH(q) estimation via maximum likelihood.
- Compare to library implementations (e.g., `arch` package).

**Bollerslev, T. (1986).** *Generalized Autoregressive Conditional Heteroskedasticity*. Journal of Econometrics.  
**Theme**: GARCH (Phase 2)  
**Key contribution**: Extends ARCH to GARCH, now standard for volatility modelling.  
**Implementation ideas**:
- Implement GARCH(1,1) from scratch and compare to Tsay examples.
- Test for remaining ARCH effects in standardised residuals.

### 3.2 Dependence, Cointegration, and Inference

**Dickey, D. A., & Fuller, W. A. (1979).** *Distribution of the Estimators for Autoregressive Time Series with a Unit Root*. Journal of the American Statistical Association.  
**Theme**: Unit root testing (Phase 2)  
**Implementation ideas**:
- Implement simple ADF test and compare to `statsmodels`.
- Examine effect of lag length selection.

**Johansen, S. (1988).** *Statistical Analysis of Cointegration Vectors*. Journal of Economic Dynamics and Control.  
**Theme**: Cointegration (Phase 2)  
**Implementation ideas**:
- Use Johansen procedure to test cointegration in pairs trading or term structure data.
- Compare to Engle‑Granger two‑step approach.

**Newey, W. K., & West, K. D. (1987).** *A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix*. Econometrica.  
**Theme**: HAC standard errors (Phase 2)  
**Implementation ideas**:
- Implement simple Newey‑West estimator.
- Compare OLS standard errors vs. HAC in return predictability regressions.

**White, H. (1980).** *A Heteroskedasticity-Consistent Covariance Matrix Estimator and a Direct Test for Heteroskedasticity*. Econometrica.  
**Theme**: Robust inference (Phase 2)  
**Implementation ideas**:
- Implement White robust covariance matrix manually.
- Compare to package implementations.

### 3.3 GMM and Efficient Estimation

**Hansen, L. P. (1982).** *Large Sample Properties of Generalized Method of Moments Estimators*. Econometrica.  
**Theme**: GMM (Phase 2–4)  
**Implementation ideas**:
- Implement simple GMM for a moment‑based asset pricing model.
- Compare results to OLS and ML where applicable.

---

## 4. Machine Learning and Overfitting in Finance

Separate two questions as you read. First, does a model improve return forecasts on later data? Second, how does selecting the best result from many trials affect its interpretation?

### 4.1 ML for Asset Pricing

**Gu, S., Kelly, B., & Xiu, D. (2020).** *[Empirical Asset Pricing via Machine Learning](https://doi.org/10.1093/rfs/hhaa009)*. Review of Financial Studies.\
**Theme**: ML for cross‑sectional return prediction (Phase 4)  
**Key contribution**: Compares methods for predicting stock returns in the authors' data. Trees and neural networks lead the comparison, and the authors trace gains to nonlinear interactions between predictors.\
**Implementation ideas**:
- Implement a subset of their methods on a reduced characteristic set.
- Compare linear and nonlinear models on the same later observations.
- Examine feature importance and economic interpretability.

**Rasekhschaffe, K. C., & Jones, R. C. (2019).** *Machine Learning for Stock Selection*. Financial Analysts Journal.  
**Theme**: Practitioner‑oriented ML (Phase 4)  
**Implementation ideas**:
- Implement their ML pipeline on publicly available equity data.
- Compare performance and turnover to simpler factor models.

### 4.2 Backtest Overfitting and CV

**Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2017).** *[The Probability of Backtest Overfitting](https://doi.org/10.21314/jcf.2016.322)*. Journal of Computational Finance.\
**Theme**: Backtest overfitting (Phase 4)  
**Key contribution**: Uses combinatorially symmetric cross-validation to estimate how often a strategy selected as best on one partition ranks below the median on its complement.\
**Implementation ideas**:
- Replicate simple examples of overfitted strategies.
- Implement their probability‑of‑backtest‑overfitting metric.

**López de Prado, M. (2018).** *[Advances in Financial Machine Learning](https://www.wiley.com/en-au/Advances%2Bin%2BFinancial%2BMachine%2BLearning-p-9781119482086)*. Wiley, Chapters 7 and 12.\
**Theme**: Cross‑validation and ML pitfalls (Phase 4)  
**Implementation ideas**:
- Implement purged and embargoed cross‑validation.
- Compare ordinary and purged cross-validation for overlapping return labels. Separately, use a walk-forward evaluation to test a rule as it would have run through time.

To reproduce the strategy selection exercise, use the [Financial Data Science backtesting lab](https://financialdatascience.co.uk/labs/lab10_backtesting.html). For an R implementation of the probability of backtest overfitting, see the [pbo package](https://CRAN.R-project.org/package=pbo).

---

## 5. Portfolio Construction and Risk

Read Markowitz to understand the portfolio problem when expected returns and covariances are given. Then ask how estimation changes the weights and the later results.

### 5.1 Foundations

**Markowitz, H. (1952).** *Portfolio Selection*. Journal of Finance.  
**Theme**: Mean–variance optimisation (Phase 1)  
**Key contribution**: Formalises diversification and introduces efficient frontier.  
**Implementation ideas**:
- Implement mean–variance optimisation from the original formulation.
- Reproduce efficient frontiers for simple datasets.

**Black, F., & Litterman, R. (1992).** *Global Portfolio Optimization*. Financial Analysts Journal.  
**Theme**: Incorporating views into optimisation (Phase 4)  
**Implementation ideas**:
- Implement a basic Black–Litterman model combining priors with investor views.
- Compare resulting portfolios to naïve Markowitz and equal‑weight.

### 5.2 Estimation Error and Robust Portfolio Choice

**DeMiguel, V., Garlappi, L., & Uppal, R. (2009).** *[Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?](https://doi.org/10.1093/rfs/hhm075)* Review of Financial Studies.\
**Theme**: Estimation risk and naïve diversification (Phase 2–4)  
**Key contribution**: Finds that the optimised rules tested do not consistently beat equal weighting across the datasets examined. The authors link the result to estimation error.\
**Implementation ideas**:
- Reproduce their comparison between 1/N and optimised portfolios.
- Investigate impact of sample length and number of assets.

**Ledoit, O., & Wolf, M. (2004).** *A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices*. Journal of Multivariate Analysis.  
**Theme**: Covariance shrinkage (Phase 2–4)  
**Implementation ideas**:
- Implement shrinkage estimator and compare eigenvalues to sample covariance.
- Test impact on portfolio performance vs. sample covariance.

---

## 6. Connecting Papers to Curriculum Phases

### Phase 1 (Foundations)

- Markowitz (1952) – mean–variance foundations.
- Use Fama–French (1992, 1993) as motivation for why covariance and expected returns matter.

### Phase 2 (Econometric Methods)

- Engle (1982), Bollerslev (1986) – volatility models.
- Dickey–Fuller, Johansen – non‑stationarity and cointegration.
- White (1980), Newey & West (1987) – robust inference.
- Hansen (1982) – GMM foundations.

### Phase 3 (Market Microstructure)

- Roll (1984), Glosten–Milgrom (1985), Kyle (1985) – spreads and information.
- Hasbrouck (1991, 2002) – information content and efficient price.
- Amihud (2002) – illiquidity and returns.

### Phase 4 (Advanced Applications)

- Fama–French (2015), Hou–Xue–Zhang (2015) – modern factor models.
- Harvey–Liu–Zhu (2016) – multiple testing standards.
- Gu–Kelly–Xiu (2020), Rasekhschaffe–Jones (2019) – ML for asset pricing.
- Bailey et al. (2017), López de Prado – backtest overfitting and CV.
- DeMiguel–Garlappi–Uppal (2009), Ledoit–Wolf (2004) – robust portfolio choice.

---

## Implementation and Replication Strategy

1. Choose one result and write down the financial question, sample and method. Record which inputs and choices you need to recover the result.
2. Reproduce the table or figure where the inputs are available. If you use a substitute sample or change the design, label the result as an extension and explain the difference.
3. Change one assumption or choice at a time. Report where the result holds up and where it changes, then give the commands needed to rerun your analysis.

Use your notes to connect the paper to the task it supports. [Quick Start](../QUICKSTART.md) · [Curriculum](../CURRICULUM.md) · [Contributing](../CONTRIBUTING.md)
