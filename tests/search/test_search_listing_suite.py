from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from config.settings import TIMEOUT
from config.locators import ProductListLocators


@pytest.mark.search
def test_listing_has_clickable_product_detail_links(page, base_url, test_data):
    keyword = test_data["search"]["primary_keyword"]
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.open_search_listing(keyword)

    links = page.locator(ProductListLocators.PRODUCT_DETAIL_LINK)
    assert links.count() > 0, "Expected search listing to contain product detail links."
    href = (links.first.get_attribute("href") or "").strip()
    assert href, "Expected first product detail link to have href."
    assert href.startswith("http") or href.startswith("/"), (
        f"Expected href to be absolute/relative URL, got: {href}"
    )
