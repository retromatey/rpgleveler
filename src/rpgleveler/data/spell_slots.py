"""
Spell slot progression tables for Basic Fantasy RPG.

This module defines the number of spell slots available to each spellcasting
class at each level. The data is derived directly from the official Basic
Fantasy RPG class progression tables.

Structure:
    SPELL_SLOTS[class_name][level] -> SpellSlotRow

Where:
    - class_name is a ClassName literal (e.g., "cleric", "magic-user")
    - level is the character level (int)
    - SpellSlotRow is a fixed-length tuple representing spell slots per spell
      level

SpellSlotRow format:
    (level_1, level_2, level_3, level_4, level_5)

Notes:
    - Only spellcasting classes are included in this table.
    - Non-spellcasting classes (e.g., fighter, thief) are omitted.
    - Clerics begin spellcasting at level 2.
    - The data is static and should not be modified at runtime.
"""

from __future__ import annotations

from typing import Final

from rpgleveler.shared.literals import ClassName

# Fixed-length tuple representing spell slots for spell levels 1–5.
type SpellSlotRow = tuple[int, int, int, int, int]


# Mapping of character level to spell slot progression.
type SpellSlotsByLevel = dict[int, SpellSlotRow]


# Spell slot progression tables keyed by class name.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
SPELL_SLOTS: Final[dict[ClassName, SpellSlotsByLevel]] = {
    "cleric": {
        1:  (0,0,0,0,0), # Clerics do not gain spells until level 2
        2:  (1,0,0,0,0),
        3:  (2,0,0,0,0),
        4:  (2,1,0,0,0),
        5:  (2,2,0,0,0),
        6:  (2,2,1,0,0),
        7:  (3,2,2,0,0),
        8:  (3,3,2,1,0),
        9:  (3,3,3,2,0),
        10: (4,3,3,2,1),
        11: (4,4,3,3,2),
        12: (4,4,4,3,2),
        13: (5,4,4,3,3),
        14: (5,5,4,4,3),
        15: (5,5,5,4,4),
        16: (6,5,5,4,4),
        17: (6,6,5,5,4),
        18: (6,6,6,5,5),
        19: (7,6,6,5,5),
        20: (7,7,6,6,5),
    },
    "magic-user": {
        1:  (1,0,0,0,0),
        2:  (2,0,0,0,0),
        3:  (2,1,0,0,0),
        4:  (2,2,0,0,0),
        5:  (2,2,1,0,0),
        6:  (2,2,2,0,0),
        7:  (3,2,2,1,0),
        8:  (3,3,2,2,0),
        9:  (3,3,3,2,1),
        10: (3,3,3,3,2),
        11: (4,3,3,3,2),
        12: (4,4,3,3,3),
        13: (4,4,4,3,3),
        14: (4,4,4,4,3),
        15: (5,4,4,4,4),
        16: (5,5,4,4,4),
        17: (5,5,5,4,4),
        18: (5,5,5,5,4),
        19: (6,5,5,5,5),
        20: (6,6,5,5,5),
    },
}
