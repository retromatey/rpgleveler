import pytest
from unittest.mock import MagicMock, patch

from rpgleveler.data import (
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)
from rpgleveler.engine.leveler import level_up, LevelUpError
from rpgleveler.shared import (
    AbilityScores,
    ClassName, 
    Race,
    Character,
    LevelUpResult,
)


# --- Fixtures -----------------------------------------------------------------

@pytest.fixture
def sample_character():
    return Character(
        name="Testy",
        race=Race.HUMAN,
        class_name=ClassName.FIGHTER,
        level=1,
        xp=9999,
        hp=10,
        attack_bonus=1,
        saving_throws=SavingThrowData(0,0,0,0,0)
        spell_slots=SpellSlots(0,0,0,0,0)
        thief_skills=ThiefSkills(0,0,0,0,0,0,0,0)
        turn_undead=TurnUndead(*(None,)*8)
        abilities=AbilityScores(0, 0, 0, 0, 0, 0),
        ability_mods={},
        ac=0,
        inventory=[],
        money_gp=0,
    )


@pytest.fixture
def rng():
    return MagicMock()


@pytest.fixture
def fully_mocked_leveler():
    with patch("rpgleveler.engine.leveler.can_level_up", return_value=True), \
         patch("rpgleveler.engine.leveler.roll_hp_gain", return_value=5), \
         patch("rpgleveler.engine.leveler.get_attack_bonus", return_value=2), \
         patch("rpgleveler.engine.leveler.get_saving_throws", return_value={"a": 1}), \
         patch("rpgleveler.engine.leveler.apply_saving_throw_modifiers", return_value={"a": 1}), \
         patch("rpgleveler.engine.leveler.get_spell_slots", return_value=None), \
         patch("rpgleveler.engine.leveler.get_thief_skills", return_value=None), \
         patch("rpgleveler.engine.leveler.get_turn_undead", return_value=None):
        yield


# --- Tests --------------------------------------------------------------------

def test_raises_if_cannot_level(sample_character, rng):
    with patch("rpgleveler.engine.leveler.can_level_up", return_value=False):
        with pytest.raises(LevelUpError):
            level_up(sample_character, rng=rng)


def test_level_is_incremented(sample_character, rng, fully_mocked_leveler):
    new_character, _ = level_up(sample_character, rng=rng)
    assert new_character.level == 2


def test_hp_is_applied(sample_character, rng, fully_mocked_leveler):
    new_character, result = level_up(sample_character, rng=rng)
    assert new_character.hp == 15
    assert result.hp_gained == 5


def test_attack_bonus_is_applied(sample_character, rng, fully_mocked_leveler):
    new_character, _ = level_up(sample_character, rng=rng)
    assert new_character.attack_bonus == 2


def test_original_character_not_modified(sample_character, rng, fully_mocked_leveler):
    original_hp = sample_character.hp
    level_up(sample_character, rng=rng)
    assert sample_character.hp == original_hp


def test_result_contains_correct_levels(sample_character, rng, fully_mocked_leveler):
    _, result = level_up(sample_character, rng=rng)
    assert result.old_level == 1
    assert result.new_level == 2
