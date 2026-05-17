from __future__ import annotations

from playwright.sync_api import Locator


class ProductCardComponent:
    def __init__(self, card: Locator):
        self.card = card

    def get_name(self, name_selector: str) -> str:
        locator = self.card.locator(name_selector).first
        if locator.count() == 0:
            return ""
        return locator.inner_text().strip()

    def get_price_text(self, price_selector: str) -> str:
        locator = self.card.locator(price_selector).first
        if locator.count() == 0:
            return ""
        return locator.inner_text().strip()

    def open_detail(self) -> None:
        self.card.locator("a").first.click()
