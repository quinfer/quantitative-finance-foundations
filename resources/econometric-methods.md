# Econometric Methods for Financial Data

A volatility forecast and a study of whether an exchange rule changed volatility ask different questions. The forecast needs a fair test on later observations. The policy study needs a credible account of what would have happened without the change. Use this guide to match a method to the question before you estimate it. [Econometric methods in the curriculum](../CURRICULUM.md#phase-2-econometric-methods-months-46)

## Preparation

You should be able to interpret a regression, a confidence interval and the assumptions behind them. Review matrix notation and maximum likelihood as needed. If financial time series are new to you, start by constructing returns and testing a simple forecast in the course lab. [Time series chapter and lab](../README.md#if-you-study-computer-science)

## Core Resources

### Analysis of Financial Time Series (Ruey S. Tsay)

Use Tsay to distinguish return forecasts from volatility forecasts. Start with Chapters 1–3 in the third edition. For cointegration, see Section 8.5. For state-space methods and the Kalman filter, see Chapter 11. [Publisher's contents](https://www.wiley.com/en-us/analysis-of-financial-time-series-3rd-edition-p-9780470414354)

**Chapter 1: Financial Time Series and Their Characteristics**
- Distributional properties of returns
- Stylised facts (fat tails, volatility clustering, leverage effects)
- Tests for serial correlation and ARCH effects

**Chapter 2: Linear Time Series Analysis and Its Applications**
- AR, MA, ARMA models
- Model specification, estimation, and diagnostics
- Forecasting with confidence intervals

**Chapter 3: Conditional Heteroscedastic Models**
- ARCH and GARCH specifications
- Asymmetric models (EGARCH, GJR-GARCH)
- See Chapter 10 for multivariate volatility models

**Chapter 4: Nonlinear Models and Their Applications**
- Threshold models and regime switching
- Smooth transition models
- Markov-switching models

**Chapter 5: High-Frequency Data Analysis and Market Microstructure**
- Realised volatility and microstructure noise
- Duration models
- Price discovery in high-frequency data

**Chapter 6: Continuous-Time Models and Their Applications**
- Estimating diffusion processes
- Jump detection
- Term structure models

Reproduce one example using Tsay's data or a comparable series. Match the specification and frequency before comparing results. Repeat the exercise in another period and explain which changes could arise from the sample or the implementation.

**Common difficulties**: Chapter 3 (GARCH models) requires numerical optimisation of non-linear likelihood functions. Likelihood functions can be poorly behaved, leading to convergence failures. Students often struggle with diagnosing why estimation fails—is it model misspecification, starting values, or numerical issues?

**Why this matters**: Nearly all quantitative finance involves modelling time series. Ignoring serial correlation and heteroskedasticity leads to invalid inference and poor forecasts. GARCH-class models remain workhorses for volatility modelling despite being "old" methods.

**Complementary resource**: Tsay's companion book *An Introduction to Analysis of Financial Data with R* provides code implementations. Even if you work in Python, examining R implementations helps understand method details.

### Mostly Harmless Econometrics (Joshua Angrist & Jörn-Steffen Pischke)

**What it provides**: Practical guide to causal inference using observational data, focusing on identification strategies and research design. Whilst examples come from labour economics, methods apply directly to finance research questions.

**How to use it**: Focus on identification strategies:

**Chapter 3: Making Regression Make Sense**
- Regression as conditional expectation
- Omitted variable bias
- What regression coefficients actually estimate

**Chapter 4: Instrumental Variables in Action**
- Two-stage least squares
- Testing instrument validity
- Weak instruments problem

**Chapter 5: Parallel Worlds: Fixed Effects, Differences-in-Differences, and Panel Data**
- Controlling for unobserved heterogeneity
- Parallel trends assumption and testing
- Difference-in-differences extensions

**Chapter 6: Getting a Little Jumpy: Regression Discontinuity Designs**
- Sharp and fuzzy discontinuities
- Bandwidth selection
- Validity tests

**Why finance students should study this**: Finance researchers increasingly need causal inference methods for policy evaluation. Do circuit breakers reduce volatility? How do regulatory changes affect market quality? What are effects of corporate governance on firm value? Answering these questions requires moving beyond correlation to causation.

**Implementation connections**: After studying differences-in-differences, analyse effects of regulatory changes on market quality using TAQ data. After learning instrumental variables, investigate endogeneity in corporate finance questions. The methods appear abstract until applied to specific problems.

**Common difficulties**: Students often struggle with identifying appropriate instruments or convincing exclusion restrictions. The key is careful institutional reasoning about what affects treatment but not outcomes directly. Economics discipline around identification proves valuable beyond specific methods.

**Complementary resource**: *Causal Inference: The Mixtape* (Cunningham) provides extensive Python code examples for causal inference methods. Available free online: https://mixtape.scunning.com/

### The Elements of Statistical Learning (Hastie, Tibshirani & Friedman)

**What it provides**: Comprehensive treatment of modern statistical learning methods—regularisation, tree-based methods, ensemble approaches, neural networks—with strong theoretical foundations and practical guidance.

**How to use it**: Don't attempt comprehensive coverage. Focus on chapters most relevant to finance:

**Chapter 3: Linear Methods for Regression**
- Ridge regression and shrinkage
- Lasso and variable selection
- Methods for prediction versus inference

**Chapter 7: Model Assessment and Selection**
- Bias-variance tradeoff
- Cross-validation approaches
- Bootstrap methods

**Chapter 9: Additive Models, Trees, and Related Methods**
- Regression trees and interpretation
- Gradient boosting
- When linear models fail

**Chapter 10: Boosting and Additive Trees**
- AdaBoost and its connections to loss functions
- Gradient boosting machines
- Tuning and regularisation

**Chapter 15: Random Forests**
- Bagging and random forests
- Variable importance
- Out-of-bag estimation

**Chapter 18: High-Dimensional Problems**
- p > n settings common in finance
- Regularisation strategies
- Multiple testing considerations

**Why this matters**: Finance increasingly involves high-dimensional prediction problems—predicting returns from large sets of characteristics, nowcasting economic conditions from alternative data, credit scoring from diverse features. These problems require methods beyond ordinary least squares.

**Implementation strategy**: Implement simple versions from scratch before using sklearn. For example, implement ridge regression by adding penalty to normal equations, verify it matches sklearn, then move to more complex methods. This builds intuition for what methods actually do.

**Common pitfalls**: Students often jump directly to complex ensemble methods without understanding simpler approaches. Start with regularised regression (Ridge, Lasso), ensuring you understand what these methods accomplish and when they help. Only then move to tree-based methods and neural networks.

**Complementary resource**: *An Introduction to Statistical Learning* by the same authors provides gentler treatment with R code examples. Start here if ESL proves too dense initially.

## Supplementary Resources

### Time Series Analysis (James Hamilton)

**Purpose**: Comprehensive theoretical treatment of time series econometrics. More advanced and theoretical than Tsay, with rigorous asymptotic theory and detailed proofs.

**Key chapters for finance**:
- Chapters 4-5: Linear projection and stationary ARMA processes
- Chapters 8-9: Generalized method of moments and modelling volatility
- Chapters 13-14: Kalman filter and state-space models
- Chapters 22-23: Cointegration and unit root processes

**When to use**: Reference for theoretical foundations when encountering asymptotic results in Tsay or when implementing complex estimators requiring understanding of underlying theory. Not appropriate for first exposure—too theoretical without sufficient financial examples.

### Econometric Analysis (William Greene)

**Purpose**: Comprehensive econometrics reference covering cross-sectional, panel, and time series methods. Standard graduate econometrics text.

**Key sections for finance**:
- Chapters 8-9: Generalised least squares and GMM
- Chapters 11-12: Panel data methods
- Chapters 14-16: Maximum likelihood estimation and time series
- Chapters 18-19: Limited dependent variables and sample selection

**When to use**: Reference for technical details of estimation methods. Not necessary to work through comprehensively, but valuable when implementing specific estimators or understanding variance estimation under various assumptions.

### Panel Data Econometrics (Arellano)

**Purpose**: Rigorous treatment of panel data methods increasingly important in corporate finance and asset pricing research.

**Key topics**:
- Fixed effects and random effects models
- Dynamic panel data models
- GMM estimation with panel data
- Non-linear panel data models

**When to use**: When working with panel datasets combining cross-sectional and time series variation (firm-level data, international returns, etc.). More specialised than core texts but essential for certain research questions.

### Bayesian Econometric Methods (Chan & Koop)

**Purpose**: Modern Bayesian approach to econometric problems, particularly valuable for complex hierarchical models and incorporating prior information.

**Key applications in finance**:
- Bayesian VAR models for forecasting
- Stochastic volatility models
- Bayesian portfolio allocation
- Model averaging and uncertainty

**When to use**: After establishing frequentist foundations. Bayesian methods prove particularly valuable for incorporating parameter uncertainty in portfolio allocation and combining information from multiple models.

## What your comparison can establish

For inference, match the standard errors to the dependence in the data. Residual diagnostics help you understand which assumptions are under pressure. Heteroskedasticity and autocorrelation consistent (HAC) standard errors address some forms of dependence in inference. A conditional volatility model serves a different purpose when volatility itself is the quantity you want to predict.

For forecasting, define what the model could have known at each decision. Tune it on rolling or expanding windows and reserve later observations for evaluation. Where outcomes span several periods, check that the outcomes used in fitting have ended before the evaluation window begins. Compare a regularised or nonlinear model with an ordinary least squares or simple forecasting benchmark on the same dates. Report the gain and its uncertainty.

For a causal claim, describe the institutional facts or research design that support the comparison. State how omitted variables, reverse causality or selection could change the interpretation. In a difference-in-differences design, for example, explain why the comparison group provides a credible account of how the treated group would have changed without the intervention.

When you search many specifications, record the tests and identify the family they belong to before choosing a multiple-testing adjustment. If the result informs portfolio weights, compare the allocation and its later performance with a simple benchmark and test sensitivity to estimation error. [Multiple testing and portfolio choice](../papers/essential-readings.md)

## Implementation Exercises

### Exercise 1: GARCH Model Estimation and Diagnostics

Implement GARCH(1,1) estimation for equity index returns:

```python
def garch11_estimation(returns):
    """
    Estimate GARCH(1,1) model using maximum likelihood.
    
    Parameters:
    returns: Array of log returns
    
    Returns:
    parameters: Estimated omega, alpha, beta
    conditional_variance: Estimated conditional variance series
    standardised_residuals: Residuals / sqrt(conditional_variance)
    loglikelihood: Log-likelihood value
    """
    # Your implementation here
    pass
```

Tasks:
- Estimate parameters using numerical optimisation
- Verify parameter constraints (non-negativity, stationarity)
- Compute standard errors using inverse Hessian
- Test standardised residuals for remaining ARCH effects
- Compare to arch library implementation
- Investigate impact of starting values on convergence

### Exercise 2: Cross-Validation for Time Series

Implement proper cross-validation respecting temporal ordering:

```python
def time_series_cv(X, y, model, window_type='rolling', train_size=252, test_size=20):
    """
    Cross-validation for time series maintaining temporal ordering.
    
    Parameters:
    X: Feature matrix
    y: Target variable
    model: Model class with fit and predict methods
    window_type: 'rolling' (fixed window) or 'expanding' (growing window)
    train_size: Size of training window
    test_size: Size of test window
    
    Returns:
    predictions: Out-of-sample predictions
    metrics: Performance metrics for each fold
    """
    # Your implementation here
    pass
```

Tasks:
- Implement both rolling and expanding window schemes
- Apply to predicting equity returns from characteristics
- Compare to naïve k-fold cross-validation (which violates temporal ordering)
- Demonstrate information leakage from improper cross-validation
- Compute performance metrics (MSE, directional accuracy, Sharpe ratio)

### Exercise 3: Regularised Regression for Return Prediction

Apply regularisation methods to high-dimensional return prediction:

```python
def regularised_prediction(X_train, y_train, X_test, method='ridge', alpha=1.0):
    """
    Predict returns using regularised regression.
    
    Parameters:
    X_train: Training features
    y_train: Training returns
    X_test: Test features
    method: 'ridge', 'lasso', or 'elasticnet'
    alpha: Regularisation parameter
    
    Returns:
    predictions: Predicted returns
    coefficients: Estimated coefficients
    selected_features: Features with non-zero coefficients (for Lasso)
    """
    # Your implementation here
    pass
```

Tasks:
- Collect characteristics for cross-section of stocks (size, value, momentum, etc.)
- Predict one-month-ahead returns using regularised regression
- Select regularisation parameter using cross-validation
- Compare Ridge, Lasso, and Elastic Net
- Investigate which characteristics receive non-zero Lasso weights
- Assess economic significance of predictive R-squared

### Exercise 4: Differences-in-Differences Analysis

Apply DiD to evaluate regulatory change impact:

```python
def difference_in_differences(data, treatment_indicator, post_period, outcome_var, controls=None):
    """
    Estimate treatment effect using differences-in-differences.
    
    Parameters:
    data: Panel dataset with treatment and control groups
    treatment_indicator: Binary variable indicating treatment group
    post_period: Binary variable indicating post-treatment period
    outcome_var: Outcome variable of interest
    controls: Additional control variables
    
    Returns:
    did_estimate: Estimated treatment effect
    standard_error: Standard error clustered at appropriate level
    parallel_trends_test: Test of pre-treatment parallel trends
    """
    # Your implementation here
    pass
```

Tasks:
- Identify regulatory change affecting some markets/firms but not others
- Collect outcome data (volatility, liquidity, trading volume) for treatment and control groups
- Estimate DiD specification with appropriate controls
- Test parallel trends assumption using pre-treatment data
- Conduct placebo tests using pre-treatment periods
- Assess robustness to alternative control groups and specifications

## Assessment Criteria

You have adequate econometric preparation when you can:

1. **Identify appropriate methods**: Given research question, select suitable econometric approach and justify choice. Explain what assumptions are required and how to test them.

2. **Implement estimators correctly**: Write code implementing major estimators (GARCH, Ridge/Lasso, GMM). Verify implementations against established libraries.

3. **Conduct proper inference**: Compute standard errors appropriately for data structure (clustering, HAC, bootstrap). Test hypotheses and interpret results.

4. **Evaluate model performance**: Implement appropriate validation procedures. Assess whether apparent performance reflects genuine signal or overfitting.

5. **Think critically about causality**: Distinguish association from causation. Identify threats to causal inference and strategies for addressing them.

6. **Communicate results clearly**: Present findings with appropriate caveats. Distinguish statistical significance from economic significance.

If you can accomplish these tasks, econometric preparation is adequate for quantitative research. If not, identify specific gaps and address them before proceeding.

---

*This resource reflects teaching experience at Ulster University Business School's Centre for Finance and Responsible Technology.*

