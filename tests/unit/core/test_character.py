import json

from rpgleveler.core import (
    AbilityScores,
    Character,
    ClassName,
    Race,
)
from rpgleveler.data import (
    get_saving_throws,
    get_spell_slots,
    get_thief_skills,
    get_turn_undead,
)


def make_character() -> Character:
    return Character(
        abilities=AbilityScores(10, 11, 12, 13, 14, 15),
        ability_mods={"STR": 2, "DEX": 1},
        ac=15,
        attack_bonus=2,
        class_name=ClassName.CLERIC,
        hp=8,
        inventory=["mace", "shield"],
        level=2,
        money_gp=50,
        name="Serialize Me",
        race=Race.HUMAN,
        saving_throws=get_saving_throws(ClassName.CLERIC, Race.HUMAN, 2),
        xp=2000,
        spell_slots=get_spell_slots(ClassName.CLERIC, 2),
        thief_skills=get_thief_skills(ClassName.CLERIC, 2),
        turn_undead=get_turn_undead(ClassName.CLERIC, 2),
    )


def test_character_to_dict_structure():
    character = make_character()

    data = character.to_dict()

    # Core fields
    assert data["name"] == "Serialize Me"
    assert data["race"] == "human"
    assert data["class"] == "cleric"
    assert data["level"] == 2
    assert data["xp"] == 2000

    # Abilities
    assert data["abilities"]["STR"] == 14
    assert data["ability_mods"]["STR"] == 2

    # Nested objects should now be dicts
    assert isinstance(data["saving_throws"], dict)
    assert isinstance(data["spell_slots"], dict)
    assert isinstance(data["thief_skills"], dict)
    assert isinstance(data["turn_undead"], dict)

    # Spot check nested values
    assert "death_ray_or_poison" in data["saving_throws"]
    assert "level_1" in data["spell_slots"]
    assert "open_locks" in data["thief_skills"]
    assert "skeleton" in data["turn_undead"]


def test_character_to_dict_is_json_serializable():
    character = make_character()

    data = character.to_dict()

    # This is the REAL test
    json_string = json.dumps(data)

    assert isinstance(json_string, str)


def test_character_to_dict_does_not_mutate():
    character = make_character()

    before = character.level
    _ = character.to_dict()

    # Ensure no mutation side effects
    assert character.level == before


def test_round_trip_shape_stability():
    character = make_character()

    data = character.to_dict()

    # Ensure no unexpected types sneak in
    def assert_primitives(obj):
        if isinstance(obj, dict):
            for v in obj.values():
                assert_primitives(v)
        elif isinstance(obj, list):
            for v in obj:
                assert_primitives(v)
        else:
            assert isinstance(obj, (str, int, float, bool, type(None)))

    assert_primitives(data)


def test_character_round_trip():
    original = make_character()

    data = original.to_dict()
    reconstructed = Character.from_dict(data)

    assert reconstructed == original
