"""
Spell slot progression tables for Basic Fantasy RPG.

This module defines the number of spell slots available to each character class
at each level. The data is derived directly from the official Basic Fantasy RPG
class progression tables.

Structure:
    SPELL_SLOTS[class_name][level] -> SpellSlots

Where:
    - class_name is a `ClassName` enum
    - level is the character level (int)
    - `SpellSlots` contains the number of available slots for spell levels 1–5

Spell slot format:
    SpellSlots(level_1, level_2, level_3, level_4, level_5)

Notes:
    - Spellcasting progression varies by class.
    - Clerics begin spellcasting at level 2.
    - Non-spellcasting classes (e.g., fighter, thief) have zero spell slots.
    - All data is treated as immutable game rules.

Implementation details:
    - Raw data is defined in mutable dictionaries for readability.
    - Data is wrapped using `MappingProxyType` to enforce runtime immutability.
    - `SpellSlots` is a frozen dataclass, ensuring values cannot be modified.

Example:
    >>> get_spell_slots(ClassName.CLERIC, 5)
    SpellSlots(level_1=2, level_2=2, level_3=0, level_4=0, level_5=0)
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Final

from rpgleveler.core import ClassName


@dataclass(frozen=True)
class SpellSlots:
    """
    Immutable container for spell slot counts.

    Each field represents the number of available spell slots for a given spell
    level.

    Attributes:
        level_1: Number of level 1 spell slots
        level_2: Number of level 2 spell slots
        level_3: Number of level 3 spell slots
        level_4: Number of level 4 spell slots
        level_5: Number of level 5 spell slots
    """
    level_1: int
    level_2: int
    level_3: int
    level_4: int
    level_5: int


type SpellSlotsByLevel = dict[int, SpellSlots]
"""Mapping of level → spell slot data."""


type SpellSlotsByClassName = dict[ClassName, SpellSlotsByLevel]
"""Mapping of class → level-based spell slot progression."""


# Spell slot progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
_raw_spell_slots: Final[SpellSlotsByClassName] = {
    ClassName.CLERIC: {
        1:  SpellSlots(0,0,0,0,0), # Clerics do not gain spells until level 2
        2:  SpellSlots(1,0,0,0,0),
        3:  SpellSlots(2,0,0,0,0),
        4:  SpellSlots(2,1,0,0,0),
        5:  SpellSlots(2,2,0,0,0),
        6:  SpellSlots(2,2,1,0,0),
        7:  SpellSlots(3,2,2,0,0),
        8:  SpellSlots(3,3,2,1,0),
        9:  SpellSlots(3,3,3,2,0),
        10: SpellSlots(4,3,3,2,1),
        11: SpellSlots(4,4,3,3,2),
        12: SpellSlots(4,4,4,3,2),
        13: SpellSlots(5,4,4,3,3),
        14: SpellSlots(5,5,4,4,3),
        15: SpellSlots(5,5,5,4,4),
        16: SpellSlots(6,5,5,4,4),
        17: SpellSlots(6,6,5,5,4),
        18: SpellSlots(6,6,6,5,5),
        19: SpellSlots(7,6,6,5,5),
        20: SpellSlots(7,7,6,6,5),
    },
    ClassName.FIGHTER: { lvl: SpellSlots(0,0,0,0,0) for lvl in range(1, 21) },
    ClassName.MAGIC_USER: {
        1:  SpellSlots(1,0,0,0,0),
        2:  SpellSlots(2,0,0,0,0),
        3:  SpellSlots(2,1,0,0,0),
        4:  SpellSlots(2,2,0,0,0),
        5:  SpellSlots(2,2,1,0,0),
        6:  SpellSlots(2,2,2,0,0),
        7:  SpellSlots(3,2,2,1,0),
        8:  SpellSlots(3,3,2,2,0),
        9:  SpellSlots(3,3,3,2,1),
        10: SpellSlots(3,3,3,3,2),
        11: SpellSlots(4,3,3,3,2),
        12: SpellSlots(4,4,3,3,3),
        13: SpellSlots(4,4,4,3,3),
        14: SpellSlots(4,4,4,4,3),
        15: SpellSlots(5,4,4,4,4),
        16: SpellSlots(5,5,4,4,4),
        17: SpellSlots(5,5,5,4,4),
        18: SpellSlots(5,5,5,5,4),
        19: SpellSlots(6,5,5,5,5),
        20: SpellSlots(6,6,5,5,5),
    },
    ClassName.THIEF: { lvl: SpellSlots(0,0,0,0,0) for lvl in range(1, 21) },
}


def _freeze(data: SpellSlotsByClassName 
) -> MappingProxyType[ClassName, MappingProxyType[int, SpellSlots]]:
    """
    Convert nested spell slot data into immutable mappings.

    Both the outer mapping (class → levels) and inner mappings (level → slots)
    are wrapped in `MappingProxyType` to prevent modification at runtime.

    Args:
        data: Mutable spell slot data.

    Returns:
        A fully read-only nested mapping structure.
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


# Public, immutable spell slots table.
SPELL_SLOTS = _freeze(_raw_spell_slots)


def get_spell_slots(class_name: ClassName, level: int) -> SpellSlots:
    """
    Retrieve the spell slots for a given class and level.

    This function provides a safe access layer over the spell slot table,
    ensuring invalid inputs are handled consistently.

    Args:
        class_name: The character class.
        level: The character level (1–20).

    Returns:
        A `SpellSlots` instance representing available spell slots.

    Raises:
        ValueError: If the class or level is not present in the table.

    Example:
        >>> get_spell_slots(ClassName.MAGIC_USER, 3)
        SpellSlots(level_1=2, level_2=1, level_3=0, level_4=0, level_5=0)
    """
    if class_name not in SPELL_SLOTS:
        raise ValueError(f"Invalid class: {class_name}")
    if level not in SPELL_SLOTS[class_name]:
        raise ValueError(f"Invalid level: {level}")

    return SPELL_SLOTS[class_name][level]
