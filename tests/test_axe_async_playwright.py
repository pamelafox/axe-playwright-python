from pathlib import Path

import pytest
import pytest_asyncio
from axe_core_python.async_playwright import Axe
from playwright.async_api import async_playwright

TEST_FILE = "test_page.html"
TEST_FILE_PATH = Path(__file__).parent.absolute() / TEST_FILE


@pytest_asyncio.fixture
async def firefox_page():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        yield page
        await browser.close()


@pytest_asyncio.fixture
async def chromium_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        yield page
        await browser.close()


@pytest_asyncio.fixture
async def webkit_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        yield page
        await browser.close()


@pytest.mark.asyncio
async def test_run_axe_sample_page_firefox(firefox_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = await _perform_axe_run(firefox_page)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


@pytest.mark.asyncio
async def test_run_axe_sample_page_chrimium(chromium_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = await _perform_axe_run(chromium_page)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


@pytest.mark.asyncio
async def test_run_axe_sample_page_webkit(webkit_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = await _perform_axe_run(webkit_page)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


async def _perform_axe_run(page):
    await page.goto("file://" + str(TEST_FILE_PATH))
    axe = Axe()
    data = await axe.run(page=page)
    return data
