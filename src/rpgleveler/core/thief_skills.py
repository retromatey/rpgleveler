from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ThiefSkills:
    """
    Immutable container for thief skill percentages.

    Each field represents the percentage chance of success for a specific thief
    ability.

    Attributes:
        open_locks: Chance to open locked objects
        pick_pockets: Chance to steal items unnoticed
        find_traps: Chance to detect traps
        remove_traps: Chance to disarm traps
        move_silently: Chance to move quietly
        climb_walls: Chance to climb surfaces
        hide_in_shadows: Chance to remain hidden
        hear_noise: Chance to detect faint sounds
    """
    open_locks: int
    pick_pockets: int
    find_traps: int
    remove_traps: int
    move_silently: int
    climb_walls: int
    hide_in_shadows: int
    hear_noise: int

    def to_dict(self) -> dict[str, int]:
        return vars(self)

    @classmethod
    def from_dict(cls, data: dict[str, int]) -> ThiefSkills:
        return cls(**data)
