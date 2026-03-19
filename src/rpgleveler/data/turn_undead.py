"""
Turn Undead progression table for Basic Fantasy RPG.

This module defines the effectiveness of a cleric's ability to turn undead by
level. The data is derived directly from the official Basic Fantasy RPG class
tables.

Structure:
    TURN_UNDEAD[level] -> TurnUndeadData

Where:
    - level is the cleric level (int)
    - TurnUndeadData maps undead types to turn results

Turn result values:
    - int  : target number to roll on d20 (lower is better)
    - "T"  : automatic success (turn)
    - "D"  : destroy undead
    - None : cannot affect this undead type

Undead categories:
    - skeleton
    - zombie
    - ghoul
    - wight
    - wraith
    - mummy
    - spectre
    - vampire

Notes:
    - This table applies only to clerics.
    - Lower numeric values are better.
    - Results improve as cleric level increases.
    - The data is static and should not be modified at runtime.
"""

from __future__ import annotations

from typing import Final, Literal, TypedDict

# Special turn undead result values.
type TurnResult = int | Literal["T", "D"] | None


class TurnUndeadData(TypedDict):
    """Turn undead results for all undead types at a given level."""
    skeleton: TurnResult
    zombie: TurnResult
    ghoul: TurnResult
    wight: TurnResult
    wraith: TurnResult
    mummy: TurnResult
    spectre: TurnResult
    vampire: TurnResult


# Mapping of cleric level to turn undead effectiveness.
type TurnUndeadTable = dict[int, TurnUndeadData]


# Turn undead progression table.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
TURN_UNDEAD: Final[TurnUndeadTable] = {
    1:  {"skeleton": 13, "zombie": 17, "ghoul": None, "wight": None, "wraith": None, "mummy": None, "spectre": None, "vampire": None},
    2:  {"skeleton": 11, "zombie": 15, "ghoul": 19,  "wight": None, "wraith": None, "mummy": None, "spectre": None, "vampire": None},
    3:  {"skeleton": 9,  "zombie": 13, "ghoul": 17,  "wight": None, "wraith": None, "mummy": None, "spectre": None, "vampire": None},
    4:  {"skeleton": 7,  "zombie": 11, "ghoul": 15,  "wight": 19,  "wraith": None, "mummy": None, "spectre": None, "vampire": None},
    5:  {"skeleton": 5,  "zombie": 9,  "ghoul": 13,  "wight": 17,  "wraith": None, "mummy": None, "spectre": None, "vampire": None},
    6:  {"skeleton": 3,  "zombie": 7,  "ghoul": 11,  "wight": 15,  "wraith": 19,  "mummy": None, "spectre": None, "vampire": None},
    7:  {"skeleton": 2,  "zombie": 5,  "ghoul": 9,   "wight": 13,  "wraith": 17,  "mummy": None, "spectre": None, "vampire": None},
    8:  {"skeleton": "T","zombie": 3,  "ghoul": 7,   "wight": 11,  "wraith": 15,  "mummy": 19,  "spectre": None, "vampire": None},
    9:  {"skeleton": "T","zombie": 2,  "ghoul": 5,   "wight": 9,   "wraith": 13,  "mummy": 17,  "spectre": None, "vampire": None},
    10: {"skeleton": "D","zombie": "T","ghoul": 3,   "wight": 7,   "wraith": 11,  "mummy": 15,  "spectre": 19,  "vampire": None},
    11: {"skeleton": "D","zombie": "T","ghoul": 2,   "wight": 5,   "wraith": 9,   "mummy": 13,  "spectre": 17,  "vampire": None},
    12: {"skeleton": "D","zombie": "D","ghoul": "T","wight": 3,   "wraith": 7,   "mummy": 11,  "spectre": 15,  "vampire": 19},
    13: {"skeleton": "D","zombie": "D","ghoul": "T","wight": 2,   "wraith": 5,   "mummy": 9,   "spectre": 13,  "vampire": 17},
    14: {"skeleton": "D","zombie": "D","ghoul": "D","wight": "T","wraith": 3,   "mummy": 7,   "spectre": 11,  "vampire": 15},
    15: {"skeleton": "D","zombie": "D","ghoul": "D","wight": "T","wraith": 2,   "mummy": 5,   "spectre": 9,   "vampire": 13},
    16: {"skeleton": "D","zombie": "D","ghoul": "D","wight": "D","wraith": "T","mummy": 3,   "spectre": 7,   "vampire": 11},
    17: {"skeleton": "D","zombie": "D","ghoul": "D","wight": "D","wraith": "T","mummy": 2,   "spectre": 5,   "vampire": 9},
    18: {"skeleton": "D","zombie": "D","ghoul": "D","wight": "D","wraith": "D","mummy": "T","spectre": 3,   "vampire": 7},
    19: {"skeleton": "D","zombie": "D","ghoul": "D","wight": "D","wraith": "D","mummy": "T","spectre": 2,   "vampire": 5},
    20: {"skeleton": "D","zombie": "D","ghoul": "D","wight": "D","wraith": "D","mummy": "D","spectre": "T","vampire": 3},
}
