"""
Thief skill progression tables for Basic Fantasy RPG.

This module defines the percentage chances for each thief skill at each level.
The data is derived directly from the official Basic Fantasy RPG class
progression tables.

Structure:
    THIEF_SKILLS[class_name][level] -> ThiefSkills

Where:
    - class_name is a `ClassName` enum
    - level is the character level (int)
    - `ThiefSkills` contains percentage values for all thief abilities

Thief skills:
    - open_locks: Chance to open locked doors and containers
    - pick_pockets: Chance to steal items unnoticed
    - find_traps: Chance to detect traps
    - remove_traps: Chance to safely disarm traps
    - move_silently: Chance to move without making noise
    - climb_walls: Chance to successfully climb vertical surfaces
    - hide_in_shadows: Chance to remain unseen in shadows
    - hear_noise: Chance to detect faint sounds

Notes:
    - Values represent percentage chances (0–100).
    - Some skills may exceed 100% at higher levels.
    - Non-thief classes have no access to these abilities (all values are zero).
    - Data is treated as immutable game rules.

Implementation details:
    - Raw data is defined in mutable dictionaries for readability.
    - Data is wrapped using `MappingProxyType` to enforce runtime immutability.
    - `ThiefSkills` is a frozen dataclass, ensuring values cannot be modified.
    - Consumers should use `get_thief_skills()` rather than accessing tables
      directly.

Example:
    >>> get_thief_skills(ClassName.THIEF, 5)
    ThiefSkills(open_locks=45, pick_pockets=50, ...)
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Final

from rpgleveler.shared import ClassName


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


type ThiefSkillsByLevel = dict[int, ThiefSkills]
"""Mapping of level → thief skill data."""


type ThiefSkillsByClassName = dict[ClassName, ThiefSkillsByLevel]
"""Mapping of class → level-based thief skill progression."""


# Thief skill progression table.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
_raw_thief_skills: Final[ThiefSkillsByClassName] = {
    ClassName.CLERIC: {
        lvl: ThiefSkills(0,0,0,0,0,0,0,0) for lvl in range(1, 21)
    },
    ClassName.FIGHTER: {
        lvl: ThiefSkills(0,0,0,0,0,0,0,0) for lvl in range(1, 21)
    },
    ClassName.MAGIC_USER: {
        lvl: ThiefSkills(0,0,0,0,0,0,0,0) for lvl in range(1, 21)
    },
    ClassName.THIEF: {
        1:  ThiefSkills(open_locks=25, pick_pockets=30, find_traps=20, remove_traps=20, move_silently=25, climb_walls=80, hide_in_shadows=10, hear_noise=30),
        2:  ThiefSkills(open_locks=30, pick_pockets=35, find_traps=25, remove_traps=25, move_silently=30, climb_walls=81, hide_in_shadows=15, hear_noise=35),
        3:  ThiefSkills(open_locks=35, pick_pockets=40, find_traps=30, remove_traps=30, move_silently=35, climb_walls=82, hide_in_shadows=20, hear_noise=40),
        4:  ThiefSkills(open_locks=40, pick_pockets=45, find_traps=35, remove_traps=35, move_silently=40, climb_walls=83, hide_in_shadows=25, hear_noise=45),
        5:  ThiefSkills(open_locks=45, pick_pockets=50, find_traps=40, remove_traps=40, move_silently=45, climb_walls=84, hide_in_shadows=30, hear_noise=50),
        6:  ThiefSkills(open_locks=50, pick_pockets=55, find_traps=45, remove_traps=45, move_silently=50, climb_walls=85, hide_in_shadows=35, hear_noise=55),
        7:  ThiefSkills(open_locks=55, pick_pockets=60, find_traps=50, remove_traps=50, move_silently=55, climb_walls=86, hide_in_shadows=40, hear_noise=60),
        8:  ThiefSkills(open_locks=60, pick_pockets=65, find_traps=55, remove_traps=55, move_silently=60, climb_walls=87, hide_in_shadows=45, hear_noise=65),
        9:  ThiefSkills(open_locks=65, pick_pockets=70, find_traps=60, remove_traps=60, move_silently=65, climb_walls=88, hide_in_shadows=50, hear_noise=70),
        10: ThiefSkills(open_locks=70, pick_pockets=75, find_traps=65, remove_traps=65, move_silently=70, climb_walls=89, hide_in_shadows=55, hear_noise=75),
        11: ThiefSkills(open_locks=75, pick_pockets=80, find_traps=70, remove_traps=70, move_silently=75, climb_walls=90, hide_in_shadows=60, hear_noise=80),
        12: ThiefSkills(open_locks=80, pick_pockets=85, find_traps=75, remove_traps=75, move_silently=80, climb_walls=91, hide_in_shadows=65, hear_noise=85),
        13: ThiefSkills(open_locks=85, pick_pockets=90, find_traps=80, remove_traps=80, move_silently=85, climb_walls=92, hide_in_shadows=70, hear_noise=90),
        14: ThiefSkills(open_locks=90, pick_pockets=92, find_traps=85, remove_traps=85, move_silently=88, climb_walls=93, hide_in_shadows=75, hear_noise=92),
        15: ThiefSkills(open_locks=92, pick_pockets=94, find_traps=88, remove_traps=88, move_silently=90, climb_walls=94, hide_in_shadows=80, hear_noise=94),
        16: ThiefSkills(open_locks=94, pick_pockets=96, find_traps=90, remove_traps=90, move_silently=92, climb_walls=95, hide_in_shadows=85, hear_noise=96),
        17: ThiefSkills(open_locks=96, pick_pockets=98, find_traps=92, remove_traps=92, move_silently=94, climb_walls=96, hide_in_shadows=90, hear_noise=98),
        18: ThiefSkills(open_locks=98, pick_pockets=99, find_traps=94, remove_traps=94, move_silently=96, climb_walls=97, hide_in_shadows=92, hear_noise=99),
        19: ThiefSkills(open_locks=99, pick_pockets=99, find_traps=96, remove_traps=96, move_silently=98, climb_walls=98, hide_in_shadows=94, hear_noise=99),
        20: ThiefSkills(open_locks=99, pick_pockets=99, find_traps=98, remove_traps=98, move_silently=99, climb_walls=99, hide_in_shadows=96, hear_noise=99),
    },
}


def _freeze(data: ThiefSkillsByClassName
) -> MappingProxyType[ClassName, MappingProxyType[int, ThiefSkills]]:
    """
    Convert nested thief skill data into immutable mappings.

    Both the outer mapping (class → levels) and inner mappings (level → skills)
    are wrapped in `MappingProxyType` to prevent modification at runtime.

    Args:
        data: Mutable thief skill data.

    Returns:
        A fully read-only nested mapping structure.
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


# Public, immutable thief skills table.
THIEF_SKILLS = _freeze(_raw_thief_skills)


def get_thief_skills(class_name: ClassName, level: int) -> ThiefSkills:
    """
    Retrieve thief skill values for a given class and level.

    This function provides a safe access layer over the thief skill table,
    ensuring invalid inputs are handled consistently.

    Args:
        class_name: The character class.
        level: The character level (1–20).

    Returns:
        A `ThiefSkills` instance representing skill percentages.

    Raises:
        ValueError: If the class or level is not present in the table.

    Example:
        >>> get_thief_skills(ClassName.THIEF, 1)
        ThiefSkills(open_locks=25, pick_pockets=30, ...)
    """
    if class_name not in THIEF_SKILLS:
        raise ValueError(f"Invalid class: {class_name}")
    if level not in THIEF_SKILLS[class_name]:
        raise ValueError(f"Invalid level: {level}")

    return THIEF_SKILLS[class_name][level]
