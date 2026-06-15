from __future__ import annotations

from urllib.parse import quote, urlsplit

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage
from components.header_component import HeaderComponent


class HomePage(BasePage):
    def __init__(self, page, timeout: int):
        super().__init__(page, timeout)
        self.header = HeaderComponent(page, timeout)

    def search_product(self, keyword: str) -> None:
        current = self.page.url
        parsed = urlsplit(current)
        if parsed.scheme and parsed.netloc:
            origin = f"{parsed.scheme}://{parsed.netloc}"
            self.page.goto(
                f"{origin}/tim-kiem/{quote(keyword)}",
                wait_until="commit",
                timeout=self.timeout,
            )
            try:
                self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
            except PlaywrightTimeoutError:
                pass
            return
        self.header.search(keyword)
