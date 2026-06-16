# Test Execution Results

## Tong quan

Lan chay gan nhat: 2026-06-17

```text
Tong so testcase: 28
Passed: 20
Failed: 8
Status su dung: pass/fail
```

Ket qua goc do pytest ghi:

```text
reports/test-results.md
```

Anh minh chung sau moi testcase:

```text
reports/screenshots/
```

File Excel tong hop:

```text
outputs/testcase_report.xlsx
```

## Ket qua tung testcase

| ID | Module | Testcase | Ket qua mong doi | Ket qua thuc te | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| TC-001 | Cart | Update cart quantity | So luong tang/giam dung khi thao tac tren input quantity. | Quantity update dung bang ArrowUp/ArrowDown. | pass | reports/screenshots/TC-001_pass_test_cart_quantity_update_20260617_015017.png |
| TC-002 | Cart | Cart persists after reload | Gio hang van con san pham sau khi reload. | Gio hang van con noi dung sau reload. | pass | reports/screenshots/TC-002_pass_test_cart_persistence_20260617_015037.png |
| TC-003 | Cart | Checkout submit without product is handled gracefully | Submit gio hang rong khong tao don va hien validation ro rang. | Khong tao don, nhung khong hien feedback/validation ro rang. | fail | reports/screenshots/TC-003_fail_test_checkout_submit_without_product_is_handled_gracefully_20260617_015042.png |
| TC-004 | Cart | Checkout ward field rejects special characters with product | Phuong/Xa khong chap nhan gia tri chi gom ky tu dac biet. | Field van giu `@@@###`, khong co validation feedback. | fail | reports/screenshots/TC-004_fail_test_checkout_ward_field_rejects_special_characters_with_product_20260617_015056.png |
| TC-005 | Cart | Checkout phone field rejects lowercase letters with product | So dien thoai khong chap nhan chu cai. | Field van giu `abcxyz`, khong co validation feedback. | fail | reports/screenshots/TC-005_fail_test_checkout_phone_field_rejects_lowercase_letters_with_product_20260617_015110.png |
| TC-006 | Cart | Checkout name field accepts lowercase letters with product | Ho ten chap nhan chu thuong hop le. | Field ho ten giu gia tri chu thuong, checkout bi chan boi phone invalid. | pass | reports/screenshots/TC-006_pass_test_checkout_name_field_accepts_lowercase_letters_with_product_20260617_015124.png |
| TC-007 | Cart | Checkout name field rejects special characters with product | Ho ten khong chap nhan gia tri chi gom ky tu dac biet. | Field van giu `@@@###`, khong co validation feedback. | fail | reports/screenshots/TC-007_fail_test_checkout_name_field_rejects_special_characters_with_product_20260617_015139.png |
| TC-008 | Cart | Checkout name field rejects digits with product | Ho ten khong chap nhan gia tri chi gom chu so. | Field van giu `123456`, khong co validation feedback. | fail | reports/screenshots/TC-008_fail_test_checkout_name_field_rejects_digits_with_product_20260617_015150.png |
| TC-009 | Cart | Checkout address field rejects blank value with product | Dia chi chi gom khoang trang bi chan. | Checkout khong hoan tat voi dia chi blank. | pass | reports/screenshots/TC-009_pass_test_checkout_address_field_rejects_blank_value_with_product_20260617_015205.png |
| TC-010 | Cart | Checkout address field rejects special characters with product | Dia chi khong chap nhan gia tri chi gom ky tu dac biet. | Field van giu `@@@###`, khong co validation feedback. | fail | reports/screenshots/TC-010_fail_test_checkout_address_field_rejects_special_characters_with_product_20260617_015218.png |
| TC-011 | Navigation | Home page loads successfully | Trang chu load duoc, body khong rong va khong co server error. | Trang chu load thanh cong. | pass | reports/screenshots/TC-011_pass_test_home_page_returns_success_and_non_blank_content_20260617_015221.png |
| TC-012 | Navigation | Cart icon links to cart route | Icon gio hang ton tai va link dung route gio hang/cart. | Link gio hang hop le. | pass | reports/screenshots/TC-012_pass_test_cart_icon_points_to_cart_route_20260617_015245.png |
| TC-013 | Navigation | Category route renders product links | Category route co noi dung va link chi tiet san pham. | Category route render product links. | pass | reports/screenshots/TC-013_pass_test_category_route_renders_product_links_without_server_error_20260617_015326.png |
| TC-014 | Navigation | Invalid route handles gracefully | Route khong ton tai khong lo server/runtime error. | Invalid route duoc xu ly an toan. | pass | reports/screenshots/TC-014_pass_test_invalid_route_is_handled_without_server_error_20260617_015331.png |
| TC-015 | Product | Product detail price is parseable | Gia detail parse duoc thanh so duong. | Gia parse duoc. | pass | reports/screenshots/TC-015_pass_test_product_detail_price_is_parseable_positive_value_20260617_015357.png |
| TC-016 | Product | Product detail add-to-cart control exists | Trang detail co control them vao gio hang. | Control add-to-cart visible. | pass | reports/screenshots/TC-016_pass_test_product_detail_add_to_cart_control_exists_20260617_015405.png |
| TC-017 | Product | View product detail | Detail co anh, mo ta va gia. | Trang detail hien du thong tin can kiem tra. | pass | reports/screenshots/TC-017_pass_test_view_product_detail_20260617_015414.png |
| TC-018 | Search | Listing prices are parseable | Gia listing parse duoc va lon hon 0. | Gia listing hop le. | pass | reports/screenshots/TC-018_pass_test_listing_prices_are_parseable_positive_values_20260617_015419.png |
| TC-019 | Search | Listing product images have valid sources | Anh san pham co src/data-src va khong broken. | Anh listing hop le. | pass | reports/screenshots/TC-019_pass_test_listing_product_images_have_valid_sources_20260617_015423.png |
| TC-020 | Search | Search unaccented keywords are handled | Keyword khong dau khong lam trang blank/runtime error. | Cac keyword khong dau duoc xu ly an toan trong lan kiem tra moi. | pass | reports/screenshots/TC-020_pass_test_search_unaccented_keywords_are_handled_20260617_043242.png |
| TC-021 | Search | Search accented keywords are handled | Keyword co dau khong lam trang blank/runtime error. | Cac keyword co dau duoc xu ly an toan trong lan kiem tra moi. | pass | reports/screenshots/TC-021_pass_test_search_accented_keywords_are_handled_20260617_043311.png |
| TC-022 | Search | Search keywords with surrounding spaces are handled | Keyword co khoang trang dau/cuoi duoc xu ly an toan. | Keyword `  ao  ` hien runtime/server error. | fail | reports/screenshots/TC-022_fail_test_search_keywords_with_surrounding_spaces_are_handled_20260617_043330.png |
| TC-023 | Search | Search special-character keywords are handled | Keyword ky tu dac biet duoc xu ly an toan. | Keyword `@#$%^&*` hien runtime/server error. | fail | reports/screenshots/TC-023_fail_test_search_special_character_keywords_are_handled_20260617_043418.png |
| TC-024 | Search | Listing has clickable product detail links | Listing co link chi tiet san pham va href hop le. | Link chi tiet hop le. | pass | reports/screenshots/TC-024_pass_test_listing_has_clickable_product_detail_links_20260617_043450.png |
| TC-025 | Search | Search product by keyword | Search keyword chinh dung URL va co ket qua lien quan. | Search keyword `ao` hop le. | pass | reports/screenshots/TC-025_pass_test_search_product_by_keyword_20260617_043509.png |
| TC-026 | Search | Product list displays cards | Listing co card san pham, ten va gia. | Product cards hien dung. | pass | reports/screenshots/TC-026_pass_test_product_list_display_20260617_043513.png |
| TC-027 | UI | Home search input is visible | O tim kiem tren home visible. | Search input visible. | pass | reports/screenshots/TC-027_pass_test_home_search_input_is_visible_20260617_043516.png |
| TC-028 | UI | Mobile viewport home page is not blank | Trang chu mobile khong blank. | Mobile home co noi dung. | pass | reports/screenshots/TC-028_pass_test_mobile_viewport_home_page_is_not_blank_20260617_043531.png |

## Nhan xet ket qua

- Cac luong Navigation, Product, Listing va UI smoke dang on dinh trong lan chay nay.
- Nhom Cart/Checkout co nhieu loi validation form.
- Nhom Search con loi voi keyword co khoang trang dau/cuoi va ky tu dac biet.
- Vi test chay tren website that, ket qua co the bi anh huong boi toc do server, mang va du lieu san pham thay doi.
