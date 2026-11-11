from playwright.sync_api import Locator


def wait_for_element(locator: Locator, timeout: int = 5000) -> None:
    locator.wait_for(state="visible", timeout=timeout)
