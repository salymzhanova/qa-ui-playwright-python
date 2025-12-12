import os
import pytest
from playwright.sync_api import sync_playwright

# Ensure artifacts folder exists for screenshots/videos
os.makedirs("artifacts/screenshots", exist_ok=True)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    # Use a fresh browser context per test to avoid shared state (cookies/localStorage)
    context = browser.new_context()
    page = context.new_page()
    # Set default timeout for actions/navigation
    page.set_default_timeout(10000)          # 10 seconds for clicks, typing, etc.
    page.set_default_navigation_timeout(15000)  # 15 seconds for page loads
    yield page
    try:
        page.close()
    except Exception:
        pass
    try:
        context.close()
    except Exception:
        import os
        import pytest

        # Ensure artifacts folder exists for screenshots/videos
        os.makedirs("artifacts/screenshots", exist_ok=True)


        @pytest.fixture(autouse=True)
        def configure_page(page):
            """Configure the plugin-provided `page` fixture for all tests.

            This replaces custom `browser`/`page` fixtures and sets default timeouts.
            """
            # Default timeouts: 10s for actions, 15s for navigation
            page.set_default_timeout(10000)
            page.set_default_navigation_timeout(15000)
            yield


        @pytest.hookimpl(tryfirst=True, hookwrapper=True)
        def pytest_runtest_makereport(item, call):
            outcome = yield
            result = outcome.get_result()
            if result.when == "call" and result.failed:
                page = item.funcargs.get("page", None)
                if page:
                    try:
                        page.screenshot(path=f"artifacts/screenshots/{item.name}.png")
                    except Exception:
                        # Best-effort: don't fail the test-reporting hook if screenshot fails
                        pass

@pytest.fixture
def logged_in_page(page):
    from e2e.pages.login_page import LoginPage
    from e2e.utils.users import STANDARD_USER

    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login(STANDARD_USER)
    try:
        yield page # Test runs here
        # Teardown code runs after test
    finally:
        try:
            page.close()
        except Exception:
            pass
