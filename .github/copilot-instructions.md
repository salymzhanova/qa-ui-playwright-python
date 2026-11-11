## Purpose
## Purpose

This file gives AI coding agents the essential, actionable knowledge to be productive in this repo: a synchronous Playwright UI test suite located under `e2e/` that runs with `pytest`.

### Big picture
- Project type: UI automation tests (Playwright sync API) organized with Page Objects.
- Tests: `e2e/tests/` use page objects in `e2e/pages/` and helpers from `e2e/utils/`.
- Fixtures & flow: `e2e/conftest.py` provides a session `browser`, per-test `page` (fresh context), and a `logged_in_page` that performs an automated login.

### Quick local workflow
- Create venv & install deps:
	```bash
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	```
- Install Playwright browsers:
	```bash
	playwright install
	```
- Run test suite: `pytest`
- Run a single test: `pytest -k test_first_product_details -q`

### Key patterns and conventions (project-specific)
- Synchronous API only: code uses `playwright.sync_api` — do not introduce async/await.
- Page objects: constructor accepts `page`; store selectors as attributes and expose action methods (see `e2e/pages/login_page.py`).
- Waiting: prefer `locator.first.click()` then `expect(locator).to_be_visible(timeout=...)` (see `e2e/pages/inventory_page.py`).
- Timeouts: `page.set_default_timeout(10000)` and `page.set_default_navigation_timeout(15000)` are set in `e2e/conftest.py` — use these defaults or override locally when necessary.
- Logged-in fixture: use `logged_in_page` to reuse a pre-authenticated page for tests that require login.

### Failure handling & artifacts
- Screenshots on failure are saved to `artifacts/screenshots/` via the test-report hook in `e2e/conftest.py`.
- `e2e/pytest.ini` enables `--video on` and `--screenshot on` by default; artifacts also appear under `artifacts/videos/`.

### Where to extend or add features
- Add new page objects under `e2e/pages/` following existing style (`login_page.py`, `inventory_page.py`).
- Use `e2e/utils/` for shared helpers and test data (e.g., `e2e/utils/users.py`).
- Keep selectors and textual locators in the page object as plain strings; expose behavior via methods.

### External dependencies & network
- `requirements.txt` pins `playwright==1.48.0`, `pytest`, and `pytest-playwright`.
- Tests exercise the live site `https://www.saucedemo.com/` — network access is required unless you add request mocks.

### Quick examples (from code)
- Login pattern: `LoginPage(page).login(STANDARD_USER)` — see `e2e/tests/test_inventory.py` and `e2e/utils/users.py`.
- Safe click + wait: `page.locator('.inventory_item a').first.click(); expect(page.locator('.inventory_details_name')).to_be_visible(timeout=10000)` — see `e2e/pages/inventory_page.py`.

If any section is unclear or you want CI-specific notes or additional examples, tell me which part to expand.
