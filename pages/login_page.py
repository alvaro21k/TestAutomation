from playwright.sync_api import Page

class LoginPage:

    URL = "https://saucedemo.com"

    def __init__(self, page:Page):
        self.page = page

        #Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_container = page.locator("[data-test='error']")

    def open_page(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_container.inner_text()




