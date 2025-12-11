import pytest
from e2e.pages.login_page import LoginPage
from e2e.utils.users import STANDARD_USER
from e2e.utils.users import LOCKED_OUT_USER

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

@pytest.mark.order(1)
def test_login(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.login(STANDARD_USER)
    assert page.url == INVENTORY_URL

@pytest.mark.order(2)
def test_locked_out_user(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.login(LOCKED_OUT_USER)
    error = page.locator("[data-test='error']")
    assert error.is_visible()
    assert "locked out" in error.inner_text().lower()
