from playwright.sync_api import expect
from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page):
        self.page = page
        # Use a more reliable clickable selector
        self.first_product_link = ".inventory_item a"

    def open_first_product(self):
        try:
            # Click first product safely
            self.page.locator(self.first_product_link).first.click()

            # Wait for the product title to be visible
            expect(self.page.locator(".inventory_details_name")).to_be_visible(timeout=10000)

        except Exception as e:
            # Ensure screenshots folder exists
            import os
            os.makedirs("artifacts/screenshots", exist_ok=True)
            self.page.screenshot(path="artifacts/screenshots/open_first_product_error.png")

            # Raise a clear runtime error
            raise RuntimeError(f"Failed to open first product: {e}") from e

    def get_first_product_name(self):
        # Return the visible name of the first product on the inventory list.
        return self.page.locator(".inventory_item .inventory_item_name").first.inner_text()

    def get_first_product_price(self):
        # Return the visible price text of the first product on the inventory list.
        return self.page.locator(".inventory_item .inventory_item_price").first.inner_text()

    # def get_cart_count(self) -> int:
    #     """Returns the current number of items in the cart, or 0 if empty."""
    #     cart_badge = self.page.locator(InventoryPageLocators.CART_BADGE)
    #     if cart_badge.is_visible():
    #         return int(cart_badge.inner_text())
    #     return 0

    # def add_first_available_item(self):
    #     """Clicks the first 'Add to Cart' button found on the page."""
    #     # Using .first in case there are multiple buttons
    #     self.page.locator(InventoryPageLocators.ADD_TO_CART_BUTTON).first.click()

    # def verify_cart_count(self, expected_count: int):
    #     """Asserts that the cart badge shows the expected number."""
    #     cart_badge = self.page.locator(InventoryPageLocators.CART_BADGE)
    #     # We use playwright's 'expect' for built-in retries
    #     from playwright.sync_api import expect
    #     expect(cart_badge).to_have_text(str(expected_count))