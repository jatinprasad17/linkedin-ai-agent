from playwright.sync_api import sync_playwright


def start_browser():

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch_persistent_context(
        user_data_dir="playwright_user_data",
        channel="chrome",
        headless=False
    )

    page = browser.pages[0]

    return playwright, browser, page