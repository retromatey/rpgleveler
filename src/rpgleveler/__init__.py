"""
Public API for rpgleveler.

This module exposes the primary interfaces for leveling up characters
and interacting with the level-up engine.

Typical usage:

    from rpgleveler import level_up

    new_character, result = level_up(character, rng=rng)
"""

from rpgleveler.core.character import Character
from rpgleveler.core.level_up_result import LevelUpResult
from rpgleveler.engine.advancement import can_level_up
from rpgleveler.engine.leveler import level_up

__all__ = [
    "Character",
    "LevelUpResult",
    "can_level_up",
    "level_up",
]
