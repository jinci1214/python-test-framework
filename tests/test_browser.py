from playwright.sync_api import Page


def test_open_baidu(page: Page):
    page.goto("https://www.baidu.com")

    title = page.title()
    print(title)

    assert "百度" in title
