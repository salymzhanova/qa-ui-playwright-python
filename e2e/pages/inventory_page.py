from playwright.sync_api import expect

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
