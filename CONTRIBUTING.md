# How to contribute

## Development

Install [poetry](https://python-poetry.org/).

Install the project dependencies:

```sh
poetry install
```

Run the tests:

```sh
poetry run pytest
```

## Publishing


Set credentials for PyPi:

```sh
poetry config pypi-token.pypi <token>
```

Build the wheels:

```sh
poetry build
```

Publish to PyPi:

```sh
poetry publish
```

## Documentation

Build locally:

```sh
mkdocs serve
```

Deploy to GitHub Pages:

```sh
mkdocs gh-deploy
```