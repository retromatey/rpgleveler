import pytest

from rpgleveler.core import Race, parse_race


def test_enum_values():
    assert Race.ELF == "elf"
    assert Race.DWARF == "dwarf"
    assert Race.HALFLING == "halfling"
    assert Race.HUMAN == "human"


def test_parse_valid_races():
    assert parse_race("elf") is Race.ELF
    assert parse_race("dwarf") is Race.DWARF
    assert parse_race("halfling") is Race.HALFLING
    assert parse_race("human") is Race.HUMAN


def test_parse_invalid_races():
    with pytest.raises(ValueError) as exc:
        parse_race("lizard")
    assert "Invalid race: lizard" in str(exc.value)
