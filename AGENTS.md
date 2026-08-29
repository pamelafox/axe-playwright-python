# Agent Instructions

## Upgrading axe-core

To upgrade the bundled `axe-core` JavaScript library (`axe_playwright_python/axe.min.js`), follow these steps:

1. Run the installation script:
   ```bash
   bash .github/scripts/install-axe.sh
   ```
   Optionally, specify a target version (e.g., `4.13.0`):
   ```bash
   bash .github/scripts/install-axe.sh 4.13.0
   ```

2. Run the test suite:
   ```bash
   pytest
   ```

3. Check code formatting and linting:
   ```bash
   ruff check .
   black --check .
   ```
