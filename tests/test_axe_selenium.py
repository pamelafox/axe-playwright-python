from pathlib import Path

import pytest
from axe_core_python.selenium import Axe
from selenium import webdriver

TEST_FILE = "test_page.html"
TEST_FILE_PATH = Path(__file__).parent.absolute() / TEST_FILE


@pytest.fixture
def firefox_webdriver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()


@pytest.fixture
def chrome_webdriver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_run_axe_sample_page_firefox(firefox_webdriver):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(firefox_webdriver)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


def test_run_axe_sample_page_chrome(chrome_webdriver):
    """Run axe against sample page and verify JSON output is as expected."""
    data = _perform_axe_run(chrome_webdriver)

    assert len(data["inapplicable"]) == 71
    assert len(data["incomplete"]) == 0
    assert len(data["passes"]) == 7
    assert len(data["violations"]) == 9


def _perform_axe_run(webdriver):
    webdriver.get("file://" + str(TEST_FILE_PATH))
    axe = Axe()
    data = axe.run(webdriver=webdriver)
    return data
