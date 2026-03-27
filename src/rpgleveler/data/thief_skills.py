"""
Thief skill progression tables for Basic Fantasy RPG.

This module defines the percentage chances for each thief skill at each level.
The data is derived directly from the official Basic Fantasy RPG class
progression tables.

Structure:
    THIEF_SKILLS[level] -> ThiefSkillData

Where:
    - level is the character level (int)
    - ThiefSkillData maps each thief skill to a success percentage

Thief skills:
    - open_locks
    - pick_pockets
    - find_traps
    - remove_traps
    - move_silently
    - climb_walls
    - hide_in_shadows
    - hear_noise

Notes:
    - Values represent percentage chances (0–100).
    - Some skills may exceed 100% at higher levels.
    - The data is static and should not be modified at runtime.
"""

from __future__ import annotations

from typing import Final, TypedDict

from rpgleveler.shared.literals import ClassName, RaceName


class ThiefSkillData(TypedDict):
    """Percentage chances for all thief skills at a given level."""
    open_locks: int
    pick_pockets: int
    find_traps: int
    remove_traps: int
    move_silently: int
    climb_walls: int
    hide_in_shadows: int
    hear_noise: int


# Mapping of character level to thief skill progression.
type ThiefSkillsByLevel = dict[int, ThiefSkillData]


# Thief skill progression table.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
THIEF_SKILLS: Final[dict[ClassName, ThiefSkillsByLevel]] = {
    "thief": {
        1:  {"open_locks": 25, "pick_pockets": 30, "find_traps": 20, "remove_traps": 20, "move_silently": 25, "climb_walls": 80, "hide_in_shadows": 10, "hear_noise": 30},
        2:  {"open_locks": 30, "pick_pockets": 35, "find_traps": 25, "remove_traps": 25, "move_silently": 30, "climb_walls": 81, "hide_in_shadows": 15, "hear_noise": 35},
        3:  {"open_locks": 35, "pick_pockets": 40, "find_traps": 30, "remove_traps": 30, "move_silently": 35, "climb_walls": 82, "hide_in_shadows": 20, "hear_noise": 40},
        4:  {"open_locks": 40, "pick_pockets": 45, "find_traps": 35, "remove_traps": 35, "move_silently": 40, "climb_walls": 83, "hide_in_shadows": 25, "hear_noise": 45},
        5:  {"open_locks": 45, "pick_pockets": 50, "find_traps": 40, "remove_traps": 40, "move_silently": 45, "climb_walls": 84, "hide_in_shadows": 30, "hear_noise": 50},
        6:  {"open_locks": 50, "pick_pockets": 55, "find_traps": 45, "remove_traps": 45, "move_silently": 50, "climb_walls": 85, "hide_in_shadows": 35, "hear_noise": 55},
        7:  {"open_locks": 55, "pick_pockets": 60, "find_traps": 50, "remove_traps": 50, "move_silently": 55, "climb_walls": 86, "hide_in_shadows": 40, "hear_noise": 60},
        8:  {"open_locks": 60, "pick_pockets": 65, "find_traps": 55, "remove_traps": 55, "move_silently": 60, "climb_walls": 87, "hide_in_shadows": 45, "hear_noise": 65},
        9:  {"open_locks": 65, "pick_pockets": 70, "find_traps": 60, "remove_traps": 60, "move_silently": 65, "climb_walls": 88, "hide_in_shadows": 50, "hear_noise": 70},
        10: {"open_locks": 70, "pick_pockets": 75, "find_traps": 65, "remove_traps": 65, "move_silently": 70, "climb_walls": 89, "hide_in_shadows": 55, "hear_noise": 75},
        11: {"open_locks": 75, "pick_pockets": 80, "find_traps": 70, "remove_traps": 70, "move_silently": 75, "climb_walls": 90, "hide_in_shadows": 60, "hear_noise": 80},
        12: {"open_locks": 80, "pick_pockets": 85, "find_traps": 75, "remove_traps": 75, "move_silently": 80, "climb_walls": 91, "hide_in_shadows": 65, "hear_noise": 85},
        13: {"open_locks": 85, "pick_pockets": 90, "find_traps": 80, "remove_traps": 80, "move_silently": 85, "climb_walls": 92, "hide_in_shadows": 70, "hear_noise": 90},
        14: {"open_locks": 90, "pick_pockets": 92, "find_traps": 85, "remove_traps": 85, "move_silently": 88, "climb_walls": 93, "hide_in_shadows": 75, "hear_noise": 92},
        15: {"open_locks": 92, "pick_pockets": 94, "find_traps": 88, "remove_traps": 88, "move_silently": 90, "climb_walls": 94, "hide_in_shadows": 80, "hear_noise": 94},
        16: {"open_locks": 94, "pick_pockets": 96, "find_traps": 90, "remove_traps": 90, "move_silently": 92, "climb_walls": 95, "hide_in_shadows": 85, "hear_noise": 96},
        17: {"open_locks": 96, "pick_pockets": 98, "find_traps": 92, "remove_traps": 92, "move_silently": 94, "climb_walls": 96, "hide_in_shadows": 90, "hear_noise": 98},
        18: {"open_locks": 98, "pick_pockets": 99, "find_traps": 94, "remove_traps": 94, "move_silently": 96, "climb_walls": 97, "hide_in_shadows": 92, "hear_noise": 99},
        19: {"open_locks": 99, "pick_pockets": 99, "find_traps": 96, "remove_traps": 96, "move_silently": 98, "climb_walls": 98, "hide_in_shadows": 94, "hear_noise": 99},
        20: {"open_locks": 99, "pick_pockets": 99, "find_traps": 98, "remove_traps": 98, "move_silently": 99, "climb_walls": 99, "hide_in_shadows": 96, "hear_noise": 99},
    },
}
