from types import MappingProxyType

import pytest

from rpgleveler.core import ClassName, TurnUndead
from rpgleveler.data.turn_undead import (
    TURN_UNDEAD,
    _freeze,
    get_turn_undead,
)

# ----------------------------
# Dataclass
# ----------------------------

def test_turn_undead_is_frozen():
    data = TurnUndead(1, 2, 3, 4, 5, 6, 7, 8)

    with pytest.raises(Exception):
        data.skeleton = 999


def test_turn_undead_values_access():
    data = TurnUndead(1, "T", "D", None, 5, 6, 7, 8)

    assert data.skeleton == 1
    assert data.zombie == "T"
    assert data.ghoul == "D"
    assert data.wight is None


# ----------------------------
# Freeze helper
# ----------------------------

def test_freeze_returns_mappingproxy():
    raw = {
        ClassName.CLERIC: {
            1: TurnUndead(1, None, None, None, None, None, None, None)
        }
    }

    frozen = _freeze(raw)

    assert isinstance(frozen, MappingProxyType)
    assert isinstance(frozen[ClassName.CLERIC], MappingProxyType)


def test_freeze_prevents_modification():
    raw = {
        ClassName.CLERIC: {
            1: TurnUndead(1, None, None, None, None, None, None, None)
        }
    }

    frozen = _freeze(raw)

    with pytest.raises(TypeError):
        frozen[ClassName.FIGHTER] = {}

    with pytest.raises(TypeError):
        frozen[ClassName.CLERIC][1] = TurnUndead(None, None, None, None, None, None, None, None)


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

    assert set(TURN_UNDEAD.keys()) == expected


def test_all_levels_present():
    expected_levels = set(range(1, 21))

    for cls, class_data in TURN_UNDEAD.items():
        # NOTE: this will FAIL until you fix range(0, 21) → (1, 21)
        assert set(class_data.keys()) == expected_levels


def test_values_are_turn_undead_instances():
    for class_data in TURN_UNDEAD.values():
        for value in class_data.values():
            assert isinstance(value, TurnUndead)


def test_non_clerics_have_none_values():
    for cls in [ClassName.FIGHTER, ClassName.MAGIC_USER, ClassName.THIEF]:
        for lvl in range(1, 21):
            result = TURN_UNDEAD[cls][lvl]
            assert all(
                getattr(result, field) is None
                for field in result.__dataclass_fields__
            )


# ----------------------------
# get_turn_undead (happy path)
# ----------------------------

def test_get_turn_undead_valid():
    result = get_turn_undead(ClassName.CLERIC, 1)

    assert result.skeleton == 13
    assert result.zombie == 17


def test_get_turn_undead_special_values():
    result = get_turn_undead(ClassName.CLERIC, 10)

    assert result.skeleton == "D"
    assert result.zombie == "T"


def test_get_turn_undead_high_level():
    result = get_turn_undead(ClassName.CLERIC, 20)

    assert result.vampire == 3
    assert result.spectre == "T"


# ----------------------------
# Error handling
# ----------------------------

def test_get_turn_undead_invalid_class():
    class FakeClass:
        pass

    with pytest.raises(ValueError) as exc:
        get_turn_undead(FakeClass(), 1)

    assert "Invalid class" in str(exc.value)


def test_get_turn_undead_invalid_level():
    with pytest.raises(ValueError) as exc:
        get_turn_undead(ClassName.CLERIC, 999)

    assert "Invalid level" in str(exc.value)
