## Purpose
Guidance for AI coding agents working in this repo: a synchronous Playwright UI test suite under `e2e/`, run with `pytest`.

### Big picture
- UI automation (Playwright sync API) organized with Page Objects.
- Tests live in `e2e/tests/`, page objects and locators in `e2e/pages/`, test users and helpers in `e2e/utils/`.
- `e2e/conftest.py` provides a per-test `page` fixture (fresh browser context, video, screenshot on failure) and a `logged_in_page` fixture.

### Local workflow
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest e2e/tests
```
Run one test: `pytest e2e/tests -k test_first_product_details -q`

### Conventions
- Sync API only: use `playwright.sync_api`, no async/await.
- Page objects take `page` in the constructor and expose action methods. Selectors live in `e2e/pages/locators.py`.
- Prefer web-first assertions (`expect(locator)...`) over `assert` and fixed waits.
- Timeouts: default 10s, navigation 15s (set in `conftest.py`); per-test limit via `--timeout` in `e2e/pytest.ini`.
- Never hard-code real credentials. SauceDemo demo users are in `e2e/utils/users.py`; the password can be overridden with `SAUCEDEMO_PASSWORD`.

### Artifacts and CI
- Screenshots on failure go to `artifacts/screenshots/`, videos to `artifacts/videos/` (git-ignored).
- CI (`.github/workflows/ci.yml`) is pinned to `ubuntu-24.04` because Playwright 1.48 cannot install system deps on newer images. Keep dependencies pinned in `requirements.txt`.
- Tests hit the live site `https://www.saucedemo.com/`, so network access is required.
