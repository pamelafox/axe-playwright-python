from abc import ABC, abstractmethod
from pathlib import Path
import os
import json
from string import Template


AXE_FILE_NAME = "axe.min.js"
AXE_FILE_PATH = Path(__file__).parent / AXE_FILE_NAME

AXE_SCRIPT = AXE_FILE_PATH.read_text()


class AxeBase(ABC):
    """Abstract base class."""

    def __init__(self, axe_script: str = AXE_SCRIPT) -> None:
        """
        Args:
            axe_script (str, optional): `axe.js` or `axe.min.js` javascript.
                Defaults to AXE_SCRIPT.
        """
        self.axe_script = axe_script

    @staticmethod
    def _format_script_args(
        context: str | list | dict | None = None, options: dict | None = None
    ) -> str:
        args_list = []
        # If context is passed, add to args
        if context:
            args_list.append(repr(context))
        # If options is passed, add to args
        if options:
            args_list.append(str(options))
        # Add comma delimiter only if both parameters are passed
        args = ",".join(args_list)

        return args

    @abstractmethod
    def run(self):
        pass

    @staticmethod
    def report_violations(results: dict) -> str:
        """
        Return readable report of accessibility violations found.
        https://github.com/dequelabs/axe-core/blob/develop/doc/API.md#result-arrays
        """
        violations = results["violations"]
        report_str = f"Found {len(violations)} accessibility violations:\n"
        tmpl_f = open(os.path.join(os.path.dirname(__file__), "violations.txt"))
        template = Template(tmpl_f.read())
        tmpl_f.close()
        for violation in violations:
            nodes_str = ""
            i = 1
            for node in violation["nodes"]:
                for target in node["target"]:
                    nodes_str += f"\n\t{i}) Target: {target}"
                    i += 1
                for item in node.get("all", []) + node.get("any", []) + node.get("none", []):
                    nodes_str += "\n\t\t" + item["message"]
            report_str += template.substitute(violation, elements=nodes_str)
        return report_str

    @staticmethod
    def save_results(results: dict, file_path: str | Path | None = None,
                     violations_only: bool = False) -> None:
        """Save results to file.
        @param results: Results from Axe analysis
        @param file_path: File path for saving results file
        """
        if violations_only:
            del results["inapplicable"]
            del results["incomplete"]
            del results["passes"]
        if file_path is None:
            cwd = Path.cwd()
            file_path = cwd / "results.json"
        Path(file_path).write_text(json.dumps(results, indent=4))

    @classmethod
    def from_file(cls, axe_min_js_path: str | Path) -> "AxeBase":
        """Load axe script from file and create Axe instance.

        Args:
            axe_min_js_path (str | Path): path to `axe.js` or `axe.min.js`

        Returns:
            AxeBase: Axe instance
        """
        axe_script = Path(axe_min_js_path).read_text(encoding="UTF-8")
        return cls(axe_script=axe_script)
