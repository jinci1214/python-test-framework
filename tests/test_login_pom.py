from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_login_success():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()


        login_page = LoginPage(page)


        login_page.open()


        login_page.login(
            "tomsmith",
            "SuperSecretPassword!"
        )


        message = login_page.get_message()


        assert "You logged into a secure area" in message


        browser.close()