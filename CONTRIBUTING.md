# How to contribute

## Development

Install the project dependencies:

```sh
python -m pip install -e '.[dev]'
playwright install --with-deps
pre-commit install
```

Run the tests:

```sh
python -m pytest
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

## Publishing

1. Update the CHANGELOG with description of changes

2. Update the version number in pyproject.toml

3. Push the changes to the main branch

4. Publish to PyPi:

    ```sh
    export FLIT_USERNAME=__token__
    export FLIT_PASSWORD=your-pypi-token
    flit publish
    ```
