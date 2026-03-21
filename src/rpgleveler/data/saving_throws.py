"""
Saving throw progression tables for Basic Fantasy RPG.

This module defines saving throw values for each class at each level.  The data
is derived directly from the official Basic Fantasy RPG class progression
tables.

Structure:
    SAVING_THROWS[class_name][level] -> SavingThrowData

Where:
    - class_name is a ClassName literal (e.g., "fighter", "cleric")
    - level is the character level (int)
    - SavingThrowData is a mapping of saving throw categories to target values

Saving throw categories:
    - death_ray_or_poison
    - magic_wands
    - paralysis_or_petrify
    - dragon_breath
    - spells

Notes:
    - Lower values are better (target number to meet or exceed on d20).
    - Each class has its own progression table.
    - The data is static and should not be modified at runtime.
"""

from __future__ import annotations

from typing import Final, TypedDict

from rpgleveler.shared.literals import ClassName, RaceName


class SavingThrowData(TypedDict):
    """Saving throw values for all categories at a given level."""
    death_ray_or_poison: int
    magic_wands: int
    paralysis_or_petrify: int
    dragon_breath: int
    spells: int


type SavingThrowsByLevel = dict[int, SavingThrowData]


# Saving throw progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
SAVING_THROWS: Final[dict[ClassName, SavingThrowsByLevel]] = {
    "cleric": {
        1:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 14, "dragon_breath": 16, "spells": 15},
        2:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 14, "dragon_breath": 16, "spells": 15},
        3:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 14, "dragon_breath": 16, "spells": 15},
        4:  {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 13, "dragon_breath": 15, "spells": 14},
        5:  {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 13, "dragon_breath": 15, "spells": 14},
        6:  {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 13, "dragon_breath": 15, "spells": 14},
        7:  {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 12, "dragon_breath": 13, "spells": 12},
        8:  {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 12, "dragon_breath": 13, "spells": 12},
        9:  {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 12, "dragon_breath": 13, "spells": 12},
        10: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 11, "dragon_breath": 11, "spells": 10},
        11: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 11, "dragon_breath": 11, "spells": 10},
        12: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 11, "dragon_breath": 11, "spells": 10},
        13: {"death_ray_or_poison": 7,  "magic_wands": 8,  "paralysis_or_petrify": 10, "dragon_breath": 9,  "spells": 8},
        14: {"death_ray_or_poison": 7,  "magic_wands": 8,  "paralysis_or_petrify": 10, "dragon_breath": 9,  "spells": 8},
        15: {"death_ray_or_poison": 7,  "magic_wands": 8,  "paralysis_or_petrify": 10, "dragon_breath": 9,  "spells": 8},
        16: {"death_ray_or_poison": 6,  "magic_wands": 7,  "paralysis_or_petrify": 9,  "dragon_breath": 7,  "spells": 6},
        17: {"death_ray_or_poison": 6,  "magic_wands": 7,  "paralysis_or_petrify": 9,  "dragon_breath": 7,  "spells": 6},
        18: {"death_ray_or_poison": 6,  "magic_wands": 7,  "paralysis_or_petrify": 9,  "dragon_breath": 7,  "spells": 6},
        19: {"death_ray_or_poison": 5,  "magic_wands": 6,  "paralysis_or_petrify": 8,  "dragon_breath": 5,  "spells": 4},
        20: {"death_ray_or_poison": 5,  "magic_wands": 6,  "paralysis_or_petrify": 8,  "dragon_breath": 5,  "spells": 4},
    },
    "fighter": {
        1:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 14, "dragon_breath": 15, "spells": 17},
        2:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 14, "dragon_breath": 15, "spells": 17},
        3:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 14, "dragon_breath": 15, "spells": 17},
        4:  {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 12, "dragon_breath": 13, "spells": 15},
        5:  {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 12, "dragon_breath": 13, "spells": 15},
        6:  {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 12, "dragon_breath": 13, "spells": 15},
        7:  {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 10, "dragon_breath": 11, "spells": 13},
        8:  {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 10, "dragon_breath": 11, "spells": 13},
        9:  {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 10, "dragon_breath": 11, "spells": 13},
        10: {"death_ray_or_poison": 6,  "magic_wands": 7,  "paralysis_or_petrify": 8,  "dragon_breath": 9,  "spells": 11},
        11: {"death_ray_or_poison": 6,  "magic_wands": 7,  "paralysis_or_petrify": 8,  "dragon_breath": 9,  "spells": 11},
        12: {"death_ray_or_poison": 6,  "magic_wands": 7,  "paralysis_or_petrify": 8,  "dragon_breath": 9,  "spells": 11},
        13: {"death_ray_or_poison": 4,  "magic_wands": 5,  "paralysis_or_petrify": 6,  "dragon_breath": 7,  "spells": 9},
        14: {"death_ray_or_poison": 4,  "magic_wands": 5,  "paralysis_or_petrify": 6,  "dragon_breath": 7,  "spells": 9},
        15: {"death_ray_or_poison": 4,  "magic_wands": 5,  "paralysis_or_petrify": 6,  "dragon_breath": 7,  "spells": 9},
        16: {"death_ray_or_poison": 2,  "magic_wands": 3,  "paralysis_or_petrify": 4,  "dragon_breath": 5,  "spells": 7},
        17: {"death_ray_or_poison": 2,  "magic_wands": 3,  "paralysis_or_petrify": 4,  "dragon_breath": 5,  "spells": 7},
        18: {"death_ray_or_poison": 2,  "magic_wands": 3,  "paralysis_or_petrify": 4,  "dragon_breath": 5,  "spells": 7},
        19: {"death_ray_or_poison": 2,  "magic_wands": 3,  "paralysis_or_petrify": 4,  "dragon_breath": 5,  "spells": 7},
        20: {"death_ray_or_poison": 2,  "magic_wands": 3,  "paralysis_or_petrify": 4,  "dragon_breath": 5,  "spells": 7},
    },
    "magic-user": {
        1:  {"death_ray_or_poison": 13, "magic_wands": 14, "paralysis_or_petrify": 13, "dragon_breath": 16, "spells": 15},
        2:  {"death_ray_or_poison": 13, "magic_wands": 14, "paralysis_or_petrify": 13, "dragon_breath": 16, "spells": 15},
        3:  {"death_ray_or_poison": 13, "magic_wands": 14, "paralysis_or_petrify": 13, "dragon_breath": 16, "spells": 15},
        4:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 12, "dragon_breath": 15, "spells": 14},
        5:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 12, "dragon_breath": 15, "spells": 14},
        6:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 12, "dragon_breath": 15, "spells": 14},
        7:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 11, "dragon_breath": 14, "spells": 13},
        8:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 11, "dragon_breath": 14, "spells": 13},
        9:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 11, "dragon_breath": 14, "spells": 13},
        10: {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 10, "dragon_breath": 13, "spells": 12},
        11: {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 10, "dragon_breath": 13, "spells": 12},
        12: {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 10, "dragon_breath": 13, "spells": 12},
        13: {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 9,  "dragon_breath": 12, "spells": 11},
        14: {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 9,  "dragon_breath": 12, "spells": 11},
        15: {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 9,  "dragon_breath": 12, "spells": 11},
        16: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 8,  "dragon_breath": 11, "spells": 10},
        17: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 8,  "dragon_breath": 11, "spells": 10},
        18: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 8,  "dragon_breath": 11, "spells": 10},
        19: {"death_ray_or_poison": 7,  "magic_wands": 8,  "paralysis_or_petrify": 7,  "dragon_breath": 10, "spells": 9},
        20: {"death_ray_or_poison": 7,  "magic_wands": 8,  "paralysis_or_petrify": 7,  "dragon_breath": 10, "spells": 9},
    },
    "thief": {
        1:  {"death_ray_or_poison": 13, "magic_wands": 14, "paralysis_or_petrify": 13, "dragon_breath": 16, "spells": 15},
        2:  {"death_ray_or_poison": 13, "magic_wands": 14, "paralysis_or_petrify": 13, "dragon_breath": 16, "spells": 15},
        3:  {"death_ray_or_poison": 13, "magic_wands": 14, "paralysis_or_petrify": 13, "dragon_breath": 16, "spells": 15},
        4:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 12, "dragon_breath": 15, "spells": 14},
        5:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 12, "dragon_breath": 15, "spells": 14},
        6:  {"death_ray_or_poison": 12, "magic_wands": 13, "paralysis_or_petrify": 12, "dragon_breath": 15, "spells": 14},
        7:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 11, "dragon_breath": 14, "spells": 13},
        8:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 11, "dragon_breath": 14, "spells": 13},
        9:  {"death_ray_or_poison": 11, "magic_wands": 12, "paralysis_or_petrify": 11, "dragon_breath": 14, "spells": 13},
        10: {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 10, "dragon_breath": 13, "spells": 12},
        11: {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 10, "dragon_breath": 13, "spells": 12},
        12: {"death_ray_or_poison": 10, "magic_wands": 11, "paralysis_or_petrify": 10, "dragon_breath": 13, "spells": 12},
        13: {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 9,  "dragon_breath": 12, "spells": 11},
        14: {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 9,  "dragon_breath": 12, "spells": 11},
        15: {"death_ray_or_poison": 9,  "magic_wands": 10, "paralysis_or_petrify": 9,  "dragon_breath": 12, "spells": 11},
        16: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 8,  "dragon_breath": 11, "spells": 10},
        17: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 8,  "dragon_breath": 11, "spells": 10},
        18: {"death_ray_or_poison": 8,  "magic_wands": 9,  "paralysis_or_petrify": 8,  "dragon_breath": 11, "spells": 10},
        19: {"death_ray_or_poison": 7,  "magic_wands": 8,  "paralysis_or_petrify": 7,  "dragon_breath": 10, "spells": 9},
        20: {"death_ray_or_poison": 7,  "magic_wands": 8,  "paralysis_or_petrify": 7,  "dragon_breath": 10, "spells": 9},
    },
}


SAVING_THROW_MODIFIERS: Final[dict[RaceName, SavingThrowData]] = {
    "dwarf": {
        # Negative values improve saving throws (lower is better)
        "death_ray_or_poison": -4,
        "magic_wands": -4,
        "paralysis_or_petrify": -4,
        "dragon_breath": -3,
        "spells": -4,
    },

    "elf": {
        # Negative values improve saving throws (lower is better)
        "death_ray_or_poison": 0,
        "magic_wands": -2,
        "paralysis_or_petrify": -1,
        "dragon_breath": 0,
        "spells": -2,
    },

    "halfling": {
        # Negative values improve saving throws (lower is better)
        "death_ray_or_poison": -4,
        "magic_wands": -4,
        "paralysis_or_petrify": -4,
        "dragon_breath": -3,
        "spells": -4,
    },

    "human": {
        "death_ray_or_poison": 0,
        "magic_wands": 0,
        "paralysis_or_petrify": 0,
        "dragon_breath": 0,
        "spells": 0,
    },
}
