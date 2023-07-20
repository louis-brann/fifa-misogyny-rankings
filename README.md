## FIFA Misogyny Rankings

With the FIFA Women's World Cup going on, I was curious of a
general rule for which countries were good at women's soccer.
I had a general idea that USA, Germany, the ex-UK colonies,
Brazil, Colombia and Scandinavia were pretty good, and that
generally misogynystic countries are not.

I wanted clear data on which countries were specifically
better at women's soccer comparatively, so that's what this
attempts to do.

## Setup

This project relies on `pyenv` and `poetry`.

- [`pyenv` installation](https://github.com/pyenv/pyenv#installation)
- [`poetry` installation](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Edit the `pyproject.toml` with info for the new project
    - name
    - description
    - packages
- Run `poetry install` to get set up

## Tools

### Code
- Type Checking: `mypy`
- Formatter: `black`

### CI/CD

- Git hooks
    - pre-commit: `pre-commit`
- Github workflows
    - `build.yaml`
