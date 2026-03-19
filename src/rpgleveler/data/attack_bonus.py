"""
Attack bonus progression tables for Basic Fantasy RPG.

This module defines the attack bonus for each class at each level.  The data is
derived directly from the official Basic Fantasy RPG class progression tables.

Structure:
    ATTACK_BONUS[class_name][level] -> attack_bonus

Where:
    - class_name is a ClassName literal (e.g., "fighter", "cleric")
    - level is the character level (int)
    - attack_bonus is the base bonus applied to attack rolls

Notes:
    - Attack bonus progression varies by class.
    - Values increase stepwise according to class tables.
    - The data is static and should not be modified at runtime.
"""

from __future__ import annotations

from typing import Final

from rpgleveler.shared.literals import ClassName

# Mapping of character level to attack bonus.
type AttackBonusByLevel = dict[int, int]


# Attack bonus progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
ATTACK_BONUS: Final[dict[ClassName, AttackBonusByLevel]] = {
    "cleric": {
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
    "fighter": {
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
    "magic-user": {
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
    "thief": {
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
