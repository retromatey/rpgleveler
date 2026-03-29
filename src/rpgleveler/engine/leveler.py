"""
Level-up engine for Basic Fantasy RPG.

This module orchestrates the process of advancing a character by one level.  It
coordinates validation, progression lookups, hit point calculation, and
construction of the updated character state.

The level-up process is intentionally implemented as a pure transformation:
    - The input Character is never modified
    - A new Character instance is returned
    - A LevelUpResult object summarizes the updated state

Flow:
    1. Validate that the character is eligible to level up
    2. Determine the next level
    3. Calculate hit point gain
    4. Retrieve updated progression data (attack bonus, saving throws, etc.)
    5. Construct a new Character instance
    6. Build a LevelUpResult summary
    7. Return both the updated character and result

Design principles:
    - No mutation: all updates produce new objects
    - No rule logic: this module delegates all game mechanics
    - Uniform data model: all progression fields are always populated, even for
      classes where the values are neutral (e.g., zero spell slots)

Delegation:
    - advancement.py:
        Determines level-up eligibility based on XP and rules
    - hit_points.py:
        Calculates hit point gains using a DiceRoller
    - rpgleveler.data:
        Provides progression table lookups

This separation keeps the engine modular, testable, and easy to extend.
"""
from dataclasses import replace

from diceroller.core import DiceRoller

from rpgleveler.core import (
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)
from rpgleveler.data import (
    get_attack_bonus,
    get_saving_throws,
    get_spell_slots,
    get_thief_skills,
    get_turn_undead,
)
from rpgleveler.engine.advancement import can_level_up
from rpgleveler.engine.hit_points import roll_hp_gain
from rpgleveler.shared import (
    Character,
    LevelUpResult,
)


class LevelUpError(Exception):
    """Raised when a character is not eligible to level up."""


def level_up(
    character: Character, 
    *, 
    rng: DiceRoller
) -> tuple[Character, LevelUpResult]:
    """
    Apply a single level-up to a character.

    This function performs a complete level-up operation, returning both the
    updated character state and a structured summary of the result.

    All progression data is retrieved through dedicated modules, ensuring that
    this function remains a pure orchestration layer.

    Args:
        character:
            The character to level up.
        rng:
            A DiceRoller instance used for hit point calculation.

    Returns:
        tuple[Character, LevelUpResult]:
            - A new Character instance reflecting the updated state
            - A LevelUpResult describing the outcome of the level-up

    Raises:
        LevelUpError:
            If the character is not eligible to level up.

    Notes:
        - The input character is never modified.
        - All progression fields are always populated.
        - Class-specific features (e.g., spell slots, thief skills) are
          represented using neutral/default values when not applicable.
    """
    _validate_can_level_up(character)

    old_level = character.level
    new_level = character.level + 1

    hp_gained = roll_hp_gain(character, rng)
    new_hp_total = character.hp + hp_gained

    new_attack_bonus = get_attack_bonus(character.class_name, new_level)

    saving_throws = get_saving_throws(
        character.class_name, character.race, new_level)

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
        race=character.race,
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
    Ensure that a character is eligible to level up.

    This function delegates eligibility checks to the advancement module, which
    evaluates XP thresholds and level constraints.

    Args:
        character:
            The character to validate.

    Raises:
        LevelUpError:
            If the character does not meet the requirements for advancement.
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
    Construct a new Character instance with updated level-dependent values.

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
            Updated spell slots.
        thief_skills:
            Updated thief skill values.
        turn_undead:
            Updated turn undead values.

    Returns:
        Character:
            A new Character instance reflecting the updated state.

    Notes:
        - The original character is not modified.
        - All fields are explicitly updated to maintain a complete, consistent
          character snapshot.
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
