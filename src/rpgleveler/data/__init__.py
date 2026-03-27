"""
TODO: add comments for shared module
"""

from rpgleveler.data.attack_bonus import ATTACK_BONUS, get_attack_bonus
from rpgleveler.data.saving_throws import (
    SAVING_THROWS, 
    SAVING_THROW_MODIFIERS, 
    get_saving_throws,
)
from rpgleveler.data.spell_slots import SPELL_SLOTS, get_spell_slots

__all__ = [
    "ATTACK_BONUS",
    "SAVING_THROWS", 
    "SAVING_THROW_MODIFIERS", 
    "SPELL_SLOTS",
    "get_attack_bonus",
    "get_saving_throws",
    "get_spell_slots",
]
