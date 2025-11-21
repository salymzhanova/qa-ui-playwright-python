class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


STANDARD_USER = User("standard_user", "secret_sauce")
LOCKED_OUT_USER = User("locked_out_user", "secret_sauce")
PROBLEM_USER = User("problem_user", "secret_sauce")
PERFORMANCE_USER = User("performance_glitch_user", "secret_sauce")