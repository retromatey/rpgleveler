"""
TODO: add comments here...
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Final

from rpgleveler.shared import ClassName


@dataclass(frozen=True)
class SpellSlots:
    """Represents spell slots for levels 1-5."""
    level_1: int
    level_2: int
    level_3: int
    level_4: int
    level_5: int


type SpellSlotsByLevel = dict[int, SpellSlots]
"""Mapping of character level to spell slot progression."""


type SpellSlotsByClassName = dict[ClassName, SpellSlotsByLevel]
"""Mapping of spells slots to class names."""


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
    TODO: add comments
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


# Public, immutable spell slots table.
SPELL_SLOTS = _freeze(_raw_spell_slots)


def get_spell_slots(class_name: ClassName, level: int) -> SpellSlots:
    """
    TODO: add comments...
    """
    try:
        return SPELL_SLOTS[class_name][level]
    except KeyError:
        err_msg = f"Invalid class/level combination: {class_name}, {level}"
        raise ValueError(err_msg)
