import pytest
from e2e.pages.login_page import LoginPage


LOGIN_USERNAME = "standard_user"
LOGIN_PASSWORD = "secret_sauce"
BASE_URL = "https://www.saucedemo.com"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

def test_login(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
    assert page.url == INVENTORY_URL
