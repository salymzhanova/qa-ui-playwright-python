def wait_for_element(locator, timeout=5000):
    locator.wait_for(state="visible", timeout=timeout)
