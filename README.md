# axe-core-python
Automated web accessibility testing using [`axe-core`](https://github.com/dequelabs/axe-core) engine.


## Features

TODO: tell them why this library is so cool.

## Requirements

You will need the following prerequisites in order to use axe-core-python:

- Python >= 3.10
- one of (or both):
    - selenium >= 4.0.0 
    - [playwright](https://github.com/microsoft/playwright-python) >= 1.25.0


### Selenium

Install with pip:

```console
pip install selenium
```

The appropriate driver for the browser you intend to use should be 
downloaded and added to your path, 
e.g. [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox:

### Playwright

Install with pip:

```console
pip install playwright
```

Then install browser binaries:

```console
python -m playwright install
```

More about [Playwright installation](https://playwright.bootcss.com/python/docs/installation).

## Installation

```console
pip install -U axe-core-python
```

## Usage

### Playwright

```python
from playwright.sync_api import sync_playwright
from axe_core_python.playwright import run

def test_axe(url: str) -> dict:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        result = run(page)
        browser.close()
        return result
```