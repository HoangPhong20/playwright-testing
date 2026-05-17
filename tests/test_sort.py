from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from utils.price_utils import is_ascending, is_descending


@pytest.mark.regression
def test_sort_price_ascending(page, base_url, test_data):
    home = HomePage(page, timeout=15000)
    listing = ProductListPage(page, timeout=15000)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.sort_by_value(test_data["sort_values"]["price_asc"])

    prices = listing.get_price_values()
    assert prices, "Expected price list not to be empty for ascending sort."
    assert is_ascending(prices), "Price list is not sorted ascending."


@pytest.mark.regression
def test_sort_price_descending(page, base_url, test_data):
    home = HomePage(page, timeout=15000)
    listing = ProductListPage(page, timeout=15000)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.sort_by_value(test_data["sort_values"]["price_desc"])

    prices = listing.get_price_values()
    assert prices, "Expected price list not to be empty for descending sort."
    assert is_descending(prices), "Price list is not sorted descending."
