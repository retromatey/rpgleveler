import pytest

from rpgleveler.core import ClassName
from rpgleveler.engine.advancement import (
    MAX_LEVEL,
    can_level_up,
    get_next_level_threshold,
    is_max_level,
)

# -------------------------
# is_max_level
# -------------------------

def test_is_max_level_true():
    assert is_max_level(MAX_LEVEL) is True
    assert is_max_level(MAX_LEVEL + 1) is True


def test_is_max_level_false():
    assert is_max_level(MAX_LEVEL - 1) is False


# -------------------------
# get_next_level_threshold
# -------------------------

def test_get_next_level_threshold_valid(monkeypatch):
    monkeypatch.setattr(
        "rpgleveler.engine.advancement.get_xp_requirement",
        lambda cls, lvl: 1234,
    )

    result = get_next_level_threshold(ClassName.FIGHTER, 5)

    assert result == 1234


def test_get_next_level_threshold_raises_at_max_level():
    with pytest.raises(ValueError):
        get_next_level_threshold(ClassName.FIGHTER, MAX_LEVEL)


# -------------------------
# can_level_up
# -------------------------

def test_can_level_up_true(monkeypatch, character_factory):
    char = character_factory(level=1, xp=2000)

    monkeypatch.setattr(
        "rpgleveler.engine.advancement.get_xp_requirement",
        lambda cls, lvl: 1500,
    )

    assert can_level_up(char) is True


def test_can_level_up_false_not_enough_xp(monkeypatch, character_factory):
    char = character_factory(level=1, xp=1000)

    monkeypatch.setattr(
        "rpgleveler.engine.advancement.get_xp_requirement",
        lambda cls, lvl: 1500,
    )

    assert can_level_up(char) is False


def test_can_level_up_false_at_max_level(monkeypatch, character_factory):
    char = character_factory(level=MAX_LEVEL, xp=9999999)

    # even if XP is huge, should not level up
    monkeypatch.setattr(
        "rpgleveler.engine.advancement.get_xp_requirement",
        lambda cls, lvl: 0,
    )

    assert can_level_up(char) is False
