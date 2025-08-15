import pytest
from e2e.pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")
    assert page.url.endswith("inventory.html")