from __future__ import annotations

from playwright.sync_api import Locator
from config.locators import ProductListLocators


class ProductCardComponent:
    def __init__(self, card: Locator):
        self.card = card

    def get_name(self) -> str:
        return self.card.locator(ProductListLocators.PRODUCT_NAME).first.inner_text().strip()

    def get_price_text(self) -> str:
        return self.card.locator(ProductListLocators.PRODUCT_PRICE).first.inner_text().strip()

    def open_detail(self) -> None:
        self.card.locator("a").first.click()
