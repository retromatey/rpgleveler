import json
from pathlib import Path

from rpgleveler.core import Character


def save_character(character: Character, path: str | Path) -> None:
    """
    Save a Character to a JSON file.

    Args:
        character: Character to serialize.
        path: Output file path.
    """
    data = character.to_dict()
    Path(path).write_text(json.dumps(data, indent=2))


def load_character(path: str | Path) -> Character:
    """
    Load a Character from a JSON file.

    Args:
        path: Path to JSON file.

    Returns:
        Character instance.
    """
    data = json.loads(Path(path).read_text())
    return Character.from_dict(data)
