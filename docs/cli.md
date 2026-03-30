# CLI Reference

The `rpgleveler` command provides a command-line interface for leveling up
Basic Fantasy RPG characters from a JSON file.

---

## Basic Usage

```bash
rpgleveler <input_file>
```

### Example

```bash
rpgleveler my_character.json
```

This will:
- Load the character from the input file
- Apply one level-up
- Print the updated character as JSON to stdout

---

## Command Help

View all available options:

```bash
rpgleveler --help
```

Example output:

```bash
{{ run("rpgleveler --help") }}
```

---

## Arguments

### `input_file` (required)

Path to a JSON file containing character data.

```bash
rpgleveler character.json
```

---

## Options

### `--seed`

Provide a seed for deterministic dice rolls.

This is useful for:

- Testing
- Reproducible results

```bash
rpgleveler character.json --seed 42
```

---

### `--out`

Write the updated character to a file instead of printing to stdout.

```bash
rpgleveler character.json --out leveled.json
```

---

### `--version`

Display the installed version of the CLI.

```bash
rpgleveler --version
```

---

## Example Workflow

Level up a character and save the result:

```bash
rpgleveler test_character.json --seed 1234 --out test_character_lvl2.json
```

---

## Output Format

The CLI outputs a JSON representation of the updated character.

Example:

```json
{
  "name": "Thorin",
  "level": 2,
  "hp": 14,
  ...
}
```

---

## Notes

- The CLI performs **exactly one level-up per invocation**
- The original input file is never modified
- Output is always valid JSON
- All game rules are enforced by the engine
