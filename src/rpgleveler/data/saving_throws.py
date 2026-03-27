"""
Saving throw progression tables for Basic Fantasy RPG.

This module defines saving throw target values for each character class at each
level, along with racial modifiers that adjust those values.

Saving throws represent the minimum d20 roll required to resist various effects.
Lower values are better.

Structure:
    SAVING_THROWS[class_name][level] -> SavingThrowData
    SAVING_THROW_MODIFIERS[race] -> SavingThrowData

Where:
    - class_name is a `ClassName` enum
    - race is a `Race` enum
    - level is the character level (int)
    - SavingThrowData contains values for all saving throw categories

Saving throw categories:
    - death_ray_or_poison: Effects involving poison or instant death
    - magic_wands: Effects from wands and similar magical devices
    - paralysis_or_petrify: Effects that immobilize or turn to stone
    - dragon_breath: Area effects such as dragon breath attacks
    - spells: General magical spell effects

Implementation details:
    - Base saving throw tables are defined per class and level.
    - Racial modifiers are applied as adjustments to these base values.
    - All data is frozen at runtime using `MappingProxyType` and frozen
      dataclasses.
    - Consumers should use `get_saving_throws()` rather than accessing tables
      directly.

Notes:
    - Lower values are better (target number to meet or exceed on d20).
    - Data is derived from official Basic Fantasy RPG tables.
    - The data is treated as immutable game rules.

Example:
    >>> get_saving_throws(ClassName.CLERIC, Race.HUMAN, 1)
    SavingThrowData(death_ray_or_poison=11, magic_wands=12, ...)
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Final

from rpgleveler.shared import ClassName, Race


@dataclass(frozen=True)
class SavingThrowData:
    """
    Immutable container for saving throw values.

    Each field represents the target number required to succeed on a d20 roll
    against a specific category of effect. Lower values indicate better saves.

    Attributes:
        death_ray_or_poison: Resistance to poison and instant-death effects
        magic_wands: Resistance to effects from magical wands
        paralysis_or_petrify: Resistance to paralysis and petrification effects
        dragon_breath: Resistance to breath weapons and area attacks
        spells: Resistance to general spell effects
    """
    death_ray_or_poison: int
    magic_wands: int
    paralysis_or_petrify: int
    dragon_breath: int
    spells: int

    def add(self, other: SavingThrowData) -> SavingThrowData:
        """
        Combine two saving throw datasets.

        This is primarily used to apply racial modifiers to base class values.

        Args:
            other: Another `SavingThrowData` instance to add.

        Returns:
            A new `SavingThrowData` instance with combined values.
        """
        return SavingThrowData(
            death_ray_or_poison=self.death_ray_or_poison + other.death_ray_or_poison,
            magic_wands=self.magic_wands + other.magic_wands,
            paralysis_or_petrify=self.paralysis_or_petrify + other.paralysis_or_petrify,
            dragon_breath=self.dragon_breath + other.dragon_breath,
            spells=self.spells + other.spells,
        )


type SavingThrowsByLevel = dict[int, SavingThrowData]
"""Mapping of level → saving throw values."""


type SavingThrowsByClassName = dict[ClassName, SavingThrowsByLevel]
"""Mapping of class → level-based saving throw progression."""


type SavingThrowsByRace = dict[Race, SavingThrowData]
"""Mapping of race → saving throw modifiers."""


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
    """
    Convert nested class-based saving throw data into immutable mappings.

    Both the outer mapping (class → levels) and inner mappings (level → data)
    are wrapped in `MappingProxyType` to prevent modification at runtime.

    Args:
        data: Mutable saving throw data by class.

    Returns:
        A fully read-only nested mapping structure.
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


def _freeze_race_modifiers(data: SavingThrowsByRace
) -> MappingProxyType[Race, SavingThrowData]:
    """
    Convert race-based modifier data into an immutable mapping.

    Since `SavingThrowData` instances are already frozen, only the outer mapping
    needs to be wrapped.

    Args:
        data: Mutable race modifier data.

    Returns:
        A read-only mapping of race → saving throw modifiers.
    """
    return MappingProxyType(data)


# Public, immutable saving throws table (by class).
SAVING_THROWS = _freeze_class_saving_throws(_raw_saving_throws)


# Public, immutable saving throw modifiers table (by race).
SAVING_THROW_MODIFIERS = _freeze_race_modifiers(_raw_saving_throw_modifiers)


def get_saving_throws(
    class_name: ClassName, 
    race: Race, 
    level: int) -> SavingThrowData:
    """
    Retrieve the effective saving throws for a character.

    This function combines base class saving throws with racial modifiers to
    produce the final saving throw values for a given character.

    Args:
        class_name: The character class.
        race: The character race.
        level: The character level (1–20).

    Returns:
        A `SavingThrowData` instance representing the final saving throws.

    Raises:
        ValueError: If the class, race, or level is invalid.

    Example:
        >>> get_saving_throws(ClassName.FIGHTER, Race.ELF, 5)
        SavingThrowData(...)
    """
    if class_name not in SAVING_THROWS:
        raise ValueError(f"Invalid class: {class_name}")
    if race not in SAVING_THROW_MODIFIERS:
        raise ValueError(f"Invalid race: {race}")
    if level not in SAVING_THROWS[class_name]:
        raise ValueError(f"Invalid level: {level}")

    saving_throws = SAVING_THROWS[class_name][level]
    modifiers = SAVING_THROW_MODIFIERS[race]

    return saving_throws.add(modifiers)
