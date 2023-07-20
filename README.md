## Python Template repo

A repo to contain the basic tools + setup info for new Python repos

## Setup

This project relies on `pyenv` and `poetry`.

- [`pyenv` installation](https://github.com/pyenv/pyenv#installation)
- [`poetry` installation](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Then run `poetry install` to get set up

## Tools

### Code
- Type Checking: `mypy`
- Formatter: `black`

### CI/CD

- Git hooks
    - pre-commit: `pre-commit`
- Github workflows
    - `build.yaml`
