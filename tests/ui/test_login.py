from pages.login_page import LoginPage

def test_successful_login(page):
    login = LoginPage(page)
    login.open_page()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_username(page):
    login = LoginPage(page)
    login.open_page()
    login.login("ldahdljas", "secret_sauce")
    assert "Epic sadface" in login.get_error_message()

def test_invalid_password(page):
    login = LoginPage(page)
    login.open_page()
    login.login("standard_user", "asdjhkajas")
    assert "Epic sadface" in login.get_error_message()