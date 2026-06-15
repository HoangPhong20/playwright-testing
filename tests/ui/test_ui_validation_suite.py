from __future__ import annotations

import pytest

from config.locators import HeaderLocators
from config.settings import TIMEOUT
from pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.smoke
def test_home_search_input_is_visible(page, base_url):
    home = HomePage(page, timeout=TIMEOUT)

    home.open(base_url)
    page.wait_for_load_state("domcontentloaded", timeout=TIMEOUT)
    home.accept_cookie_if_present()

    search_input = page.locator(HeaderLocators.SEARCH_INPUT).first
    assert search_input.count() > 0, "Expected search input to exist on home page."
    assert search_input.is_visible(), "Expected search input to be visible on home page."


@pytest.mark.ui
@pytest.mark.edge
def test_mobile_viewport_home_page_is_not_blank(page, base_url):
    page.set_viewport_size({"width": 390, "height": 844})
    home = HomePage(page, timeout=TIMEOUT)

    home.open(base_url)
    page.wait_for_load_state("domcontentloaded", timeout=TIMEOUT)
    home.accept_cookie_if_present()

    body = page.locator("body").inner_text(timeout=TIMEOUT).strip()
    assert body, "Expected mobile viewport home page body not to be blank."
