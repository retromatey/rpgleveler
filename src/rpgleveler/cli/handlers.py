import json

from diceroller.core import DiceRoller

from rpgleveler.engine.leveler import level_up
from rpgleveler.io.character_io import load_character, save_character


def handle_level_up(
    *,
    input_path: str,
    rng: DiceRoller,
    output_path: str | None,
) -> None:
    """
    Load a character, level them up, and output the result.
    """
    character = load_character(input_path)
    new_character, result = level_up(character, rng=rng)

    if output_path:
        save_character(new_character, output_path)
    else:
        data = new_character.to_dict()
        output = json.dumps(data, indent=2)
        print(output)
