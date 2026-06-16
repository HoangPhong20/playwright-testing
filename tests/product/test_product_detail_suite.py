from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage
from config.locators import ProductListLocators
from config.settings import TIMEOUT


@pytest.mark.smoke
@pytest.mark.regression
def test_view_product_detail(page, base_url, test_data):
    fallback_keywords = test_data["search"]["fallback_keywords"]
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)
    detail = ProductDetailPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    for keyword in fallback_keywords:
        if page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0:
            break
        listing.open_search_listing(keyword)
    assert page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0, (
        "No product detail link found. Listing locator may be outdated or site has no products."
    )
    listing.open_first_product_detail()

    assert detail.is_image_visible(), "Expected product image to be visible."
    assert detail.get_description(), "Expected product description not to be empty."
    assert detail.get_price(), "Expected product price not to be empty."
