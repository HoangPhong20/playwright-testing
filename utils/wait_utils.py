from __future__ import annotations

from playwright.sync_api import Page
from config.locators import ProductListLocators


def wait_for_products_loaded(page: Page, timeout: int) -> None:
    page.locator(ProductListLocators.PRODUCT_CARDS).first.wait_for(
        state="visible",
        timeout=timeout,
    )
