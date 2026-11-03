"""Shared test setup. pytest runs this automatically."""

import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    """Open the login page and give it to the test."""
    login = LoginPage(page)
    login.open()
    return login
