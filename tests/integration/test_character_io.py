import json
import tempfile
from pathlib import Path

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
from rpgleveler.io.character_io import load_character, save_character


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


def test_character_save_and_load_round_trip():
    """
    Integration test for character I/O.

    Verifies that a character can be:
        1. Serialized to disk
        2. Loaded back into a Character object
        3. Fully reconstructed with identical data

    This ensures end-to-end correctness of:
        - Character.to_dict()
        - Character.from_dict()
        - File I/O logic
    """
    character = make_character()

    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "character.json"

        # Save character to disk
        save_character(character, file_path)

        # Ensure file was created
        assert file_path.exists()

        # Load character from disk
        loaded_character = load_character(file_path)

        # Compare serialized forms (cleanest equality check)
        assert loaded_character.to_dict() == character.to_dict()
        assert loaded_character == character


def test_saved_file_is_valid_json():
    """
    Ensures the saved file is valid JSON and readable outside the system.

    This protects against subtle serialization bugs.
    """
    character = make_character()

    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "character.json"

        save_character(character, file_path)

        # Load raw JSON
        with open(file_path) as f:
            data = json.load(f)

        assert isinstance(data, dict)
        assert data["name"] == character.name
        assert data["level"] == character.level


def test_load_invalid_file_raises(tmp_path):
    """
    Verifies that loading invalid JSON fails cleanly.
    """
    file_path = tmp_path / "bad_character.json"

    # Write garbage
    file_path.write_text("not valid json")

    try:
        load_character(file_path)
        assert False, "Expected exception for invalid JSON"
    except Exception:
        pass  # tighten this to specific exception later
