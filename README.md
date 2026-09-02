# timely-beliefs Contributions — Total Ordering & Metadata Retention

Contributions to the open-source **timely-beliefs** sensor time-series library ([SeitaBV/timely-beliefs](https://github.com/SeitaBV/timely-beliefs)).

## Key Contributions

- **Strict Total Ordering for `BeliefSource` (PR #245 - Merged):** Implemented deterministic tiebreaking for `BeliefSource.__lt__` comparisons to eliminate silent `NaN` values during Pandas MultiIndex alignment.
- **`event_resolution` Metadata Retention (PR #247):** Fixed sensor metadata loss when converting between `BeliefsDataFrame` and `BeliefsSeries`.
