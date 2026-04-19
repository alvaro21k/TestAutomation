from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):

        self.item_list = page.locator(".inventory_item")



