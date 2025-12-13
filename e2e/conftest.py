import os
import pytest
from playwright.sync_api import sync_playwright

ARTIFACTS = "artifacts"
SCREENSHOTS = f"{ARTIFACTS}/screenshots"
VIDEOS = f"{ARTIFACTS}/videos"

os.makedirs(SCREENSHOTS, exist_ok=True)
os.makedirs(VIDEOS, exist_ok=True)

# Browser (session-scoped)
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

# Page (function-scoped)
@pytest.fixture
def page(browser, request):
    context = browser.new_context(
        record_video_dir=VIDEOS
    )
    page = context.new_page()

    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)

    # Attach page to test item so hooks can access it
    request.node.page = page

    yield page

    # Close AFTER pytest_runtest_makereport runs
    try:
        context.close()
    except Exception:
        pass

# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"{SCREENSHOTS}/{item.name}.png"
            try:
                page.screenshot(path=screenshot_path, full_page=True)
            except Exception:
                pass

# Logged-in page fixture
@pytest.fixture
def logged_in_page(page):
    from e2e.pages.login_page import LoginPage
    from e2e.utils.users import STANDARD_USER

    page.goto("https://www.saucedemo.com/")
    LoginPage(page).login(STANDARD_USER)

    yield page
