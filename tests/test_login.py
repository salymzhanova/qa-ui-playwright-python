import pytest
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page.locator(".inventory_list")).to_be_visible()
