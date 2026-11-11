import re
from pathlib import Path

import pytest

from e2e.pages.login_page import LoginPage
from e2e.utils.users import STANDARD_USER

ARTIFACTS = Path("artifacts")
SCREENSHOTS = ARTIFACTS / "screenshots"
VIDEOS = ARTIFACTS / "videos"
BASE_URL = "https://www.saucedemo.com/"


def _safe_name(name: str) -> str:
    """Make a test id safe to use as a file name."""
    return re.sub(r"[^\w.\-\[\]]+", "_", name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Expose each phase's report on the item so fixtures can inspect the outcome."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def page(browser, request):
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    VIDEOS.mkdir(parents=True, exist_ok=True)

    context = browser.new_context(record_video_dir=str(VIDEOS))
    page = context.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)

    try:
        yield page
    finally:
        report = getattr(request.node, "rep_call", None)
        if report is not None and report.failed:
            try:
                page.screenshot(
                    path=str(SCREENSHOTS / f"{_safe_name(request.node.name)}.png"),
                    full_page=True,
                )
            except Exception as exc:  # screenshot is best-effort
                print(f"Could not capture failure screenshot: {exc}")
        # Close after the screenshot so the video is finalized.
        context.close()


@pytest.fixture
def logged_in_page(page):
    page.goto(BASE_URL)
    LoginPage(page).login(STANDARD_USER)
    return page
