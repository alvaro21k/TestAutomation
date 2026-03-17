import pytest
from pages.login_page import LoginPage

def test_successful_login(page):
    login = LoginPage(page)
    login.open_page()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.parametrize("username, password",
                         [("invalid_user", "secret_sauce"),
                          ("standard_user", "invalid_password"),
                          ("standard_user", ""),
                          ("","secret_sauce"),
                          ("","")
                          ])
def test_invalid_login(page, username, password):
    login = LoginPage(page)
    login.open_page()
    login.login(username, password)
    assert "Epic sadface" in login.get_error_message()
