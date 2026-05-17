from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage
from config.settings import TIMEOUT


@pytest.mark.smoke
def test_view_product_detail(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)
    detail = ProductDetailPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    if page.locator(".itemTitle a").count() == 0:
        page.goto("https://aobongda.net/tim-kiem/ao", wait_until="commit", timeout=TIMEOUT)
    if page.locator(".itemTitle a").count() == 0:
        page.goto("https://aobongda.net/tim-kiem/giay", wait_until="commit", timeout=TIMEOUT)
    if page.locator(".itemTitle a").count() == 0:
        pytest.skip("No product detail link available on current page data.")
    listing.open_first_product_detail()

    assert detail.is_image_visible(), "Expected product image to be visible."
    assert detail.get_description(), "Expected product description not to be empty."
    assert detail.get_price(), "Expected product price not to be empty."
