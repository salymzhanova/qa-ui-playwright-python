# QA UI Automation with Python + Playwright

[![UI Tests](https://github.com/salymzhanova/qa-ui-playwright-python/actions/workflows/ci.yml/badge.svg)](https://github.com/salymzhanova/qa-ui-playwright-python/actions/workflows/ci.yml)

End-to-end UI test suite for the public demo shop [SauceDemo](https://www.saucedemo.com/),
built with Python, Playwright and pytest, and run automatically in GitHub Actions.

## Tech stack
- Python 3.12
- Playwright (sync API) + pytest + pytest-playwright
- pytest-html (reports), pytest-order, pytest-timeout
- GitHub Actions (CI)

## What is tested
- Login with a valid user
- Login rejection for a locked-out user
- Product details page opens from the inventory
- Product name and price match between the inventory list and the details page

## Project structure
```
e2e/
├── conftest.py        # fixtures: isolated page per test, logged-in page, failure screenshots, video
├── pages/             # Page Objects and centralized locators
├── tests/             # test suites (login, inventory)
└── utils/             # test users and helpers
.github/workflows/     # CI pipeline
```

## Design notes
- **Page Object Model** with all selectors kept in `e2e/pages/locators.py`.
- **Isolated browser context per test**, with video recording and a screenshot on failure.
- **Web-first assertions** (`expect`) that retry automatically instead of fixed waits.
- **CI** runs on every push and pull request to `main`, with least-privilege permissions,
  and uploads the HTML report, screenshots and videos as artifacts.

## How to run locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest e2e/tests --html=reports/ui_report.html --self-contained-html
```

## Notes
- The SauceDemo credentials are the public demo ones. Override the shared
  password with the `SAUCEDEMO_PASSWORD` environment variable if needed.
- Never commit `.env` files or tokens; they are git-ignored.
