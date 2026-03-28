"""TODO add comment"""

from __future__ import annotations

from types import MappingProxyType
from typing import Final

from rpgleveler.shared import ClassName

type XPByLevel = dict[int, int]
"""TODO add comment"""


type XPByClassName = dict[ClassName, XPByLevel]
"""TODO add comment"""


# XP progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
_raw_xp_tables: Final[XPByClassName] = {
    ClassName.CLERIC: {
        1: 0,
        2: 1500,
        3: 3000,
        4: 6000,
        5: 13000,
        6: 27500,
        7: 55000,
        8: 110000,
        9: 225000,
        10: 450000,
        11: 675000,
        12: 900000,
        13: 1125000,
        14: 1350000,
        15: 1575000,
        16: 1800000,
        17: 2025000,
        18: 2250000,
        19: 2475000,
        20: 2700000,
    },
    ClassName.FIGHTER: {
        1: 0,
        2: 2000,
        3: 4000,
        4: 8000,
        5: 16000,
        6: 32000,
        7: 64000,
        8: 120000,
        9: 240000,
        10: 360000,
        11: 480000,
        12: 600000,
        13: 720000,
        14: 840000,
        15: 960000,
        16: 1080000,
        17: 1200000,
        18: 1320000,
        19: 1440000,
        20: 1560000,
    },
    ClassName.MAGIC_USER: {
        1: 0,
        2: 2500,
        3: 5000,
        4: 10000,
        5: 20000,
        6: 40000,
        7: 80000,
        8: 150000,
        9: 300000,
        10: 450000,
        11: 600000,
        12: 750000,
        13: 900000,
        14: 1050000,
        15: 1200000,
        16: 1350000,
        17: 1500000,
        18: 1650000,
        19: 1800000,
        20: 1950000,
    },
    ClassName.THIEF: {
        1: 0,
        2: 1250,
        3: 2500,
        4: 5000,
        5: 10000,
        6: 20000,
        7: 40000,
        8: 70000,
        9: 140000,
        10: 210000,
        11: 280000,
        12: 350000,
        13: 420000,
        14: 490000,
        15: 560000,
        16: 630000,
        17: 700000,
        18: 770000,
        19: 840000,
        20: 910000,
    },
}


def _freeze(data: XPByClassName
) -> MappingProxyType[ClassName, MappingProxyType[int, int]]:
    """
    TODO: add comments
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


# Public, immutable xp tables.
XP_TABLES = _freeze(_raw_xp_tables)


def get_xp_requirement(class_name: ClassName, level: int) -> int:
    """
    TODO: add comments
    """
    if class_name not in XP_TABLES:
        raise ValueError(f"Invalid class: {class_name}")
    if level not in XP_TABLES[class_name]:
        raise ValueError(f"Invalid level: {level}")

    return XP_TABLES[class_name][level]
