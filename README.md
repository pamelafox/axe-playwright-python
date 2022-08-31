# axe-core-python

[![Latest Version](https://pypip.in/version/axe-core-python>/badge.svg)](https://pypi.python.org/pypi/axe-core-python/)


Automated web accessibility testing using [axe-core](https://github.com/dequelabs/axe-core) engine.

## Features

TODO: tell them why this library is so cool.

## Documentation

- [Full documentation](https://ruslan-rv-ua.github.io/axe-core-python/).

## Requirements

- Python >= 3.10
- [selenium](https://www.selenium.dev) >= 4.4.0 
or [playwright](https://github.com/microsoft/playwright-python) >= 1.25.0

## Installation

```console
pip install -U axe-core-python
```

## Usage

```python
from playwright.sync_api import sync_playwright
from axe_core_python.sync_playwright import Axe

axe = Axe()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com")
    result = axe.run(page)
    browser.close()

violations = result['violations']
print(f"{len(violations)} violations found.")
```

More examples and API available in [documentation](https://ruslan-rv-ua.github.io/axe-core-python/).