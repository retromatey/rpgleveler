"""
Turn Undead progression tables for Basic Fantasy RPG.

This module defines the effectiveness of a cleric's ability to turn undead by
level. The data is derived directly from the official Basic Fantasy RPG class
progression tables.

Structure:
    TURN_UNDEAD[class_name][level] -> TurnUndead

Where:
    - class_name is a `ClassName` enum
    - level is the character level (int)
    - `TurnUndead` contains turn results for each undead type

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
    - Only clerics can turn undead; other classes have no effect (all values
      None).
    - Lower numeric values indicate better effectiveness.
    - Results improve as level increases.
    - Data is treated as immutable game rules.

Implementation details:
    - Raw data is defined in mutable dictionaries for readability.
    - Data is wrapped using `MappingProxyType` to enforce runtime immutability.
    - `TurnUndead` is a frozen dataclass.
    - Consumers should use `get_turn_undead()` rather than accessing tables
      directly.

Example:
    >>> get_turn_undead(ClassName.CLERIC, 5)
    TurnUndead(skeleton=5, zombie=9, ...)
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Final, Literal

from rpgleveler.core import ClassName

# Special turn undead result values.
type TurnResult = int | Literal["T", "D"] | None


@dataclass(frozen=True)
class TurnUndead:
    """
    Immutable container for turn undead results.

    Each field represents the effectiveness of turning a specific undead type.

    Values:
        - int: Target number to roll on d20 (lower is better)
        - "T": Automatic success (turn)
        - "D": Destroy undead
        - None: Cannot affect this undead type

    Attributes:
        skeleton: Turn result for skeletons
        zombie: Turn result for zombies
        ghoul: Turn result for ghouls
        wight: Turn result for wights
        wraith: Turn result for wraiths
        mummy: Turn result for mummies
        spectre: Turn result for spectres
        vampire: Turn result for vampires
    """
    skeleton: TurnResult
    zombie: TurnResult
    ghoul: TurnResult
    wight: TurnResult
    wraith: TurnResult
    mummy: TurnResult
    spectre: TurnResult
    vampire: TurnResult


type TurnUndeadByLevel = dict[int, TurnUndead]
"""Mapping of level → turn undead data."""


type TurnUndeadByClassName = dict[ClassName, TurnUndeadByLevel]
"""Mapping of class → level-based turn undead progression."""


# Turn undead progression table.
# Values are derived from Basic Fantasy RPG class tables.
# This data is treated as immutable game rules.
_raw_turn_undead: Final[TurnUndeadByClassName] = {
    ClassName.CLERIC: {
        1:  TurnUndead(skeleton=13,  zombie=17,  ghoul=None, wight=None, wraith=None, mummy=None, spectre=None, vampire=None),
        2:  TurnUndead(skeleton=11,  zombie=15,  ghoul=19,   wight=None, wraith=None, mummy=None, spectre=None, vampire=None),
        3:  TurnUndead(skeleton=9,   zombie=13,  ghoul=17,   wight=None, wraith=None, mummy=None, spectre=None, vampire=None),
        4:  TurnUndead(skeleton=7,   zombie=11,  ghoul=15,   wight=19,   wraith=None, mummy=None, spectre=None, vampire=None),
        5:  TurnUndead(skeleton=5,   zombie=9,   ghoul=13,   wight=17,   wraith=None, mummy=None, spectre=None, vampire=None),
        6:  TurnUndead(skeleton=3,   zombie=7,   ghoul=11,   wight=15,   wraith=19,   mummy=None, spectre=None, vampire=None),
        7:  TurnUndead(skeleton=2,   zombie=5,   ghoul=9,    wight=13,   wraith=17,   mummy=None, spectre=None, vampire=None),
        8:  TurnUndead(skeleton="T", zombie=3,   ghoul=7,    wight=11,   wraith=15,   mummy=19,   spectre=None, vampire=None),
        9:  TurnUndead(skeleton="T", zombie=2,   ghoul=5,    wight=9,    wraith=13,   mummy=17,   spectre=None, vampire=None),
        10: TurnUndead(skeleton="D", zombie="T", ghoul=3,    wight=7,    wraith=11,   mummy=15,   spectre=19,   vampire=None),
        11: TurnUndead(skeleton="D", zombie="T", ghoul=2,    wight=5,    wraith=9,    mummy=13,   spectre=17,   vampire=None),
        12: TurnUndead(skeleton="D", zombie="D", ghoul="T",  wight=3,    wraith=7,    mummy=11,   spectre=15,   vampire=19),
        13: TurnUndead(skeleton="D", zombie="D", ghoul="T",  wight=2,    wraith=5,    mummy=9,    spectre=13,   vampire=17),
        14: TurnUndead(skeleton="D", zombie="D", ghoul="D",  wight="T",  wraith=3,    mummy=7,    spectre=11,   vampire=15),
        15: TurnUndead(skeleton="D", zombie="D", ghoul="D",  wight="T",  wraith=2,    mummy=5,    spectre=9,    vampire=13),
        16: TurnUndead(skeleton="D", zombie="D", ghoul="D",  wight="D",  wraith="T",  mummy=3,    spectre=7,    vampire=11),
        17: TurnUndead(skeleton="D", zombie="D", ghoul="D",  wight="D",  wraith="T",  mummy=2,    spectre=5,    vampire=9),
        18: TurnUndead(skeleton="D", zombie="D", ghoul="D",  wight="D",  wraith="D",  mummy="T",  spectre=3,    vampire=7),
        19: TurnUndead(skeleton="D", zombie="D", ghoul="D",  wight="D",  wraith="D",  mummy="T",  spectre=2,    vampire=5),
        20: TurnUndead(skeleton="D", zombie="D", ghoul="D",  wight="D",  wraith="D",  mummy="D",  spectre="T",  vampire=3),
    },
    ClassName.FIGHTER: {
        lvl: TurnUndead(*(None,)*8) for lvl in range(1, 21) 
    },
    ClassName.MAGIC_USER: {
        lvl: TurnUndead(*(None,)*8) for lvl in range(1, 21) 
    },
    ClassName.THIEF: {
        lvl: TurnUndead(*(None,)*8) for lvl in range(1, 21) 
    },
}


def _freeze(
    data: TurnUndeadByClassName,
) -> MappingProxyType[ClassName, MappingProxyType[int, TurnUndead]]:
    """
    Convert nested turn undead data into immutable mappings.

    Both the outer mapping (class → levels) and inner mappings (level → turn
    results) are wrapped in `MappingProxyType` to prevent modification at
    runtime.

    Args:
        data: Mutable turn undead data.

    Returns:
        A fully read-only nested mapping structure.
    """
    return MappingProxyType({
        cls: MappingProxyType(levels) for cls, levels in data.items()
    })


# Public, immutable turn undead table.
TURN_UNDEAD = _freeze(_raw_turn_undead)


def get_turn_undead(class_name: ClassName, level: int) -> TurnUndead:
    """
    Retrieve turn undead results for a given class and level.

    This function provides a safe access layer over the turn undead table,
    ensuring invalid inputs are handled consistently.

    Args:
        class_name: The character class.
        level: The character level (1–20).

    Returns:
        A `TurnUndead` instance representing turn results.

    Raises:
        ValueError: If the class or level is not present in the table.

    Example:
        >>> get_turn_undead(ClassName.CLERIC, 10)
        TurnUndead(skeleton="D", zombie="T", ...)
    """
    if class_name not in TURN_UNDEAD:
        raise ValueError(f"Invalid class: {class_name}")
    if level not in TURN_UNDEAD[class_name]:
        raise ValueError(f"Invalid level: {level}")

    return TURN_UNDEAD[class_name][level]
