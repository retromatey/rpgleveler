"""
Hit Dice progression tables for Basic Fantasy RPG.

This module defines the hit dice formula for each class at each level.  The
data is derived directly from the official Basic Fantasy RPG class progression
tables.

Structure:
    HIT_DICE[class_name][level] -> str

Where:
    - class_name is a `ClassName` enum
    - level is the character level (int)
    - value is a dice expression string (e.g., "3d6", "9d8+2")

Notes:
    - Values are expressed as dice formulas compatible with the dice roller.
    - Most classes increase hit dice linearly until level 9, after which
      bonuses are applied instead of additional dice.
    - All classes have entries for levels 1–20.
    - Data is treated as immutable game rules.

Implementation details:
    - Raw data is defined in mutable dictionaries for readability.
    - Data is wrapped using `MappingProxyType` to enforce runtime immutability.
    - Consumers should use `get_hit_dice()` rather than accessing tables
      directly.
"""

from __future__ import annotations

from types import MappingProxyType
from typing import Final

from rpgleveler.core import ClassName

type HitDiceByLevel = dict[int, str]
"""Mapping of level → hit dice formula string."""


type HitDiceByClassName = dict[ClassName, HitDiceByLevel]
"""Mapping of class → level-based hit dice progression."""


_raw_hit_dice: Final[HitDiceByClassName] = {
    ClassName.CLERIC: {
        1: "1d6",     2: "2d6",     3: "3d6",    4: "4d6",     5: "5d6",
        6: "6d6",     7: "7d6",     8: "8d6",    9: "9d6",    10: "9d6+1", 
        11: "9d6+2",  12: "9d6+3", 13: "9d6+4", 14: "9d6+5",  15: "9d6+6",  
        16: "9d6+7",  17: "9d6+8", 18: "9d6+9", 19: "9d6+10", 20: "9d6+11",
    },
    ClassName.FIGHTER: {
        1: "1d8",      2: "2d8",     3: "3d8",     4: "4d8",     5: "5d8",
        6: "6d8",      7: "7d8",     8: "8d8",     9: "9d8",    10: "9d8+2", 
        11: "9d8+4",  12: "9d8+6",  13: "9d8+8",  14: "9d8+10", 15: "9d8+12", 
        16: "9d8+14", 17: "9d8+16", 18: "9d8+18", 19: "9d8+20", 20: "9d8+22",
    },
    ClassName.MAGIC_USER: {
        1: "1d4",     2: "2d4",    3: "3d4",    4: "4d4",     5: "5d4",
        6: "6d4",     7: "7d4",    8: "8d4",    9: "9d4",    10: "9d4+1", 
        11: "9d4+2", 12: "9d4+3", 13: "9d4+4", 14: "9d4+5",  15: "9d4+6", 
        16: "9d4+7", 17: "9d4+8", 18: "9d4+9", 19: "9d4+10", 20: "9d4+11",
    },
    ClassName.THIEF: {
        1: "1d4",      2: "2d4",     3: "3d4",     4: "4d4",     5: "5d4",
        6: "6d4",      7: "7d4",     8: "8d4",     9: "9d4",    10: "9d4+2", 
        11: "9d4+4",  12: "9d4+6",  13: "9d4+8",  14: "9d4+10", 15: "9d4+12", 
        16: "9d4+14", 17: "9d4+16", 18: "9d4+18", 19: "9d4+20", 20: "9d4+22",
    },
}


def _freeze(
    data: HitDiceByClassName,
) -> MappingProxyType[ClassName, MappingProxyType[int, str]]:
    """Convert nested hit dice data into immutable mappings."""
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


# Public, immutable hit dice table.
HIT_DICE = _freeze(_raw_hit_dice)


def get_hit_dice(class_name: ClassName, level: int) -> str:
    """
    Retrieve the hit dice formula for a given class and level.

    Args:
        class_name: The character class.
        level: The character level (1–20).

    Returns:
        A dice expression string (e.g., "5d8", "9d6+3").

    Raises:
        ValueError: If the class or level is invalid.
    """
    if class_name not in HIT_DICE:
        raise ValueError(f"Invalid class: {class_name}")
    if level not in HIT_DICE[class_name]:
        raise ValueError(f"Invalid level: {level}")

    return HIT_DICE[class_name][level]
