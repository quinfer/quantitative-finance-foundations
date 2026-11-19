# Quick start

Begin with a small return calculation you can check by hand. Take two consecutive adjusted closing prices, divide the second by the first and subtract one. Check what the data provider adjusts for, then calculate the same return in Python. Write down what the number measures and which dates it covers. This is the first step towards comparing portfolios whose returns you can explain.

## Choose your starting point

- **If you study finance**, use a familiar question about returns or portfolio risk to practise working with data in Python. Start with the first portfolio task and use the programming guide as you work. [Curriculum foundations](CURRICULUM.md#phase-1-foundations-months-13) · [Programming practices](resources/programming-practices.md)
- **If you study computer science**, start with the bank returns lab. It asks you to explain which banks appear in the sample and why others are missing. Continue with the chapter and lab pairs that fill gaps in your finance preparation. [Computer science route](README.md#if-you-study-computer-science)

Use this list to decide what to review alongside your first task:

| Preparation | What to check |
| --- | --- |
| Mathematics | Can you work with vectors and matrices, take derivatives and interpret an expectation or variance? |
| Statistics | Can you interpret a regression coefficient and a confidence interval? Review maximum likelihood before estimating a volatility model. |
| Python | Can you load a CSV with pandas, sort observations by date and write a function you can check on a small example? |
| Finance | Can you explain a return, a portfolio weight and the purpose of a benchmark? Review derivatives and how orders become trades as you reach tasks that use them. |

## Set up Python

The linked Financial Data Science labs have Colab notebooks. For local work, use the environment in this repository.

```bash
git clone https://github.com/quinfer/quantitative-finance-foundations.git
cd quantitative-finance-foundations
conda env create -f environment.yml
conda activate qf-foundations
jupyter notebook
```

Keep your analysis in a separate Git repository. Record the data source and retrieval date, the commands needed to rerun the analysis and the versions you actually used. [Environment specification](environment.yml) · [Version control and testing](resources/programming-practices.md#version-control-with-git)

## Your first week

1. **Build a return series.** Choose a few assets with comparable price data. Record how the file handles dividends, splits, missing prices and assets that left the sample. Check one return by hand.
2. **Compare portfolios.** Calculate the returns of an equal-weighted portfolio and a second portfolio with specified weights. Use weights known before the return period. Plot their cumulative returns and explain one difference between them.
3. **Examine volatility.** Plot rolling volatility, state the window in trading days and explain how an unusually large return affects successive estimates. Read Tsay alongside the calculation. [Time series reading guide](resources/econometric-methods.md#analysis-of-financial-time-series-ruey-s-tsay)
4. **Rerun your work.** Start from the original input and check that the tables and figures reproduce. Record one decision that could change your conclusion.

Then extend the first portfolio calculation into Task 1. Move to portfolio optimisation when you can explain how your weights and data produced the return series. Use the remaining phases to plan your study. [Curriculum](CURRICULUM.md)
