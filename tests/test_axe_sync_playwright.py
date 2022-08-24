from pathlib import Path

import pytest
from axe_core_python.sync_plalywright import Axe
from playwright.sync_api import sync_playwright

TEST_FILE = "test_page.html"
TEST_FILE_PATH = Path(__file__).parent.absolute() / TEST_FILE


@pytest.fixture
def firefox_page():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def chromium_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def webkit_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


def test_run_axe_sample_page_firefox(firefox_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(firefox_page)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


def test_run_axe_sample_page_chrimium(chromium_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(chromium_page)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


def test_run_axe_sample_page_webkit(webkit_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(webkit_page)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


def _perform_axe_run(page):
    page.goto("file://" + str(TEST_FILE_PATH))
    axe = Axe()
    data = axe.run(page=page)
    return data
