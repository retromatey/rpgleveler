from types import MappingProxyType

import pytest

from rpgleveler.core import ClassName, SpellSlots
from rpgleveler.data.spell_slots import (
    SPELL_SLOTS,
    _freeze,
    get_spell_slots,
)

# ----------------------------
# SpellSlots dataclass
# ----------------------------

def test_spell_slots_is_frozen():
    slots = SpellSlots(1, 2, 3, 4, 5)

    with pytest.raises(Exception):
        slots.level_1 = 999  # frozen dataclass


def test_spell_slots_values_access():
    slots = SpellSlots(1, 2, 3, 4, 5)

    assert slots.level_1 == 1
    assert slots.level_2 == 2
    assert slots.level_3 == 3
    assert slots.level_4 == 4
    assert slots.level_5 == 5


# ----------------------------
# Freeze helper
# ----------------------------

def test_freeze_returns_mappingproxy():
    raw = {
        ClassName.CLERIC: {
            1: SpellSlots(1, 0, 0, 0, 0)
        }
    }

    frozen = _freeze(raw)

    assert isinstance(frozen, MappingProxyType)
    assert isinstance(frozen[ClassName.CLERIC], MappingProxyType)


def test_freeze_prevents_modification():
    raw = {
        ClassName.CLERIC: {
            1: SpellSlots(1, 0, 0, 0, 0)
        }
    }

    frozen = _freeze(raw)

    # Outer immutable
    with pytest.raises(TypeError):
        frozen[ClassName.FIGHTER] = {}

    # Inner immutable
    with pytest.raises(TypeError):
        frozen[ClassName.CLERIC][1] = SpellSlots(0, 0, 0, 0, 0)


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

    assert set(SPELL_SLOTS.keys()) == expected


def test_all_levels_present():
    expected_levels = set(range(1, 21))

    for class_data in SPELL_SLOTS.values():
        assert set(class_data.keys()) == expected_levels


def test_values_are_spellslots():
    for class_data in SPELL_SLOTS.values():
        for value in class_data.values():
            assert isinstance(value, SpellSlots)


def test_non_spellcasters_have_zero_slots():
    for lvl in range(1, 21):
        fighter = SPELL_SLOTS[ClassName.FIGHTER][lvl]
        thief = SPELL_SLOTS[ClassName.THIEF][lvl]

        assert fighter == SpellSlots(0, 0, 0, 0, 0)
        assert thief == SpellSlots(0, 0, 0, 0, 0)


# ----------------------------
# get_spell_slots (happy path)
# ----------------------------

def test_get_spell_slots_valid_cases():
    cleric_lvl2 = get_spell_slots(ClassName.CLERIC, 2)
    assert cleric_lvl2.level_1 == 1

    mage_lvl3 = get_spell_slots(ClassName.MAGIC_USER, 3)
    assert mage_lvl3.level_2 == 1

    fighter_lvl10 = get_spell_slots(ClassName.FIGHTER, 10)
    assert fighter_lvl10 == SpellSlots(0, 0, 0, 0, 0)


# ----------------------------
# Error handling
# ----------------------------

def test_get_spell_slots_invalid_class():
    class FakeClass:
        pass

    with pytest.raises(ValueError) as exc:
        get_spell_slots(FakeClass(), 1)

    assert "Invalid class" in str(exc.value)


def test_get_spell_slots_invalid_level():
    with pytest.raises(ValueError) as exc:
        get_spell_slots(ClassName.CLERIC, 999)

    assert "Invalid level" in str(exc.value)
