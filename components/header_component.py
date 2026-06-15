from __future__ import annotations

from urllib.parse import urljoin

from playwright.sync_api import Page
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from config.locators import HeaderLocators
from utils.wait_utils import wait_for_cart_rendered


class HeaderComponent:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def search(self, keyword: str) -> None:
        search_input = self.page.locator(HeaderLocators.SEARCH_INPUT).first
        search_input.wait_for(state="visible", timeout=self.timeout)
        previous_url = self.page.url
        search_input.fill(keyword)
        submit = self.page.locator(HeaderLocators.SEARCH_SUBMIT).first
        if submit.count() > 0:
            submit.click()
        else:
            search_input.press("Enter")
        try:
            self.page.wait_for_function(
                """(previousUrl) => window.location.href !== previousUrl
                    || document.querySelector('.list_sp .item, .productHome .itemBox') !== null""",
                arg=previous_url,
                timeout=min(self.timeout, 5000),
            )
        except PlaywrightTimeoutError:
            pass

    def open_cart(self) -> None:
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
        except PlaywrightTimeoutError:
            pass
        href = self._cart_href() or self._default_cart_href()
        if href:
            try:
                self.page.goto(href, wait_until="domcontentloaded", timeout=self.timeout)
                wait_for_cart_rendered(self.page, self.timeout)
            except PlaywrightError:
                pass
            return

    def _cart_href(self) -> str | None:
        for _ in range(3):
            try:
                cart_links = self.page.locator(HeaderLocators.CART_ICON)
                for index in range(cart_links.count()):
                    href = cart_links.nth(index).get_attribute("href")
                    if href and ("gio-hang" in href or "cart" in href):
                        return href
                return None
            except PlaywrightError:
                try:
                    self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
                except PlaywrightTimeoutError:
                    pass
        return None

    def _default_cart_href(self) -> str | None:
        if not self.page.url.startswith(("http://", "https://")):
            return None
        return urljoin(self.page.url, "/gio-hang.html")
