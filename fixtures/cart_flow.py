from __future__ import annotations

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from config.locators import ProductListLocators
from config.settings import TIMEOUT
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.product_list_page import ProductListPage


def open_product_detail_and_add_to_cart(page, base_url: str, test_data: dict):
    primary_keyword = test_data["search"]["primary_keyword"]
    fallback_keywords = test_data["search"]["fallback_keywords"]
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)
    detail = ProductDetailPage(page, timeout=TIMEOUT)
    cart = CartPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    for keyword in fallback_keywords:
        if page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0:
            break
        listing.open_search_listing(keyword)
    assert page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0, (
        "No product detail link found. Listing locator may be outdated or site has no products."
    )

    try:
        listing.open_search_listing(primary_keyword)
    except PlaywrightTimeoutError:
        for keyword in fallback_keywords:
            if keyword == primary_keyword:
                continue
            listing.open_search_listing(keyword)
            break
    links = page.locator(ProductListLocators.PRODUCT_DETAIL_LINK)
    chosen_href = None
    for index in range(min(links.count(), 20)):
        href = links.nth(index).get_attribute("href") or ""
        if f"/{primary_keyword}-" in href.lower():
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
