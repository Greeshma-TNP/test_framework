"""Login tests for https://www.saucedemo.com"""

from framework.navigation_actions import get_current_url


def test_valid_login(login_page, page):
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in get_current_url(page)


def test_invalid_login(login_page):
    login_page.login("standard_user", "wrong_password")

    assert login_page.is_error_shown()
    assert login_page.get_error_message() == (
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_empty_username_and_password(login_page):
    login_page.login("", "")

    assert login_page.get_error_message() == "Epic sadface: Username is required"


def test_empty_password(login_page):
    login_page.login("standard_user", "")

    assert login_page.get_error_message() == "Epic sadface: Password is required"
