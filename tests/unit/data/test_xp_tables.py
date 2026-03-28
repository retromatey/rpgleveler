from types import MappingProxyType

import pytest

from rpgleveler.data.xp_tables import (
    XP_TABLES,
    _freeze,
    get_xp_requirement,
)
from rpgleveler.shared import ClassName

# ----------------------------
# Freeze helper
# ----------------------------

def test_freeze_returns_mappingproxy():
    raw = {
        ClassName.CLERIC: {
            1: 0
        }
    }

    frozen = _freeze(raw)

    assert isinstance(frozen, MappingProxyType)
    assert isinstance(frozen[ClassName.CLERIC], MappingProxyType)


def test_freeze_prevents_modification():
    raw = {
        ClassName.CLERIC: {
            1: 0
        }
    }

    frozen = _freeze(raw)

    # Outer immutability
    with pytest.raises(TypeError):
        frozen[ClassName.FIGHTER] = {}

    # Inner immutability
    with pytest.raises(TypeError):
        frozen[ClassName.CLERIC][1] = 999


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

    assert set(XP_TABLES.keys()) == expected


def test_all_levels_present():
    expected_levels = set(range(1, 21))

    for class_data in XP_TABLES.values():
        assert set(class_data.keys()) == expected_levels


def test_values_are_ints():
    for class_data in XP_TABLES.values():
        for value in class_data.values():
            assert isinstance(value, int)


def test_level_one_is_zero_for_all_classes():
    for cls in ClassName:
        assert XP_TABLES[cls][1] == 0


# ----------------------------
# get_xp_requirement (happy path)
# ----------------------------

def test_get_xp_requirement_valid():
    assert get_xp_requirement(ClassName.CLERIC, 2) == 1500
    assert get_xp_requirement(ClassName.FIGHTER, 5) == 16000
    assert get_xp_requirement(ClassName.MAGIC_USER, 3) == 5000
    assert get_xp_requirement(ClassName.THIEF, 2) == 1250


def test_get_xp_requirement_high_level():
    assert get_xp_requirement(ClassName.CLERIC, 20) == 2700000
    assert get_xp_requirement(ClassName.THIEF, 20) == 910000


# ----------------------------
# Error handling
# ----------------------------

def test_get_xp_requirement_invalid_class():
    class FakeClass:
        pass

    with pytest.raises(ValueError) as exc:
        get_xp_requirement(FakeClass(), 1)

    assert "Invalid class" in str(exc.value)


def test_get_xp_requirement_invalid_level():
    with pytest.raises(ValueError) as exc:
        get_xp_requirement(ClassName.CLERIC, 999)

    assert "Invalid level" in str(exc.value)
