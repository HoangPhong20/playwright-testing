from __future__ import annotations

from playwright.sync_api import Page
from config.locators import CartLocators, ProductDetailLocators
from config.locators import ProductListLocators


def wait_for_products_loaded(page: Page, timeout: int) -> None:
    page.locator(ProductListLocators.PRODUCT_CARDS).first.wait_for(
        state="visible",
        timeout=timeout,
    )


def wait_for_product_detail_loaded(page: Page, timeout: int) -> None:
    page.wait_for_function(
        """(selectors) => {
            const isVisible = (element) => {
                if (!element) return false;
                const style = window.getComputedStyle(element);
                const rect = element.getBoundingClientRect();
                return style.visibility !== 'hidden'
                    && style.display !== 'none'
                    && rect.width > 0
                    && rect.height > 0;
            };

            return selectors.some((selector) =>
                Array.from(document.querySelectorAll(selector)).some(isVisible)
            );
        }""",
        arg=[
            ProductDetailLocators.GALLERY_IMAGE,
            ProductDetailLocators.DESCRIPTION,
            ProductDetailLocators.PRODUCT_PRICE,
        ],
        timeout=timeout,
    )


def wait_for_checkout_ready(page: Page, timeout: int) -> None:
    page.wait_for_function(
        """(selectors) => {
            const text = (document.body?.innerText || '').toLowerCase();
            const url = window.location.href.toLowerCase();
            const ready = document.readyState !== 'loading';
            if (!ready) return false;
            if ((url.includes('gio-hang') || url.includes('checkout')) && text.trim()) return true;
            if (text.includes('gio hang') || text.includes('giỏ hàng')) return true;

            return selectors.some((selector) => {
                const element = document.querySelector(selector);
                if (!element) return false;
                const style = window.getComputedStyle(element);
                const rect = element.getBoundingClientRect();
                return style.visibility !== 'hidden'
                    && style.display !== 'none'
                    && rect.width > 0
                    && rect.height > 0;
            });
        }""",
        arg=[
            CartLocators.CART_TABLE,
            CartLocators.CART_ITEMS,
            CartLocators.CART_TOTAL_MONEY,
            CartLocators.CHECKOUT_FORM,
        ],
        timeout=timeout,
    )


def wait_for_cart_rendered(page: Page, timeout: int) -> None:
    page.wait_for_function(
        """(selectors) => {
            const bodyText = (document.body?.innerText || '').toLowerCase();
            const emptyPattern = /giỏ hàng trống|gio hang trong|cart empty|empty cart/;
            if (emptyPattern.test(bodyText)) {
                return true;
            }

            const hasVisibleElement = (selector) => {
                return Array.from(document.querySelectorAll(selector)).some((element) => {
                    const style = window.getComputedStyle(element);
                    const rect = element.getBoundingClientRect();
                    return style.visibility !== 'hidden'
                        && style.display !== 'none'
                        && rect.width > 0
                        && rect.height > 0;
                });
            };

            const total = document.querySelector(selectors.totalSelector);
            const totalText = (total?.innerText || total?.textContent || '').replace(/\\D/g, '');
            const totalValue = Number(totalText || '0');
            if (totalValue > 0) return true;
            if (hasVisibleElement(selectors.itemSelector)) return true;
            const table = document.querySelector(selectors.tableSelector);
            if (!table) return false;
            return Array.from(table.querySelectorAll('td, th, div, span')).some((element) => {
                const text = (element.innerText || element.textContent || '').trim();
                if (!text) return false;
                const style = window.getComputedStyle(element);
                const rect = element.getBoundingClientRect();
                return style.visibility !== 'hidden'
                    && style.display !== 'none'
                    && rect.width > 0
                    && rect.height > 0
                    && /\\d/.test(text);
            });
        }""",
        arg={
            "tableSelector": CartLocators.CART_TABLE,
            "itemSelector": CartLocators.CART_ITEMS,
            "totalSelector": CartLocators.CART_TOTAL_MONEY,
        },
        timeout=timeout,
    )


def wait_for_quantity_value(page: Page, previous_value: str, timeout: int) -> None:
    page.wait_for_function(
        """(args) => {
            const input = document.querySelector(args.selector);
            if (!input) return true;
            const value = (input.value || input.getAttribute('value') || '').trim();
            return value !== args.previousValue;
        }""",
        arg={
            "selector": CartLocators.QUANTITY_INPUT,
            "previousValue": previous_value,
        },
        timeout=min(timeout, 3000),
    )


def wait_for_cart_item_removed(page: Page, previous_count: int, timeout: int) -> None:
    page.wait_for_function(
        """(args) => {
            const currentCount = document.querySelectorAll(args.itemSelector).length;
            const bodyText = (document.body?.innerText || '').toLowerCase();
            const emptyPattern = /giỏ hàng trống|gio hang trong|cart empty|empty cart/;
            return currentCount < args.previousCount
                || emptyPattern.test(bodyText);
        }""",
        arg={
            "itemSelector": CartLocators.CART_ITEMS,
            "previousCount": previous_count,
        },
        timeout=timeout,
    )
