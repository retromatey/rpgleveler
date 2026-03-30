# Getting Started

This guide will help you install **rpgleveler** and level up your Basic Fantasy
RPG leveler.

---

## Install

The easiest way to install the project is from a release build hosted on GitHub.

```bash
pip install https://github.com/retromatey/rpgleveler/releases/download/v0.1.0/rpgleveler-0.1.0-py3-none-any.whl
```

!!! note
    Replace `v0.1.0` with the latest version from the
    [GitHub releases page](https://github.com/retromatey/rpgleveler/releases).

---

## Verify Installation

After installation, confirm the CLI is available:

```bash
rpgleveler --help
```

You should see the command line usage information printed to the terminal.

---

## Level Up Your Character

=== "CLI"

    Level Up Your Character

    ```bash
    rpgleveler character_lvl1.json --output character_lvl2.json
    ```

=== "Python"

    ```python
    from rpgleveler import level_up, load_character
    from diceroller.core import DiceRoller

    rng = DiceRoller()
    character = load_character("character.json")
    new_character, result = level_up(character, rng=rng)
    print(new_character.to_dict())
    ```

---

## Deterministic Character Leveling

You can level up a character in the same way repeatedly by providing a seed
value.

=== "CLI"

    ```bash
    rpgleveler character_lvl1.json --output character_lvl2.json --seed 42
    ```

=== "Python"

    ```python
    from diceroller.core import DiceRoller

    rng = DiceRoller(seed=42)
    ```

!!! tip
    Seeds are useful for testing and reproducible examples.

---

## Development Installation

If you want to work on the project locally:

```bash
git clone https://github.com/retromatey/rpgleveler.git
cd rpgleveler
pip install -e .[dev]
```

This installs the package in **editable mode**, allowing changes to the source
code to immediately affect the installed package.

---

## Verify Project Health

Run the following commands to check the health of the project:

```bash
ruff check .
mypy src
pytest --cov=rpgleveler --cov-report=term-missing
python -m build
```

---

## Next Steps

- See **Character Leveling** to understand how characters are leveled up.
- See **CLI Reference** for all command-line options.
- See **API Reference** for the full Python interface.

