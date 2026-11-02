# Changelog

All notable changes to this project will be documented in this file.

## [0.1.9] - November 2, 2026

- Upgraded axe-core JS version to v4.14.0. You may see the number of violations change as a result, as new axe-core versions sometimes add new rules and update existing ones.
- This axe-core upgrade fixes relative `@import` URLs in stylesheets being resolved against the page URL instead of the stylesheet URL, which caused spurious 404 requests and incomplete `css-orientation-lock` results.
- Fixed `generate_report()` raising `TypeError` when a violation targets an element inside shadow DOM (nested target selectors). Shadow DOM targets are now shown as `host >>> element`.

## [0.1.8] - July 24, 2026

- Upgraded axe-core JS version to v4.12.1. You may see the number of violations change as a result, as new axe-core versions sometimes add new rules and update existing ones.

## [0.1.7] - November 30, 2025

- Fixed issue with passing custom options to `Axe.run()` method, which caused options to be ignored.
- Added support for Python 3.14.

## [0.1.6] - October 23, 2025

- Upgraded axe-core JS version to v4.11.0. You may see the number of violations change as a result, as new axe-core versions sometimes add new rules and update existing ones.

## [0.1.5] - June  21, 2025

- Upgraded axe-core JS version to v4.10.3. You may see the number of violations change as a result, as they added new rules and updated existing ones.
