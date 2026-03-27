"""
TODO: add comments
"""

from __future__ import annotations

from types import MappingProxyType
from typing import Final, cast

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
    TODO: add comments
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


ATTACK_BONUS = _freeze(_raw_attack_bonus)


def get_attack_bonus(class_name: ClassName, level: int) -> int:
    """
    TODO: add comments
    """
    try:
        return cast(int, ATTACK_BONUS[class_name][level])
    except KeyError:
        err_msg = f"Invalid class/level combination: {class_name}, {level}"
        raise ValueError(err_msg)
