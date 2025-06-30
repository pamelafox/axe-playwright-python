# How to contribute

## Development

Install the project dependencies:

```sh
python3 -m pip install -e '.[dev]'
playwright install --with-deps
pre-commit install
```

Run the tests:

```sh
python3 -m pytest
```

## Publishing

Configure flit to use token-based PyPi credentials:

```sh
export FLIT_USERNAME=__token__
export FLIT_PASSWORD=your-pypi-token
```

Publish to PyPi:

```sh
flit publish
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
