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
    SORT_DROPDOWN = (
        "select.orderby, select[name*='orderby'], select[name*='sort'], "
        ".sort select, .sapxep select, .order select"
    )
    FILTER_PANEL = (
        ".widget, .filter, [class*='filter'], .cateLeft, .cateContent, "
        ".box.cate, .menuMain .subMenuTop"
    )
    CATEGORY_FILTER = (
        "a[href*='product-category'], input[name*='category'], "
        ".cateContent a, .subMenuTop a"
    )
    BRAND_FILTER = "a[href*='brand'], input[name*='brand']"
    PRICE_MIN = "input[name*='min_price'], input[min]"
    PRICE_MAX = "input[name*='max_price'], input[max]"
    APPLY_FILTER = "button:has-text('Lọc'), button:has-text('Apply')"
    RESET_FILTER = "a:has-text('Xóa lọc'), button:has-text('Reset')"
    PRODUCT_DETAIL_LINK = ".itemTitle a, a.viewDetail, .itemDetail .itemTitle a"


class ProductDetailLocators:
    GALLERY_IMAGE = (
        ".productPicture img, .contentPicture img, .khungAnh img, "
        ".detailProduct img, .itemDetail img, .slideProduct img, .imgDetail img"
    )
    DESCRIPTION = ".contentDetail, .description, .itemTitle"
    PRODUCT_PRICE = ".listPrice .subItem span, .listPrice span"
    ADD_TO_CART = (
        "a[onclick*='GoToCart1'], a:has-text('Mua ngay'), "
        "button:has-text('MUA NGAY'), button:has-text('Thêm vào giỏ'), button[name='add-to-cart']"
    )


class CartLocators:
    CART_ITEMS = (
        "#TableCart .item, #TableCart .itemBox, #TableCart .itemCart, "
        "#TableCart .cart_item, .cart_item, .woocommerce-cart-form__cart-item, .itemCart, .listCart .item"
    )
    CART_TABLE = "#TableCart"
    CART_TOTAL_MONEY = "#cartTotalMoney"
    REMOVE_ITEM = "a.remove, button:has-text('Xóa'), a:has-text('Xóa')"
    EMPTY_MESSAGE = ".cart-empty, p:has-text('Giỏ hàng trống'), text=/trong|empty/i"
    CHECKOUT_FORM = ".thongTinGiaoHang, form.checkout, .woocommerce-checkout"
    QUANTITY_INPUT = "input.qty, .sl input[type='text'], .sl input[type='number']"
    INCREASE_BUTTON = ".sl .plus, .quantity .plus, button:has-text('+')"
    DECREASE_BUTTON = ".sl .minus, .quantity .minus, button:has-text('-')"
    CONTINUE_SHOPPING = (
        "a.tiepTucMua, a:has-text('Tiếp tục mua hàng'), "
        "a:has-text('Ti?p t?c mua hàng')"
    )
