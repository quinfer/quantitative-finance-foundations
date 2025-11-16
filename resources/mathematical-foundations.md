# Mathematical Foundations for Quantitative Finance

## Purpose and Scope

Mathematical preparation enables formal reasoning about uncertainty, dynamics, and optimisation—core concerns in quantitative finance. This differs from mathematics for pure theory: we need sufficient rigour to avoid errors whilst maintaining focus on application and implementation.

The goal is not comprehensive mastery of mathematical analysis or measure theory, but rather developing working knowledge of probability, linear algebra, calculus, and optimisation sufficient to understand quantitative methods, implement them correctly, and reason about their properties.

## Prerequisites

Before engaging with these resources:

- **Undergraduate calculus**: Derivatives, integrals, Taylor series, multivariate optimisation

- **Linear algebra basics**: Matrix operations, determinants, solving linear systems

- **Probability fundamentals**: Sample spaces, random variables, expectation, variance

If these prerequisites aren't met, address gaps first. Khan Academy, MIT OpenCourseWare, and Gilbert Strang's *Introduction to Linear Algebra* provide accessible foundations.

## Core Resources

### Stochastic Calculus for Finance II (Steven Shreve)

**What it provides**: Rigorous but accessible treatment of continuous-time stochastic processes, Brownian motion, stochastic calculus, and applications to derivatives pricing. This is the standard text for mathematical finance preparation.

**How to use it**: Work through Chapters 1-4 carefully:
- Chapter 1: General Probability Theory (measure-theoretic foundations)
- Chapter 2: Information and Conditioning (filtrations, conditional expectation)
- Chapter 3: Brownian Motion (construction, properties, martingale property)
- Chapter 4: Stochastic Calculus (Itô's lemma, stochastic differential equations)

Don't expect immediate mastery of all measure-theoretic details. Focus on developing intuition for concepts whilst accepting some formalism remains abstract initially. The measure theory becomes clearer with repeated exposure and implementation.

**Implementation connections**: After Chapter 4, implement geometric Brownian motion simulation and pricing of European options. After Chapter 5, implement binomial tree methods and verify convergence to Black-Scholes. These implementations crystallise abstract concepts.

**Common difficulties**: Students often struggle with measure-theoretic probability (Chapter 1) and conditional expectation (Chapter 2). Don't get stuck here—proceed to Brownian motion (Chapter 3) where concepts become more concrete, then return to earlier chapters as needed.

**Complementary resource**: *Stochastic Calculus for Finance I* (Shreve) covers discrete-time models and provides gentler introduction if continuous-time material proves initially overwhelming.

### Linear Algebra and Its Applications (Gilbert Strang)

**What it provides**: Intuitive yet rigorous treatment of linear algebra emphasising geometric understanding and applications. Strang focuses on concepts that actually matter for applications rather than comprehensive theoretical coverage.

**How to use it**: Prioritise chapters directly relevant to quantitative finance:
- Chapter 1: Introduction to Vectors (inner products, projections)
- Chapter 2: Solving Linear Equations (elimination, matrix factorisation)
- Chapter 3: Vector Spaces and Subspaces (fundamental subspaces, rank)
- Chapter 6: Eigenvalues and Eigenvectors (diagonalisation, applications)
- Chapter 7: The Singular Value Decomposition (SVD and applications)

The eigenvalue and SVD chapters prove particularly important for portfolio optimisation, principal component analysis, and covariance matrix estimation.

**Implementation connections**: Implement PCA from scratch using eigenvalue decomposition. Compare your implementation to sklearn. Implement portfolio optimisation using matrix notation. Build covariance matrix from historical returns and investigate numerical stability issues.

**Why this matters**: Nearly all portfolio optimisation, risk modelling, and factor analysis involves matrix operations. Poor understanding of linear algebra leads to implementations that fail mysteriously when covariance matrices become ill-conditioned or data is nearly collinear.

**Complementary resource**: Strang's *Introduction to Linear Algebra* provides gentler treatment if applications version proves too dense. His MIT OpenCourseWare lectures (available free) offer excellent video supplement.

### A Probability Path (Sidney Resnick)

**What it provides**: Rigorous probability theory without excessive measure-theoretic formalism. Resnick develops intuition alongside formal definitions, making abstract concepts accessible whilst maintaining mathematical precision.

**How to use it**: Focus on Chapters 1-5:
- Chapter 1: Sets and Events (basic probability spaces)
- Chapter 2: Random Variables and Distributions (rigorous treatment)
- Chapter 3: Transforms and Convergence (characteristic functions, generating functions)
- Chapter 4: Sums and Symmetry (laws of large numbers, central limit theorem)
- Chapter 5: Conditioning and Martingales (conditional expectation, martingale concepts)

The convergence concepts (Chapter 4) and conditioning (Chapter 5) prove essential for understanding asymptotic theory in econometrics and properties of trading strategies.

**Implementation connections**: Implement Monte Carlo simulation illustrating different convergence concepts. Verify law of large numbers and central limit theorem empirically. Implement martingale betting strategies and verify why they fail (martingale property doesn't guarantee profit).

**Common difficulties**: Conditional expectation (Chapter 5) confuses many students initially. The key insight: conditional expectation is itself a random variable (a function of conditioning information), not a number. Work through examples systematically before attempting abstract theory.

**Why this matters**: Much of quantitative finance involves reasoning under uncertainty and conditioning on information. Rigorous probability theory prevents common errors like confusing conditional and unconditional expectations or misapplying limit theorems.

## Supplementary Resources

### Numerical Methods in Finance and Economics (Paolo Brandimarte)

**Purpose**: Bridges mathematical concepts and computational implementation, showing how continuous-time models and abstract optimisation problems translate into algorithms.

**Key chapters**:
- Chapter 3: Numerical Linear Algebra (solving systems, eigenvalue problems)
- Chapter 6: Numerical Methods for ODEs and SDEs (simulating stochastic processes)
- Chapter 8: Optimization Models (numerical methods for portfolio optimisation)
- Chapter 11: An Introduction to Simulation (Monte Carlo methods)

**When to use**: After developing mathematical foundations, work through this text whilst implementing econometric and portfolio methods. It addresses practical questions glossed over in theoretical treatments: How to actually solve these equations? What causes numerical instability? How to verify implementations are correct?

### Probability and Statistics for Finance (Svetlozar Rachev et al.)

**Purpose**: Comprehensive treatment of probability and statistics specifically for finance applications, with extensive examples from derivatives pricing, risk management, and portfolio theory.

**Distinctive features**: Covers distributions common in finance (stable distributions, generalised hyperbolic distributions) and statistical methods for heavy-tailed data. More applied than Resnick, less theoretical.

**When to use**: As reference when encountering specific probability distributions or statistical methods in finance contexts. Not necessary to work through comprehensively, but useful for looking up properties of specific distributions and estimation methods.

### Mathematical Statistics (Jun Shao)

**Purpose**: Rigorous treatment of statistical theory including decision theory, hypothesis testing, and asymptotic theory. More comprehensive than typically needed for quantitative finance, but invaluable for understanding econometric theory.

**Key sections**:
- Chapters 2-3: Sufficient statistics and point estimation (foundations for maximum likelihood)
- Chapter 5: Hypothesis testing (understanding power, size, p-values rigorously)
- Chapter 7: Asymptotic theory (understanding consistency, asymptotic normality)

**When to use**: Reference when encountering statistical concepts in econometrics texts and wanting rigorous foundations. Not appropriate for initial learning—too abstract without applications.

## Common Pitfalls and How to Address Them

### Pitfall 1: Attempting comprehensive mastery before implementation

**Symptom**: Spending months working through probability theory before writing any code.

**Problem**: Mathematical concepts remain abstract without implementation experience. You don't truly understand stochastic processes until you've simulated them and debugged your code.

**Solution**: Implement simple versions concurrently with theoretical study. After learning about Brownian motion, simulate it. After studying martingales, implement examples. Theory and practice develop together.

### Pitfall 2: Using libraries without understanding underlying mathematics

**Symptom**: Calls `numpy.linalg.lstsq()` without understanding what least squares actually computes or why it might fail.

**Problem**: When implementations fail or produce unexpected results, you can't diagnose problems or determine whether issues are mathematical, computational, or data-related.

**Solution**: Implement simple cases from scratch before using sophisticated libraries. Solve 2x2 linear system by hand, then write Python code, then compare to numpy. This develops intuition for what libraries actually do.

### Pitfall 3: Ignoring numerical stability and computational considerations

**Symptom**: Implementations that work on toy examples but fail on real data due to ill-conditioned matrices, overflow, or underflow.

**Problem**: Mathematical theory assumes exact arithmetic. Computers use finite-precision floating point arithmetic where naïve implementations fail.

**Solution**: Study Brandimarte's numerical methods text alongside theoretical treatments. Learn to recognise when covariance matrices become ill-conditioned, when likelihood functions encounter overflow, when iterative algorithms fail to converge.

### Pitfall 4: Confusing measure-theoretic formalism with practical understanding

**Symptom**: Can recite definitions of σ-algebras but can't explain what conditional expectation actually means or compute it for specific examples.

**Problem**: Measure theory provides rigorous foundations but doesn't substitute for intuition and practical facility with probability concepts.

**Solution**: Always work concrete examples alongside abstract theory. For every theorem, construct examples satisfying and violating conditions. Verify results through simulation. Mathematical rigour and practical understanding develop together.

## Integration with Other Topics

Mathematical foundations support all subsequent work:

**Econometric methods** require probability theory (convergence concepts, conditional expectation), linear algebra (matrix formulations of regression and GMM), and optimisation (maximum likelihood, GMM estimation).

**Portfolio optimisation** requires linear algebra (matrix formulations, quadratic forms), optimisation theory (Lagrange multipliers, KKT conditions), and probability (expected utility, risk measures).

**Derivatives pricing** requires stochastic calculus (Itô's lemma, Girsanov theorem), partial differential equations (Black-Scholes PDE), and numerical methods (finite differences, Monte Carlo).

**Machine learning** requires linear algebra (SVD, eigenvalue methods), optimisation (gradient descent, convex optimisation), and probability (Bayesian inference, generalisation bounds).

Rather than attempting complete mastery before proceeding, develop mathematical foundations concurrently with applications. Return to mathematical texts when encountering gaps in understanding during implementation.

## Implementation Exercises

### Exercise 1: Simulating Stochastic Processes

Implement geometric Brownian motion simulation following Shreve Chapter 4:

```python
def gbm_path(S0, mu, sigma, T, steps):
    """
    Simulate geometric Brownian motion path.
    
    Parameters:
    S0: Initial value
    mu: Drift parameter
    sigma: Volatility parameter
    T: Time horizon
    steps: Number of time steps
    
    Returns:
    Array of simulated values
    """
    # Your implementation here
    pass
```

Verify that:
- Simulated paths have correct expected terminal value: E[S_T] = S0 * exp(mu * T)
- Simulated paths have correct variance: Var[log(S_T)] = sigma^2 * T
- Distribution of log returns is approximately normal

Investigate how results depend on number of steps. Plot sample paths and terminal distribution.

### Exercise 2: Principal Component Analysis from Scratch

Implement PCA using eigenvalue decomposition:

```python
def pca_eigenvalue(X, n_components):
    """
    Principal component analysis using eigenvalue decomposition.
    
    Parameters:
    X: Data matrix (n_samples, n_features)
    n_components: Number of components to return
    
    Returns:
    components: Principal component vectors
    explained_variance: Variance explained by each component
    transformed_data: Data projected onto principal components
    """
    # Your implementation here
    pass
```

Apply to equity returns data:
- Compute correlation matrix of returns
- Find eigenvalues and eigenvectors
- Determine how many components explain 90% of variance
- Compare your implementation to sklearn.decomposition.PCA
- Investigate what happens when covariance matrix is nearly singular

### Exercise 3: Portfolio Optimisation Using Matrix Notation

Implement mean-variance portfolio optimisation:

```python
def markowitz_portfolio(mu, Sigma, target_return=None, risk_free_rate=0):
    """
    Mean-variance portfolio optimisation.
    
    Parameters:
    mu: Expected returns (n_assets,)
    Sigma: Covariance matrix (n_assets, n_assets)
    target_return: Target portfolio return (optional)
    risk_free_rate: Risk-free rate for Sharpe ratio maximisation
    
    Returns:
    weights: Optimal portfolio weights
    portfolio_return: Expected return
    portfolio_std: Portfolio standard deviation
    """
    # Your implementation here
    pass
```

Test on historical equity returns:
- Compute sample mean and covariance from data
- Find minimum variance portfolio
- Compute efficient frontier
- Compare long-only and long-short solutions
- Investigate sensitivity to estimation error in mu and Sigma
- Document when optimisation fails due to numerical issues

### Exercise 4: Monte Carlo Convergence

Verify law of large numbers and central limit theorem empirically:

```python
def monte_carlo_convergence(distribution, n_samples_range):
    """
    Demonstrate convergence properties via Monte Carlo.
    
    Parameters:
    distribution: Function that generates random samples
    n_samples_range: List of sample sizes to test
    
    Returns:
    results: DataFrame showing convergence of sample mean to population mean
    """
    # Your implementation here
    pass
```

Test with different distributions:
- Normal distribution
- Student's t with different degrees of freedom (demonstrates slow convergence with heavy tails)
- Cauchy distribution (no finite mean—sample average doesn't converge)

Visualise convergence rates. Verify that for distributions with finite variance, standard error decreases at rate 1/sqrt(n).

## Assessment Criteria

You have adequate mathematical preparation when you can:

1. **Simulate and reason about stochastic processes**: Implement Brownian motion, geometric Brownian motion, Ornstein-Uhlenbeck process. Verify properties through simulation. Explain why certain properties hold.

2. **Manipulate matrices confidently**: Implement operations using matrix notation. Recognise when covariance matrices become ill-conditioned. Apply eigenvalue and SVD methods appropriately.

3. **Apply probability theory to financial problems**: Compute expectations and variances for portfolio returns. Apply conditional expectation correctly. Understand martingale property and implications.

4. **Verify mathematical results numerically**: When encountering theoretical result, construct simulation verifying it holds. When result doesn't hold, identify violated assumptions.

5. **Diagnose implementation problems**: When numerical methods fail, identify whether issue is mathematical (problem is ill-posed), computational (numerical instability), or coding error.

If you can accomplish these tasks, mathematical foundations are adequate for proceeding to econometric methods and implementation. If not, identify specific gaps and address them before continuing.

## Further Reading

For students wanting deeper mathematical preparation:

**Probability Theory**: *Probability: Theory and Examples* (Durrett) provides comprehensive measure-theoretic treatment. More advanced than needed for most applications, but valuable reference.

**Stochastic Processes**: *Brownian Motion and Stochastic Calculus* (Karatzas & Shreve) is definitive rigorous treatment. Appropriate for PhD students specialising in mathematical finance, excessive for most practitioners.

**Linear Algebra**: *Matrix Computations* (Golub & Van Loan) covers numerical linear algebra comprehensively. Essential for understanding computational issues in portfolio optimisation and factor models.

**Optimisation**: *Convex Optimization* (Boyd & Vandenberghe) provides rigorous foundations. Key results (KKT conditions, duality) appear throughout portfolio theory and risk management.

These advanced resources become valuable after establishing foundations, particularly when encountering specific technical problems requiring deeper theoretical understanding.

---

*This resource reflects teaching experience at Ulster University Business School's Centre for Finance and Responsible Technology. Questions or suggestions welcome via repository issues.*

