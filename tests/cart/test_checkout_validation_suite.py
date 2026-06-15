from __future__ import annotations

import pytest

from config.settings import TIMEOUT
from pages.cart_page import CartPage
from pages.home_page import HomePage
from tests.cart.test_cart_suite import _open_product_detail_and_add_to_cart


SPECIAL_CHARACTER_WARD = "@@@###"


def _open_empty_checkout(page, base_url) -> CartPage:
    home = HomePage(page, timeout=TIMEOUT)
    cart = CartPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    page.goto(f"{base_url.rstrip('/')}/gio-hang.html", wait_until="domcontentloaded", timeout=TIMEOUT)
    cart.wait_checkout_loaded()
    return cart


def _assert_ward_rejects_special_characters(cart: CartPage) -> None:
    cart.fill_shipping_information(ward=SPECIAL_CHARACTER_WARD)
    cart.complete_order()
    ward_value = cart.get_ward_value()

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order with invalid special-character ward value."
    )
    assert ward_value != SPECIAL_CHARACTER_WARD, (
        "Expected ward field to reject a value made only from special characters after submit."
    )
    assert not any(char in ward_value for char in "@#$%"), (
        f"Expected ward field not to keep special characters, got: {ward_value!r}"
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_submit_without_product_is_handled_gracefully(page, base_url):
    cart = _open_empty_checkout(page, base_url)

    cart.fill_shipping_information(ward="Phuong 1")
    cart.complete_order()

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order when cart has no product."
    )
    assert cart.has_checkout_validation_feedback(), (
        "Expected checkout to show a clear validation message when submitting without product."
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_ward_field_rejects_special_characters_with_product(page, base_url):
    cart, _ = _open_product_detail_and_add_to_cart(page, base_url)
    cart.wait_cart_rendered()

    assert cart.has_cart_content(), "Expected cart to contain product before checkout validation."
    _assert_ward_rejects_special_characters(cart)
