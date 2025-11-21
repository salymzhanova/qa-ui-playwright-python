import pytest
from e2e.pages.login_page import LoginPage
from e2e.utils.users import STANDARD_USER

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

def test_login(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.login(STANDARD_USER)
    assert page.url == INVENTORY_URL
