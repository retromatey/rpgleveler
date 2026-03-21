# rpgleveler

A Python library and CLI for leveling up characters in the Basic Fantasy RPG
system.

## Features

- Class-based progression (XP, attack bonus, saving throws)
- Spell slot progression
- Thief skill progression
- Turn undead mechanics
- Immutable character updates

## Example

```python
from rpgleveler import level_up
from diceroller.core import DiceRoller

rng = DiceRoller()
new_character, result = level_up(character, rng=rng)
```

---

## Project Structure

The project is organized into a few core modules:

| Module                | Purpose                            |
|-----------------------|------------------------------------|
| `engine`              | Core character leveling logic      |

See the **API Reference** section for full documentation.

---

## Next Steps

- See **Getting Started** to install the project
- See **CLI Reference** for command line usage
- See **Character Leveling** to understand the rules implemented
- See **API Reference** for the Python interface

---

## License

This project is distributed under the **MIT License**.

Basic Fantasy RPG is an open tabletop RPG.  
This project is a fan-made utility and is not affiliated with the original
authors or publishers.
