import pytest
from playwright.sync_api import expect

from e2e.conftest import BASE_URL
from e2e.pages.locators import LoginPageLocators
from e2e.pages.login_page import LoginPage
from e2e.utils.users import LOCKED_OUT_USER, STANDARD_USER

INVENTORY_URL = f"{BASE_URL}inventory.html"


@pytest.mark.order(1)
def test_login(page):
    page.goto(BASE_URL)
    LoginPage(page).login(STANDARD_USER)
    expect(page).to_have_url(INVENTORY_URL)


@pytest.mark.order(2)
def test_locked_out_user(page):
    page.goto(BASE_URL)
    LoginPage(page).login(LOCKED_OUT_USER)
    error = page.locator(LoginPageLocators.ERROR_MESSAGE)
    expect(error).to_be_visible()
    expect(error).to_contain_text("locked out")
