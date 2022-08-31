### Selenium

TODO:

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
            "console": False,
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

TODO:

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
https://camo.githubusercontent.com/41415ee92389d5dd1a36783f3f230a67aa8a9cd64a36f324719bf7011e8f0513/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6178652d73656c656e69756d2d707974686f6e2e737667