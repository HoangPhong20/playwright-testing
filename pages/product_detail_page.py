from __future__ import annotations

from playwright.sync_api import Page
from config.locators import ProductDetailLocators


class ProductDetailPage:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def is_image_visible(self) -> bool:
        return bool(
            self.page.evaluate(
                """(selector) => {
                    const imgs = Array.from(document.querySelectorAll(selector));
                    return imgs.some((img) => {
                        const src = (img.getAttribute('src') || '').trim();
                        const dataSrc = (img.getAttribute('data-src') || '').trim();
                        const looksLikeProductImage = src.includes('/pic/Product/') || dataSrc.includes('/pic/Product/');
                        return looksLikeProductImage;
                    });
                }""",
                ProductDetailLocators.GALLERY_IMAGE,
            )
        )

    def get_description(self) -> str:
        locator = self.page.locator(ProductDetailLocators.DESCRIPTION).first
        if locator.count() == 0:
            return ""
        return locator.inner_text().strip()

    def get_price(self) -> str:
        locator = self.page.locator(ProductDetailLocators.PRODUCT_PRICE).first
        if locator.count() == 0:
            return ""
        return locator.inner_text().strip()

    def add_to_cart(self) -> None:
        button = self.page.locator(ProductDetailLocators.ADD_TO_CART).first
        if button.count() == 0:
            return
        button.wait_for(state="visible", timeout=self.timeout)
        button.click()
