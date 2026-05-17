from __future__ import annotations

from playwright.sync_api import Page
from config.locators import CommonLocators


class BasePage:
    def __init__(self, page: Page, timeout: int):
        self.page = page
        self.timeout = timeout

    def open(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded", timeout=self.timeout)

    def accept_cookie_if_present(self) -> None:
        for locator in CommonLocators.COOKIE_ACCEPT_BUTTONS:
            button = self.page.locator(locator).first
            if button.is_visible():
                button.click()
                break
