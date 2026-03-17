from playwright.sync_api import Page

class LoginPage:

    URL = "https://saucedemo.com"

    def __init__(self, page:Page):
        self.page = page

        #Locators