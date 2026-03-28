from unittest.mock import MagicMock

import pytest

from rpgleveler.core import ClassName, Race
from rpgleveler.data import (
    get_attack_bonus,
    get_saving_throws,
    get_spell_slots,
    get_thief_skills,
    get_turn_undead,
)
from rpgleveler.engine.leveler import level_up
from rpgleveler.shared import AbilityScores, Character


def make_character(class_name: ClassName) -> Character:
    return Character(
        abilities=AbilityScores(10, 10, 10, 10, 10, 10),
        ability_mods={"STR": 0},
        ac=10,
        attack_bonus=get_attack_bonus(class_name, 1),
        class_name=class_name,
        hp=5,
        inventory=[],
        level=1,
        money_gp=100,
        name=f"{class_name} tester",
        race=Race.HUMAN,
        saving_throws=get_saving_throws(class_name, Race.HUMAN, 1),
        xp=999999,  # always enough to level
    )


@pytest.mark.parametrize("class_name", list(ClassName))
def test_level_up_multi_level_progression(class_name: ClassName):
    character = make_character(class_name)

    rng = MagicMock()
    rng.roll.return_value = 4  # deterministic HP gain

    previous_hp = character.hp
    previous_attack = character.attack_bonus

    # 🔥 Walk levels 1 → 5
    for expected_level in range(2, 6):
        new_char, result = level_up(character, rng=rng)

        # -------------------------
        # Level progression
        # -------------------------
        assert new_char.level == expected_level
        assert result.new_level == expected_level
        assert result.old_level == expected_level - 1

        # -------------------------
        # HP progression (monotonic)
        # -------------------------
        assert new_char.hp > previous_hp
        assert result.new_hp_total == new_char.hp
        previous_hp = new_char.hp

        # -------------------------
        # Attack bonus matches table
        # -------------------------
        expected_attack = get_attack_bonus(class_name, expected_level)
        assert new_char.attack_bonus == expected_attack
        assert result.new_attack_bonus == expected_attack

        # optional monotonic check (fighters should increase, others may plateau)
        assert new_char.attack_bonus >= previous_attack
        previous_attack = new_char.attack_bonus

        # -------------------------
        # Saving throws
        # -------------------------
        expected_saves = get_saving_throws(class_name, Race.HUMAN, expected_level)
        assert new_char.saving_throws == expected_saves
        assert result.saving_throws == expected_saves

        # -------------------------
        # Spell slots (casters only)
        # -------------------------
        expected_spells = get_spell_slots(class_name, expected_level)
        assert new_char.spell_slots == expected_spells
        assert result.new_spell_slots == expected_spells

        # -------------------------
        # Thief skills (always present)
        # -------------------------
        expected_thief = get_thief_skills(class_name, expected_level)
        assert new_char.thief_skills == expected_thief

        # -------------------------
        # Turn undead (cleric only)
        # -------------------------
        expected_turn = get_turn_undead(class_name, expected_level)
        assert new_char.turn_undead == expected_turn
        assert result.turn_undead == expected_turn

        # -------------------------
        # Immutability
        # -------------------------
        assert new_char is not character

        # advance loop
        character = new_char
