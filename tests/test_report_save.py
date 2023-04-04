import os
import json
from pathlib import Path

import pytest

from axe_core_python.sync_playwright import Axe


@pytest.fixture
def test_results_json():   
    result_path = os.path.join(os.path.dirname(__file__), "test_result.json")
    with open(result_path, "r") as f:
        results = json.load(f)
    return results


def test_report(test_results_json):
    report = Axe.report_violations(test_results_json)
    report_path = os.path.join(os.path.dirname(__file__), "test_report.txt")
    with open(report_path, "r") as f:
        assert report == f.read()


def test_save_results(test_results_json):
    Axe.save_results(test_results_json)
    # Assert that file was created and looks like JSON
    assert Path("results.json").is_file()
    with open("results.json", "r") as f:
        assert f.readline() == "{\n"
    os.remove("results.json")


def test_save_results_with_path(test_results_json):
    Axe.save_results(test_results_json, "results2.json")
    assert Path("results2.json").is_file()
    os.remove("results2.json")


def test_save_results_with_pathlib(test_results_json):
    Axe.save_results(test_results_json, Path("results3.json"))
    assert Path("results3.json").is_file()
    os.remove("results3.json")

def test_save_results_violations_only(test_results_json):
    file_path = Path("results_violations.json")
    Axe.save_results(test_results_json, file_path, violations_only=True)
    assert file_path.is_file()
    results_json = open(file_path).read()
    assert "incomplete" not in results_json
    assert "passes" not in results_json
    assert "inapplicable" not in results_json
    os.remove(file_path)
