"""
TODO: add comments for class_names module
"""
from enum import StrEnum, auto


class ClassName(StrEnum):
    """
    TODO: add comments for ClassName enum
    """
    CLERIC = auto()
    FIGHTER = auto()
    MAGIC_USER = auto()
    THIEF = auto()


def parse_class_name(class_name: str) -> ClassName:
    """
    TODO: add comments for parse_class_name function
    """
    try:
        return ClassName(class_name)
    except ValueError:
        raise ValueError(f"Invalid class name: {class_name}")
