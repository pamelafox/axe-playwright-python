# axe-core-python

![PyPI](https://img.shields.io/pypi/v/axe-core-python) 
![PyPI - License](https://img.shields.io/pypi/l/axe-core-python) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/axe-core-python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/axe-core-python) 


Automated web accessibility testing using [axe-core](https://github.com/dequelabs/axe-core) engine.

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

For more examples see [documentation](https://ruslan-rv-ua.github.io/axe-core-python/).