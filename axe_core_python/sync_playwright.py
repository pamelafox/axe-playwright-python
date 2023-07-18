from .base import AxeBase, AxeResults

DEFAULT_OPTIONS = {"resultTypes": ["violations"]}

class Axe(AxeBase):
    def run(
        self,
        page,
        context: str | list | dict | None = None,
        options: dict | None = DEFAULT_OPTIONS,
    ) -> AxeResults:
        """Run axe accessibility checks against webpage.

        Args:
            page (playwright.sync_api._generated.Page): Page object
            context (str | list | dict | None, optional): context.
                Defaults to None.
            options (dict | None, optional): options.
                Defaults to None.

        For more information on `context` and `options`, 
            view the [axe-core documentation]().

        Returns:
            dict: test result
        """

        # inject `Axe` into document
        page.evaluate(self.axe_script)

        # Run `Axe` against the current page
        args_str = self._format_script_args(context=context, options=options)
        command_template = "axe.run(%s).then(results => {return results;})"
        command = command_template % args_str
        response = page.evaluate(command)
        return AxeResults(response)
