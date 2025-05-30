
The first step is to run `axe.run()` on a Playwright `Page` object

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
```

The `results` object is an instance of `AxeResults`,
and we can work with it in several ways.

### Count the number of violations

```python
print(f"Found {results.violations_count} violations.")
```

```console
Found 6 violations.
```

### Generate a human-readable report of violations

```python
print(results.generate_report())
```

```console
Found 6 accessibility violations:
Rule Violated:
aria-allowed-role - Ensures role attribute has an appropriate value for the element
    URL: https://dequeuniversity.com/rules/axe/4.4/aria-allowed-role?application=axeAPI
    Impact Level: minor
    Tags: ['cat.aria', 'best-practice']
    Elements Affected:
    

        1)      Target: #APjFqb
                Snippet: <textarea class="gLFyf" jsaction="paste:puy29d;" id="APjFqb" maxlength="2048" name="q" rows="1" aria-activedescendant="" aria-autocomplete="both" aria-controls="Alh6id" aria-expanded="false" aria-haspopup="both" aria-owns="Alh6id" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" type="search" value="" aria-label="Search" data-ved="0ahUKEwjwp-W68p2AAxVyDEQIHUlIA_IQ39UDCAc">
                Messages:
                * ARIA role combobox is not allowed for given element
    ... (report truncated for brevity)
```

### Generate a snapshot of violations

This can be helpful for snapshot testing.

```python
print(results.generate_snapshot())
```

```console
aria-allowed-role (minor) : 1
aria-valid-attr-value (critical) : 2
color-contrast (serious) : 8
landmark-one-main (moderate) : 1
page-has-heading-one (moderate) : 1
region (moderate) : 9
```

### Show the full axe-core response

```python
print(f"Full axe-core response: {results.response}")
```

The response is of the form described in the [axe-core API docs](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md#results-object).

### Save the full axe-core response to a file

```python
results.save_to_file("results.json")
```
