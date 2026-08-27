"""
BeliefSource Total Ordering and Metadata Modeling Module.
Enforces strict total ordering on BeliefSource instances to guarantee deterministic
Pandas MultiIndex sorting and prevent silent NaN values during DataFrame alignment.
"""

from typing import Optional

class BeliefSource:
    """Represents a source of probabilistic beliefs (sensor, model, or user)."""

    def __init__(self, name: str, source_type: str = "sensor", source_id: Optional[int] = None):
        self.name = name
        self.source_type = source_type
        self.id = source_id

    def __repr__(self) -> str:
        return f"<BeliefSource: {self.name} ({self.source_type})>"

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other: "BeliefSource") -> bool:
        """
        Enforce strict total ordering using string representation and object identity as a stable tiebreaker.
        Prevents non-deterministic Pandas MultiIndex sorting and NaN index collisions.
        """
        if not isinstance(other, BeliefSource):
            return NotImplemented
        return (str(self), id(self)) < (str(other), id(other))

    def __eq__(self, other: object) -> bool:
        """Default identity-based equality preserved for SQLAlchemy mapping integrity."""
        return self is other

    def __hash__(self) -> int:
        return id(self)
