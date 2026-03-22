"""
Since this is a data table test, we are just verifying the following:

- keys exist
- levels exist
- fields exist
- types are correct
- values are sane

"""

from rpgleveler.data.spell_slots import SPELL_SLOTS
from rpgleveler.shared.literals import ClassName

EXPECTED_CASTERS: set[ClassName] = {"cleric", "magic-user"}
EXPECTED_LEVELS = set(range(1, 21))


def test_only_spellcasting_classes_present():
    assert set(SPELL_SLOTS.keys()) == EXPECTED_CASTERS


def test_all_levels_present():
    for class_data in SPELL_SLOTS.values():
        assert set(class_data.keys()) == EXPECTED_LEVELS


def test_values_are_tuples_of_ints():
    for class_name, class_data in SPELL_SLOTS.items():
        if class_name not in EXPECTED_CASTERS:
            continue

        for slots in class_data.values():
            assert isinstance(slots, tuple)
            assert len(slots) == 5
            for value in slots:
                assert isinstance(value, int)
                assert value >= 0


def test_spell_slots_do_not_shrink():
    """
    Sanity check: spell progression should not decrease dramatically.
    (Allows same or increasing total slots)
    """
    for class_name, class_data in SPELL_SLOTS.items():
        if class_name not in EXPECTED_CASTERS:
            continue

        previous_total = 0
        for level in range(1, 21):
            current_total = sum(class_data[level])
            assert current_total >= previous_total
            previous_total = current_total
