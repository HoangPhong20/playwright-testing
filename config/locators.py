from __future__ import annotations


class CommonLocators:
    COOKIE_ACCEPT_BUTTONS = [
        "button:has-text('Đồng ý')",
        "button:has-text('Chấp nhận')",
        "button:has-text('Accept')",
    ]


class HeaderLocators:
    SEARCH_INPUT = "input[type='search'], input[name='s'], input[placeholder*='Tìm']"
    SEARCH_SUBMIT = "button[type='submit'], button:has-text('Tìm')"
    CART_ICON = "a[href*='gio-hang'], a[href*='cart']"
    CART_COUNT = ".cart-contents-count, .count"


class ProductListLocators:
    PRODUCT_CARDS = ".product, .product-item, li.product"
    PRODUCT_NAME = "h2, h3, .product-title, .woocommerce-loop-product__title"
    PRODUCT_PRICE = ".price, .woocommerce-Price-amount, [class*='price']"
    SORT_DROPDOWN = "select.orderby, select[name*='orderby']"
    FILTER_PANEL = ".widget, .filter, [class*='filter']"
    CATEGORY_FILTER = "a[href*='product-category'], input[name*='category']"
    BRAND_FILTER = "a[href*='brand'], input[name*='brand']"
    PRICE_MIN = "input[name*='min_price'], input[min]"
    PRICE_MAX = "input[name*='max_price'], input[max]"
    APPLY_FILTER = "button:has-text('Lọc'), button:has-text('Apply')"
    RESET_FILTER = "a:has-text('Xóa lọc'), button:has-text('Reset')"


class ProductDetailLocators:
    GALLERY_IMAGE = ".woocommerce-product-gallery img, .product-image img"
    DESCRIPTION = ".woocommerce-product-details__short-description, .description, .product-description"
    PRODUCT_PRICE = ".summary .price, .product .price"
    ADD_TO_CART = "button[name='add-to-cart'], button:has-text('Thêm vào giỏ')"


class CartLocators:
    CART_ITEMS = ".cart_item, .woocommerce-cart-form__cart-item"
    REMOVE_ITEM = "a.remove, button:has-text('Xóa')"
    EMPTY_MESSAGE = ".cart-empty, p:has-text('Giỏ hàng trống')"
