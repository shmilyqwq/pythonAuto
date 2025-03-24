import pytest
from src.core.browser import Browser
from src.pages.login_page import LoginPage

@pytest.fixture(scope="module")
def browser():
    browser = Browser()
    browser.start()
    yield browser
    browser.quit()

def test_login(browser):
    login_page = LoginPage(browser.driver)
    login_page.open()
    login_page.login("username", "password")
    assert "Welcome" in browser.driver.title