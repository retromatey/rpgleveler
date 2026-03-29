from types import MappingProxyType

import pytest

from rpgleveler.core import ClassName
from rpgleveler.data.attack_bonus import (
    ATTACK_BONUS,
    _freeze,
    get_attack_bonus,
)


def test_freeze_returns_mappingproxy():
    data = {
        ClassName.CLERIC: {1: 1}
    }

    frozen = _freeze(data)

    assert isinstance(frozen, MappingProxyType)
    assert isinstance(frozen[ClassName.CLERIC], MappingProxyType)


def test_freeze_prevents_modification():
    data = {
        ClassName.CLERIC: {1: 1}
    }

    frozen = _freeze(data)

    # Outer dict is immutable
    with pytest.raises(TypeError):
        frozen[ClassName.FIGHTER] = {}

    # Inner dict is immutable
    with pytest.raises(TypeError):
        frozen[ClassName.CLERIC][1] = 999


def test_attack_bonus_structure_contains_all_classes():
    expected_classes = {
        ClassName.CLERIC,
        ClassName.FIGHTER,
        ClassName.MAGIC_USER,
        ClassName.THIEF,
    }

    assert set(ATTACK_BONUS.keys()) == expected_classes


def test_attack_bonus_contains_all_levels():
    expected_levels = set(range(1, 21))

    for class_data in ATTACK_BONUS.values():
        assert set(class_data.keys()) == expected_levels


def test_attack_bonus_values_are_ints():
    for class_data in ATTACK_BONUS.values():
        for value in class_data.values():
            assert isinstance(value, int)


def test_get_attack_bonus_valid_cases():
    assert get_attack_bonus(ClassName.CLERIC, 1) == 1
    assert get_attack_bonus(ClassName.FIGHTER, 20) == 20
    assert get_attack_bonus(ClassName.MAGIC_USER, 2) == 1
    assert get_attack_bonus(ClassName.THIEF, 10) == 6


def test_get_attack_bonus_invalid_class():
    class FakeClass:
        pass

    with pytest.raises(ValueError) as exc:
        get_attack_bonus(FakeClass(), 1)

    assert "Invalid class" in str(exc.value)


def test_get_attack_bonus_invalid_level():
    with pytest.raises(ValueError) as exc:
        get_attack_bonus(ClassName.CLERIC, 999)

    assert "Invalid level" in str(exc.value)


def test_attack_bonus_progression_monotonic():
    for class_data in ATTACK_BONUS.values():
        previous = -999
        for level in range(1, 21):
            current = class_data[level]
            assert current >= previous
            previous = current
