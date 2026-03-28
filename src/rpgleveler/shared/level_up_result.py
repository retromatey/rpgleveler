from dataclasses import dataclass

from rpgleveler.data (
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)
from class_names import ClassName
from races import Race


@dataclass
class LevelUpResult:
    """Represents the outcome of a character leveling up.

    This data object captures all changes that occur when a character
    advances from one level to the next. It is returned by the level-up
    engine and provides a structured summary of updated character state.

    The result includes both universal changes (such as hit points,
    attack bonus, and saving throws) and optional class-specific updates
    (such as spell slots or thief skills).

    Attributes:
        class_name:
            The character's class.

        race:
            The character's race.

        old_level:
            The character's level before leveling up.

        new_level:
            The character's level after leveling up.

        hp_gained:
            The number of hit points gained during this level-up.

        new_hp_total:
            The character's total hit points after leveling up.

        new_attack_bonus:
            The updated attack bonus for the new level.

        saving_throws:
            The updated saving throw values for the new level.

        new_spell_slots:
            Updated spell slots for spellcasting classes.
            None for non-spellcasting classes.

        thief_skills:
            Updated thief skill percentages for thieves.
            None for non-thief classes.

        turn_undead:
            Turn undead effectiveness values for clerics.
            Maps undead types to turn results (target number, "T", or "D").
            None for non-cleric classes.

    Notes:
        - This object represents the *resulting state*, not the delta between
          old and new values (except for hit points gained).
        - Optional fields are only populated for relevant classes.
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
