from types import MappingProxyType

import pytest

from rpgleveler.data.thief_skills import (
    THIEF_SKILLS,
    ThiefSkills,
    _freeze,
    get_thief_skills,
)
from rpgleveler.core import ClassName

# ----------------------------
# ThiefSkills dataclass
# ----------------------------

def test_thief_skills_is_frozen():
    skills = ThiefSkills(1, 2, 3, 4, 5, 6, 7, 8)

    with pytest.raises(Exception):
        skills.open_locks = 999  # frozen dataclass


def test_thief_skills_values_access():
    skills = ThiefSkills(1, 2, 3, 4, 5, 6, 7, 8)

    assert skills.open_locks == 1
    assert skills.pick_pockets == 2
    assert skills.find_traps == 3
    assert skills.remove_traps == 4
    assert skills.move_silently == 5
    assert skills.climb_walls == 6
    assert skills.hide_in_shadows == 7
    assert skills.hear_noise == 8


# ----------------------------
# Freeze helper
# ----------------------------

def test_freeze_returns_mappingproxy():
    raw = {
        ClassName.THIEF: {
            1: ThiefSkills(1, 1, 1, 1, 1, 1, 1, 1)
        }
    }

    frozen = _freeze(raw)

    assert isinstance(frozen, MappingProxyType)
    assert isinstance(frozen[ClassName.THIEF], MappingProxyType)


def test_freeze_prevents_modification():
    raw = {
        ClassName.THIEF: {
            1: ThiefSkills(1, 1, 1, 1, 1, 1, 1, 1)
        }
    }

    frozen = _freeze(raw)

    # Outer immutable
    with pytest.raises(TypeError):
        frozen[ClassName.FIGHTER] = {}

    # Inner immutable
    with pytest.raises(TypeError):
        frozen[ClassName.THIEF][1] = ThiefSkills(0, 0, 0, 0, 0, 0, 0, 0)


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

    assert set(THIEF_SKILLS.keys()) == expected


def test_all_levels_present():
    expected_levels = set(range(1, 21))

    for class_data in THIEF_SKILLS.values():
        assert set(class_data.keys()) == expected_levels


def test_values_are_thiefskills():
    for class_data in THIEF_SKILLS.values():
        for value in class_data.values():
            assert isinstance(value, ThiefSkills)


def test_non_thief_classes_have_zero_skills():
    zero = ThiefSkills(0, 0, 0, 0, 0, 0, 0, 0)

    for cls in [ClassName.CLERIC, ClassName.FIGHTER, ClassName.MAGIC_USER]:
        for lvl in range(1, 21):
            assert THIEF_SKILLS[cls][lvl] == zero


# ----------------------------
# get_thief_skills (happy path)
# ----------------------------

def test_get_thief_skills_valid():
    result = get_thief_skills(ClassName.THIEF, 1)

    assert result.open_locks == 25
    assert result.pick_pockets == 30


def test_get_thief_skills_high_level():
    result = get_thief_skills(ClassName.THIEF, 20)

    assert result.open_locks == 99
    assert result.move_silently == 99


# ----------------------------
# Error handling
# ----------------------------

def test_get_thief_skills_invalid_class():
    class FakeClass:
        pass

    with pytest.raises(ValueError) as exc:
        get_thief_skills(FakeClass(), 1)

    assert "Invalid class" in str(exc.value)


def test_get_thief_skills_invalid_level():
    with pytest.raises(ValueError) as exc:
        get_thief_skills(ClassName.THIEF, 999)

    assert "Invalid level" in str(exc.value)
