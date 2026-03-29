"""
TODO: add comments for shared module
"""

from rpgleveler.data.attack_bonus import get_attack_bonus
from rpgleveler.data.hit_dice import get_hit_dice
from rpgleveler.data.saving_throws import get_saving_throws
from rpgleveler.data.spell_slots import get_spell_slots
from rpgleveler.data.thief_skills import get_thief_skills
from rpgleveler.data.turn_undead import get_turn_undead
from rpgleveler.data.xp_tables import get_xp_requirement

__all__ = [
    "get_attack_bonus",
    "get_hit_dice",
    "get_saving_throws",
    "get_spell_slots",
    "get_thief_skills",
    "get_turn_undead",
    "get_xp_requirement",
]
