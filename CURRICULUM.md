# Quantitative finance curriculum

Start by explaining where a portfolio return came from. You will then ask how much of what you observe is predictable, what it would cost to trade on a forecast and how the evidence changes when you try many models. By the end, you should be able to state a financial question, choose a method that answers it and give someone else the information they need to reproduce your result.

The four phases give an indicative twelve-month plan for self-study. Work on the readings and code together. Use the Quick Start to choose a first task, then use the checks below to judge whether you are ready to move on. [Quick Start](QUICKSTART.md) · [Research papers by phase](papers/essential-readings.md#6-connecting-papers-to-curriculum-phases)

## Phase 1: Foundations (months 1–3)

Begin with returns, weights and covariance. Use Strang to work through vectors, projections and matrix decompositions as you calculate portfolio risk. Use Resnick to study expectation and convergence alongside simulation. Read Shreve on probability spaces and conditional expectation when you are ready for continuous-time models. Use McKinney to organise price data in pandas and consult Slatkin as you turn repeated notebook steps into functions. [Mathematics](resources/mathematical-foundations.md) · [Programming](resources/programming-practices.md)

1. **Portfolio returns and performance.** Compare equal-weighted and value-weighted equity portfolios. For a historical index replication, use membership and weights available at each date. If you have only a fixed list of assets, report the result for that sample and explain how its selection limits the comparison. Document corporate actions and missing observations, then report rolling volatility and Sharpe ratios with their frequency and assumptions.
2. **Mean–variance optimisation.** Build an efficient frontier and compare it under long-only and leverage constraints. Change the estimated means or covariance matrix and show how the weights respond. Compare a simple case with a library implementation.
3. **GARCH estimation.** Fit a GARCH(1,1) model to equity index returns by maximum likelihood. Compare your estimates with a library using the same return scaling, mean specification and innovation distribution. Investigate any difference before using the model to forecast.

Before moving on, explain one data decision that changed a result and show how you checked one calculation independently.

## Phase 2: Econometric methods (months 4–6)

Distinguish a forecasting question from a causal question. Tsay gives you models for dependence in returns and volatility. Read the linear and conditional volatility chapters first, then the cointegration section for Task 5. Use Angrist and Pischke to study how institutional details can support a causal comparison, such as an evaluation of a change in trading rules. Read Hastie, Tibshirani and Friedman on regularisation and model assessment before selecting a return forecasting model. [Econometric methods](resources/econometric-methods.md)

4. **Volatility forecasts.** Compare GARCH, exponential GARCH and GJR-GARCH forecasts for several assets. Hold the forecast horizon and evaluation sample fixed. Choose a volatility proxy and loss function, such as QLIKE with an appropriate proxy, and explain what the comparison can establish.
5. **Cointegration and pairs trading.** Test whether a pair of securities has a stable long-run relationship. Form the rule on a training period, test it on later observations and state the costs, rebalancing dates and risk limits. Explain separately what the cointegration test says and what the trading result says.
6. **Regularised return prediction.** Compare ridge, lasso and elastic net with ordinary least squares. Use time-ordered validation for tuning and a later test sample for evaluation. Explain how the coefficients and forecast errors change across specifications.

Before moving on, show which observations were available at each model choice. For a causal analysis, state the identifying assumption and explain which parts of it the data can help you assess.

## Phase 3: Market microstructure (months 7–9)

A strategy trades at prices shaped by spreads, available depth and the response of other traders. Use O'Hara to understand how trading arrangements and private information affect prices. Read Hasbrouck to connect those mechanisms to trades and quotes, then use Cartea, Jaimungal and Penalva to study execution and inventory risk. [Market microstructure](resources/market-microstructure.md)

7. **Spreads and liquidity.** Use trades and quotes for liquid equities to compare quoted, effective and realised spreads. Record how you match a trade to a quote and how far ahead you measure the realised spread. Check the data requirements before committing to the exercise.
8. **Optimal execution.** Implement the Almgren–Chriss model and compare it with schedules based on time or market volume. Show how the comparison changes with order size and assumptions about impact.
9. **Order book simulation.** Build a small limit order book and test a market-making rule. Measure inventory exposure and investigate how fill assumptions and adverse selection affect simulated results.

Before moving on, state which costs you can estimate from the data and which enter through a modelling assumption.

## Phase 4: Advanced applications (months 10–12)

Bring prediction, portfolio construction and trading costs into one study. Read Ang on factor investing, then consult López de Prado on sample weights, cross-validation and backtesting as your design requires. Use the chapters in Jurczenko's edited volume that match your data or estimation problem. The annotated papers provide comparisons for factor models, machine learning and the effect of searching many specifications. [Advanced topics](resources/advanced-topics.md) · [Essential readings](papers/essential-readings.md)

1. **Systematic equity strategy.** Define a factor signal, portfolio rule and benchmark. Fix the evaluation design, record the alternatives you try and show whether the result survives transaction costs and changes in assumptions.
2. **Microstructure study.** Formulate a question you can answer with trades, quotes or order book data you can access. Explain what the design identifies, quantify uncertainty and report the result in a short paper or technical report.
3. **Reproducible research pipeline.** Build a workflow from data acquisition through backtesting to reporting. Give a reader the inputs, dependencies and commands needed to reproduce the result. Ask a second person to rerun it and document any discrepancies.

## Assess your work

For each task, keep the question, inputs, code and results together. Report the magnitude of the result in financial units as well as its statistical uncertainty. Explain which assumptions matter, what happened when you changed them and what the evidence still leaves open. For a strategy search, record the rules you tried so that readers can tell how the reported rule was selected.

Use the same standard when reading new research. Start with one finding, examine how the authors obtained it and try to reproduce a table or figure where the inputs are available. [How to read and reproduce a paper](papers/essential-readings.md#implementation-and-replication-strategy)
