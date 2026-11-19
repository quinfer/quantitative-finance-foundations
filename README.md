# Quantitative Finance Foundations

A trading rule can look profitable because you chose it after seeing the returns. To judge whether it might work on new data, you need to know how the returns were measured, how the rule was chosen and what evidence you set aside to test it. This curriculum develops that judgement through readings and exercises in empirical asset pricing, financial econometrics and systematic trading.

## Where to start

### If you study finance

Start with a question you already know from finance, such as whether a portfolio's returns can be explained by its exposure to the market. Use that question to practise working with return data in Python and interpreting a regression. Build your mathematics, econometrics and Python in parallel. Read about how orders become trades so that you can explain what a strategy's simulated returns assume about execution. [Mathematical foundations](resources/mathematical-foundations.md) · [Econometric methods](resources/econometric-methods.md) · [Programming practices](resources/programming-practices.md) · [Market microstructure](resources/market-microstructure.md)

### If you study computer science

If you already write code, start with what the numbers mean in finance. The Financial Data Science course introduces these questions through worked examples. Read each chapter for the financial argument, then run the lab to see what changes when you alter an assumption or test a result on later data. Each lab has an **Open in Colab** link and can be used without a Bloomberg Terminal. [Financial Data Science](https://financialdatascience.co.uk/)

1. **Measure a return.** Calculate monthly returns from UK bank share prices and explain which banks are missing from the sample. [Data and measurement chapter](https://financialdatascience.co.uk/chapters/02_data_measurement.html) · [UK banks lab](https://financialdatascience.co.uk/labs/lab02_survivorship_bias.html)
2. **Forecast in time order.** Compare a model for daily returns with a simple benchmark using observations that come after those used to fit the model. [Time series chapter](https://financialdatascience.co.uk/chapters/time_series.html) · [Time series lab](https://financialdatascience.co.uk/labs/lab03_time_series.html)
3. **Build a portfolio.** Use four exchange-traded funds to study how estimated returns and risks shape an allocation, then see how that allocation fares on later data. [Portfolio optimisation chapter](https://financialdatascience.co.uk/chapters/04_robo_advisors_algorithmic_investment.html) · [Robo-advisers lab](https://financialdatascience.co.uk/labs/lab05_robo.html)
4. **Explain portfolio performance.** Use factor regressions to ask how much of a portfolio's return can be explained by common sources of risk and how precisely you can estimate the return left unexplained. [Factor investing chapter](https://financialdatascience.co.uk/chapters/09_factor_investing.html) · [Factor investing lab](https://financialdatascience.co.uk/labs/lab09_factor_replication.html)
5. **Test a trading rule.** Simulate strategies with no predictive edge and see how impressive the best historical result can look after a search. [Backtesting and validation chapter](https://financialdatascience.co.uk/chapters/10_backtesting_production_ml.html) · [Backtesting and validation lab](https://financialdatascience.co.uk/labs/lab10_backtesting.html)

Work through the pairs that fill gaps in your preparation. Then use the econometrics readings to study the methods you have just used, and the market microstructure readings to learn how order placement, liquidity and trading costs affect the strategies you test. [Econometric methods](resources/econometric-methods.md) · [Market microstructure](resources/market-microstructure.md)

## Working through the curriculum

The two routes lead to the same programme of independent study. The preparation checklist covers undergraduate multivariate calculus, linear algebra and probability, together with regression, hypothesis testing and maximum likelihood. It also covers Python, asset pricing, portfolio theory and the basics of derivatives and market structure. Use it to identify what to study next. [Quick start](QUICKSTART.md) · [Curriculum](CURRICULUM.md)

When you read a paper, reproduce one result and keep a record of the data, assumptions and choices needed to obtain it. Change one choice at a time and explain what the result can still support. The readings give priority to work whose methods and evidence you can examine in this way.

## Repository guide

- [Resources](resources/) contains annotated readings on mathematics, econometrics, market microstructure, programming and advanced topics.
- [Papers](papers/) lists essential research papers with notes on what to read.
- [Implementations](implementations/) and [exercises](exercises/) are under development. Treat code there as experimental until its documentation says it has been tested.

## Contributing and feedback

Suggest additions through GitHub issues. Explain what the resource adds, what evidence supports its use and where it fits in the curriculum. [Contribution guide](CONTRIBUTING.md)

## Citation

Use this citation when you draw on the curriculum in teaching or research.

```
Quinn, B. (2025). Quantitative Finance Foundations.
Centre for Finance and Responsible Technology,
Ulster University Business School.
https://github.com/quinfer/quantitative-finance-foundations
```

## Institutional Context

Professor Barry Quinn maintains this curriculum at the Centre for Finance and Responsible Technology, Ulster University Business School. The curriculum complements the Centre's programmes in quantitative finance and responsible technology. We welcome collaboration with other institutions developing similar programmes.

## Licence

This work is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). You are free to share and adapt this material with appropriate attribution.

## Acknowledgements

This curriculum builds on teaching experience, research collaborations, and conversations with colleagues across academia and industry. Particular thanks to students whose questions revealed gaps in existing resources and motivated clearer exposition of quantitative methods.
