from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def fill(self, locator, text):
        locator.fill(text)

    def get_inner_text(self, locator):
        return locator.inner_text()

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url