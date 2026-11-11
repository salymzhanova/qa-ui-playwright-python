import pytest
from playwright.sync_api import expect

from e2e.conftest import BASE_URL
from e2e.pages.inventory_page import InventoryPage
from e2e.pages.locators import InventoryPageLocators
from e2e.pages.login_page import LoginPage
from e2e.utils.users import STANDARD_USER


@pytest.mark.order(1)
def test_first_product_details(page):
    page.goto(BASE_URL)
    LoginPage(page).login(STANDARD_USER)

    InventoryPage(page).open_first_product()

    expect(page.locator(InventoryPageLocators.PRODUCT_DETAILS_NAME)).to_be_visible()


@pytest.mark.order(2)
def test_verify_consistent_product_details(logged_in_page):
    page = logged_in_page
    inventory = InventoryPage(page)

    first_product_name = inventory.get_first_product_name()
    first_product_price = inventory.get_first_product_price()

    inventory.open_first_product()

    expect(page.locator(InventoryPageLocators.PRODUCT_DETAILS_NAME)).to_have_text(first_product_name)
    expect(page.locator(InventoryPageLocators.PRODUCT_DETAILS_PRICE)).to_have_text(first_product_price)
