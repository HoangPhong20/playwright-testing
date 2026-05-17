from __future__ import annotations

import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage


@pytest.mark.smoke
def test_view_product_detail(page, base_url):
    home = HomePage(page, timeout=15000)
    listing = ProductListPage(page, timeout=15000)
    detail = ProductDetailPage(page, timeout=15000)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.open_first_product_detail()

    assert detail.is_image_visible(), "Expected product image to be visible."
    assert detail.get_description(), "Expected product description not to be empty."
    assert detail.get_price(), "Expected product price not to be empty."
