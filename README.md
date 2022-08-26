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

### Selenium

```python
axe_core_python.selenium.Axe.run(
    webdriver,
    context: str | list | dict | None = None,
    options: dict | None = None,
) -> dict:
```

For `context` and `options` paremeters see [axe-core API documentation](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md#api-name-axerun).

Remote testing:

```python
from selenium import webdriver
from axe_core_python.selenium import Axe
from pathlib import Path
import json

desired_caps = {
            'platform' : "win10",
            'browserName' : "chrome",
            'version' :  "67.0",
            "resolution": "1024x768",
            "name": "LambdaTest python google search test ",
            "build": "LambdaTest python google search build",
            "network": True,
            "video": False,
            "visual": False,
            "console": True,
        }

# remote Chrome browser on [lambdatest.com](https://www.lambdatest.com)
driver = webdriver.Remote(
            desired_capabilities=desired_caps,
            command_executor=f"https://{LAMBDATEST_USERNAME}:{LAMBDATEST_ACCESS_TOKEN}@hub.lambdatest.com/wd/hub"
        )
driver.get("https://www.google.com")

axe = Axe()

# run test only on element with `id="user-content"`
result = axe.run(driver, context="#user-content")

# save issues only
violations_json = json.dumps(result['violations], indent=2)
Path('violations.json').write_text(violations_json, encoding='utf8')
```



### Playwright

```python
async axe_core_python.async_playwright.Axe.run(
    page: playwright.sync_api.Page,
    context: str | list | dict | None = None,
    options: dict | None = None,
) -> dict:
```

Async function to test webpage for color contrast issues only:

```python
from playwright.async_api import async_playwright
from axe_core_python.async_playwright import Axe

axe = Axe()

async def test_color_contrast(url: str) -> dict:
    async with sync_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        result = await axe.run(page, options={'runOnly': 'color-contrast'})
        await browser.close()
        return result['violations']
```
