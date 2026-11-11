from pathlib import Path

from playwright.sync_api import Page, expect

from e2e.pages.locators import InventoryPageLocators


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def open_first_product(self) -> None:
        try:
            self.page.locator(InventoryPageLocators.FIRST_PRODUCT_LINK).first.click()
            expect(self.page.locator(InventoryPageLocators.PRODUCT_DETAILS_NAME)).to_be_visible(timeout=10000)
        except Exception as e:
            screenshots = Path("artifacts/screenshots")
            screenshots.mkdir(parents=True, exist_ok=True)
            self.page.screenshot(path=str(screenshots / "open_first_product_error.png"))
            raise RuntimeError(f"Failed to open first product: {e}") from e

    def get_first_product_name(self) -> str:
        """Return the visible name of the first product on the inventory list."""
        return self.page.locator(InventoryPageLocators.PRODUCT_NAME).first.inner_text()

    def get_first_product_price(self) -> str:
        """Return the visible price text of the first product on the inventory list."""
        return self.page.locator(InventoryPageLocators.PRODUCT_PRICE).first.inner_text()
