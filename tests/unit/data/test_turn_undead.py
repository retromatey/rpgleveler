"""
Since this is a data table test, we are just verifying the following:

- keys exist
- levels exist
- fields exist
- types are correct
- values are sane

"""

from rpgleveler.data.turn_undead import TURN_UNDEAD

EXPECTED_LEVELS = set(range(1, 21))
VALID_SPECIAL = {"T", "D"}


def test_all_levels_present():
    assert set(TURN_UNDEAD.keys()) == EXPECTED_LEVELS


def test_all_fields_present():
    for level_data in TURN_UNDEAD.values():
        assert set(level_data.keys()) == {
            "skeleton",
            "zombie",
            "ghoul",
            "wight",
            "wraith",
            "mummy",
            "spectre",
            "vampire",
        }


def test_values_valid():
    for level_data in TURN_UNDEAD.values():
        for value in level_data.values():
            assert (
                value is None
                or isinstance(value, int)
                or value in VALID_SPECIAL)
