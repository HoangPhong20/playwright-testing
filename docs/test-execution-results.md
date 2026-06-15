# Test Execution Results

## Tong quan

Trang thai sau khi bo 5 testcase yeu/trung va sap xep lai ID tu `TC-001` den `TC-021`:

```text
Tong so testcase active: 21
Passed tham chieu: 17
Failed tham chieu: 4
```

Report HTML: `reports/report.html`

Bang ket qua goc do pytest ghi: `reports/test-results.md`

Thu muc screenshot: `reports/screenshots/`

Ket qua ben duoi la ket qua tham chieu tu lan chay truoc, da duoc doi ID va doi ten screenshot cho khop bo 21 testcase active. Nen chay lai full suite de tao report va screenshot moi.

## Ket qua tung testcase

| ID | Testcase | Lam gi | Ket qua thuc te | Status | Screenshot |
| --- | --- | --- | --- | --- | --- |
| TC-001 | Update cart quantity | Them san pham vao gio va kiem tra nut tang/giam so luong. | So luong khong bi thay doi sai khi bam tang/giam. | pass | `reports/screenshots/TC-001_pass_test_cart_quantity_update_20260615_201201.png` |
| TC-002 | Cart persists after reload | Them san pham vao gio, reload trang gio hang/checkout va kiem tra gio hang con noi dung. | Gio hang van con noi dung sau reload. | pass | `reports/screenshots/TC-002_pass_test_cart_persistence_20260615_201222.png` |
| TC-003 | Home page loads successfully | Mo trang chu, kiem tra status khong phai loi server, body khong rong va khong co text loi runtime. | Trang chu load duoc, noi dung khong rong. | pass | `reports/screenshots/TC-003_pass_test_home_page_returns_success_and_non_blank_content_20260615_201244.png` |
| TC-004 | Cart icon links to cart route | Mo trang chu, tim icon/link gio hang va kiem tra href tro toi route gio hang. | Link gio hang ton tai va href hop le. | pass | `reports/screenshots/TC-004_pass_test_cart_icon_points_to_cart_route_20260615_201325.png` |
| TC-005 | Category route renders product links | Mo route category `/ao-doi-tuyen`, kiem tra trang khong loi va co link chi tiet san pham. | Timeout sau 15000ms khi load `/ao-doi-tuyen`; co the do mang/load cham, chua ket luan la bug chuc nang. | fail | `reports/screenshots/TC-005_fail_test_category_route_renders_product_links_without_server_error_20260615_201416.png` |
| TC-006 | Invalid route handles gracefully | Mo route khong ton tai va kiem tra trang khong bi server/runtime error. | Route khong ton tai duoc xu ly an toan, khong co loi server/runtime. | pass | `reports/screenshots/TC-006_pass_test_invalid_route_is_handled_without_server_error_20260615_201429.png` |
| TC-007 | Product detail price is parseable | Mo trang chi tiet san pham va parse gia thanh so duong. | Gia parse duoc va lon hon 0. | pass | `reports/screenshots/TC-007_pass_test_product_detail_price_is_parseable_positive_value_20260615_201506.png` |
| TC-008 | Product detail add-to-cart control exists | Mo trang chi tiet san pham va kiem tra nut them vao gio hang hien thi. | Nut add-to-cart ton tai va visible. | pass | `reports/screenshots/TC-008_pass_test_product_detail_add_to_cart_control_exists_20260615_201521.png` |
| TC-009 | View product detail | Mo chi tiet san pham va kiem tra co anh, mo ta va gia. | Trang chi tiet co du anh, mo ta va gia. | pass | `reports/screenshots/TC-009_pass_test_view_product_detail_20260615_201530.png` |
| TC-010 | Listing prices are parseable | Mo listing search `ao`, lay gia san pham va parse thanh so duong. | Gia listing parse duoc va deu lon hon 0. | pass | `reports/screenshots/TC-010_pass_test_listing_prices_are_parseable_positive_values_20260615_201535.png` |
| TC-011 | Listing product images have valid sources | Mo listing search `ao`, kiem tra anh san pham co `src`/`data-src` va khong broken. | Anh san pham co nguon hop le, khong bi broken. | pass | `reports/screenshots/TC-011_pass_test_listing_product_images_have_valid_sources_20260615_201539.png` |
| TC-012 | Search unaccented keywords are handled | Search cac keyword khong dau `ao`, `giay`, `quan` va kiem tra trang khong crash. | Cac keyword khong dau duoc xu ly, trang khong crash. | pass | `reports/screenshots/TC-012_pass_test_search_unaccented_keywords_are_handled_20260615_201553.png` |
| TC-013 | Search accented keywords are handled | Search cac keyword co dau `ao`, `giay`, `quan` ban co dau va kiem tra trang khong crash. | Cac keyword co dau duoc xu ly, trang khong crash. | pass | `reports/screenshots/TC-013_pass_test_search_accented_keywords_are_handled_20260615_201606.png` |
| TC-014 | Search keywords with surrounding spaces are handled | Search cac keyword co khoang trang dau/cuoi: `  ao  `, `   giay  `, ` quan  `. | Website dieu huong toi URL co `%20` va hien loi runtime/server cho ca 3 du lieu. | fail | `reports/screenshots/TC-014_fail_test_search_keywords_with_surrounding_spaces_are_handled_20260615_201612.png` |
| TC-015 | Listing has clickable product detail links | Mo listing search `ao`, kiem tra link chi tiet san pham co href hop le. | Listing co link chi tiet va href hop le. | pass | `reports/screenshots/TC-015_pass_test_listing_has_clickable_product_detail_links_20260615_201616.png` |
| TC-016 | Search product by keyword | Search keyword `ao`, kiem tra URL search va ket qua san pham lien quan. | URL search va ket qua san pham hop le. | pass | `reports/screenshots/TC-016_pass_test_search_product_by_keyword_20260615_201620.png` |
| TC-017 | Product list displays cards | Mo listing search `ao`, kiem tra co card san pham, ten va gia. | Listing co card san pham voi ten va gia. | pass | `reports/screenshots/TC-017_pass_test_product_list_display_20260615_201644.png` |
| TC-018 | Home search input is visible | Mo trang chu va kiem tra o tim kiem ton tai, visible. | O tim kiem trang chu ton tai va visible. | pass | `reports/screenshots/TC-018_pass_test_home_search_input_is_visible_20260615_201648.png` |
| TC-019 | Mobile home page is not blank | Set viewport mobile 390x844, mo trang chu va kiem tra body khong rong. | Trang chu mobile khong bi rong. | pass | `reports/screenshots/TC-019_pass_test_mobile_viewport_home_page_is_not_blank_20260615_201720.png` |
| TC-020 | Checkout submit without product is handled gracefully | Mo gio hang rong, dien thong tin giao hang hop le, bam `HOAN TAT DON HANG`. | Website khong dat hang thanh cong nhung cung khong hien thong bao validation ro rang khi submit gio hang rong. | fail | `reports/screenshots/TC-020_fail_test_checkout_submit_without_product_is_handled_gracefully_20260615_205540.png` |
| TC-021 | Checkout ward field rejects special characters with product | Them san pham vao gio, dien `@@@###` vao `Phuong/Xa`, bam `HOAN TAT DON HANG`. | Sau submit, field van giu `@@@###`; website khong chan validation ro rang. | fail | `reports/screenshots/TC-021_fail_test_checkout_ward_field_rejects_special_characters_with_product_20260615_205558.png` |

## Tong hop loi can chu y

| ID | Loai | Nhan dinh |
| --- | --- | --- |
| TC-014 | Functional bug | Search keyword co khoang trang dau/cuoi tao URL `%20...%20` va hien loi runtime/server. |
| TC-020 | Functional bug | Submit checkout khi gio hang rong khong hien thong bao validation ro rang, tao cam giac bi treo/khong phan hoi hop le. |
| TC-021 | Functional bug | Form giao hang khong chan gia tri `Phuong/Xa` chi gom ky tu dac biet khi gio hang co san pham. |
| TC-005 | Timeout/loading | Category `/ao-doi-tuyen` timeout, co the do mang/load cham; nen manual confirm. |
