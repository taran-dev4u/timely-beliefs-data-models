"""DataFrame alignment and NaN prevention utilities."""
import pandas as pd
from typing import List
from timely_beliefs_models.sources import BeliefSource

def align_belief_series(sources: List[BeliefSource], values: List[float]) -> pd.Series:
    sorted_pairs = sorted(zip(sources, values), key=lambda p: p[0])
    idx = [str(p[0]) for p in sorted_pairs]
    data = [p[1] for p in sorted_pairs]
    return pd.Series(data, index=idx)
