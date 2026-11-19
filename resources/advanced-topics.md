# Advanced Topics in Quantitative Finance

A better return forecast can lead to a worse strategy if it trades too often. To evaluate a new signal, follow it from the data available at the decision date through portfolio weights, trading costs and later outcomes. Use the readings below to decide which comparison can tell you whether the signal adds value. [Advanced applications in the curriculum](../CURRICULUM.md#phase-4-advanced-applications-months-1012)

## Preparation

Begin here once you can build a simple factor or forecasting benchmark, evaluate it on later observations and explain how execution affects the result. Use the [econometrics guide](econometric-methods.md) to review validation or the [market microstructure guide](market-microstructure.md) to review implementation costs.

## Core Resources

### Advances in Financial Machine Learning (Marcos López de Prado)

Choose the chapters that address your design. Start with sample weights and cross-validation if outcome windows overlap. Use the backtesting chapters to compare ways of evaluating a strategy. [Publisher's contents](https://www.wiley.com/en-au/Advances%2Bin%2BFinancial%2BMachine%2BLearning-p-9781119482086)

**Chapter 1: Financial Machine Learning as a Distinct Subject**
- Why finance differs from other ML applications
- Common mistakes and how to avoid them

**Chapter 2: Financial Data Structures**
- Tick, volume, and dollar bars
- Information-driven sampling
- Why standard time bars often suboptimal

**Chapter 3: Labeling**
- Triple-barrier method
- Fixed-time horizon problems
- Meta-labeling approach

**Chapter 4: Sample Weights**
- Addressing sample overlap
- Uniqueness and decay
- Implementation details

**Chapter 7: Cross-Validation in Finance**
- Why standard k-fold CV fails
- Purging and embargo for overlapping or nearby observations

**Chapter 10: Bet Sizing**
- From probability to position sizing
- Dynamic bet sizing
- Managing trading frequency

**Chapter 11: The Dangers of Backtesting**
- Backtest overfitting
- Probability of backtest overfitting
- How to backtest properly

**Chapter 12: Backtesting through Cross-Validation**
- Walk-forward analysis and cross-validation
- Combinatorial purged cross-validation

Start with a time-ordered comparison. If return labels overlap the evaluation window, compare the result when you exclude those training labels. Chapter 7 discusses purging and embargo. Chapter 12 discusses combinatorial purged cross-validation. Bailey and colleagues estimate the probability of backtest overfitting by comparing the rankings of candidate strategies across complementary partitions. Use the annotated papers and course lab to distinguish those questions. [Backtest overfitting readings](../papers/essential-readings.md#42-backtest-overfitting-and-cv) · [Backtesting lab](https://financialdatascience.co.uk/labs/lab10_backtesting.html)

**Complementary resource**: López de Prado's papers provide additional detail on specific topics. His website includes code examples and presentations.

### Machine Learning for Asset Managers (Marcos López de Prado)

**What it provides**: Shorter, more accessible treatment focusing on portfolio construction applications of machine learning.

**Key topics**:
- Feature importance and overfitting
- Covariance matrix estimation with denoising
- Distance metrics for portfolio diversification
- Machine learning-based portfolio construction

**Why this matters**: Bridges machine learning and portfolio theory. Shows how ML techniques improve covariance estimation, identify diversifying assets, and enhance portfolio construction.

**When to use**: After López de Prado's main text or as more accessible introduction to his methods.

### Asset Management: A Systematic Approach to Factor Investing (Andrew Ang)

**What it provides**: Comprehensive treatment of factor investing from practitioner perspective, covering equity factors, fixed income factors, alternative risk premia, and portfolio construction.

**How to use it**: Work through systematically:

**Part I: Factors and Investors**
- What are factors and why they matter
- Factor theory: risk versus behavioral explanations
- Factor performance evaluation

**Part II: Equity Factors**
- Value, momentum, carry, defensive, and other factors
- Empirical evidence and theoretical foundations
- Implementation considerations

**Part III: Macroeconomic Factors**
- Economic growth, inflation, volatility, and liquidity factors
- Asset allocation using macro factors
- Tactical versus strategic exposure

**Part IV: Creating Factor Portfolios**
- Factor definition and portfolio construction
- Long-short versus long-only implementation
- Transaction costs and turnover management

**Part V: Measuring and Managing Factor Portfolios**
- Performance attribution
- Risk management
- Combining factors efficiently

**Why this matters**: Factor investing represents dominant approach in systematic equity management. Understanding what factors exist, why they might persist, and how to implement them proves essential for quantitative portfolio management.

**Implementation connections**: Construct factor portfolios from characteristics. Implement long-short and long-only versions. Analyze factor performance across time periods and geographies. Build multi-factor portfolios with optimal factor allocations.

**Critical perspective**: Not all published factors represent genuine risk premia or behavioral biases. Many reflect data mining. Focus on well-established factors (value, momentum, quality, low volatility) with strong theoretical foundations and robust empirical support.

### Machine Learning in Finance: From Theory to Practice (Dixon, Halperin & Bilokon)

**What it provides**: Rigorous treatment of modern machine learning methods applied to finance, covering supervised learning, reinforcement learning, and natural language processing.

**Key sections**:

**Part I: Supervised Learning**
- Linear models and regularisation
- Tree-based methods and ensemble approaches
- Neural networks and deep learning

**Part II: Sequential Learning and Reinforcement Learning**
- Markov decision processes
- Q-learning and policy gradient methods
- Applications to trading and execution

**Part III: Natural Language Processing**
- Text preprocessing and representation
- Sentiment analysis for trading signals
- Event extraction from news

**Why this matters**: Covers modern ML methods with finance-specific applications and considerations. More technically rigorous than many practitioner-oriented texts.

**When to use**: After establishing foundations in both finance and machine learning. Not appropriate for first exposure to either field—assumes sophistication in both.

### Empirical Asset Pricing: The Cross Section of Stock Returns (Bali, Engle & Murray)

**What it provides**: Comprehensive empirical treatment of cross-sectional asset pricing, covering factors, characteristics, anomalies, and testing methodologies.

**Key topics**:
- CAPM, three-factor, and multi-factor models
- Momentum, value, and other anomalies
- Liquidity and other characteristics
- Testing methodology and multiple testing

**Why this matters**: Understanding asset pricing literature essential for evaluating factor strategies. Distinguishes robust findings from spurious patterns. Addresses multiple testing and data mining issues.

**When to use**: Reference for understanding specific factors or anomalies. Not necessary to work through comprehensively, but valuable for grounding factor strategies in academic literature.

## Supplementary Resources

### Big Data and Machine Learning in Quantitative Investment (Jurczenko, ed.)

**Purpose**: Collection of papers applying modern data science methods to quantitative investment, covering alternative data, dimension reduction, and ensemble methods.

**Key chapters**:
- Alternative data sources and preprocessing
- Elastic net and Lasso for return prediction
- Random forests and gradient boosting
- Autoencoders for feature extraction

**When to use**: Reference for specific methods or alternative data applications. Variable quality across chapters—some rigorous, some promotional.

### Quantitative Momentum (Wesley Gray & Jack Vogel)

**Purpose**: Practitioner treatment of momentum strategies, covering implementation, enhancements, and portfolio construction.

**Key topics**:
- Momentum measurement alternatives
- Interaction with other factors
- Risk management for momentum
- International momentum

**When to use**: When implementing momentum strategies. More practitioner-oriented than academic treatments, with attention to implementation details.

### Expected Returns (Antti Ilmanen)

**Purpose**: Comprehensive treatment of return sources across asset classes from practitioner-researcher at AQR Capital Management.

**Key topics**:
- Historical returns across asset classes
- Return sources: static premia, dynamic strategies, alpha
- Value and momentum everywhere
- Carry trades across markets

**When to use**: Reference for understanding return sources across asset classes. Broader than equity focus, covering fixed income, commodities, currencies, and alternatives.

### Efficiently Inefficient (Lasse Heje Pedersen)

**Purpose**: Accessible treatment of market efficiency and limits to arbitrage, covering factor investing, high-frequency trading, and hedge fund strategies.

**Key topics**:
- Market efficiency and inefficiency
- Value, momentum, and carry strategies
- High-frequency market making
- Hedge fund performance

**When to use**: Accessible introduction to systematic strategies across asset classes. Less technical than academic treatments but more rigorous than popular finance books.

## Alternative Data in Finance

Alternative data—satellite imagery, credit card transactions, web scraping, social media sentiment—increasingly used in quantitative strategies. Key considerations:

### Data Quality and Validation

**Survivorship and backfill bias**: Many alternative data vendors provide "history" that wasn't actually available in real time. Always verify data availability dates.

**Signal stability**: Does relationship persist out-of-sample? Alternative data often undergoes structural breaks as markets adapt.

**Legal and ethical considerations**: Not all data acquisition methods are legal or ethical. Understand data provenance and usage restrictions.

### Implementation Challenges

**Data preprocessing**: Alternative data often require substantial cleaning, normalisation, and feature engineering before being useful.

**Latency considerations**: How quickly does data become available? Historical relationships may not be exploitable with realistic latency.

**Cost-benefit analysis**: Alternative data can be expensive. Does signal strength justify cost? Can simpler, cheaper data achieve similar results?

### Evaluation Standards

Apply same rigour as traditional factors:
- Proper out-of-sample testing
- Realistic transaction costs
- Multiple testing adjustment
- Economic rationale for why signal might persist

Avoid promotional claims from data vendors. Demand empirical evidence with proper validation.

## Decide what a better forecast is worth

Set the benchmark and time-ordered evaluation before tuning. Record the features, models and parameter combinations you try. If you report the winner of a strategy search, explain the search behind that result and check how often its ranking changes across partitions. Keep that diagnosis distinct from the evaluation of a forward trading rule.

Report both forecast performance and the performance of the portfolio that uses it. An improvement in prediction may have little economic value after turnover and trading costs. Compare a simple rule with the same investable universe and cost assumptions. Show how results vary by period and how they change under a different cost or market-impact estimate.

Interpret the result in terms of the financial question. State when each predictor was available and why it could matter. Explain which patterns you can document and which economic mechanisms would need a different research design to test. [Essential readings](../papers/essential-readings.md)

## Implementation Projects

### Project 1: Multi-Factor Portfolio with ML Enhancement

Build systematic equity strategy combining traditional factors with machine learning:

**Components**:
- Collect equity characteristics (value, momentum, quality, size, volatility)
- Construct factor portfolios using traditional approaches
- Apply machine learning to predict returns from characteristics
- Implement proper cross-validation with purging and embargo
- Combine predictions with traditional factors
- Optimize portfolio with transaction cost awareness
- Conduct rigorous backtest with realistic assumptions

**Validation**:
- Out-of-sample performance vs. benchmarks
- Turnover and transaction cost analysis
- Factor exposure analysis
- Sensitivity to hyperparameters
- Performance across time periods

### Project 2: Alternative Data Integration

Integrate alternative data source into quantitative strategy:

**Steps**:
- Identify alternative data source (sentiment, web traffic, satellite, etc.)
- Validate data quality and availability dates
- Engineer features from raw data
- Test predictive power out-of-sample
- Evaluate economic significance after transaction costs
- Compare to traditional data sources
- Assess cost-benefit tradeoff

**Considerations**:
- Legal and ethical data usage
- Data preprocessing and cleaning
- Signal decay and adaptation
- Combination with traditional signals

### Project 3: Reinforcement Learning for Execution

Apply reinforcement learning to optimal execution problem:

**Components**:
- Define state space (inventory, spread, volatility, time remaining)
- Define action space (order sizes and types)
- Specify reward function (implementation shortfall, risk-adjusted cost)
- Implement Q-learning or policy gradient method
- Train using historical order book data or simulation
- Compare to Almgren-Chriss and heuristic strategies
- Evaluate on held-out data

**Validation**:
- Out-of-sample execution cost vs. benchmarks
- Robustness to market conditions
- Interpretability of learned policy
- Computational requirements for real-time use

## Assessment Criteria

You have adequate preparation in advanced topics when you can:

1. **Apply ML to finance correctly**: Implement proper cross-validation for time series. Avoid lookahead bias. Account for transaction costs in model evaluation.

2. **Evaluate factor strategies critically**: Distinguish robust factors from data mining. Understand economic rationale. Implement with attention to transaction costs and capacity.

3. **Work with alternative data**: Evaluate data quality. Engineer features appropriately. Assess economic value relative to cost.

4. **Integrate multiple methods**: Combine econometric, machine learning, and microstructure methods coherently. Understand when each approach adds value.

5. **Maintain critical perspective**: Question published results. Test robustness. Identify limitations. Distinguish marketing from rigorous research.

6. **Build production-quality implementations**: Create reproducible, tested, documented research pipelines suitable for live trading or institutional research.

If you can accomplish these tasks, you have capability for advanced quantitative research and strategy development. Continue learning from research papers, attending conferences, and implementing new methods as field evolves.

## Research Frontiers

Current active research areas (evaluate critically—not all will prove valuable):

**Causal machine learning**: Combining causal inference from econometrics with prediction from machine learning. Promising for strategy development where causal understanding matters.

**Deep learning for time series**: Attention mechanisms, transformers, and other architectures. Mixed evidence in finance—sometimes helps, often doesn't justify complexity.

**Reinforcement learning**: Applications to trading, execution, and portfolio construction. Theoretically appealing, practically challenging due to sample efficiency and stability issues.

**Explainable AI**: Making black-box models interpretable. Valuable for understanding what drives model predictions and identifying when models may fail.

**ESG integration**: Incorporating environmental, social, and governance factors. Active research on whether ESG predicts returns or represents separate investor preferences.

**Cryptocurrency and DeFi**: Unique features (continuous trading, on-chain data, MEV) create new opportunities and challenges. Market maturity still developing.

Approach research frontiers with skepticism. Most "innovations" prove incremental or fail under scrutiny. Focus on methods with solid theoretical foundations and robust empirical validation.

## Further Reading

For continued development:

**Academic journals**: JF, JFE, RFS, JFQA for top-tier research. QF, JPM for practitioner-oriented work.

**Working papers**: SSRN, arXiv for recent research before publication. Variable quality—evaluate critically.

**Conferences**: AFA, WFA, FMA for academic research. CQA, QuantCon for practitioner focus.

**Industry publications**: AQR, Research Affiliates, and other systematic managers publish quality research.

Continuous learning essential. Quantitative finance evolves as markets change, data becomes available, and methods develop. Foundations here enable adaptation and continued growth.

---

*This resource reflects teaching experience at Ulster University Business School's Centre for Finance and Responsible Technology.*

