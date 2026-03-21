"""
Character advancement and leveling rules for Basic Fantasy RPG.

This module defines the rules governing whether a character can level up, as
well as the experience point (XP) thresholds required for progression.

These functions encapsulate the logic for determining level advancement
eligibility and should be used by the level-up engine rather than accessing XP
tables directly.

Structure:
    - can_level_up: Determines if a character qualifies for the next level
    - get_next_level_threshold: Returns XP required for the next level

Notes:
    - This module operates on XP progression rules only.
    - It does not modify character state.
    - All functions are deterministic and side-effect free.
"""

from __future__ import annotations

from rpgleveler.shared.character import Character
from rpgleveler.shared.literals import ClassName

MAX_LEVEL = 20


def can_level_up(character: Character) -> bool:
    """
    Determine whether a character qualifies to level up.

    A character can level up if:
        - Their current level is below the maximum supported level
        - Their experience points meet or exceed the threshold for the next level

    Args:
        character:
            The character to evaluate.

    Returns:
        bool:
            True if the character can level up, False otherwise.
    """
    raise NotImplementedError


def get_next_level_threshold(class_name: ClassName, level: int) -> int:
    """
    Return the XP threshold required to reach the next level.

    Args:
        class_name:
            The character class.
        level:
            The character's current level.

    Returns:
        int:
            The XP required to advance to the next level.

    Raises:
        KeyError:
            If the class or level is not found in the XP tables.
    """
    raise NotImplementedError


def is_max_level(level: int) -> bool:
    """
    Determine whether the given level is the maximum supported level.

    Args:
        level:
            The character's current level.

    Returns:
        bool:
            True if the level is at or above MAX_LEVEL, False otherwise.
    """
    raise NotImplementedError
