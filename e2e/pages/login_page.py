class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_button)
