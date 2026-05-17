from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage


@pytest.mark.cart
@pytest.mark.regression
def test_add_and_remove_product_from_cart(page, base_url):
    home = HomePage(page, timeout=15000)
    listing = ProductListPage(page, timeout=15000)
    detail = ProductDetailPage(page, timeout=15000)
    cart = CartPage(page, timeout=15000)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.open_first_product_detail()
    detail.add_to_cart()
    home.header.open_cart()

    assert cart.get_item_count() >= 1, "Expected at least one item in cart after add."

    cart.remove_first_item()
    assert cart.get_item_count() == 0 or cart.is_empty_message_visible(), (
        "Expected cart to be empty after removing the product."
    )
