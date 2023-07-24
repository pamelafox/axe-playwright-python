# How to contribute

## Development

Install the project dependencies:

```sh
python3 -m pip install -e '.[test]'
playwright install --with-deps
```

Run the tests:

```sh
python3 -m pytest
```

## Publishing


Install the build dependencies:

```sh
python3 -m pip install -e '.[build]'
```

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