"""
Progression table access for Basic Fantasy RPG.

This module provides a consistent interface for retrieving class-based
progression data such as attack bonuses, saving throws, spell slots, thief
skills, and turn undead effectiveness.

These functions act as a thin abstraction layer over the underlying data tables,
allowing the level-up engine to remain decoupled from direct table access.

Structure:
    - get_attack_bonus: Attack bonus progression
    - get_saving_throws: Saving throw progression
    - apply_saving_throw_modifiers: Apply modifiers to saving throws by race
    - get_spell_slots: Spell slot progression (casters only)
    - get_thief_skills: Thief skill progression (thief only)
    - get_turn_undead: Turn undead progression (cleric only)

Notes:
    - All functions are pure and side-effect free.
    - Class-specific functions return None when not applicable.
    - This module should be the only place where progression tables
      are accessed directly by the engine layer.
"""
from typing import cast

from rpgleveler.data import (
    get_attack_bonus,
    get_saving_throws,
    get_spell_slots,
    get_thief_skills,
    get_turn_undead,
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)
from rpgleveler.shared import ClassName, Race


def get_attack_bonus(class_name: ClassName, level: int) -> int:
    """
    Return the attack bonus for the given class and level.

    Args:
        class_name:
            The character class.
        level:
            The character level.

    Returns:
        int:
            The attack bonus value for the specified class and level.

    Raises:
        KeyError:
            If the class or level is not found in the progression table.
    """
    raise NotImplemented


def get_saving_throws(class_name: ClassName, level: int) -> SavingThrowData:
    """
    Return saving throw values for the given class and level.

    Args:
        class_name:
            The character class.
        level:
            The character level.

    Returns:
        SavingThrowData:
            A mapping of saving throw categories to target values.

    Raises:
        KeyError:
            If the class or level is not found in the progression table.
    """
    raise NotImplemented


def apply_saving_throw_modifiers(
    base_saving_throws: SavingThrowData,
    race: RaceName,
) -> SavingThrowData:
    """
    Apply racial modifiers to base saving throw values.

    This function combines class-based saving throw values with any
    race-specific modifiers to produce the final saving throw targets for a
    character.

    The base values are typically derived from class progression tables, while
    modifiers are defined per race and applied additively.

    Args:
        base_saving_throws:
            The base saving throw values for a given class and level.
        race:
            The character's race.

    Returns:
        SavingThrowData:
            A new mapping of saving throw categories to final values
            after applying racial modifiers.

    Notes:
        - Lower saving throw values are better in Basic Fantasy RPG.
        - Negative modifiers improve saving throws (reduce target number).
        - Positive modifiers worsen saving throws (increase target number).
        - If a race has no defined modifiers, the base values are returned
          unchanged.
        - This function does not mutate the input data; a new mapping is
          returned.

    Example:
        Base (fighter, level 5):
            {"death_ray_or_poison": 12, "magic_wands": 13, ...}

        Dwarf modifiers:
            {"death_ray_or_poison": -2, "magic_wands": -1, ...}

        Result:
            {"death_ray_or_poison": 10, "magic_wands": 12, ...}
    """
    raise NotImplemented


def get_spell_slots(class_name: ClassName, level: int) -> SpellSlots:
    """
    Return spell slots for the given class and level.

    Args:
        class_name:
            The character class.
        level:
            The character level.

    Returns:
        SpellSlotRow | None:
            A tuple representing spell slots by spell level (1–5),
            or None if the class does not cast spells.

    Notes:
        - Only clerics and magic-users have spell slots.
    """
    raise NotImplemented


def get_thief_skills(class_name: ClassName, level: int) -> ThiefSkills:
    """
    Return thief skill values for the given class and level.

    Args:
        class_name:
            The character class.
        level:
            The character level.

    Returns:
        ThiefSkillData | None:
            A mapping of thief skills to percentage values,
            or None if the class is not a thief.
    """
    raise NotImplemented


def get_turn_undead(class_name: ClassName, level: int) -> TurnUndead:
    """
    Return turn undead effectiveness for the given class and level.

    Args:
        class_name:
            The character class.
        level:
            The character level.

    Returns:
        TurnUndeadData | None:
            A mapping of undead types to turn results,
            or None if the class is not a cleric.

    Notes:
        - Turn results may be integers (target rolls), "T" (turn),
          or "D" (destroy).
    """
    raise NotImplemented
