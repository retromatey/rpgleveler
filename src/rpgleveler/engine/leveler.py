"""
Level-up engine for Basic Fantasy RPG.

This module orchestrates the process of advancing a character by one level.  It
coordinates validation, progression lookups, hit point calculation, and
construction of the updated character state.

The level-up process is intentionally structured as a pure transformation:
    - The input character is not modified
    - A new Character instance is returned
    - A LevelUpResult object summarizes the changes

Flow:
    1. Validate that the character can level up
    2. Determine the next level
    3. Calculate hit point gain
    4. Retrieve updated progression data
    5. Build a new Character instance
    6. Construct a LevelUpResult summary
    7. Return both the updated character and result

Notes:
    - This module contains no direct game rule logic.
    - Rule implementations are delegated to:
        - advancement.py (XP and level eligibility)
        - progression.py (table lookups)
        - hit_points.py (HP calculation)
    - This separation keeps the engine maintainable and testable.
"""
from dataclasses import replace

from diceroller.core import DiceRoller

from rpgleveler.data (
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)
from rpgleveler.shared import (
    ClassName, 
    Race,
    Character,
    LevelUpResult,
)
from advancement import can_level_up
from hit_points import roll_hp_gain
from progression import (
    apply_saving_throw_modifiers,
    get_attack_bonus,
    get_saving_throws,
    get_spell_slots,
    get_thief_skills,
    get_turn_undead,
)


class LevelUpError(Exception):
    """Raised when a character cannot level up."""


def level_up(
    character: Character, 
    *, 
    rng: DiceRoller
) -> tuple[Character, LevelUpResult]:
    """
    Apply a single level-up to a character.

    This function performs a complete level-up operation, returning both the
    updated character state and a structured summary of the changes.

    Args:
        character:
            The character to level up.
        rng:
            A DiceRoller instance used for hit point calculation.

    Returns:
        tuple[Character, LevelUpResult]:
            A tuple containing:
                - The new Character instance with updated values
                - A LevelUpResult describing the changes

    Raises:
        LevelUpError:
            If the character is not eligible to level up.

    Notes:
        - The original character is not modified.
        - All rule logic is delegated to engine submodules.
    """
    _validate_can_level_up(character)

    old_level = character.level
    new_level = character.level + 1

    hp_gained = roll_hp_gain(character, rng)
    new_hp_total = character.hp + hp_gained

    new_attack_bonus = get_attack_bonus(character.class_name, new_level)

    base_saves = get_saving_throws(character.class_name, new_level)
    saving_throws = apply_saving_throw_modifiers(base_saves, character.race)

    new_spell_slots = get_spell_slots(character.class_name, new_level)
    thief_skills = get_thief_skills(character.class_name, new_level)
    turn_undead = get_turn_undead(character.class_name, new_level)

    new_character = _build_new_character(
        character=character,
        new_level=new_level,
        new_hp_total=new_hp_total,
        new_attack_bonus=new_attack_bonus,
        saving_throws=saving_throws,
        new_spell_slots=new_spell_slots,
        thief_skills=thief_skills,
        turn_undead=turn_undead,
    )

    level_up_result = LevelUpResult(
        class_name=character.class_name,
        old_level=old_level,
        new_level=new_level,
        hp_gained=hp_gained,
        new_hp_total=new_hp_total,
        new_attack_bonus=new_attack_bonus,
        saving_throws=saving_throws,
        new_spell_slots=new_spell_slots,
        thief_skills=thief_skills,
        turn_undead=turn_undead,
    )

    return new_character, level_up_result


def _validate_can_level_up(character: Character) -> None:
    """
    Validate that a character is eligible to level up.

    This function delegates to the advancement module to determine whether the
    character meets XP and level requirements.

    Args:
        character:
            The character to validate.

    Raises:
        LevelUpError:
            If the character does not qualify for level advancement.
    """
    if not can_level_up(character):
        raise LevelUpError("Character cannot level up")


def _build_new_character(
    character: Character,
    *,
    new_level: int,
    new_hp_total: int,
    new_attack_bonus: int,
    saving_throws: SavingThrowData,
    new_spell_slots: SpellSlots,
    thief_skills: ThiefSkills,
    turn_undead: TurnUndead
) -> Character:
    """
    Construct a new Character instance with updated level-up values.

    This function uses dataclasses.replace to preserve immutability while
    updating only the fields affected by leveling.

    Args:
        character:
            The original character.
        new_level:
            The updated level.
        new_hp_total:
            Total hit points after applying the HP gain.
        new_attack_bonus:
            Updated attack bonus.
        saving_throws:
            Updated saving throw values.
        new_spell_slots:
            Updated spell slots (if applicable).
        thief_skills:
            Updated thief skill values (if applicable).
        turn_undead:
            Updated turn undead values (if applicable).

    Returns:
        Character:
            A new Character instance reflecting the updated state.

    Notes:
        - The original character is not modified.
        - Only level-dependent fields are updated.
    """
    return replace(
        character,
        level=new_level,
        hp=new_hp_total,
        attack_bonus=new_attack_bonus,
        saving_throws=saving_throws,
        spell_slots=new_spell_slots,
        thief_skills=thief_skills,
        turn_undead=turn_undead,
    )
