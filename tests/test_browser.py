from playwright.sync_api import sync_playwright

def test_open_baidu():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.baidu.com")

        title = page.title()
        print(title)

        assert "百度" in title


        browser.close()