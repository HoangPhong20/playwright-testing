from __future__ import annotations

import pytest

from config.settings import TIMEOUT


SERVER_ERROR_TEXT = ("server error", "exception", "stack trace", "traceback")


@pytest.mark.negative
@pytest.mark.edge
def test_invalid_route_is_handled_without_server_error(page, base_url):
    response = page.goto(
        f"{base_url.rstrip('/')}/duong-dan-khong-ton-tai-automation-test",
        wait_until="domcontentloaded",
        timeout=TIMEOUT,
    )

    body = page.locator("body").inner_text(timeout=TIMEOUT).strip()
    status = response.status if response else None

    assert status is None or status < 500, (
        f"Expected invalid route not to return server error, got status: {status}"
    )
    assert body, "Expected invalid route to render a non-blank page."
    assert not any(error in body.lower() for error in SERVER_ERROR_TEXT), (
        "Expected invalid route not to expose server/runtime error details."
    )
