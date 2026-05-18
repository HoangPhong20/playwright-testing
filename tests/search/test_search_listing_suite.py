from __future__ import annotations

import pytest
from pages.home_page import HomePage
from config.settings import TIMEOUT
from config.locators import ProductListLocators


@pytest.mark.search
def test_navigate_to_category_listing(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    page.goto("https://aobongda.net/ao-doi-tuyen", wait_until="domcontentloaded", timeout=TIMEOUT)

    assert "/ao-doi-tuyen" in page.url, (
        f"Expected category URL '/ao-doi-tuyen', got: {page.url}"
    )
    assert page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0, (
        "Expected category listing page to have at least one product detail link."
    )


@pytest.mark.search
def test_listing_has_clickable_product_detail_links(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    page.goto("https://aobongda.net/tim-kiem/ao", wait_until="domcontentloaded", timeout=TIMEOUT)

    links = page.locator(ProductListLocators.PRODUCT_DETAIL_LINK)
    assert links.count() > 0, "Expected search listing to contain product detail links."
    href = (links.first.get_attribute("href") or "").strip()
    assert href, "Expected first product detail link to have href."
    assert href.startswith("http") or href.startswith("/"), (
        f"Expected href to be absolute/relative URL, got: {href}"
    )
