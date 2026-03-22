import pytest

from rpgleveler.engine.advancement import (
    can_level_up,
    get_next_level_threshold,
    is_max_level,
    MAX_LEVEL,
)
from rpgleveler.shared.character import Character, AbilityScores


# --- Fixtures -----------------------------------------------------------------

@pytest.fixture
def base_character():
    return Character(
        name="Testy",
        race="human",
        class_name="fighter",
        level=1,
        xp=0,
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


# --- is_max_level -------------------------------------------------------------

def test_is_max_level_true_at_max():
    assert is_max_level(MAX_LEVEL) is True


def test_is_max_level_true_above_max():
    assert is_max_level(MAX_LEVEL + 1) is True


def test_is_max_level_false_below_max():
    assert is_max_level(MAX_LEVEL - 1) is False


# --- get_next_level_threshold -------------------------------------------------

def test_get_next_level_threshold_returns_int():
    result = get_next_level_threshold("fighter", 1)
    assert isinstance(result, int)


def test_get_next_level_threshold_invalid_class_raises():
    with pytest.raises(KeyError):
        get_next_level_threshold("invalid_class", 1)


def test_get_next_level_threshold_invalid_level_raises():
    with pytest.raises(KeyError):
        get_next_level_threshold("fighter", 999)


# --- can_level_up -------------------------------------------------------------

def test_can_level_up_true_when_xp_meets_threshold(base_character):
    character = base_character.__class__(**{
        **base_character.__dict__,
        "xp": 999999,  # assume enough XP
    })
    result = can_level_up(character)
    assert result is True


def test_can_level_up_false_when_xp_below_threshold(base_character):
    character = base_character.__class__(**{
        **base_character.__dict__,
        "xp": 0,
    })
    result = can_level_up(character)
    assert result is False


def test_can_level_up_false_at_max_level(base_character):
    character = base_character.__class__(**{
        **base_character.__dict__,
        "level": MAX_LEVEL,
        "xp": 999999,
    })
    result = can_level_up(character)
    assert result is False


def test_can_level_up_false_above_max_level(base_character):
    character = base_character.__class__(**{
        **base_character.__dict__,
        "level": MAX_LEVEL + 1,
        "xp": 999999,
    })
    result = can_level_up(character)
    assert result is False
