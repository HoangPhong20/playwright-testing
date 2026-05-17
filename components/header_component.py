from __future__ import annotations

from playwright.sync_api import Page
from config.locators import HeaderLocators


class HeaderComponent:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def search(self, keyword: str) -> None:
        search_input = self.page.locator(HeaderLocators.SEARCH_INPUT).first
        search_input.wait_for(state="visible", timeout=self.timeout)
        search_input.fill(keyword)
        submit = self.page.locator(HeaderLocators.SEARCH_SUBMIT).first
        if submit.count() > 0:
            submit.click()
        else:
            search_input.press("Enter")

    def open_cart(self) -> None:
        self.page.locator(HeaderLocators.CART_ICON).first.click()
