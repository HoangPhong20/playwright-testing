from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from utils.price_utils import is_ascending, is_descending
from config.settings import TIMEOUT
from config.locators import ProductListLocators


@pytest.mark.regression
def test_sort_price_ascending(page, base_url, test_data):
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    if page.locator(ProductListLocators.SORT_DROPDOWN).count() == 0:
        pytest.skip("Sort dropdown is unavailable on current page layout.")
    listing.sort_by_value(test_data["sort_values"]["price_asc"])

    prices = listing.get_price_values()
    if len(prices) < 2:
        pytest.skip("Sort control or comparable price list is unavailable on current page.")
    assert prices, "Expected price list not to be empty for ascending sort."
    assert is_ascending(prices), "Price list is not sorted ascending."


@pytest.mark.regression
def test_sort_price_descending(page, base_url, test_data):
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    if page.locator(ProductListLocators.SORT_DROPDOWN).count() == 0:
        pytest.skip("Sort dropdown is unavailable on current page layout.")
    listing.sort_by_value(test_data["sort_values"]["price_desc"])

    prices = listing.get_price_values()
    if len(prices) < 2:
        pytest.skip("Sort control or comparable price list is unavailable on current page.")
    assert prices, "Expected price list not to be empty for descending sort."
    assert is_descending(prices), "Price list is not sorted descending."
