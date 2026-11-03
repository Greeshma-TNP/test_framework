"""Login page of https://www.saucedemo.com

The real ids of the application live here, not in the framework.
"""

from framework.element_actions import clear_and_fill, click_element, is_element_visible
from framework.message_actions import get_validation_message
from framework.navigation_actions import open_url


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page
        # actual ids from the Sauce Demo application
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        open_url(self.page, self.URL)

    def login(self, username, password):
        clear_and_fill(self.username_input, username)
        clear_and_fill(self.password_input, password)
        click_element(self.login_button)

    def get_error_message(self):
        return get_validation_message(self.error_message)

    def is_error_shown(self):
        return is_element_visible(self.error_message)
