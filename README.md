# axe-python-playwright

Automated web accessibility testing using [axe-core](https://github.com/dequelabs/axe-core) engine
and [Playwright](https://playwright.dev/python/docs/intro).

## Documentation

- [Full documentation](https://pamelafox.github.io/axe-playwright-python/).

## Requirements

- Python >= 3.10
- [playwright](https://github.com/microsoft/playwright-python) >= 1.25.0

## Installation

```console
python3 -m pip install -U axe-playwright-python
python3 -m playwright install --with-deps
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
    results = axe.run(page)
    browser.close()

print(f"Found {results.violations_count} violations.")
print(f"Full axe-core response: {results.response}")
```

For more examples see [documentation](https://pamelafox.github.io/axe-playwright-python/).

## Contributing

See [guide on contributing](CONTRIBUTING.md).