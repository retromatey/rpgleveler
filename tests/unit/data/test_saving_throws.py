from types import MappingProxyType

import pytest

from rpgleveler.data.saving_throws import (
    SAVING_THROW_MODIFIERS,
    SAVING_THROWS,
    SavingThrowData,
    _freeze_class_saving_throws,
    _freeze_race_modifiers,
    get_saving_throws,
)
from rpgleveler.core import ClassName, Race

# ----------------------------
# SavingThrowData behavior
# ----------------------------

def test_saving_throw_data_is_frozen():
    data = SavingThrowData(1, 2, 3, 4, 5)

    with pytest.raises(Exception):
        data.spells = 999  # frozen dataclass


def test_saving_throw_add():
    base = SavingThrowData(10, 10, 10, 10, 10)
    mod = SavingThrowData(-1, -2, -3, -4, -5)

    result = base.add(mod)

    assert result.death_ray_or_poison == 9
    assert result.magic_wands == 8
    assert result.paralysis_or_petrify == 7
    assert result.dragon_breath == 6
    assert result.spells == 5


# ----------------------------
# Freeze helpers
# ----------------------------

def test_freeze_class_saving_throws():
    raw = {
        ClassName.CLERIC: {
            1: SavingThrowData(1, 1, 1, 1, 1)
        }
    }

    frozen = _freeze_class_saving_throws(raw)

    assert isinstance(frozen, MappingProxyType)
    assert isinstance(frozen[ClassName.CLERIC], MappingProxyType)

    # Outer immutable
    with pytest.raises(TypeError):
        frozen[ClassName.FIGHTER] = {}

    # Inner immutable
    with pytest.raises(TypeError):
        frozen[ClassName.CLERIC][1] = SavingThrowData(0, 0, 0, 0, 0)


def test_freeze_race_modifiers():
    raw = {
        Race.HUMAN: SavingThrowData(0, 0, 0, 0, 0)
    }

    frozen = _freeze_race_modifiers(raw)

    assert isinstance(frozen, MappingProxyType)

    with pytest.raises(TypeError):
        frozen[Race.ELF] = SavingThrowData(0, 0, 0, 0, 0)


# ----------------------------
# Data integrity
# ----------------------------

def test_all_classes_present():
    expected = {
        ClassName.CLERIC,
        ClassName.FIGHTER,
        ClassName.MAGIC_USER,
        ClassName.THIEF,
    }

    assert set(SAVING_THROWS.keys()) == expected


def test_all_levels_present():
    expected_levels = set(range(1, 21))

    for class_data in SAVING_THROWS.values():
        assert set(class_data.keys()) == expected_levels


def test_values_are_saving_throw_data():
    for class_data in SAVING_THROWS.values():
        for value in class_data.values():
            assert isinstance(value, SavingThrowData)


def test_race_modifiers_present():
    expected = {
        Race.DWARF,
        Race.ELF,
        Race.HALFLING,
        Race.HUMAN,
    }

    assert set(SAVING_THROW_MODIFIERS.keys()) == expected


# ----------------------------
# get_saving_throws (happy path)
# ----------------------------

def test_get_saving_throws_human_no_modifier():
    result = get_saving_throws(ClassName.CLERIC, Race.HUMAN, 1)

    base = SAVING_THROWS[ClassName.CLERIC][1]

    assert result == base


def test_get_saving_throws_with_modifier():
    result = get_saving_throws(ClassName.CLERIC, Race.DWARF, 1)

    base = SAVING_THROWS[ClassName.CLERIC][1]
    mod = SAVING_THROW_MODIFIERS[Race.DWARF]

    expected = base.add(mod)

    assert result == expected


# ----------------------------
# Validation errors
# ----------------------------

def test_invalid_class_raises():
    class FakeClass:
        pass

    with pytest.raises(ValueError) as exc:
        get_saving_throws(FakeClass(), Race.HUMAN, 1)

    assert "Invalid class" in str(exc.value)


def test_invalid_race_raises():
    class FakeRace:
        pass

    with pytest.raises(ValueError) as exc:
        get_saving_throws(ClassName.CLERIC, FakeRace(), 1)

    assert "Invalid race" in str(exc.value)


def test_invalid_level_raises():
    with pytest.raises(ValueError) as exc:
        get_saving_throws(ClassName.CLERIC, Race.HUMAN, 999)

    assert "Invalid level" in str(exc.value)
