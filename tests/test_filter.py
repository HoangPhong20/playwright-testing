from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage


@pytest.mark.regression
def test_filter_product_by_category_brand_price(page, base_url, test_data):
    home = HomePage(page, timeout=15000)
    listing = ProductListPage(page, timeout=15000)

    home.open(base_url)
    home.accept_cookie_if_present()

    listing.filter_by_category()
    listing.filter_by_brand()
    listing.filter_by_price_range(
        test_data["price_filter"]["min"],
        test_data["price_filter"]["max"],
    )

    names = listing.get_product_names()
    assert names, "Expected filtered results not to be empty."
