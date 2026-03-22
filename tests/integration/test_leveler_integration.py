import pytest
from unittest.mock import MagicMock, patch

from rpgleveler.engine.leveler import level_up
from rpgleveler.shared.character import Character, AbilityScores


@pytest.fixture
def sample_character():
    return Character(
        name="Testy",
        race="human",
        class_name="fighter",
        level=1,
        xp=9999,
        hp=10,
        attack_bonus=1,
        saving_throws=None,
        spell_slots=None,
        thief_skills=None,
        turn_undead=None,
        abilities=AbilityScores(0, 0, 0, 0, 0, 0),
        ability_mods={},
        ac=0,
        inventory=[],
        money_gp=0,
    )


def test_level_up_full_flow_not_implemented(sample_character):
    """
    This test ensures the full pipeline runs once implementations exist.
    Currently expected to fail due to NotImplementedError.
    """
    rng = MagicMock()
    with pytest.raises(NotImplementedError):
        level_up(sample_character, rng=rng)
