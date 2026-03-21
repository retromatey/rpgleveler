from dataclasses import replace

from diceroller.core import DiceRoller

from rpgleveler.data.saving_throws import SavingThrowData
from rpgleveler.data.spell_slots import SpellSlotRow
from rpgleveler.data.thief_skills import ThiefSkillData
from rpgleveler.shared.character import Character
from rpgleveler.shared.level_up_result import LevelUpResult


class LevelUpError(Exception):
    """Raised when a character cannot level up."""


def level_up(
    character: Character, 
    *, 
    rng: DiceRoller
) -> tuple[Character, LevelUpResult]:
    """
    Return a new character with one level applied, along with the result
    summary.
    """
    _validate_can_level_up(character)

    old_level = character.level
    new_level = character.level + 1

    hp_gained = _roll_hp_gain(character, rng)
    new_hp_total = character.hp + hp_gained

    new_attack_bonus = _get_attack_bonus_for_level(character.class_name, new_level)
    saving_throws = _get_saving_throws_for_level(character.class_name, new_level)

    new_spell_slots = _get_spell_slots_for_level(character.class_name, new_level)
    thief_skills = _get_thief_skills_for_level(character.class_name, new_level)

    new_character = _build_new_character(
        character=character,
        new_level=new_level,
        new_hp_total=new_hp_total,
        new_attack_bonus=new_attack_bonus,
        saving_throws=saving_throws,
        new_spell_slots=new_spell_slots,
        thief_skills=thief_skills,
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
    )

    return new_character, level_up_result


def _validate_can_level_up(character: Character) -> None:
    """Raise an error if the character is not eligible to level up."""
    raise NotImplementedError


def _roll_hp_gain(character: Character, rng: DiceRoller) -> int:
    """Roll hit point gain for the next level."""
    raise NotImplementedError


def _get_attack_bonus_for_level(class_name: ClassName, level: int) -> int:
    """Return the attack bonus for the given class and level."""
    raise NotImplementedError


def _get_saving_throws_for_level(
    class_name: ClassName, 
    level: int
) -> SavingThrowData:
    """Return saving throws for the given class and level."""
    raise NotImplementedError


def _get_spell_slots_for_level(
    class_name: ClassName, 
    level: int
) -> SpellSlotRow | None:
    """Return spell slots for the given class and level, if applicable."""
    raise NotImplementedError


def _get_thief_skills_for_level(
    class_name: ClassName, 
    level: int
) -> ThiefSkillData | None:
    """Return thief skills for the given class and level, if applicable."""
    raise NotImplementedError


def _build_new_character(
    character: Character,
    *,
    new_level: int,
    new_hp_total: int,
    new_attack_bonus: int,
    saving_throws: SavingThrowData,
    new_spell_slots: SpellSlotRow | None,
    thief_skills: ThiefSkillData | None,
) -> Character:
    """Return a new Character with updated level-up values."""

    # TODO: correct this code, but keep the "replace()" function here
    return replace(
        character,
        level=new_level,
        hp=new_hp_total,
        attack_bonus=new_attack_bonus,
        saving_throws=saving_throws,
        spell_slots=new_spell_slots,
        thief_skills=thief_skills,
    )
