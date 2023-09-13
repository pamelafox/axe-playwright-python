# axe-playwright-python

Automated web accessibility testing using [axe-core](https://github.com/dequelabs/axe-core) engine
and [Playwright](https://playwright.dev/python/docs/intro).

## Documentation

- [Full documentation](https://pamelafox.github.io/axe-playwright-python/).

### Further Reading & More
- ["Automated accessibility audits" - Pamela Fox (North Bay Python 2023)](https://www.youtube.com/watch?v=J-4Qa6PSomM&pp=ygUUcGFtZWxhIGZveCBub3J0aCBiYXk%3D)
- [Using Python to Fix my Accessibility Night of a Website](https://kjaymiller.com/blog/using-python-to-fix-my-accessibility-nightmare-of-a-website.html) & [Website Accessibility Audit Reports via GH Actions](https://kjaymiller.com/blog/website-accessibility-audit-reports-via-gh-actions.html) by [Jay Miller](https://github.com/kjaymiller)


## Dependencies

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
from axe_playwright_python.sync_playwright import Axe

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

## Acknowledgments

This project is based on [axe-core-python](https://github.com/ruslan-rv-ua/axe-core-python) by @ruslan-rv-ua and also takes inspiration from [axe-selenium-python](https://pypi.org/project/axe-selenium-python/) for output formats.
