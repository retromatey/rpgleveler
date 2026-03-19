"""
Since this is a data table test, we are just verifying the following:

- keys exist
- levels exist
- fields exist
- types are correct
- values are sane

"""

from rpgleveler.data.saving_throws import SAVING_THROWS
from rpgleveler.shared.literals import ClassName

EXPECTED_CLASSES: set[ClassName] = {"cleric", "fighter", "magic-user", "thief"}
EXPECTED_LEVELS = set(range(1, 21))


def test_all_classes_present():
    assert set(SAVING_THROWS.keys()) == EXPECTED_CLASSES


def test_all_levels_present():
    for class_data in SAVING_THROWS.values():
        assert set(class_data.keys()) == EXPECTED_LEVELS


def test_all_fields_present():
    for class_data in SAVING_THROWS.values():
        for level_data in class_data.values():
            assert set(level_data.keys()) == {
                "death_ray_or_poison",
                "magic_wands",
                "paralysis_or_petrify",
                "dragon_breath",
                "spells",
            }


def test_values_are_ints():
    for class_data in SAVING_THROWS.values():
        for level_data in class_data.values():
            for value in level_data.values():
                assert isinstance(value, int)


def test_values_are_reasonable():
    for class_data in SAVING_THROWS.values():
        for level_data in class_data.values():
            for value in level_data.values():
                assert 2 <= value <= 20
