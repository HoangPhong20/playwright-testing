from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
import pytest
from playwright.sync_api import Playwright, sync_playwright
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from config.settings import BASE_URL, BROWSER, HEADLESS, TIMEOUT
from fixtures.data_loader import load_test_data
from utils.test_case_registry import TEST_CASE_BY_KEY, test_case_key


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


def pytest_sessionstart(session):
    if session.config.option.collectonly:
        return
    reports = Path("reports")
    reports.mkdir(parents=True, exist_ok=True)
    result_file = reports / "test-results.md"
    result_file.write_text(
        "# Test Run Results\n\n"
        "| ID | Testcase | Status | Screenshot | Failure Reason |\n"
        "| --- | --- | --- | --- | --- |\n",
        encoding="utf-8",
    )


def pytest_collection_modifyitems(config, items):
    missing_cases = []
    for item in items:
        case = TEST_CASE_BY_KEY.get(_item_test_case_key(item))
        if not case:
            missing_cases.append(item.nodeid)
            continue
        item.test_case_id = case["id"]
        item.test_case_title = case["title"]
    if missing_cases:
        missing = "\n".join(f"- {nodeid}" for nodeid in missing_cases)
        raise pytest.UsageError(
            "Missing testcase registry entries in utils/test_case_registry.py:\n"
            f"{missing}"
        )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


def _safe_file_name(value: str, max_length: int = 120) -> str:
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")
    return safe_name[:max_length] or "testcase"


def _report_status(report) -> str:
    if report and report.outcome == "passed":
        return "pass"
    return "fail"


def _item_test_case_key(item) -> tuple:
    path = Path(str(item.path)).as_posix()
    try:
        path = Path(str(item.path)).relative_to(Path.cwd()).as_posix()
    except ValueError:
        pass
    function = getattr(item, "originalname", None) or item.name.split("[", 1)[0]
    params = getattr(getattr(item, "callspec", None), "params", None)
    return test_case_key(path, function, params)


def _markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", "<br>")


def _failure_reason(report) -> str:
    if not report or report.outcome == "passed":
        return ""
    longrepr = getattr(report, "longreprtext", None) or str(getattr(report, "longrepr", ""))
    return longrepr.strip().splitlines()[-1] if longrepr.strip() else report.outcome


def _append_test_result(
    case_id: str,
    title: str,
    status: str,
    screenshot: Path | None,
    failure_reason: str,
) -> None:
    screenshot_link = ""
    if screenshot:
        screenshot_link = screenshot.as_posix()
    line = (
        f"| {case_id} | {_markdown_cell(title)} | {status} | "
        f"{screenshot_link} | {_markdown_cell(failure_reason)} |\n"
    )
    with (Path("reports") / "test-results.md").open("a", encoding="utf-8") as report:
        report.write(line)


def _write_test_log_to_terminal(config, case_id: str, title: str, status: str) -> None:
    terminal = config.pluginmanager.get_plugin("terminalreporter")
    if terminal:
        display_status = "passed" if status == "pass" else "failed"
        terminal.write_line(f"Testcase: {case_id} - {title} | Status: {display_status}")


def _capture_test_screenshot(page, screenshot_path: Path) -> bool:
    screenshot_options = [
        {"full_page": True, "animations": "disabled", "timeout": min(TIMEOUT, 30000)},
        {"full_page": False, "animations": "disabled", "timeout": min(TIMEOUT, 30000)},
    ]
    for _ in range(3):
        try:
            page.wait_for_load_state("domcontentloaded", timeout=5000)
        except PlaywrightError:
            pass
        try:
            page.locator("body").wait_for(state="attached", timeout=5000)
        except PlaywrightError:
            pass
        for options in screenshot_options:
            try:
                page.screenshot(path=str(screenshot_path), **options)
                return True
            except PlaywrightError:
                continue
        try:
            page.wait_for_timeout(1000)
        except PlaywrightError:
            break
    return False


def _settle_page_before_screenshot(page) -> None:
    try:
        page.wait_for_load_state("domcontentloaded", timeout=5000)
    except PlaywrightError:
        pass
    try:
        page.wait_for_timeout(500)
    except PlaywrightError:
        pass


@pytest.fixture(autouse=True)
def screenshot_after_test(request, page):
    yield
    rep_call = getattr(request.node, "rep_call", None)
    screenshots = Path("reports") / "screenshots"
    screenshots.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = _safe_file_name(request.node.name)
    status = _report_status(rep_call)
    failure_reason = _failure_reason(rep_call)
    case_id = getattr(request.node, "test_case_id", "TC-000")
    title = getattr(request.node, "test_case_title", request.node.name)
    file_name = f"{case_id}_{status}_{safe_test_name}_{ts}.png"
    screenshot_path = screenshots / file_name
    _settle_page_before_screenshot(page)
    if not _capture_test_screenshot(page, screenshot_path):
        screenshot_path = None
    _append_test_result(case_id, title, status, screenshot_path, failure_reason)
    _write_test_log_to_terminal(request.config, case_id, title, status)
