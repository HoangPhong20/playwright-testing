from __future__ import annotations

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from config.locators import CartLocators
from utils.wait_utils import (
    wait_for_cart_item_removed,
    wait_for_cart_rendered,
    wait_for_checkout_ready,
    wait_for_quantity_value,
)


class CartPage:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def get_item_count(self) -> int:
        return self.page.locator(CartLocators.CART_ITEMS).count()

    def wait_cart_rendered(self) -> None:
        wait_for_cart_rendered(self.page, self.timeout)

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
            return "gio-hang" in self.page.url or "checkout" in self.page.url

    def wait_checkout_loaded(self) -> None:
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
        except PlaywrightTimeoutError:
            pass
        wait_for_checkout_ready(self.page, self.timeout)

    def get_first_quantity(self) -> int:
        qty = self.page.locator(CartLocators.QUANTITY_INPUT).first
        if qty.count() == 0:
            return 0
        value = (qty.input_value() or "").strip()
        digits = "".join(ch for ch in value if ch.isdigit())
        return int(digits) if digits else 0

    def increase_first_item_quantity(self) -> None:
        previous_value = self._first_quantity_value()
        if self._step_first_quantity("ArrowUp", previous_value):
            return
        plus = self.page.locator(CartLocators.INCREASE_BUTTON).first
        if plus.count() == 0:
            return
        plus.click()
        try:
            wait_for_quantity_value(self.page, previous_value, self.timeout)
        except PlaywrightTimeoutError:
            pass

    def decrease_first_item_quantity(self) -> None:
        previous_value = self._first_quantity_value()
        if self._step_first_quantity("ArrowDown", previous_value):
            return
        minus = self.page.locator(CartLocators.DECREASE_BUTTON).first
        if minus.count() == 0:
            return
        minus.click()
        try:
            wait_for_quantity_value(self.page, previous_value, self.timeout)
        except PlaywrightTimeoutError:
            pass

    def remove_first_item(self) -> None:
        remove = self.page.locator(CartLocators.REMOVE_ITEM).first
        remove.wait_for(state="visible", timeout=self.timeout)
        previous_count = self.get_item_count()
        remove.click()
        try:
            wait_for_cart_item_removed(self.page, previous_count, self.timeout)
        except PlaywrightTimeoutError:
            pass

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

    def fill_shipping_information(
        self,
        *,
        name: str = "Automation Test",
        phone: str = "0989248835",
        ward: str = "Phường 1",
        address: str = "So 1 Duong Test",
        note: str = "Automation validation test",
    ) -> None:
        self._fill_if_present(CartLocators.CUSTOMER_NAME, name)
        self._fill_if_present(CartLocators.CUSTOMER_PHONE, phone)
        self._select_first_available_option(CartLocators.PROVINCE_SELECT)
        self._select_first_available_option(CartLocators.DISTRICT_SELECT)
        self._fill_if_present(CartLocators.WARD_INPUT, ward)
        self._fill_if_present(CartLocators.SHIPPING_ADDRESS, address)
        self._fill_if_present(CartLocators.SHIPPING_NOTE, note)

    def get_ward_value(self) -> str:
        return self._input_value(CartLocators.WARD_INPUT)

    def get_name_value(self) -> str:
        return self._input_value(CartLocators.CUSTOMER_NAME)

    def get_phone_value(self) -> str:
        return self._input_value(CartLocators.CUSTOMER_PHONE)

    def get_address_value(self) -> str:
        return self._input_value(CartLocators.SHIPPING_ADDRESS)

    def complete_order(self) -> None:
        button = self.page.locator(CartLocators.COMPLETE_ORDER).first
        button.wait_for(state="visible", timeout=self.timeout)
        button.click()
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=self.timeout)
        except PlaywrightTimeoutError:
            pass

    def is_order_success_visible(self) -> bool:
        try:
            success = self.page.locator(CartLocators.ORDER_SUCCESS_TEXT).first
            return success.count() > 0 and success.is_visible()
        except Exception:
            return False

    def has_empty_checkout_validation_feedback(self) -> bool:
        return self._has_visible_feedback(CartLocators.EMPTY_CHECKOUT_VALIDATION_FEEDBACK)

    def has_phone_validation_feedback(self) -> bool:
        return self._has_field_validation_feedback(
            CartLocators.PHONE_VALIDATION_FEEDBACK,
            CartLocators.CUSTOMER_PHONE,
        )

    def has_name_validation_feedback(self) -> bool:
        return self._has_field_validation_feedback(
            CartLocators.NAME_VALIDATION_FEEDBACK,
            CartLocators.CUSTOMER_NAME,
        )

    def has_address_validation_feedback(self) -> bool:
        return self._has_field_validation_feedback(
            CartLocators.ADDRESS_VALIDATION_FEEDBACK,
            CartLocators.SHIPPING_ADDRESS,
        )

    def has_ward_validation_feedback(self) -> bool:
        return self._has_field_validation_feedback(
            CartLocators.WARD_VALIDATION_FEEDBACK,
            CartLocators.WARD_INPUT,
        )

    def _has_visible_feedback(self, selector: str) -> bool:
        try:
            feedback = self.page.locator(selector).first
            return feedback.count() > 0 and feedback.is_visible()
        except Exception:
            return False

    def _has_field_validation_feedback(self, feedback_selector: str, field_selector: str) -> bool:
        return (
            self._has_visible_feedback(feedback_selector)
            or self._has_html5_validation_message(field_selector)
        )

    def _has_html5_validation_message(self, field_selector: str) -> bool:
        try:
            return bool(
                self.page.evaluate(
                    """(selector) => {
                        const fields = Array.from(document.querySelectorAll(selector));
                        return fields.some((field) => {
                            if (typeof field.checkValidity !== 'function') return false;
                            return !field.checkValidity() && Boolean(field.validationMessage);
                        });
                    }""",
                    field_selector,
                )
            )
        except Exception:
            return False

    def _fill_if_present(self, selector: str, value: str) -> None:
        field = self.page.locator(selector).first
        if field.count() == 0:
            return
        field.wait_for(state="visible", timeout=self.timeout)
        field.fill(value)

    def _input_value(self, selector: str) -> str:
        field = self.page.locator(selector).first
        field.wait_for(state="visible", timeout=self.timeout)
        return (field.input_value() or "").strip()

    def _select_first_available_option(self, selector: str) -> None:
        select = self.page.locator(selector).first
        if select.count() == 0:
            return
        select.wait_for(state="visible", timeout=self.timeout)
        for _ in range(10):
            options = select.locator("option")
            for index in range(options.count()):
                value = (options.nth(index).get_attribute("value") or "").strip()
                label = (options.nth(index).inner_text() or "").strip()
                if value and "*" not in label:
                    select.select_option(value=value)
                    try:
                        self.page.wait_for_timeout(300)
                    except PlaywrightTimeoutError:
                        pass
                    return
            try:
                self.page.wait_for_timeout(500)
            except PlaywrightTimeoutError:
                return

    def _first_quantity_value(self) -> str:
        qty = self.page.locator(CartLocators.QUANTITY_INPUT).first
        if qty.count() == 0:
            return ""
        return (qty.input_value() or "").strip()

    def _step_first_quantity(self, key: str, previous_value: str) -> bool:
        qty = self.page.locator(CartLocators.QUANTITY_INPUT).first
        if qty.count() == 0:
            return False
        qty.wait_for(state="visible", timeout=self.timeout)
        qty.focus()
        qty.press(key)
        try:
            wait_for_quantity_value(self.page, previous_value, self.timeout)
            return True
        except PlaywrightTimeoutError:
            return False
