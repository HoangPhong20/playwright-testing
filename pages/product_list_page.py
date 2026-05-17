from __future__ import annotations

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from config.locators import ProductListLocators
from components.product_card_component import ProductCardComponent
from utils.price_utils import parse_price_to_int
from utils.wait_utils import wait_for_products_loaded


class ProductListPage:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def wait_loaded(self) -> None:
        try:
            wait_for_products_loaded(self.page, self.timeout)
        except PlaywrightTimeoutError:
            pass

    def get_product_cards(self) -> list[ProductCardComponent]:
        cards = self.page.locator(ProductListLocators.PRODUCT_CARDS)
        return [ProductCardComponent(cards.nth(i)) for i in range(cards.count())]

    def get_product_names(self) -> list[str]:
        self.wait_loaded()
        return [card.get_name() for card in self.get_product_cards()]

    def get_price_values(self) -> list[int]:
        self.wait_loaded()
        prices: list[int] = []
        for card in self.get_product_cards():
            try:
                prices.append(parse_price_to_int(card.get_price_text()))
            except Exception:
                continue
        return [p for p in prices if p > 0]

    def sort_by_value(self, value: str) -> None:
        dropdown = self.page.locator(ProductListLocators.SORT_DROPDOWN).first
        dropdown.wait_for(state="visible", timeout=self.timeout)
        dropdown.select_option(value=value)
        self.wait_loaded()

    def filter_by_category(self) -> None:
        category = self.page.locator(ProductListLocators.CATEGORY_FILTER).first
        category.click()
        self.wait_loaded()

    def filter_by_brand(self) -> None:
        brand = self.page.locator(ProductListLocators.BRAND_FILTER).first
        brand.click()
        self.wait_loaded()

    def filter_by_price_range(self, min_price: str, max_price: str) -> None:
        min_input = self.page.locator(ProductListLocators.PRICE_MIN).first
        max_input = self.page.locator(ProductListLocators.PRICE_MAX).first
        min_input.fill(min_price)
        max_input.fill(max_price)
        self.page.locator(ProductListLocators.APPLY_FILTER).first.click()
        self.wait_loaded()

    def open_first_product_detail(self) -> None:
        cards = self.get_product_cards()
        if not cards:
            raise AssertionError("No product card found to open detail page.")
        cards[0].open_detail()
