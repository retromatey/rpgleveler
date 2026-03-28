"""
Attack bonus progression tables for Basic Fantasy RPG.

This module defines the base attack bonus for each character class at each
level.  The data is derived directly from the official Basic Fantasy RPG class
progression tables and is treated as immutable game rules.

Structure:
    ATTACK_BONUS[class_name][level] -> attack_bonus

Where:
    - class_name is a `ClassName` enum
    - level is the character level (int)
    - attack_bonus is the base modifier applied to attack rolls

Implementation details:
    - Raw data is defined in a mutable dictionary for readability.
    - Data is then wrapped using `MappingProxyType` to enforce runtime
      immutability.
    - Both outer (class) and inner (level) mappings are protected.

Notes:
    - Attack bonus progression varies by class.
    - Values increase stepwise according to class tables.
    - Consumers should use `get_attack_bonus()` instead of accessing the table
      directly.

Example:
    >>> get_attack_bonus(ClassName.FIGHTER, 5)
    5

    >>> get_attack_bonus(ClassName.MAGIC_USER, 1)
    1
"""

from __future__ import annotations

from types import MappingProxyType
from typing import Final

from rpgleveler.shared import ClassName

# Mapping of character level to attack bonus.
type AttackBonusByLevel = dict[int, int]


# Mapping of class name to attack bonus data.
type AttackBonusByClassName = dict[ClassName, AttackBonusByLevel]


# Attack bonus progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
_raw_attack_bonus: Final[AttackBonusByClassName] = {
    ClassName.CLERIC: {
        1: 1,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 4,
        7: 4,
        8: 5,
        9: 5,
        10: 6,
        11: 6,
        12: 7,
        13: 7,
        14: 8,
        15: 8,
        16: 9,
        17: 9,
        18: 10,
        19: 10,
        20: 11,
    },
    ClassName.FIGHTER: {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
    },
    ClassName.MAGIC_USER: {
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 5,
        10: 5,
        11: 6,
        12: 6,
        13: 7,
        14: 7,
        15: 8,
        16: 8,
        17: 9,
        18: 9,
        19: 10,
        20: 10,
    },
    ClassName.THIEF: {
        1: 1,
        2: 2,
        3: 2,
        4: 3,
        5: 3,
        6: 4,
        7: 4,
        8: 5,
        9: 5,
        10: 6,
        11: 6,
        12: 7,
        13: 7,
        14: 8,
        15: 8,
        16: 9,
        17: 9,
        18: 10,
        19: 10,
        20: 11,
    },
}


def _freeze(data: AttackBonusByClassName
) -> MappingProxyType[ClassName, MappingProxyType[int, int]]:
    """
    Convert nested dictionaries into fully immutable mappings.

    This function wraps both the outer dictionary (keyed by `ClassName`) and
    each inner dictionary (keyed by level) using `MappingProxyType`, producing a
    read-only view of the data.

    Args:
        data: Mutable attack bonus mapping.

    Returns:
        A nested `MappingProxyType` structure that prevents modification at
        runtime.

    Notes:
        - The returned mapping is a read-only view; attempting to modify it will
          raise `TypeError`.
        - The original input dictionary should not be modified after freezing,
          as changes would still be reflected in the proxy.
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


# Public, immutable attack bonus table.
ATTACK_BONUS = _freeze(_raw_attack_bonus)


def get_attack_bonus(class_name: ClassName, level: int) -> int:
    """
    Retrieve the attack bonus for a given class and level.

    This function provides a safe access layer over the attack bonus table,
    ensuring that invalid inputs are handled consistently.

    Args:
        class_name: The character class.
        level: The character level (1–20).

    Returns:
        The attack bonus for the specified class and level.

    Raises:
        ValueError: If the class or level is not present in the table.

    Example:
        >>> get_attack_bonus(ClassName.CLERIC, 4)
        3
    """
    if class_name not in ATTACK_BONUS:
        raise ValueError(f"Invalid class: {class_name}")
    if level not in ATTACK_BONUS[class_name]:
        raise ValueError(f"Invalid level: {level}")
    
    return ATTACK_BONUS[class_name][level]
