from unittest.mock import MagicMock

import pytest

from rpgleveler.core import (
    ClassName,
    Race,
    SavingThrowData,
    SpellSlots,
    ThiefSkills,
    TurnUndead,
)
from rpgleveler.engine.leveler import (
    LevelUpError,
    _build_new_character,
    _validate_can_level_up,
    level_up,
)
from rpgleveler.shared import (
    AbilityScores,
    Character,
    LevelUpResult,
)

# -------------------------
# Helpers
# -------------------------

def make_character() -> Character:
    return Character(
        abilities=AbilityScores(10, 10, 10, 10, 10, 10),
        ability_mods={"STR": 0},
        ac=10,
        attack_bonus=1,
        class_name=ClassName.CLERIC,
        hp=5,
        inventory=[],
        level=1,
        money_gp=100,
        name="Test",
        race=Race.HUMAN,
        saving_throws=SavingThrowData(10, 10, 10, 10, 10),
        xp=999999,  # ensure level-up eligible
    )


# -------------------------
# level_up happy path
# -------------------------

def test_level_up_success(monkeypatch):
    character = make_character()

    rng = MagicMock()

    # Mock dependencies
    monkeypatch.setattr(
        "rpgleveler.engine.leveler.can_level_up",
        lambda c: True
    )

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.roll_hp_gain",
        lambda c, rng: 4
    )

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.get_attack_bonus",
        lambda cls, lvl: 42
    )

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.get_saving_throws",
        lambda cls, race, lvl: SavingThrowData(1, 2, 3, 4, 5)
    )

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.get_spell_slots",
        lambda cls, lvl: SpellSlots(1, 1, 1, 1, 1)
    )

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.get_thief_skills",
        lambda cls, lvl: ThiefSkills(1, 1, 1, 1, 1, 1, 1, 1)
    )

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.get_turn_undead",
        lambda cls, lvl: TurnUndead(*(1,) * 8)
    )

    new_char, result = level_up(character, rng=rng)

    # Character assertions
    assert new_char is not character
    assert new_char.level == 2
    assert new_char.hp == 9
    assert new_char.attack_bonus == 42

    # Result assertions
    assert isinstance(result, LevelUpResult)
    assert result.old_level == 1
    assert result.new_level == 2
    assert result.hp_gained == 4
    assert result.new_hp_total == 9
    assert result.new_attack_bonus == 42


# -------------------------
# Validation failure
# -------------------------

def test_level_up_raises_when_not_eligible(monkeypatch):
    character = make_character()
    rng = MagicMock()

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.can_level_up",
        lambda c: False
    )

    with pytest.raises(LevelUpError):
        level_up(character, rng=rng)


# -------------------------
# _validate_can_level_up
# -------------------------

def test_validate_can_level_up_pass(monkeypatch):
    character = make_character()

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.can_level_up",
        lambda c: True
    )

    # Should not raise
    _validate_can_level_up(character)


def test_validate_can_level_up_fail(monkeypatch):
    character = make_character()

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.can_level_up",
        lambda c: False
    )

    with pytest.raises(LevelUpError):
        _validate_can_level_up(character)


# -------------------------
# _build_new_character
# -------------------------

def test_build_new_character_updates_fields():
    character = make_character()

    updated = _build_new_character(
        character=character,
        new_level=2,
        new_hp_total=20,
        new_attack_bonus=99,
        saving_throws=SavingThrowData(1, 1, 1, 1, 1),
        new_spell_slots=SpellSlots(1, 0, 0, 0, 0),
        thief_skills=ThiefSkills(1, 1, 1, 1, 1, 1, 1, 1),
        turn_undead=TurnUndead(*(None,) * 8),
    )

    # Ensure immutability (new object)
    assert updated is not character

    # Ensure fields updated
    assert updated.level == 2
    assert updated.hp == 20
    assert updated.attack_bonus == 99
    assert updated.saving_throws.death_ray_or_poison == 1
    assert updated.spell_slots.level_1 == 1


# -------------------------
# Edge: ensure delegation wiring
# -------------------------

def test_level_up_calls_all_progression_functions(monkeypatch):
    character = make_character()
    rng = MagicMock()

    calls = {
        "attack": False,
        "saving": False,
        "spell": False,
        "thief": False,
        "turn": False,
    }

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.can_level_up",
        lambda c: True
    )

    monkeypatch.setattr(
        "rpgleveler.engine.leveler.roll_hp_gain",
        lambda c, rng: 1
    )

    def attack(cls, lvl):
        calls["attack"] = True
        return 1

    def saving(cls, race, lvl):
        calls["saving"] = True
        return SavingThrowData(1, 1, 1, 1, 1)

    def spell(cls, lvl):
        calls["spell"] = True
        return SpellSlots(0, 0, 0, 0, 0)

    def thief(cls, lvl):
        calls["thief"] = True
        return ThiefSkills(0, 0, 0, 0, 0, 0, 0, 0)

    def turn(cls, lvl):
        calls["turn"] = True
        return TurnUndead(*(None,) * 8)

    monkeypatch.setattr("rpgleveler.engine.leveler.get_attack_bonus", attack)
    monkeypatch.setattr("rpgleveler.engine.leveler.get_saving_throws", saving)
    monkeypatch.setattr("rpgleveler.engine.leveler.get_spell_slots", spell)
    monkeypatch.setattr("rpgleveler.engine.leveler.get_thief_skills", thief)
    monkeypatch.setattr("rpgleveler.engine.leveler.get_turn_undead", turn)

    level_up(character, rng=rng)

    assert all(calls.values())
