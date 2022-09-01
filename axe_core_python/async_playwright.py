from .base import AxeBase


class Axe(AxeBase):
    async def run(
        self,
        page,
        context: str | list | dict | None = None,
        options: dict | None = None,
    ) -> dict:
        """Asynchronously run axe accessibility checks against webpage.

        Args:
            page (playwright.async_api.Page): Page object
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
        await page.evaluate(self.axe_script)

        # Run `Axe` against the current page
        args_str = self._format_script_args(context=context, options=options)
        command_template = "axe.run(%s).then(results => {return results;})"
        command = command_template % args_str
        response = await page.evaluate(command)
        return response
