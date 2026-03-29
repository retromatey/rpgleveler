from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SpellSlots:
    """
    Immutable container for spell slot counts.

    Each field represents the number of available spell slots for a given spell
    level.

    Attributes:
        level_1: Number of level 1 spell slots
        level_2: Number of level 2 spell slots
        level_3: Number of level 3 spell slots
        level_4: Number of level 4 spell slots
        level_5: Number of level 5 spell slots
    """
    level_1: int
    level_2: int
    level_3: int
    level_4: int
    level_5: int

    def to_dict(self) -> dict[str, int]:
        return vars(self)
    
    @classmethod
    def from_dict(cls, data: dict[str, int]) -> SpellSlots:
        return cls(**data)
