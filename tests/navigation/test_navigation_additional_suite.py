from __future__ import annotations

import pytest

from config.locators import HeaderLocators, ProductListLocators
from config.settings import TIMEOUT
from pages.home_page import HomePage


SERVER_ERROR_TEXT = ("server error", "exception", "stack trace", "traceback")
CATEGORY_ROUTE_TIMEOUT = max(TIMEOUT, 30000)


def _assert_no_server_error_text(body: str) -> None:
    assert not any(error in body.lower() for error in SERVER_ERROR_TEXT), (
        "Expected page content not to expose server/runtime error details."
    )


@pytest.mark.navigation
@pytest.mark.smoke
def test_home_page_returns_success_and_non_blank_content(page, base_url):
    response = page.goto(base_url, wait_until="domcontentloaded", timeout=TIMEOUT)
    body = page.locator("body").inner_text(timeout=TIMEOUT).strip()

    assert response is None or response.status < 500, (
        f"Expected home page not to return server error, got status: {response.status if response else None}"
    )
    assert body, "Expected home page body not to be blank."
    _assert_no_server_error_text(body)


@pytest.mark.navigation
@pytest.mark.regression
def test_cart_icon_points_to_cart_route(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)

    home.open(base_url)
    page.wait_for_load_state("domcontentloaded", timeout=TIMEOUT)
    home.accept_cookie_if_present()

    cart = page.locator(HeaderLocators.CART_ICON).first
    assert cart.count() > 0, "Expected header cart icon/link to exist."

    href = (cart.get_attribute("href") or "").strip()
    assert href, "Expected cart icon/link to have a non-empty href."
    assert "gio-hang" in href or "cart" in href, (
        f"Expected cart link to point to cart route, got href: {href}"
    )


@pytest.mark.navigation
@pytest.mark.search
@pytest.mark.regression
def test_category_route_renders_product_links_without_server_error(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)

    home.open(base_url)
    page.wait_for_load_state("domcontentloaded", timeout=TIMEOUT)
    home.accept_cookie_if_present()
    page.goto(
        f"{base_url.rstrip('/')}/ao-doi-tuyen",
        wait_until="domcontentloaded",
        timeout=CATEGORY_ROUTE_TIMEOUT,
    )

    body = page.locator("body").inner_text(timeout=TIMEOUT).strip()
    assert body, "Expected category page body not to be blank."
    _assert_no_server_error_text(body)
    assert page.locator(ProductListLocators.PRODUCT_DETAIL_LINK).count() > 0, (
        "Expected category route to render at least one product detail link."
    )
