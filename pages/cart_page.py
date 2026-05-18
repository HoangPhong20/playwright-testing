from __future__ import annotations

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from config.locators import CartLocators


class CartPage:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def get_item_count(self) -> int:
        return self.page.locator(CartLocators.CART_ITEMS).count()

    def wait_cart_rendered(self) -> None:
        table = self.page.locator(CartLocators.CART_TABLE).first
        if table.count() == 0:
            self.page.wait_for_timeout(1200)
            return
        self.page.wait_for_timeout(1800)

    def has_cart_content(self) -> bool:
        if self.get_item_count() > 0:
            return True
        total = self.page.locator(CartLocators.CART_TOTAL_MONEY).first
        if total.count() == 0:
            return False
        txt = (total.inner_text() or "").strip()
        return bool(txt and txt != "0")

    def is_checkout_view(self) -> bool:
        try:
            return (
                self.page.locator(CartLocators.CHECKOUT_FORM).count() > 0
                or "gio-hang" in self.page.url
                or "checkout" in self.page.url
            )
        except Exception:
            self.page.wait_for_timeout(600)
            return "gio-hang" in self.page.url or "checkout" in self.page.url

    def wait_checkout_loaded(self) -> None:
        self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
        self.page.wait_for_timeout(1200)

    def get_first_quantity(self) -> int:
        qty = self.page.locator(CartLocators.QUANTITY_INPUT).first
        if qty.count() == 0:
            return 0
        value = (qty.input_value() or "").strip()
        digits = "".join(ch for ch in value if ch.isdigit())
        return int(digits) if digits else 0

    def increase_first_item_quantity(self) -> None:
        plus = self.page.locator(CartLocators.INCREASE_BUTTON).first
        if plus.count() == 0:
            return
        plus.click()
        self.page.wait_for_timeout(800)

    def decrease_first_item_quantity(self) -> None:
        minus = self.page.locator(CartLocators.DECREASE_BUTTON).first
        if minus.count() == 0:
            return
        minus.click()
        self.page.wait_for_timeout(800)

    def remove_first_item(self) -> None:
        remove = self.page.locator(CartLocators.REMOVE_ITEM).first
        remove.wait_for(state="visible", timeout=self.timeout)
        remove.click()
        self.page.wait_for_timeout(1200)

    def is_empty_message_visible(self) -> bool:
        return self.page.locator(CartLocators.EMPTY_MESSAGE).first.is_visible()

    def continue_shopping(self) -> bool:
        btn = self.page.locator(CartLocators.CONTINUE_SHOPPING).first
        if btn.count() == 0:
            return False
        try:
            btn.click()
            self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
            return True
        except PlaywrightTimeoutError:
            return False
