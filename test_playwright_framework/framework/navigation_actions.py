"""Generic navigation actions."""


def open_url(page, url):
    """Open the given URL in the current page."""
    page.goto(url)


def get_current_url(page):
    """Return the URL of the current page."""
    return page.url


def get_page_title(page):
    """Return the title of the current page."""
    return page.title()
