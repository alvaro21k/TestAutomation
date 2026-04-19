from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://saucedemo.com"

    def __init__(self, page:Page):
        super().__init__(page)

        #Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_container = page.locator("[data-test='error']")

    def open_page(self):
        self.navigate(self.URL)


    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_inner_text(self.error_container)




