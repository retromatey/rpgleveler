from types import MappingProxyType

import pytest

from rpgleveler.core import ClassName
from rpgleveler.data.hit_dice import (
    HIT_DICE,
    _freeze,
    _raw_hit_dice,
    get_hit_dice,
)

# ------------------------
# _freeze tests
# ------------------------

def test_freeze_returns_mappingproxy():
    frozen = _freeze(_raw_hit_dice)

    assert isinstance(frozen, MappingProxyType)

    for cls, levels in frozen.items():
        assert isinstance(levels, MappingProxyType)


def test_freeze_is_immutable():
    frozen = _freeze(_raw_hit_dice)

    with pytest.raises(TypeError):
        frozen[ClassName.CLERIC] = {}

    with pytest.raises(TypeError):
        frozen[ClassName.CLERIC][1] = "2d6"


# ------------------------
# HIT_DICE structure tests
# ------------------------

def test_hit_dice_contains_all_classes():
    for cls in ClassName:
        assert cls in HIT_DICE


def test_hit_dice_levels_range():
    for cls in ClassName:
        levels = HIT_DICE[cls]
        assert set(levels.keys()) == set(range(1, 21))


def test_hit_dice_values_are_strings():
    for cls in ClassName:
        for value in HIT_DICE[cls].values():
            assert isinstance(value, str)


# ------------------------
# get_hit_dice happy paths
# ------------------------

@pytest.mark.parametrize(
    "class_name, level, expected",
    [
        (ClassName.CLERIC, 1, "1d6"),
        (ClassName.CLERIC, 10, "9d6+1"),
        (ClassName.FIGHTER, 20, "9d8+22"),
        (ClassName.MAGIC_USER, 10, "9d4+1"),
        (ClassName.THIEF, 10, "9d4+2"),
    ],
)
def test_get_hit_dice_valid(class_name, level, expected):
    result = get_hit_dice(class_name, level)
    assert result == expected


# ------------------------
# error handling
# ------------------------

def test_get_hit_dice_invalid_class():
    with pytest.raises(ValueError):
        get_hit_dice("not-a-class", 1)


def test_get_hit_dice_invalid_level_low():
    with pytest.raises(ValueError):
        get_hit_dice(ClassName.CLERIC, 0)


def test_get_hit_dice_invalid_level_high():
    with pytest.raises(ValueError):
        get_hit_dice(ClassName.CLERIC, 21)


# ------------------------
# edge consistency checks
# ------------------------

def test_hit_dice_progression_transition_point():
    """
    Ensure transition from dice growth to flat bonus happens at level 10.
    """
    assert HIT_DICE[ClassName.CLERIC][9] == "9d6"
    assert HIT_DICE[ClassName.CLERIC][10] == "9d6+1"


def test_hit_dice_high_level_scaling():
    """
    Ensure high-level bonus scaling behaves as expected.
    """
    assert HIT_DICE[ClassName.FIGHTER][10] == "9d8+2"
    assert HIT_DICE[ClassName.FIGHTER][20] == "9d8+22"
