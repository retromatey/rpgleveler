"""
Since this is a data table test, we are just verifying the following:

- keys exist
- levels exist
- fields exist
- types are correct
- values are sane

"""

from rpgleveler.data.thief_skills import THIEF_SKILLS

EXPECTED_LEVELS = set(range(1, 21))


def test_all_levels_present():
    assert set(THIEF_SKILLS.keys()) == EXPECTED_LEVELS


def test_all_fields_present():
    for level_data in THIEF_SKILLS.values():
        assert set(level_data.keys()) == {
            "open_locks",
            "pick_pockets",
            "find_traps",
            "remove_traps",
            "move_silently",
            "climb_walls",
            "hide_in_shadows",
            "hear_noise",
        }


def test_values_are_percentages():
    for level_data in THIEF_SKILLS.values():
        for value in level_data.values():
            assert isinstance(value, int)
            assert 0 <= value <= 100
