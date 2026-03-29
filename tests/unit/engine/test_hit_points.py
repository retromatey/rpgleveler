import pytest

from rpgleveler.core import Character, ClassName, Race
from rpgleveler.engine.hit_points import (
    _apply_racial_cap,
    _parse_hit_dice,
    roll_hp_gain,
)

# -------------------------
# Helpers
# -------------------------

class DummyDiceRoller:
    def __init__(self, value: int):
        self.value = value

    def roll(self, expr: str) -> int:
        return self.value


def make_character(
    *,
    level=1,
    race=Race.HUMAN,
    con_mod=0,
    class_name=ClassName.FIGHTER,
):
    return Character(
        abilities=None,
        ability_mods={"CON": con_mod},
        ac=10,
        attack_bonus=0,
        class_name=class_name,
        hp=10,
        inventory=[],
        level=level,
        money_gp=0,
        name=None,
        race=race,
        saving_throws=None,
        xp=0,
    )


# -------------------------
# _parse_hit_dice
# -------------------------

def test_parse_hit_dice_with_bonus():
    assert _parse_hit_dice("3d6+2") == (3, 6, 2)


def test_parse_hit_dice_without_bonus():
    assert _parse_hit_dice("2d8") == (2, 8, 0)


def test_parse_hit_dice_invalid():
    with pytest.raises(ValueError):
        _parse_hit_dice("bad_input")


# -------------------------
# _apply_racial_cap
# -------------------------

def test_racial_cap_applies_to_elf():
    assert _apply_racial_cap(8, Race.ELF) == 6


def test_racial_cap_applies_to_halfling():
    assert _apply_racial_cap(10, Race.HALFLING) == 6


def test_racial_cap_not_applied():
    assert _apply_racial_cap(8, Race.HUMAN) == 8


# -------------------------
# roll_hp_gain
# -------------------------

def test_roll_hp_gain_pre_9_with_con(monkeypatch):
    """
    Level < 10 → roll + CON modifier
    """
    char = make_character(level=1, con_mod=2)

    monkeypatch.setattr(
        "rpgleveler.engine.hit_points.get_hit_dice",
        lambda c, lvl: "1d8"
    )

    rng = DummyDiceRoller(5)

    result = roll_hp_gain(char, rng)

    assert result == 7  # 5 + 2


def test_roll_hp_gain_pre_9_minimum_one(monkeypatch):
    """
    Ensure minimum HP gain is 1
    """
    char = make_character(level=1, con_mod=-10)

    monkeypatch.setattr(
        "rpgleveler.engine.hit_points.get_hit_dice",
        lambda c, lvl: "1d4"
    )

    rng = DummyDiceRoller(1)

    result = roll_hp_gain(char, rng)

    assert result == 1


def test_roll_hp_gain_racial_cap(monkeypatch):
    """
    Elf caps die size to d6
    """
    char = make_character(level=1, race=Race.ELF)

    monkeypatch.setattr(
        "rpgleveler.engine.hit_points.get_hit_dice",
        lambda c, lvl: "1d8"
    )

    captured = {}

    class CaptureRoller:
        def roll(self, expr):
            captured["expr"] = expr
            return 3

    rng = CaptureRoller()

    roll_hp_gain(char, rng)

    assert captured["expr"] == "1d6"


def test_roll_hp_gain_post_9_fixed(monkeypatch):
    """
    Level >= 10 → fixed bonus only, no CON
    """
    char = make_character(level=9, con_mod=5)

    monkeypatch.setattr(
        "rpgleveler.engine.hit_points.get_hit_dice",
        lambda c, lvl: "9d8+3"
    )

    rng = DummyDiceRoller(999)  # should not matter

    result = roll_hp_gain(char, rng)

    assert result == 3


def test_roll_hp_gain_post_9_minimum_one(monkeypatch):
    """
    Fixed bonus still respects minimum of 1
    """
    char = make_character(level=9)

    monkeypatch.setattr(
        "rpgleveler.engine.hit_points.get_hit_dice",
        lambda c, lvl: "9d8+0"
    )

    rng = DummyDiceRoller(0)

    result = roll_hp_gain(char, rng)

    assert result == 1
