# Advent of Code 2024 ![status](https://github.com/pmareke/aoc/actions/workflows/app.yml/badge.svg)

## Requirements

- You only need to have [Poetry](https://python-poetry.org) installed.

**Important: Please run the `make local-setup` command before starting with the code.**

_In order to create a commit you have to pass the pre-commit phase which runs the check and test commands._

## Folder structure

- There is a `tests` folder with the tests files.
  - In order to add new tests please follow the [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) recommendations.
- The production code goes inside the `src` folder.
- Inside the `scripts` folder you can find the git hooks files.

## Project commands

The project uses [Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html) to run the most common tasks:

- `check-typing`: Runs a static analyzer over the code in order to find issues.
- `check-format`: Checks the code format.
- `check-lint`: Checks the code lint.
- `format`: Formats the code.
- `lints`: Lints the code.
- `help` : Shows this help.
- `install`: Installs the app packages.
- `local-setup`: Sets up the local environment (e.g. install git hooks).
- `test`: Run all the tests.
- `watch`: Run all the tests in watch mode.

## Packages

This project uses [Poetry](https://python-poetry.org) as the package manager.

### Testing

- [pytest](https://docs.pytest.org/en/7.1.x/contents.html): Testing runner.
- [pytest-xdist](https://github.com/pytest-dev/pytest-xdist): Pytest plugin to run the tests in parallel.
- [expects](https://expects.readthedocs.io/en/stable/): An expressive and extensible TDD/BDD assertion library for Python..

### Code style

- [mypy](https://mypy.readthedocs.io/en/stable/): A static type checker.
- [ruff](https://github.com/astral-sh/ruff): An extremely fast Python linter and formatter, written in Rust..
