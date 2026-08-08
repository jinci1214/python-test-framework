from playwright.sync_api import sync_playwright


def test_login_page():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "tomsmith")

        page.fill("#password", "SuperSecretPassword!")

        page.click("button[type='submit']")

        message = page.locator("#flash").inner_text()

        print(f"啊{message}")

        assert "You logged into a secure area" in message

        browser.close()