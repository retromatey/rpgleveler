from dataclasses import dataclass

from rpgleveler.core.class_names import ClassName
from rpgleveler.core.races import Race
from rpgleveler.core.saving_throw_data import SavingThrowData
from rpgleveler.core.spell_slots import SpellSlots
from rpgleveler.core.thief_skills import ThiefSkills
from rpgleveler.core.turn_undead import TurnUndead


@dataclass
class LevelUpResult:
    """Represents the outcome of a single level-up operation.

    This object provides a structured summary of the updated character state
    after advancing from one level to the next. It is returned by the level-up
    engine alongside the newly constructed Character instance.

    The design mirrors the Character model: all fields are always present, and
    class-specific features are represented using neutral/default values rather
    than being omitted.

    This ensures a consistent, predictable structure for consumers such as CLI
    output, logging, or UI rendering.

    Attributes:
        class_name:
            The character's class.

        race:
            The character's race.

        old_level:
            The character's level prior to leveling up.

        new_level:
            The character's level after leveling up.

        hp_gained:
            The number of hit points gained during this level-up.

        new_hp_total:
            The character's total hit points after applying the HP gain.

        new_attack_bonus:
            The updated attack bonus for the new level.

        saving_throws:
            The updated saving throw values for the new level.

        new_spell_slots:
            Spell slots available at the new level.
            Non-spellcasting classes contain zero values.

        thief_skills:
            Thief skill percentages at the new level.
            Non-thief classes contain zero values.

        turn_undead:
            Turn undead effectiveness at the new level.
            Non-cleric classes contain only None values.

    Notes:
        - This object represents the resulting state after leveling up,
          not a field-by-field delta.
        - Hit point gain is included explicitly, as it is a rolled value.
        - All attributes are always populated to maintain a uniform data shape.
    """
    class_name: ClassName
    race: Race
    old_level: int
    new_level: int

    hp_gained: int
    new_hp_total: int

    new_attack_bonus: int
    saving_throws: SavingThrowData

    new_spell_slots: SpellSlots = SpellSlots(0,0,0,0,0)
    thief_skills: ThiefSkills = ThiefSkills(0,0,0,0,0,0,0,0)
    turn_undead: TurnUndead = TurnUndead(*(None,)*8)
