"""Generic message actions."""


def get_validation_message(locator):
    """Return the text of a visible validation/error message."""
    return locator.inner_text().strip()
