"""
Centralized locators for e2e tests.
Organized by page/component for easy maintenance.
"""


class LoginPageLocators:
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"


class InventoryPageLocators:
    PRODUCT_NAME = ".inventory_item .inventory_item_name"
    PRODUCT_PRICE = ".inventory_item .inventory_item_price"
    PRODUCT_DETAILS_NAME = ".inventory_details_name"
    PRODUCT_DETAILS_PRICE = ".inventory_details_price"
    FIRST_PRODUCT_LINK = ".inventory_item a"
    ADD_TO_CART_BUTTON = "button[data-test^='add-to-cart']"
    REMOVE_BUTTON = "button[data-test^='remove']"
    CART_BADGE = ".shopping_cart_badge"
