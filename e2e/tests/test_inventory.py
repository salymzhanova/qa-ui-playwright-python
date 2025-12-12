import pytest
from e2e.pages.login_page import LoginPage
from e2e.pages.inventory_page import InventoryPage
from e2e.utils.users import STANDARD_USER

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

@pytest.mark.order(1)
def test_first_product_details(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.login(STANDARD_USER)

    inventory = InventoryPage(page)
    inventory.open_first_product()

    assert page.locator(".inventory_details_name").is_visible()

@pytest.mark.order(2)
def test_verify_consistent_product_details(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.login(STANDARD_USER)

    inventory = InventoryPage(page)
    first_product_name = inventory.get_first_product_name()
    first_product_price = inventory.get_first_product_price()
    inventory.open_first_product()

    detail_name = page.locator(".inventory_details_name").inner_text()
    detail_price = page.locator(".inventory_details_price").inner_text()

    assert first_product_name == detail_name
    assert first_product_price == detail_price