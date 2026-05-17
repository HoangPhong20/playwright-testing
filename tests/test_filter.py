from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from config.locators import ProductListLocators
from config.settings import TIMEOUT


@pytest.mark.regression
def test_filter_product_by_category_brand_price(page, base_url, test_data):
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    if page.locator(ProductListLocators.FILTER_PANEL).count() == 0:
        pytest.skip("Filter controls are unavailable on current page layout.")

    listing.filter_by_category()
    listing.filter_by_brand()
    listing.filter_by_price_range(
        test_data["price_filter"]["min"],
        test_data["price_filter"]["max"],
    )

    names = listing.get_product_names()
    assert names, "Expected filtered results not to be empty."
