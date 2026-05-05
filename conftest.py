import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")  #scope="session" = tarayıcıyı bir kere aç, tüm testler bitince kapat.
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser #yield = testi çalıştır, bitince browser.close() ile kapat.
        browser.close()

#→ Her test için yeni bir sekme aç, test bitince sekmeyi kapat.
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()