# How to contribute

## Development

Install [poetry](https://python-poetry.org/).

Install the project dependencies:

```
poetry install
```

Run the tests:

```
poetry run pytest
```

## Publishing


Set credentials for PyPi:

```
poetry config pypi-token.pypi <token>
```

Build the wheels:

```
poetry build
```

Publish to PyPi:

```
poetry publish
```

## Documentation

Build locally:

```
mkdocs serve
```

Deploy to GitHub Pages:

```
mkdocs gh-deploy
```