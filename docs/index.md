# axe-core-python

![PyPI](https://img.shields.io/pypi/v/axe-core-python) 
![PyPI - License](https://img.shields.io/pypi/l/axe-core-python) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/axe-core-python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/axe-core-python) 


Automated web accessibility testing using [axe-core](https://github.com/dequelabs/axe-core) engine.

## Requirements

You will need the following prerequisites in order to use axe-core-python:

- Python >= 3.10
- [selenium](https://www.selenium.dev) >= 4.4.0 
or [playwright](https://github.com/microsoft/playwright-python) >= 1.25.0

## Installation

```console
pip install -U axe-core-python
```

### Selenium

To install Selenium:

```console
pip install selenium
```

The appropriate driver for the browser you intend to use should be 
downloaded and added to your path, 
e.g. [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox:

To simplify management of binary drivers for different browsers: 
[Webdriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager).

### Playwright

To install Playwright ([docs](https://playwright.bootcss.com/python/docs/installation)):

```console
pip install playwright
```

Also install browser binaries:

```console
python -m playwright install
```
