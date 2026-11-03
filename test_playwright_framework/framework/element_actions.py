"""Generic element actions. No application ids here.

The project passes in a Playwright Locator (for example page.locator("#username")).
"""


def clear_and_fill(locator, value):
    """Replace the field's current value with the given value."""
    locator.fill(value)


def click_element(locator):
    """Click a button or link."""
    locator.click()


def is_element_visible(locator):
    """Return True if the element is visible, otherwise False."""
    return locator.is_visible()
