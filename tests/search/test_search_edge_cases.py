from __future__ import annotations

import pytest

from config.settings import TIMEOUT
from pages.home_page import HomePage


SERVER_ERROR_TEXT = ("server error", "exception", "stack trace", "traceback")


def _body_text(page) -> str:
    return page.locator("body").inner_text(timeout=TIMEOUT).strip()


def _page_error(page, base_url: str) -> str | None:
    body = _body_text(page)
    if not body:
        return f"page body is blank at {page.url}"
    if any(error in body.lower() for error in SERVER_ERROR_TEXT):
        return f"page exposes server/runtime error at {page.url}"
    if not page.url.startswith(base_url.rstrip("/")):
        return f"search left tested website: {page.url}"
    return None


def _assert_keyword_group_is_handled(page, base_url: str, keywords: list[str]) -> None:
    home = HomePage(page, timeout=TIMEOUT)
    failures: list[str] = []

    for keyword in keywords:
        home.open(base_url)
        home.accept_cookie_if_present()
        home.search_product(keyword)

        error = _page_error(page, base_url)
        if error:
            failures.append(f"{keyword!r}: {error}")

    assert not failures, "Expected all keyword variants to be handled:\n" + "\n".join(failures)


@pytest.mark.search
@pytest.mark.edge
def test_search_unaccented_keywords_are_handled(page, base_url):
    _assert_keyword_group_is_handled(page, base_url, ["ao", "giay", "quan"])


@pytest.mark.search
@pytest.mark.edge
def test_search_accented_keywords_are_handled(page, base_url):
    _assert_keyword_group_is_handled(page, base_url, ["áo", "giày", "quần"])


@pytest.mark.search
@pytest.mark.edge
def test_search_keywords_with_surrounding_spaces_are_handled(page, base_url):
    _assert_keyword_group_is_handled(page, base_url, ["  ao  ", "   giay  ", " quan  "])
