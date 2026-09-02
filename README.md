# timely-beliefs — Probabilistic Time-Series Modeling & MultiIndex Metadata Retention

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-MultiIndex%20DataFrames-orange.svg)](https://pandas.pydata.org/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red.svg)](https://www.sqlalchemy.org/)
[![Open Source](https://img.shields.io/badge/Open%20Source-Merged%20Contributions-green.svg)](https://github.com/SeitaBV/timely-beliefs)

---

## 📌 Executive Summary & Open Source Contributions

**timely-beliefs** is an open-source probabilistic time-series modeling framework designed to track uncertainties, historical sensor observations, probabilistic forecasts, and belief formations over time.

This repository features **Upstream Contributions** authored by **Taran Mamidala** to [`SeitaBV/timely-beliefs`](https://github.com/SeitaBV/timely-beliefs).

---

## 🚀 Key Upstream Engineering Contributions

### 1. Strict Total Ordering for `BeliefSource` ([PR #245](https://github.com/SeitaBV/timely-beliefs/pull/245) - Merged)
- Resolved an issue where non-total `__lt__` comparisons on `BeliefSource` caused ambiguous sorting during Pandas MultiIndex alignment, resulting in silent `NaN` generation.
- Implemented deterministic `(str(self), id(self)) < (str(other), id(other))` tiebreaker while preserving default SQLAlchemy identity-based `__eq__` and `__hash__`.

### 2. `event_resolution` Retention across DataFrame & Series Conversions ([PR #247](https://github.com/SeitaBV/timely-beliefs/pull/247))
- Fixed metadata loss when converting between `BeliefsDataFrame` and `BeliefsSeries`, ensuring sensor references and `event_resolution` timedelta headers are preserved across slicing and constructor delegations.

---

## 📂 Repository Structure

```
timely-beliefs-data-models/
├── src/timely_beliefs_models/
│   ├── sources.py                   # BeliefSource class with total ordering
│   └── dataframe_utils.py           # MultiIndex DataFrame/Series conversion utilities
├── tests/                           # Regression and metadata retention test suites
└── README.md                        # Documentation
```

---

## 👨‍💻 Author & Contributor
- **Author:** Taran Mamidala
- **Upstream Repository:** [SeitaBV/timely-beliefs](https://github.com/SeitaBV/timely-beliefs)
