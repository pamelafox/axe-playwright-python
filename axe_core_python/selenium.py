from .base import AxeBase


class Axe(AxeBase):
    def run(
        self,
        webdriver,
        context: str | list | dict | None = None,
        options: dict | None = None,
    ) -> dict:
        # Recursively inject `Axe` into all iframes and the top level document
        webdriver.execute_script(self.axe_script)

        # Run `Axe` against the current page
        args_str = self._format_script_args(context, options)
        command_template = (
            "var seleniumCallback = arguments[arguments.length - 1];"
            "axe.run(%s).then(results => seleniumCallback(results))"
        )
        command = command_template % args_str
        response = webdriver.execute_async_script(command)
        return response
