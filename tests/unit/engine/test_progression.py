import pytest

from rpgleveler.engine.progression import (
    get_attack_bonus,
    get_saving_throws,
    apply_saving_throw_modifiers,
    get_spell_slots,
    get_thief_skills,
    get_turn_undead,
)


# --- Attack Bonus -------------------------------------------------------------

def test_get_attack_bonus_returns_value():
    result = get_attack_bonus("fighter", 1)
    assert isinstance(result, int)


def test_get_attack_bonus_invalid_class_raises():
    with pytest.raises(KeyError):
        get_attack_bonus("invalid_class", 1)


def test_get_attack_bonus_invalid_level_raises():
    with pytest.raises(KeyError):
        get_attack_bonus("fighter", 999)


# --- Saving Throws ------------------------------------------------------------

def test_get_saving_throws_returns_dict():
    result = get_saving_throws("fighter", 1)
    assert isinstance(result, dict)
    assert len(result) > 0


def test_get_saving_throws_invalid_class_raises():
    with pytest.raises(KeyError):
        get_saving_throws("invalid_class", 1)


def test_get_saving_throws_invalid_level_raises():
    with pytest.raises(KeyError):
        get_saving_throws("fighter", 999)


# --- Saving Throw Modifiers ---------------------------------------------------

def test_apply_saving_throw_modifiers_returns_new_dict():
    base = {
        "death_ray_or_poison": 12,
        "magic_wands": 13,
        "death_ray_or_poison": 12,
        "magic_wands": 13,
        "paralysis_or_petrify": 14,
        "dragon_breath": 15,
        "spells": 16,
    }
    result = apply_saving_throw_modifiers(base, "human")
    assert result is not base


def test_apply_saving_throw_modifiers_applies_values():
    base = {
        "death_ray_or_poison": 12,
        "magic_wands": 13,
        "death_ray_or_poison": 12,
        "magic_wands": 13,
        "paralysis_or_petrify": 14,
        "dragon_breath": 15,
        "spells": 16,
    }
    result = apply_saving_throw_modifiers(base, "dwarf")
    # exact values depend on your table, but we expect *some* change
    assert result["death_ray_or_poison"] != base["death_ray_or_poison"]


def test_apply_saving_throw_modifiers_unknown_race_returns_base():
    base = { "death_ray_or_poison": 12, }
    result = apply_saving_throw_modifiers(base, "unknown_race")
    assert result == base


# --- Spell Slots --------------------------------------------------------------

def test_get_spell_slots_returns_tuple_for_caster():
    result = get_spell_slots("magic_user", 1)
    assert isinstance(result, tuple)


def test_get_spell_slots_returns_none_for_non_caster():
    result = get_spell_slots("fighter", 1)
    assert result is None


# --- Thief Skills -------------------------------------------------------------

def test_get_thief_skills_throws_invalid_class_raises():
    with pytest.raises(KeyError):
        get_thief_skills("invalid_class", 1)


def test_get_thief_skills_returns_dict_for_thief():
    result = get_thief_skills("thief", 1)
    assert isinstance(result, dict)


def test_get_thief_skills_returns_none_for_non_thief():
    result = get_thief_skills("fighter", 1)
    assert result is None


# --- Turn Undead --------------------------------------------------------------

def test_get_turn_undead_throws_invalid_class_raises():
    with pytest.raises(KeyError):
        get_turn_undead("invalid_class", 1)

def test_get_turn_undead_returns_dict_for_cleric():
    result = get_turn_undead("cleric", 1)
    assert isinstance(result, dict)


def test_get_turn_undead_returns_none_for_non_cleric():
    result = get_turn_undead("fighter", 1)
    assert result is None
