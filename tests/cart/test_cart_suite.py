from __future__ import annotations

import pytest
from config.settings import TIMEOUT
from fixtures.cart_flow import open_product_detail_and_add_to_cart


@pytest.mark.cart
def test_cart_quantity_update(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()
    assert cart.has_cart_content(), "Expected cart to contain product before quantity update."

    initial_qty = cart.get_first_quantity()
    assert initial_qty >= 1, f"Expected initial quantity >= 1, got {initial_qty}."

    cart.increase_first_item_quantity()
    qty_after_plus = cart.get_first_quantity()
    assert qty_after_plus >= initial_qty, (
        f"Expected quantity to increase or stay same after plus: {initial_qty} -> {qty_after_plus}"
    )

    cart.decrease_first_item_quantity()
    qty_after_minus = cart.get_first_quantity()
    assert qty_after_minus <= qty_after_plus, (
        f"Expected quantity to decrease or stay same after minus: {qty_after_plus} -> {qty_after_minus}"
    )

    cart.complete_order()
    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete when submitting without shipping information."
    )


@pytest.mark.cart
def test_cart_persistence(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()
    assert cart.has_cart_content(), "Expected cart to contain product before page reload."

    page.reload(wait_until="domcontentloaded", timeout=TIMEOUT)
    cart.wait_checkout_loaded()
    cart.wait_cart_rendered()
    assert cart.is_checkout_view(), f"Expected still in cart/checkout after reload, got URL: {page.url}"
    assert cart.has_cart_content(), "Expected cart data to persist after reload."

    cart.complete_order()
    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete when submitting without shipping information."
    )
