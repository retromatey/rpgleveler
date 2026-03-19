"""
Experience point (XP) progression tables for Basic Fantasy RPG.

This module defines the XP thresholds required for each class to reach a given
level. The data is derived directly from the official Basic Fantasy RPG class
progression tables.

Structure:
    XP_TABLE[class_name][level] -> xp_required

Where:
    - class_name is a ClassName literal (e.g., "fighter", "cleric")
    - level is the target character level (int)
    - xp_required is the minimum XP needed to attain that level

Notes:
    - Level 1 always starts at 0 XP.
    - XP thresholds are cumulative (not incremental).
    - All classes use independent progression tables.
    - The data is static and should not be modified at runtime.
"""

from __future__ import annotations

from typing import Final

from rpgleveler.shared.literals import ClassName

# Mapping of character level to required XP.
type XPByLevel = dict[int, int]


# XP progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
XP_TABLES: Final[dict[ClassName, XPByLevel]] = {
    "cleric": {
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
    "fighter": {
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
    "magic-user": {
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
    "thief": {
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
