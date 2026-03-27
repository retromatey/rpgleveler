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

from dataclasses import dataclass
from types import MappingProxyType
from typing import Final

from rpgleveler.shared import ClassName, Race


@dataclass
class SavingThrowData:
    """Container for saving throws categories in Basic Fantasy.

    Attributes:
        death_ray_or_poison: comment here...
        magic_wands: comment here...
        paralysis_or_petrify: comment here...
        dragon_breath: comment here...
        spells: comment here...
    """
    death_ray_or_poison: int
    magic_wands: int
    paralysis_or_petrify: int
    dragon_breath: int
    spells: int


type SavingThrowsByLevel = dict[int, SavingThrowData]


type SavingThrowsByClassName = dict[ClassName, SavingThrowsByLevel]


type SavingThrowsByRace = dict[Race, SavingThrowData]


# Saving throw progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
_raw_saving_throws: Final[SavingThrowsByClassName] = {
    ClassName.CLERIC: {
        1:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=14, dragon_breath=16, spells=15),
        2:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=14, dragon_breath=16, spells=15),
        3:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=14, dragon_breath=16, spells=15),
        4:  SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=13, dragon_breath=15, spells=14),
        5:  SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=13, dragon_breath=15, spells=14),
        6:  SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=13, dragon_breath=15, spells=14),
        7:  SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=12, dragon_breath=13, spells=12),
        8:  SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=12, dragon_breath=13, spells=12),
        9:  SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=12, dragon_breath=13, spells=12),
        10: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=11, dragon_breath=11, spells=10),
        11: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=11, dragon_breath=11, spells=10),
        12: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=11, dragon_breath=11, spells=10),
        13: SavingThrowData(death_ray_or_poison=7,  magic_wands=8,  paralysis_or_petrify=10, dragon_breath=9,  spells=8),
        14: SavingThrowData(death_ray_or_poison=7,  magic_wands=8,  paralysis_or_petrify=10, dragon_breath=9,  spells=8),
        15: SavingThrowData(death_ray_or_poison=7,  magic_wands=8,  paralysis_or_petrify=10, dragon_breath=9,  spells=8),
        16: SavingThrowData(death_ray_or_poison=6,  magic_wands=7,  paralysis_or_petrify=9,  dragon_breath=7,  spells=6),
        17: SavingThrowData(death_ray_or_poison=6,  magic_wands=7,  paralysis_or_petrify=9,  dragon_breath=7,  spells=6),
        18: SavingThrowData(death_ray_or_poison=6,  magic_wands=7,  paralysis_or_petrify=9,  dragon_breath=7,  spells=6),
        19: SavingThrowData(death_ray_or_poison=5,  magic_wands=6,  paralysis_or_petrify=8,  dragon_breath=5,  spells=4),
        20: SavingThrowData(death_ray_or_poison=5,  magic_wands=6,  paralysis_or_petrify=8,  dragon_breath=5,  spells=4),
    },
    ClassName.FIGHTER: {
        1:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=14, dragon_breath=15, spells=17),
        2:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=14, dragon_breath=15, spells=17),
        3:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=14, dragon_breath=15, spells=17),
        4:  SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=12, dragon_breath=13, spells=15),
        5:  SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=12, dragon_breath=13, spells=15),
        6:  SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=12, dragon_breath=13, spells=15),
        7:  SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=10, dragon_breath=11, spells=13),
        8:  SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=10, dragon_breath=11, spells=13),
        9:  SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=10, dragon_breath=11, spells=13),
        10: SavingThrowData(death_ray_or_poison=6,  magic_wands=7,  paralysis_or_petrify=8,  dragon_breath=9,  spells=11),
        11: SavingThrowData(death_ray_or_poison=6,  magic_wands=7,  paralysis_or_petrify=8,  dragon_breath=9,  spells=11),
        12: SavingThrowData(death_ray_or_poison=6,  magic_wands=7,  paralysis_or_petrify=8,  dragon_breath=9,  spells=11),
        13: SavingThrowData(death_ray_or_poison=4,  magic_wands=5,  paralysis_or_petrify=6,  dragon_breath=7,  spells=9),
        14: SavingThrowData(death_ray_or_poison=4,  magic_wands=5,  paralysis_or_petrify=6,  dragon_breath=7,  spells=9),
        15: SavingThrowData(death_ray_or_poison=4,  magic_wands=5,  paralysis_or_petrify=6,  dragon_breath=7,  spells=9),
        16: SavingThrowData(death_ray_or_poison=2,  magic_wands=3,  paralysis_or_petrify=4,  dragon_breath=5,  spells=7),
        17: SavingThrowData(death_ray_or_poison=2,  magic_wands=3,  paralysis_or_petrify=4,  dragon_breath=5,  spells=7),
        18: SavingThrowData(death_ray_or_poison=2,  magic_wands=3,  paralysis_or_petrify=4,  dragon_breath=5,  spells=7),
        19: SavingThrowData(death_ray_or_poison=2,  magic_wands=3,  paralysis_or_petrify=4,  dragon_breath=5,  spells=7),
        20: SavingThrowData(death_ray_or_poison=2,  magic_wands=3,  paralysis_or_petrify=4,  dragon_breath=5,  spells=7),
    },
    ClassName.MAGIC_USER: {
        1:  SavingThrowData(death_ray_or_poison=13, magic_wands=14, paralysis_or_petrify=13, dragon_breath=16, spells=15),
        2:  SavingThrowData(death_ray_or_poison=13, magic_wands=14, paralysis_or_petrify=13, dragon_breath=16, spells=15),
        3:  SavingThrowData(death_ray_or_poison=13, magic_wands=14, paralysis_or_petrify=13, dragon_breath=16, spells=15),
        4:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=12, dragon_breath=15, spells=14),
        5:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=12, dragon_breath=15, spells=14),
        6:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=12, dragon_breath=15, spells=14),
        7:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=11, dragon_breath=14, spells=13),
        8:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=11, dragon_breath=14, spells=13),
        9:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=11, dragon_breath=14, spells=13),
        10: SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=10, dragon_breath=13, spells=12),
        11: SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=10, dragon_breath=13, spells=12),
        12: SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=10, dragon_breath=13, spells=12),
        13: SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=9,  dragon_breath=12, spells=11),
        14: SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=9,  dragon_breath=12, spells=11),
        15: SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=9,  dragon_breath=12, spells=11),
        16: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=8,  dragon_breath=11, spells=10),
        17: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=8,  dragon_breath=11, spells=10),
        18: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=8,  dragon_breath=11, spells=10),
        19: SavingThrowData(death_ray_or_poison=7,  magic_wands=8,  paralysis_or_petrify=7,  dragon_breath=10, spells=9),
        20: SavingThrowData(death_ray_or_poison=7,  magic_wands=8,  paralysis_or_petrify=7,  dragon_breath=10, spells=9),
    },
    ClassName.THIEF: {
        1:  SavingThrowData(death_ray_or_poison=13, magic_wands=14, paralysis_or_petrify=13, dragon_breath=16, spells=15),
        2:  SavingThrowData(death_ray_or_poison=13, magic_wands=14, paralysis_or_petrify=13, dragon_breath=16, spells=15),
        3:  SavingThrowData(death_ray_or_poison=13, magic_wands=14, paralysis_or_petrify=13, dragon_breath=16, spells=15),
        4:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=12, dragon_breath=15, spells=14),
        5:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=12, dragon_breath=15, spells=14),
        6:  SavingThrowData(death_ray_or_poison=12, magic_wands=13, paralysis_or_petrify=12, dragon_breath=15, spells=14),
        7:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=11, dragon_breath=14, spells=13),
        8:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=11, dragon_breath=14, spells=13),
        9:  SavingThrowData(death_ray_or_poison=11, magic_wands=12, paralysis_or_petrify=11, dragon_breath=14, spells=13),
        10: SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=10, dragon_breath=13, spells=12),
        11: SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=10, dragon_breath=13, spells=12),
        12: SavingThrowData(death_ray_or_poison=10, magic_wands=11, paralysis_or_petrify=10, dragon_breath=13, spells=12),
        13: SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=9,  dragon_breath=12, spells=11),
        14: SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=9,  dragon_breath=12, spells=11),
        15: SavingThrowData(death_ray_or_poison=9,  magic_wands=10, paralysis_or_petrify=9,  dragon_breath=12, spells=11),
        16: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=8,  dragon_breath=11, spells=10),
        17: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=8,  dragon_breath=11, spells=10),
        18: SavingThrowData(death_ray_or_poison=8,  magic_wands=9,  paralysis_or_petrify=8,  dragon_breath=11, spells=10),
        19: SavingThrowData(death_ray_or_poison=7,  magic_wands=8,  paralysis_or_petrify=7,  dragon_breath=10, spells=9),
        20: SavingThrowData(death_ray_or_poison=7,  magic_wands=8,  paralysis_or_petrify=7,  dragon_breath=10, spells=9),
    },
}


_raw_saving_throw_modifiers: Final[SavingThrowsByRace] = {
    Race.DWARF: SavingThrowData(
        # Negative values improve saving throws (lower is better)
        death_ray_or_poison=-4,
        magic_wands=-4,
        paralysis_or_petrify=-4,
        dragon_breath=-3,
        spells=-4,
    ),

    Race.ELF: SavingThrowData(
        # Negative values improve saving throws (lower is better)
        death_ray_or_poison=0,
        magic_wands=-2,
        paralysis_or_petrify=-1,
        dragon_breath=0,
        spells=-2,
    ),

    Race.HALFLING: SavingThrowData(
        # Negative values improve saving throws (lower is better)
        death_ray_or_poison=-4,
        magic_wands=-4,
        paralysis_or_petrify=-4,
        dragon_breath=-3,
        spells=-4,
    ),

    Race.HUMAN: SavingThrowData(
        death_ray_or_poison=0,
        magic_wands=0,
        paralysis_or_petrify=0,
        dragon_breath=0,
        spells=0,
    ),
}


def _freeze_class_saving_throws(data: SavingThrowsByClassName
) -> MappingProxyType[ClassName, MappingProxyType[int, SavingThrowData]]:
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


def _freeze_race_modifiers(data: SavingThrowsByRace
) -> MappingProxyType[Race, SavingThrowData]:
    return MappingProxyType({
        race: st_data for race, st_data in data.items()
    })


# Public, immutable saving throws table (by class).
SAVING_THROWS = _freeze_class_saving_throws(_raw_saving_throws)


# Public, immutable saving throw modifiers table (by race).
SAVING_THROW_MODIFIERS = _freeze_race_modifiers(_raw_saving_throw_modifiers)


def get_saving_throws(
    class_name: ClassName, 
    race: Race, 
    level: int) -> SavingThrowData:
    try:
        saving_throws = SAVING_THROWS[class_name][level]
        modifiers = SAVING_THROW_MODIFIERS[race]

        death_ray_or_poison = saving_throws.death_ray_or_poison + modifiers.death_ray_or_poison
        magic_wands = saving_throws.magic_wands + modifiers.magic_wands
        paralysis_or_petrify = saving_throws.paralysis_or_petrify + modifiers.paralysis_or_petrify
        dragon_breath = saving_throws.dragon_breath + modifiers.dragon_breath
        spells = saving_throws.spells + modifiers.spells

        return SavingThrowData(
            death_ray_or_poison=death_ray_or_poison,
            magic_wands=magic_wands,
            paralysis_or_petrify=paralysis_or_petrify,
            dragon_breath=dragon_breath,
            spells=spells
        )
    except KeyError:
        err_msg = f"Invalid class/race/level combination: {class_name}, {race}, {level}"
        raise ValueError(err_msg)
