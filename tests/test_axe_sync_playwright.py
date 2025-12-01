from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from axe_playwright_python.sync_playwright import Axe

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


def _perform_axe_run(page):
    page.goto("file://" + str(TEST_FILE_PATH))
    axe = Axe()
    results = axe.run(page=page)
    return results.response


def test_run_axe_sample_page_firefox(firefox_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(firefox_page)

    assert len(data["inapplicable"]) == 75
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 6
    assert len(data["violations"]) == 9


def test_run_axe_sample_page_chromium(chromium_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(chromium_page)

    assert len(data["inapplicable"]) == 75
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 6
    assert len(data["violations"]) == 9


def test_run_axe_sample_page_webkit(webkit_page):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(webkit_page)

    assert len(data["inapplicable"]) == 75
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 6
    assert len(data["violations"]) == 9


def test_run_axe_detects_region_violation(chromium_page):
    """Baseline check confirming region violation is reported by default."""
    chromium_page.goto("file://" + str(TEST_FILE_PATH))
    axe = Axe()

    # First run with default options
    results = axe.run(page=chromium_page)
    violation_ids = {violation["id"] for violation in results.response["violations"]}
    assert "region" in violation_ids

    # Now run again with region rule disabled
    options = {"rules": {"region": {"enabled": False}}}
    results = axe.run(page=chromium_page, options=options)
    violation_ids = {violation["id"] for violation in results.response["violations"]}
    assert "region" not in violation_ids
