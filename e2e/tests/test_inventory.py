from e2e.pages.login_page import LoginPage
from e2e.pages.inventory_page import InventoryPage

def test_first_product_details(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.open_first_product()

    # Now safe to assert
    assert page.locator(".inventory_details_name").is_visible()
