# AGENTS.md

## Cursor Cloud specific instructions

This is an educational curriculum repository (markdown docs + one utility script). There is no application to "build" or "serve" — the runnable code is Python scripts and Jupyter notebooks.

### Tech stack
- **Python 3.12** (system), all dependencies installed via `pip` (see `environment.yml` for the canonical list).
- Key packages: `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`, `jupyter`, `statsmodels`, `requests`, `arch`, `yfinance`.

### Running code
- The only checked-in script is `scripts/find_dois.py` — an **interactive CLI** that queries the Crossref API. It requires `papers/bibliography.csv` as input and prompts the user for each match, so it cannot be run non-interactively without modification.
- Jupyter is available via `python3 -m jupyter notebook` or `python3 -m jupyter lab` (the `jupyter` binary may not be on `PATH`; always invoke via `python3 -m`).
- Financial data fetching (`yfinance`) requires network access.

### Linting / testing
- No test suite or linter configuration exists in this repo. If you add Python code, follow PEP 8 and use type hints per `CONTRIBUTING.md`.

### Gotchas
- `environment.yml` targets conda with Python 3.11, but the cloud VM uses Python 3.12 with pip. All listed packages install and work correctly on 3.12.
- There are no pre-commit hooks or CI pipelines configured.
