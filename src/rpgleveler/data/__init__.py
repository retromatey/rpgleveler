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
from rpgleveler.data.thief_skills import THIEF_SKILLS, get_thief_skills
from rpgleveler.data.turn_undead import TURN_UNDEAD, get_turn_undead
from rpgleveler.data.xp_tables import XP_TABLES, get_xp_requirement

__all__ = [
    "ATTACK_BONUS",
    "SAVING_THROWS", 
    "SAVING_THROW_MODIFIERS", 
    "THIEF_SKILLS",
    "SPELL_SLOTS",
    "TURN_UNDEAD",
    "XP_TABLES",
    "get_attack_bonus",
    "get_saving_throws",
    "get_spell_slots",
    "get_thief_skills",
    "get_turn_undead",
    "get_xp_requirement",
]
