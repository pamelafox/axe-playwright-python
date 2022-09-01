from .base import AxeBase


class Axe(AxeBase):
    def run(
        self,
        webdriver,
        context: str | list | dict | None = None,
        options: dict | None = None,
    ) -> dict:
        """Run axe accessibility checks against webdriver.


        Args:
            webdriver (): selenium webdriver
            context (str | list | dict | None, optional): context.
                Defaults to None.
            options (dict | None, optional): options.
                Defaults to None.

        For more information on `context` and `options`, 
            view the [axe-core documentation]().

        Returns:
            dict: test result
        """
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
