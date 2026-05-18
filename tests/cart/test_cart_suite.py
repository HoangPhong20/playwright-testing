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
        page.goto("https://aobongda.net/tim-kiem/ao", wait_until="domcontentloaded", timeout=TIMEOUT)
    if page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() == 0:
        page.goto("https://aobongda.net/tim-kiem/giay", wait_until="domcontentloaded", timeout=TIMEOUT)
    assert page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0, (
        "No product detail link found. Listing locator may be outdated or site has no products."
    )

    try:
        page.goto("https://aobongda.net/tim-kiem/ao", wait_until="domcontentloaded", timeout=TIMEOUT)
    except PlaywrightTimeoutError:
        page.goto("https://aobongda.net/tim-kiem/giay", wait_until="domcontentloaded", timeout=TIMEOUT)
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
@pytest.mark.regression
def test_add_and_remove_product_from_cart(page, base_url):
    cart, home = _open_product_detail_and_add_to_cart(page, base_url)

    assert cart.is_checkout_view(), (
        f"Expected redirect to checkout/cart view after add-to-cart, got URL: {page.url}"
    )
    cart.wait_cart_rendered()
    assert cart.has_cart_content(), (
        "Expected checkout/cart to contain product after add-to-cart action."
    )

    initial_qty = cart.get_first_quantity()
    assert initial_qty >= 1, f"Expected default quantity >= 1, got {initial_qty}."

    cart.increase_first_item_quantity()
    qty_after_plus = cart.get_first_quantity()
    if qty_after_plus > 0:
        assert qty_after_plus >= initial_qty, (
            f"Expected quantity not to decrease after plus click: {initial_qty} -> {qty_after_plus}"
        )

    cart.decrease_first_item_quantity()
    qty_after_minus = cart.get_first_quantity()
    if qty_after_minus > 0 and qty_after_plus > 0:
        assert qty_after_minus <= qty_after_plus, (
            f"Expected quantity not to increase after minus click: {qty_after_plus} -> {qty_after_minus}"
        )

    cart.remove_first_item()
    assert cart.get_item_count() == 0 or cart.is_empty_message_visible(), (
        "Expected cart to be empty after removing the product."
    )

    # Validate user can go back to shopping from checkout/cart view.
    home.header.open_cart()
    if cart.continue_shopping():
        assert "/gio-hang" not in page.url and "/checkout" not in page.url, (
            f"Expected leaving checkout/cart after continue shopping, got URL: {page.url}"
        )


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
