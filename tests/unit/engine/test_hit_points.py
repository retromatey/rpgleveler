import pytest
from unittest.mock import MagicMock

from rpgleveler.engine.hit_points import roll_hp_gain
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
        ability_mods={"CON": 0},
        ac=0,
        inventory=[],
        money_gp=0,
    )


@pytest.fixture
def rng():
    return MagicMock()


# --- Basic Behavior -----------------------------------------------------------

def test_roll_hp_gain_returns_int(base_character, rng):
    rng.roll.return_value = 4
    result = roll_hp_gain(base_character, rng)
    assert isinstance(result, int)


def test_roll_hp_gain_uses_rng(base_character, rng):
    rng.roll.return_value = 4
    roll_hp_gain(base_character, rng)
    rng.roll.assert_called_once()


# --- Class-Based Dice ---------------------------------------------------------

def test_roll_hp_gain_varies_by_class(rng, base_character):
    """
    Different classes should use different hit dice.
    This test will evolve once hit dice are implemented.
    """
    rng.roll.return_value = 4
    fighter = base_character
    cleric = base_character.__class__(**{**base_character.__dict__, "class_name": "cleric"})
    result_fighter = roll_hp_gain(fighter, rng)
    result_cleric = roll_hp_gain(cleric, rng)
    # We don't assert exact values yet, just that function runs
    assert isinstance(result_fighter, int)
    assert isinstance(result_cleric, int)


# --- Constitution Modifier ----------------------------------------------------

def test_roll_hp_gain_applies_con_modifier(rng, base_character):
    rng.roll.return_value = 4
    character = base_character.__class__(**{
        **base_character.__dict__,
        "ability_mods": {"CON": 2},
    })
    result = roll_hp_gain(character, rng)
    assert result >= 6  # 4 roll + 2 modifier


# --- Minimum HP Rule ----------------------------------------------------------

def test_roll_hp_gain_minimum_one(rng, base_character):
    """
    Even with negative CON modifiers, HP gain should not drop below 1.
    """
    rng.roll.return_value = 1
    character = base_character.__class__(**{
        **base_character.__dict__,
        "ability_mods": {"CON": -5},
    })
    result = roll_hp_gain(character, rng)
    assert result >= 1


# --- Immutability -------------------------------------------------------------

def test_roll_hp_gain_does_not_modify_character(base_character, rng):
    rng.roll.return_value = 4
    original_hp = base_character.hp
    roll_hp_gain(base_character, rng)
    assert base_character.hp == original_hp


# --- Error Handling -----------------------------------------------------------

def test_roll_hp_gain_invalid_class_raises(rng, base_character):
    character = base_character.__class__(**{
        **base_character.__dict__,
        "class_name": "invalid_class",
    })
    with pytest.raises(KeyError):
        roll_hp_gain(character, rng)
