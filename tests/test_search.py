from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage


@pytest.mark.smoke
@pytest.mark.parametrize("keyword", ["ao", "giay", "phu kien"])
def test_search_product_by_keyword(page, base_url, keyword):
    home = HomePage(page, timeout=15000)
    listing = ProductListPage(page, timeout=15000)

    home.open(base_url)
    home.accept_cookie_if_present()
    home.search_product(keyword)

    names = listing.get_product_names()
    assert names, "Expected search result list not to be empty."
    assert any(keyword.lower() in name.lower() for name in names), (
        f"Expected at least one product name to contain keyword: {keyword}"
    )


@pytest.mark.regression
def test_search_with_non_existing_keyword(page, base_url, test_data):
    home = HomePage(page, timeout=15000)
    listing = ProductListPage(page, timeout=15000)

    home.open(base_url)
    home.accept_cookie_if_present()
    home.search_product(test_data["non_existing_keyword"])

    names = listing.get_product_names()
    assert not names, "Expected no product for non-existing keyword."
