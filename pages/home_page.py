from __future__ import annotations

from pages.base_page import BasePage
from components.header_component import HeaderComponent


class HomePage(BasePage):
    def __init__(self, page, timeout: int):
        super().__init__(page, timeout)
        self.header = HeaderComponent(page, timeout)

    def search_product(self, keyword: str) -> None:
        self.header.search(keyword)
