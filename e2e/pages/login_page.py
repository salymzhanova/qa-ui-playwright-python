from playwright.sync_api import Page

from e2e.pages.locators import LoginPageLocators
from e2e.utils.users import User


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, user: User) -> None:
        self.page.fill(LoginPageLocators.USERNAME_INPUT, user.username)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, user.password)
        self.page.click(LoginPageLocators.LOGIN_BUTTON)
