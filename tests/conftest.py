import pytest
from playwright.sync_api import Browser, Page, Playwright, sync_playwright


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    """Start Playwright once for the whole test session."""
    with sync_playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Browser:
    """Share one headless Chromium browser across all UI tests."""
    browser_instance = playwright.chromium.launch(headless=True)
    yield browser_instance
    browser_instance.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    """Give every test an isolated browser page and close it afterwards."""
    page_instance = browser.new_page()
    yield page_instance
    page_instance.close()
