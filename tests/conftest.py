from pathlib import Path

import pytest

from rpgleveler.core import Character


def pytest_collection_modifyitems(config, items):
    for item in items:
        parts = Path(item.fspath).parts

        if "unit" in parts:
            item.add_marker(pytest.mark.unit)
        elif "integration" in parts:
            item.add_marker(pytest.mark.integration)


@pytest.fixture
def character_factory():
    def _factory(**overrides):
        base = {
            "name": "Thorin",
            "race": "dwarf",
            "class_name": "fighter",
            "level": 1,
            "hp": 10,
        }
        base.update(overrides)
        return Character(**base)
    return _factory
