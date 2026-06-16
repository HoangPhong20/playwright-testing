from __future__ import annotations

from urllib.parse import quote, urlsplit

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from config.locators import ProductListLocators
from components.product_card_component import ProductCardComponent
from utils.price_utils import parse_price_to_int
from utils.wait_utils import wait_for_product_detail_loaded, wait_for_products_loaded


class ProductListPage:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def wait_loaded(self) -> None:
        wait_for_products_loaded(self.page, self.timeout)

    def get_product_cards(self) -> list[ProductCardComponent]:
        cards = self.page.locator(self._card_selector())
        return [ProductCardComponent(cards.nth(i)) for i in range(cards.count())]

    def get_product_names(self) -> list[str]:
        self.wait_loaded()
        names = [card.get_name(self._name_selector()) for card in self.get_product_cards()]
        return [name for name in names if name]

    def get_price_values(self) -> list[int]:
        self.wait_loaded()
        prices: list[int] = []
        for card in self.get_product_cards():
            try:
                prices.append(parse_price_to_int(card.get_price_text(self._price_selector())))
            except Exception:
                continue
        return [p for p in prices if p > 0]

    def _card_selector(self) -> str:
        url = self.page.url
        if "/tim-kiem/" in url:
            return ProductListLocators.SEARCH_PRODUCT_CARDS
        return ProductListLocators.HOME_PRODUCT_CARDS

    def _name_selector(self) -> str:
        url = self.page.url
        if "/tim-kiem/" in url:
            return ProductListLocators.SEARCH_PRODUCT_NAME
        return ProductListLocators.HOME_PRODUCT_NAME

    def _price_selector(self) -> str:
        url = self.page.url
        if "/tim-kiem/" in url:
            return ProductListLocators.SEARCH_PRODUCT_PRICE
        return ProductListLocators.HOME_PRODUCT_PRICE

    def open_search_listing(self, keyword: str) -> None:
        keyword = keyword.strip()
        parsed = urlsplit(self.page.url)
        if not parsed.scheme or not parsed.netloc:
            raise AssertionError("Cannot derive base URL from current page.")

        self.page.goto(
            f"{parsed.scheme}://{parsed.netloc}/tim-kiem/{quote(keyword)}",
            wait_until="domcontentloaded",
            timeout=max(self.timeout, 30000),
        )
        self.wait_loaded()

    def filter_by_category(self) -> None:
        category = self.page.locator(ProductListLocators.CATEGORY_FILTER).first
        if category.count() == 0:
            return
        category.click()
        self.wait_loaded()

    def filter_by_brand(self) -> None:
        brand = self.page.locator(ProductListLocators.BRAND_FILTER).first
        if brand.count() == 0:
            return
        brand.click()
        self.wait_loaded()

    def filter_by_price_range(self, min_price: str, max_price: str) -> None:
        min_input = self.page.locator(ProductListLocators.PRICE_MIN).first
        max_input = self.page.locator(ProductListLocators.PRICE_MAX).first
        if min_input.count() == 0 or max_input.count() == 0:
            return
        min_input.fill(min_price)
        max_input.fill(max_price)
        apply = self.page.locator(ProductListLocators.APPLY_FILTER).first
        if apply.count() > 0:
            apply.click()
        self.wait_loaded()

    def open_first_product_detail(self) -> None:
        self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
        title_link = self.page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).first
        if title_link.count() == 0:
            for keyword in ("ao", "giày"):
                self.open_search_listing(keyword)
                title_link = self.page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).first
                if title_link.count() > 0:
                    break

        if title_link.count() > 0:
            try:
                title_link.click()
                self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
                wait_for_product_detail_loaded(self.page, self.timeout)
                return
            except PlaywrightTimeoutError:
                href = title_link.get_attribute("href")
                if href:
                    self.page.goto(href, wait_until="domcontentloaded", timeout=self.timeout)
                    wait_for_product_detail_loaded(self.page, self.timeout)
                    return

        cards = self.get_product_cards()
        if not cards:
            raise AssertionError("No product card found to open detail page.")
        cards[0].open_detail()
