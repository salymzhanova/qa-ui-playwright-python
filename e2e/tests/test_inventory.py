from e2e.pages.login_page import LoginPage
from e2e.pages.inventory_page import InventoryPage
from e2e.utils.users import STANDARD_USER

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

def test_first_product_details(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.login(STANDARD_USER)

    inventory = InventoryPage(page)
    inventory.open_first_product()

    # Now safe to assert
    assert page.locator(".inventory_details_name").is_visible()
