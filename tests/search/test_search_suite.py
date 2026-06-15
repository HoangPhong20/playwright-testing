from __future__ import annotations

import pytest
from urllib.parse import quote
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from config.settings import TIMEOUT


@pytest.mark.smoke
@pytest.mark.search
@pytest.mark.regression
def test_search_product_by_keyword(page, base_url):
    keyword = "ao"
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    home.search_product(keyword)

    names = listing.get_product_names()
    assert "/tim-kiem/" in page.url, (
        f"Expected search page URL to contain '/tim-kiem/', got: {page.url}"
    )
    assert names, "Expected search result list not to be empty."
    assert f"/tim-kiem/{quote(keyword)}" in page.url, (
        f"Expected URL to include searched keyword '{keyword}', got: {page.url}"
    )
    assert any(keyword.lower() in name.lower() for name in names), (
        f"Expected at least one product name to contain keyword: {keyword}"
    )


@pytest.mark.search
def test_product_list_display(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.open_search_listing("ao")

    cards = listing.get_product_cards()
    assert cards, "Expected listing page to display at least one product card."
    assert any(card.get_name(listing._name_selector()) for card in cards), (
        "Expected at least one product card to have a non-empty name."
    )
    assert any(card.get_price_text(listing._price_selector()) for card in cards), (
        "Expected at least one product card to have a non-empty price."
    )
