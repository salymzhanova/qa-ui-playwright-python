import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    # Set default timeout for actions/navigation
    page.set_default_timeout(10000)          # 10 seconds for clicks, typing, etc.
    page.set_default_navigation_timeout(15000)  # 15 seconds for page loads
    yield page
    page.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            page.screenshot(path=f"artifacts/screenshots/{item.name}.png")
