import pytest
from playwright.sync_api import sync_playwright
from api.seventeen_lands_client import SeventeenLandsClient


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session")
def api_client():
    """
    Session-scoped fixture - creates one client for the entire
    test session rather than one per test.
    """
    return SeventeenLandsClient()