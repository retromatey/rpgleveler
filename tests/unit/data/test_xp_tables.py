"""
Since this is a data table test, we are just verifying the following:

- keys exist
- levels exist
- fields exist
- types are correct
- values are sane

"""

from rpgleveler.data.xp_tables import XP_TABLES
from rpgleveler.shared.literals import ClassName

EXPECTED_CLASSES: set[ClassName] = {"cleric", "fighter", "magic-user", "thief"}
EXPECTED_LEVELS = set(range(1, 21))


def test_all_classes_present():
    assert set(XP_TABLES.keys()) == EXPECTED_CLASSES


def test_all_levels_present():
    for class_data in XP_TABLES.values():
        assert set(class_data.keys()) == EXPECTED_LEVELS


def test_values_are_ints():
    for class_data in XP_TABLES.values():
        for value in class_data.values():
            assert isinstance(value, int)


def test_values_increase_monotonically():
    for class_data in XP_TABLES.values():
        previous = -1
        for level in range(1, 21):
            current = class_data[level]
            assert current > previous
            previous = current
