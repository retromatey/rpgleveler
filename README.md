[![CI](https://github.com/retromatey/rpgleveler/actions/workflows/ci.yml/badge.svg)](https://github.com/retromatey/rpgleveler/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/retromatey/rpgleveler/branch/main/graph/badge.svg)](https://codecov.io/gh/retromatey/rpgleveler)
[![GitHub release](https://img.shields.io/github/v/release/retromatey/rpgleveler)](https://github.com/retromatey/rpgleveler/releases)
![Python](https://img.shields.io/badge/python-3.14+-blue.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

# rpgleveler

A Python library + CLI for leveling up **Basic Fantasy RPG** characters.

---

## What this project does

- stuff

---

## Quick Start

---

## Example

---

## How to install

### Install the release build

Install the .whl from latest [release](https://github.com/retromatey/rpgleveler/releases):
**NOTE**: Replace `v0.1.0` with the latest release version if needed.

```bash
pip install https://github.com/retromatey/rpgleveler/releases/download/v0.1.0/rpgleveler-0.1.0-py3-none-any.whl
```

### Clone for development

```bash
git clone https://github.com/retromatey/rpgleveler.git
cd rpgleveler
pip install -e .[dev]
```

Run the following commands to check the health of the project:

```bash
ruff check .
mypy src
pytest --cov=rpgleveler --cov-report=term-missing
python -m build
```

---

## Usage

### CLI

Run the `rpgleveler --help` command to view options.

```bash
usage: rpgleveler [-h] [--version] 

Basic Fantasy Character Leveler CLI

options:
  -h, --help          show this help message and exit
  --version           show program's version number and exit
```

### Library

Minimal Python code example.

```python
```

---

## License

Copyright Jason Tennant, 2026.

Distributed under the terms of the MIT license, rpgleveler is free and open
source software.

---

## Credits / Legal

Basic Fantasy RPG is an open tabletop RPG. This project is a fan-made utility
and is not affiliated with the original authors/publishers.
