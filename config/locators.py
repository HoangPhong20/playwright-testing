from __future__ import annotations


class CommonLocators:
    COOKIE_ACCEPT_BUTTONS = [
        "button:has-text('Đồng ý')",
        "button:has-text('Chấp nhận')",
        "button:has-text('Accept')",
    ]


class HeaderLocators:
    SEARCH_INPUT = "#tbSearchOnHeader, input[type='search'], input[name='s'], input[placeholder*='Tìm'], input[placeholder*='tim']"
    SEARCH_SUBMIT = "button[type='submit'], input[type='submit'], button:has-text('Tìm')"
    CART_ICON = "a[href*='gio-hang'], a[href*='cart']"
    CART_COUNT = ".cart-contents-count, .count"


class ProductListLocators:
    # Home template
    HOME_PRODUCT_CARDS = ".productHome .itemBox"
    HOME_PRODUCT_NAME = ".itemTitle"
    HOME_PRODUCT_PRICE = ".listPrice .subItem span, .listPrice span"

    # Search/listing template
    SEARCH_PRODUCT_CARDS = ".list_sp .item"
    SEARCH_PRODUCT_NAME = ".itemTitle"
    SEARCH_PRODUCT_PRICE = ".listPrice .subItem span, .listPrice span"

    # Fallback template
    PRODUCT_CARDS = ".list_sp .item, .productHome .itemBox"
    PRODUCT_NAME = ".itemTitle, h2, h3, .product-title"
    PRODUCT_PRICE = ".listPrice .subItem span, .listPrice span, .price"
    SORT_DROPDOWN = "select.orderby, select[name*='orderby']"
    FILTER_PANEL = ".widget, .filter, [class*='filter']"
    CATEGORY_FILTER = "a[href*='product-category'], input[name*='category']"
    BRAND_FILTER = "a[href*='brand'], input[name*='brand']"
    PRICE_MIN = "input[name*='min_price'], input[min]"
    PRICE_MAX = "input[name*='max_price'], input[max]"
    APPLY_FILTER = "button:has-text('Lọc'), button:has-text('Apply')"
    RESET_FILTER = "a:has-text('Xóa lọc'), button:has-text('Reset')"


class ProductDetailLocators:
    GALLERY_IMAGE = ".detailProduct img, .itemDetail img, .slideProduct img, .imgDetail img"
    DESCRIPTION = ".contentDetail, .description, .itemTitle"
    PRODUCT_PRICE = ".listPrice .subItem span, .listPrice span"
    ADD_TO_CART = "button:has-text('MUA NGAY'), button:has-text('Thêm vào giỏ'), button[name='add-to-cart']"


class CartLocators:
    CART_ITEMS = ".cart_item, .woocommerce-cart-form__cart-item, .itemCart, .listCart .item"
    REMOVE_ITEM = "a.remove, button:has-text('Xóa'), a:has-text('Xóa')"
    EMPTY_MESSAGE = ".cart-empty, p:has-text('Giỏ hàng trống'), text=/trong|empty/i"
