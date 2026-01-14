import os
import pytest
from playwright.sync_api import sync_playwright

ARTIFACTS = "artifacts"
SCREENSHOTS = f"{ARTIFACTS}/screenshots"
VIDEOS = f"{ARTIFACTS}/videos"

os.makedirs(SCREENSHOTS, exist_ok=True)
os.makedirs(VIDEOS, exist_ok=True)

# Page (function-scoped)
@pytest.fixture
def page(browser, request):
    context = browser.new_context(record_video_dir=VIDEOS)
    page = context.new_page()

    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)

    # Save context + page so hooks can see both
    request.node.page = page
    request.node.context = context

    yield page

    # Don't close here — let hook run first

# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        page = getattr(item, "page", None)
        context = getattr(item, "context", None)

        # Screenshot on failure
        if result.failed and page:
            screenshot_path = f"{SCREENSHOTS}/{item.name}.png"
            try:
                page.screenshot(path=screenshot_path, full_page=True)
            except Exception:
                pass

        # Close context AFTER screenshot + video finalize
        if context:
            try:
                context.close()
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
