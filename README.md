# axe-core-python

Automated web accessibility testing using [`axe-core`](https://github.com/dequelabs/axe-core) engine.

## Features

TODO: tell them why this library is so cool.

## Requirements

You will need the following prerequisites in order to use axe-core-python:

- Python >= 3.10
- [selenium](https://www.selenium.dev) >= 4.4.0 
or [playwright](https://github.com/microsoft/playwright-python) >= 1.25.0

## Installation

```console
pip install -U axe-core-python
```

To install Selenium:

```console
pip install selenium
```

Also the appropriate driver for the browser you intend to use should be 
downloaded and added to your path, 
e.g. [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox:

To install Playwright ([docs](https://playwright.bootcss.com/python/docs/installation)):

```console
pip install playwright
```

Also install browser binaries:

```console
python -m playwright install
```

## Usage

Use `Axe.run()` on browser's Page.

### Playwright

```python
from playwright.sync_api import sync_playwright
from axe_core_python.sync_playwright import Axe

axe = Axe()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://github.com/Microsoft/playwright-python")
    result = axe.run(page)
    browser.close()
```
