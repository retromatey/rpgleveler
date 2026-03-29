from dataclasses import dataclass
from typing import Any

from rpgleveler.core import (
    ClassName,
    Race,
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)


@dataclass
class AbilityScores:
    """Container for the six Basic Fantasy ability scores.

    This structure holds the raw ability values for a character. These scores
    are used to derive modifiers and influence various gameplay mechanics.

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
    """Represents a character's complete game state at a given level.

    This object is the authoritative snapshot of a character, containing both
    base attributes (such as ability scores) and all derived statistics (such as
    hit points, attack bonus, and saving throws).

    The design intentionally avoids optional or class-specific fields. All
    characters possess the same set of attributes, with non-applicable features
    represented by default or neutral values (e.g., zeroed spell slots).

    This approach simplifies downstream logic by eliminating the need for
    conditional checks based on class.

    Attributes:
        abilities:
            The character's raw ability scores.

        ability_mods:
            Ability modifiers keyed by ability name (e.g., "STR", "DEX").

        ac:
            Armor Class at the current state.

        attack_bonus:
            Attack bonus applied to attack rolls.

        class_name:
            Canonical lowercase class identifier.

        hp:
            Current hit points.

        inventory:
            List of carried item names.

        level:
            Current character level.

        money_gp:
            Current wealth in gold pieces.

        name:
            Optional character name.

        race:
            Canonical race identifier.

        saving_throws:
            Saving throw targets keyed by saving throw category.

        xp:
            Total accumulated experience points.

        spell_slots:
            Spell slots available by spell level (levels 1–5).
            Non-spellcasting classes have all values set to zero.

        thief_skills:
            Percentile values for thief abilities.
            Non-thief classes have all values set to zero.

        turn_undead:
            Turn undead effectiveness values by undead type.
            Non-cleric classes contain only None values.
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
    race: Race
    saving_throws: SavingThrowData
    xp: int
    spell_slots: SpellSlots = SpellSlots(0,0,0,0,0)
    thief_skills: ThiefSkills = ThiefSkills(0,0,0,0,0,0,0,0)
    turn_undead: TurnUndead = TurnUndead(*(None,)*8)

    def to_dict(self) -> dict[str, Any]:
        """Serialize the character into a JSON-friendly dictionary.

        This method converts the Character into a structure suitable for JSON
        encoding. Nested data structures are included as-is and may require
        their own serialization methods.

        Returns:
            dict[str, Any]: A dictionary containing character data, including
                identity, progression stats, combat values, and inventory.
        """
        return {
            "name": self.name,
            "race": self.race.value,
            "class": self.class_name.value,
            "level": self.level,
            "xp": self.xp,
            "abilities": vars(self.abilities),
            "ability_mods": self.ability_mods,
            "hp": self.hp,
            "ac": self.ac,
            "attack_bonus": self.attack_bonus,
            "saving_throws": self.saving_throws.to_dict(),
            "spell_slots": self.spell_slots.to_dict(),
            "thief_skills": self.thief_skills.to_dict(),
            "turn_undead": self.turn_undead.to_dict(),
            "money_gp": self.money_gp,
            "inventory": self.inventory,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Character:
        return cls(
            name=data["name"],
            race=Race(data["race"]),
            class_name=ClassName(data["class"]),
            level=data["level"],
            xp=data["xp"],
            abilities=AbilityScores(**data["abilities"]),
            ability_mods=data["ability_mods"],
            hp=data["hp"],
            ac=data["ac"],
            attack_bonus=data["attack_bonus"],
            saving_throws=SavingThrowData.from_dict(data["saving_throws"]),
            spell_slots=SpellSlots.from_dict(data["spell_slots"]),
            thief_skills=ThiefSkills.from_dict(data["thief_skills"]),
            turn_undead=TurnUndead.from_dict(data["turn_undead"]),
            money_gp=data["money_gp"],
            inventory=data["inventory"],
        )
