from unittest.mock import patch

import pytest

from rpgleveler.cli.cli import create_dice_roller, main, parse_args


def test_parse_args_defaults():
    args = parse_args(["input.json"])

    assert args.input_file == "input.json"
    assert args.seed is None
    assert args.out is None


def test_parse_args_with_options():
    args = parse_args(["input.json", "--seed", "42", "--out", "out.json"])

    assert args.seed == 42
    assert args.out == "out.json"


def test_create_dice_roller_without_seed():
    rng = create_dice_roller(None)
    assert rng is not None


def test_create_dice_roller_with_seed():
    rng = create_dice_roller(123)
    assert rng is not None


@patch("rpgleveler.cli.cli.handle_level_up")
def test_main_calls_handler(mock_handler):
    main(["input.json"])

    mock_handler.assert_called_once()


@patch("rpgleveler.cli.cli.handle_level_up", side_effect=Exception("boom"))
def test_main_handles_exception(mock_handler, capsys):
    with pytest.raises(SystemExit) as exc:
        main(["input.json"])

    assert exc.value.code == 2

    captured = capsys.readouterr()
    assert "Error: boom" in captured.err
