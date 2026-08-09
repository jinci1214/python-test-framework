from playwright.sync_api import Page


def test_login_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")

    page.fill("#password", "SuperSecretPassword!")

    page.click("button[type='submit']")

    message = page.locator("#flash").inner_text()

    print(message)

    assert "You logged into a secure area" in message
