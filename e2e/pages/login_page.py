class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"

    def login(self, user):
        self.page.fill(self.username, user.username)
        self.page.fill(self.password, user.password)
        self.page.click(self.login_button)
