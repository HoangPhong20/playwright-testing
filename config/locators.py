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
    CUSTOMER_NAME = (
        ".thongTinGiaoHang input[placeholder*='Họ'], "
        ".thongTinGiaoHang input[placeholder*='Ho'], "
        "form.checkout input[name*='name'], input[name*='Name']"
    )
    CUSTOMER_PHONE = (
        ".thongTinGiaoHang input[placeholder*='Điện thoại'], "
        ".thongTinGiaoHang input[placeholder*='Dien thoai'], "
        "form.checkout input[type='tel'], input[name*='phone'], input[name*='Phone']"
    )
    PROVINCE_SELECT = (
        ".thongTinGiaoHang select:has-text('Tỉnh'), "
        ".thongTinGiaoHang select:has-text('Thành phố'), "
        ".thongTinGiaoHang select:has-text('Tinh')"
    )
    DISTRICT_SELECT = (
        ".thongTinGiaoHang select:has-text('Quận'), "
        ".thongTinGiaoHang select:has-text('Huyện'), "
        ".thongTinGiaoHang select:has-text('Quan')"
    )
    WARD_INPUT = (
        ".thongTinGiaoHang input[placeholder*='Phường'], "
        ".thongTinGiaoHang input[placeholder*='Xã'], "
        ".thongTinGiaoHang input[placeholder*='Phuong'], "
        ".thongTinGiaoHang input[name*='ward'], input[name*='Ward']"
    )
    SHIPPING_ADDRESS = (
        ".thongTinGiaoHang input[placeholder*='Địa chỉ'], "
        ".thongTinGiaoHang input[placeholder*='Dia chi'], "
        "form.checkout input[name*='address'], input[name*='Address']"
    )
    SHIPPING_NOTE = (
        ".thongTinGiaoHang textarea[placeholder*='Ghi chú'], "
        ".thongTinGiaoHang textarea[placeholder*='Ghi chu'], "
        "form.checkout textarea"
    )
    COMPLETE_ORDER = (
        "button:has-text('HOÀN TẤT ĐƠN HÀNG'), "
        "button:has-text('Hoàn tất đơn hàng'), "
        "input[type='submit'][value*='HOÀN TẤT'], "
        "input[type='button'][value*='HOÀN TẤT'], "
        "a:has-text('HOÀN TẤT ĐƠN HÀNG')"
    )
    ORDER_SUCCESS_TEXT = (
        "text=/đặt hàng thành công|dat hang thanh cong|cảm ơn|thank you|order received/i"
    )
    CHECKOUT_VALIDATION_FEEDBACK = (
        "text=/giỏ hàng trống|gio hang trong|chưa có sản phẩm|chua co san pham|"
        "không có sản phẩm|khong co san pham|vui lòng|vui long|bắt buộc|bat buoc|"
        "không hợp lệ|khong hop le|lỗi|loi|error/i"
    )
