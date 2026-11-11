"""Test users for https://www.saucedemo.com/.

These are the publicly documented demo credentials of the SauceDemo sandbox,
not real secrets. The shared password can be overridden through the
SAUCEDEMO_PASSWORD environment variable (e.g. a GitHub Actions secret/variable)
so no credential has to be hard-wired if the target ever changes.
"""
import os
from dataclasses import dataclass, field

_DEFAULT_PASSWORD = "secret_sauce"  # public SauceDemo demo password


def _password() -> str:
    return os.environ.get("SAUCEDEMO_PASSWORD", _DEFAULT_PASSWORD)


@dataclass(frozen=True)
class User:
    username: str
    # repr=False keeps the password out of logs and assertion output.
    password: str = field(default_factory=_password, repr=False)


STANDARD_USER = User("standard_user")
LOCKED_OUT_USER = User("locked_out_user")
PROBLEM_USER = User("problem_user")
PERFORMANCE_USER = User("performance_glitch_user")
