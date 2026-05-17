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
        self.page.wait_for_timeout(1000)

    def open_cart(self) -> None:
        cart = self.page.locator(HeaderLocators.CART_ICON).first
        href = cart.get_attribute("href") if cart.count() > 0 else None
        if href:
            self.page.goto(href, wait_until="commit", timeout=self.timeout)
            return
        cart.click()
