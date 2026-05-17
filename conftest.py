from __future__ import annotations

from datetime import datetime
from pathlib import Path
import pytest
from playwright.sync_api import Playwright, sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from config.settings import BASE_URL, BROWSER, HEADLESS, TIMEOUT
from fixtures.data_loader import load_test_data


@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright):
    browser_type = getattr(playwright_instance, BROWSER)
    browser = browser_type.launch(headless=HEADLESS)
    yield browser
    browser.close()


@pytest.fixture()
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture()
def page(context):
    page = context.new_page()
    page.set_default_timeout(TIMEOUT)
    yield page
    page.close()


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def test_data() -> dict:
    return load_test_data()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        reports = Path("reports")
        reports.mkdir(exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{request.node.name}_{ts}.png"
        try:
            page.screenshot(path=str(reports / file_name), full_page=True)
        except PlaywrightTimeoutError:
            pass
