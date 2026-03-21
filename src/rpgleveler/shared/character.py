from dataclasses import dataclass, fields
from typing import Any, cast

from rpgleveler.data.saving_throws import SavingThrowData
from rpgleveler.data.spell_slots import SpellSlotRow
from rpgleveler.data.thief_skills import ThiefSkillData
from rpgleveler.shared.literals import ClassName


@dataclass
class AbilityScores:
    """Container for the six Basic Fantasy ability scores.

    Attributes:
        CHA: Charisma score.
        CON: Constitution score.
        DEX: Dexterity score.
        INT: Intelligence score.
        STR: Strength score.
        WIS: Wisdom score.
    """

    CHA: int
    CON: int
    DEX: int
    INT: int
    STR: int
    WIS: int


@dataclass
class Character:
    """Represent a fully generated level-1 character.

    The object contains the character's rolled abilities along with all derived
    statistics such as hit points, armor class, attack bonus, saving throws, and
    starting wealth.

    Attributes:
        abilities: 
            Rolled or assigned ability scores.

        ability_mods: 
            Ability modifiers keyed by ability name.

        ac: 
            Final armor class value at the current state.

        attack_bonus: 
            Attack bonus applied to attack rolls.

        class_name: 
            Normalized class name (lowercase).

        hp: 
            Current hit points.

        inventory: 
            Carried items as display names.

        level: 
            Character level.

        money_gp: 
            Current wealth in gold pieces.

        name: 
            Optional character name.

        race: 
            Normalized race name (lowercase).

        saving_throws: 
            Saving throw targets keyed by saving throw name.

        spell_slots:
            Available spell slots by spell level for spellcasting classes.
            Represented as a fixed-length tuple of integers (levels 1–5).  None
            for non-spellcasting classes.

        thief_skills:
            Percentage chances for each thief skill.
            Populated only for thief characters; None for other classes.
    """

    abilities: AbilityScores
    ability_mods: dict[str, int]
    ac: int
    attack_bonus: int
    class_name: ClassName
    hp: int
    inventory: list[str]
    level: int
    money_gp: int
    name: str | None
    race: str
    saving_throws: SavingThrowData
    spell_slots: SpellSlotRow | None = None
    thief_skills: ThiefSkillData | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize the character to a JSON-friendly dictionary.

        Returns:
            dict[str, Any]: Character data including abilities, combat values,
                money, and inventory.
        """
        return {
            "name": self.name,
            "race": self.race,
            "class": self.class_name,
            "level": self.level,
            "abilities": vars(self.abilities),
            "ability_mods": self.ability_mods,
            "hp": self.hp,
            "ac": self.ac,
            "attack_bonus": self.attack_bonus,
            "saving_throws": self.saving_throws,
            "spell_slots": self.spell_slots,
            "thief_skills": self.thief_skills,
            "money_gp": self.money_gp,
            "inventory": self.inventory,
        }
