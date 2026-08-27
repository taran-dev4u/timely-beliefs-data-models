# timely-beliefs — Probabilistic Sensor & Time-Series Data Modeling

[![CI](https://github.com/taran-dev4u/timely-beliefs-data-models/actions/workflows/ci.yml/badge.svg)](https://github.com/taran-dev4u/timely-beliefs-data-models/actions/workflows/ci.yml)
[![Upstream PR](https://img.shields.io/badge/SeitaBV%2Ftimely--beliefs-PR%20%23245%20Merged-green?logo=github)](https://github.com/SeitaBV/timely-beliefs/pull/245)
[![Upstream Stars](https://img.shields.io/badge/Upstream%20Stars-42%2B%20%E2%AD%90-yellow?logo=github)](https://github.com/SeitaBV/timely-beliefs)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Production open-source data modeling framework extending [SeitaBV/timely-beliefs](https://github.com/SeitaBV/timely-beliefs), a library for managing probabilistic time-series and sensor belief uncertainty.

---

## 🎯 Background & Problem Statement

In multi-source sensor and market telemetry pipelines, aligning `BeliefsDataFrame` instances across duplicate or identical belief sources produced silent `NaN` values. This occurred because `BeliefSource` lacked a strict total ordering implementation in `__lt__`, leading to non-deterministic sorting and index alignment drift in Pandas MultiIndex operations.

---

## 💡 Solution Architecture

- **Strict Total Ordering:** Implemented `__lt__` with a stable `(str(self), id(self)) < (str(other), id(other))` tiebreaker.
- **SQLAlchemy Identity Preservation:** Retained identity-based `__eq__` and `__hash__` to preserve database session and ORM unit-of-work guarantees.
- **Automated Regression Test Suite:** Validated Pandas MultiIndex alignment, sort stability, and total order axioms.

---

## 🏛️ Upstream Merged Pull Request

- **Repository:** [SeitaBV/timely-beliefs](https://github.com/SeitaBV/timely-beliefs)
- **Pull Request:** [#245 — fix: enforce strict total ordering on BeliefSource](https://github.com/SeitaBV/timely-beliefs/pull/245)
- **Status:** **Merged upstream** by Seita Energy maintainers.

---

## 📄 License

Licensed under the [Apache License, Version 2.0](LICENSE).
