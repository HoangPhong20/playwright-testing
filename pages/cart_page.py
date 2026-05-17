from __future__ import annotations

from playwright.sync_api import Page
from config.locators import CartLocators


class CartPage:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def get_item_count(self) -> int:
        return self.page.locator(CartLocators.CART_ITEMS).count()

    def remove_first_item(self) -> None:
        remove = self.page.locator(CartLocators.REMOVE_ITEM).first
        remove.wait_for(state="visible", timeout=self.timeout)
        remove.click()

    def is_empty_message_visible(self) -> bool:
        return self.page.locator(CartLocators.EMPTY_MESSAGE).first.is_visible()
