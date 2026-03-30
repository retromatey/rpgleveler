import json
from unittest.mock import MagicMock, patch

from rpgleveler.cli.handlers import handle_level_up


@patch("rpgleveler.cli.handlers.load_character")
@patch("rpgleveler.cli.handlers.level_up")
def test_handle_level_up_prints_output(mock_level_up, mock_load, capsys):
    mock_character = MagicMock()
    mock_character.to_dict.return_value = {"name": "Test"}

    mock_load.return_value = mock_character
    mock_level_up.return_value = (mock_character, None)

    handle_level_up(
        input_path="input.json",
        rng=MagicMock(),
        output_path=None,
    )

    captured = capsys.readouterr()
    output = json.loads(captured.out)

    assert output["name"] == "Test"


@patch("rpgleveler.cli.handlers.save_character")
@patch("rpgleveler.cli.handlers.load_character")
@patch("rpgleveler.cli.handlers.level_up")
def test_handle_level_up_writes_file(
    mock_level_up,
    mock_load,
    mock_save,
):
    mock_character = MagicMock()

    mock_load.return_value = mock_character
    mock_level_up.return_value = (mock_character, None)

    handle_level_up(
        input_path="input.json",
        rng=MagicMock(),
        output_path="out.json",
    )

    mock_save.assert_called_once_with(mock_character, "out.json")
