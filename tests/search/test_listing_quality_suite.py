from __future__ import annotations

import pytest

from config.locators import ProductListLocators
from config.settings import TIMEOUT
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage


@pytest.mark.search
@pytest.mark.regression
@pytest.mark.edge
def test_listing_prices_are_parseable_positive_values(page, base_url, test_data):
    keyword = test_data["search"]["primary_keyword"]
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.open_search_listing(keyword)

    prices = listing.get_price_values()
    assert prices, "Expected listing to expose at least one parseable product price."
    assert all(price > 0 for price in prices), (
        f"Expected all parsed prices to be positive values, got: {prices}"
    )


@pytest.mark.search
@pytest.mark.regression
@pytest.mark.edge
def test_listing_product_images_have_valid_sources(page, base_url, test_data):
    keyword = test_data["search"]["primary_keyword"]
    home = HomePage(page, timeout=TIMEOUT)
    listing = ProductListPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    listing.open_search_listing(keyword)

    image_sources = page.evaluate(
        """(cardSelector) => {
            const cards = Array.from(document.querySelectorAll(cardSelector)).slice(0, 10);
            return cards.flatMap((card) => {
                const imgs = Array.from(card.querySelectorAll('img'));
                return imgs.map((img) => ({
                    src: (img.getAttribute('src') || '').trim(),
                    dataSrc: (img.getAttribute('data-src') || '').trim(),
                    naturalWidth: img.naturalWidth,
                    complete: img.complete,
                }));
            });
        }""",
        ProductListLocators.SEARCH_PRODUCT_CARDS,
    )

    assert image_sources, "Expected product listing to contain product images."
    broken_images = [
        image
        for image in image_sources
        if not (image["src"] or image["dataSrc"]) or (image["complete"] and image["naturalWidth"] == 0)
    ]
    assert not broken_images, f"Expected product images not to be broken, got: {broken_images}"
