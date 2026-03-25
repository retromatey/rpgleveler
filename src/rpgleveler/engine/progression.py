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

from rpgleveler.data.attack_bonus import ATTACK_BONUS
from rpgleveler.data.saving_throws import (
    clone_saving_throws,
    SAVING_THROW_MODIFIERS,
    SAVING_THROWS,
    SavingThrowData,
)
from rpgleveler.data.spell_slots import SPELL_SLOTS, SpellSlotRow
from rpgleveler.data.thief_skills import THIEF_SKILLS, ThiefSkillData
from rpgleveler.data.turn_undead import TURN_UNDEAD, TurnUndeadData
from rpgleveler.shared.literals import ClassName, RaceName


def _normalize_class_name(class_name: str) -> str:
    """Normalize common external class aliases to canonical table keys."""
    if class_name == "magic_user":
        return "magic-user"
    return class_name


def _class_key(class_name: ClassName, table: dict[ClassName, object]) -> ClassName:
    normalized = _normalize_class_name(class_name)
    if normalized not in table:
        raise KeyError(normalized)
    return cast(ClassName, normalized)


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
    class_key = _class_key(class_name, cast(dict[ClassName, object], ATTACK_BONUS))
    return ATTACK_BONUS[class_key][level]


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
    class_key = _class_key(class_name, cast(dict[ClassName, object], SAVING_THROWS))
    return clone_saving_throws(SAVING_THROWS[class_key][level])


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
    result = cast(dict[str, int], dict(cast(dict[str, int], base_saving_throws)))
    modifiers = SAVING_THROW_MODIFIERS.get(race)
    if modifiers is None:
        return cast(SavingThrowData, result)

    for key, value in result.items():
        result[key] = value + cast(int, modifiers.get(key, 0))
    return cast(SavingThrowData, result)


def get_spell_slots(class_name: ClassName, level: int) -> SpellSlotRow | None:
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
    table_class = _normalize_class_name(class_name)
    if table_class not in SPELL_SLOTS:
        return None
    class_key = _class_key(class_name, cast(dict[ClassName, object], SPELL_SLOTS))
    return SPELL_SLOTS[class_key][level]


def get_thief_skills(class_name: ClassName, level: int) -> ThiefSkillData | None:
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
    table_class = _normalize_class_name(class_name)
    if table_class == "thief":
        return cast(ThiefSkillData, THIEF_SKILLS[level].copy())
    if table_class in {"cleric", "fighter", "magic-user"}:
        return None
    raise KeyError(table_class)


def get_turn_undead(class_name: ClassName, level: int) -> TurnUndeadData | None:
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
    table_class = _normalize_class_name(class_name)
    if table_class == "cleric":
        return cast(TurnUndeadData, TURN_UNDEAD[level].copy())
    if table_class in {"fighter", "magic-user", "thief"}:
        return None
    raise KeyError(table_class)
