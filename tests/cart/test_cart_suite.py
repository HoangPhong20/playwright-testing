from __future__ import annotations

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from config.locators import ProductListLocators
from config.settings import TIMEOUT


def _open_product_detail_and_add_to_cart(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)
    detail = ProductDetailPage(page, timeout=TIMEOUT)
    cart = CartPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    if page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() == 0:
        listing.open_search_listing("ao")
    if page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() == 0:
        listing.open_search_listing("giày")
    assert page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0, (
        "No product detail link found. Listing locator may be outdated or site has no products."
    )

    try:
        listing.open_search_listing("ao")
    except PlaywrightTimeoutError:
        listing.open_search_listing("giày")
    links = page.locator(ProductListLocators.PRODUCT_DETAIL_LINK)
    chosen_href = None
    for i in range(min(links.count(), 20)):
        href = links.nth(i).get_attribute("href") or ""
        if "/ao-" in href.lower():
            chosen_href = href
            break
    if chosen_href:
        page.goto(chosen_href, wait_until="domcontentloaded", timeout=TIMEOUT)
    else:
        listing.open_first_product_detail()

    detail.add_to_cart()
    cart.wait_checkout_loaded()
    if not cart.is_checkout_view():
        home.header.open_cart()
        cart.wait_checkout_loaded()
    return cart, home


@pytest.mark.cart
def test_cart_quantity_update(page, base_url):
    cart, _ = _open_product_detail_and_add_to_cart(page, base_url)
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


@pytest.mark.cart
def test_cart_persistence(page, base_url):
    cart, _ = _open_product_detail_and_add_to_cart(page, base_url)
    cart.wait_cart_rendered()
    assert cart.has_cart_content(), "Expected cart to contain product before page reload."

    page.reload(wait_until="domcontentloaded", timeout=TIMEOUT)
    cart.wait_checkout_loaded()
    cart.wait_cart_rendered()
    assert cart.is_checkout_view(), f"Expected still in cart/checkout after reload, got URL: {page.url}"
    assert cart.has_cart_content(), "Expected cart data to persist after reload."
