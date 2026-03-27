import pytest

from rpgleveler.shared import ClassName, parse_class_name


def test_enum_values():
    assert ClassName.CLERIC == "cleric"
    assert ClassName.FIGHTER == "fighter"
    assert ClassName.MAGIC_USER == "magic-user"
    assert ClassName.THIEF == "thief"


def test_parse_valid_class_names():
    assert parse_class_name("cleric") is ClassName.CLERIC
    assert parse_class_name("fighter") is ClassName.FIGHTER
    assert parse_class_name("magic-user") is ClassName.MAGIC_USER
    assert parse_class_name("thief") is ClassName.THIEF


def test_parse_invalid_class_name():
    with pytest.raises(ValueError) as exc:
        parse_class_name("wizard")
    assert "Invalid class name: wizard" in str(exc.value)
