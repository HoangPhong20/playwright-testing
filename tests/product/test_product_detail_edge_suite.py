from __future__ import annotations

import pytest

from config.locators import ProductDetailLocators, ProductListLocators
from config.settings import TIMEOUT
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.product_list_page import ProductListPage
from utils.price_utils import parse_price_to_int


def _open_first_product_detail(page, base_url) -> ProductDetailPage:
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    if page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() == 0:
        listing.open_search_listing("ao")
    if page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() == 0:
        listing.open_search_listing("giày")

    assert page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0, (
        "Expected at least one product detail link before opening product detail."
    )
    listing.open_first_product_detail()
    return ProductDetailPage(page, timeout=TIMEOUT)


@pytest.mark.product
@pytest.mark.regression
def test_product_detail_price_is_parseable_positive_value(page, base_url):
    detail = _open_first_product_detail(page, base_url)

    price_text = detail.get_price()
    price = parse_price_to_int(price_text)
    assert price > 0, f"Expected product detail price to be parseable and positive, got: {price_text!r}"


@pytest.mark.product
@pytest.mark.cart
@pytest.mark.regression
def test_product_detail_add_to_cart_control_exists(page, base_url):
    _open_first_product_detail(page, base_url)

    add_to_cart = page.locator(ProductDetailLocators.ADD_TO_CART).first
    assert add_to_cart.count() > 0, "Expected product detail page to expose add-to-cart control."
    assert add_to_cart.is_visible(), "Expected add-to-cart control to be visible."
