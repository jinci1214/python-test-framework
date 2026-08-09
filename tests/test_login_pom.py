from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_login_success(page: Page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    message = login_page.get_message()

    assert "You logged into a secure area" in message
