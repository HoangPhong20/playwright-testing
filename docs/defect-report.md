# Defect Report

## Tong quan defect

Lan cap nhat gan nhat co 8 testcase fail. Cac loi duoc nhom thanh 2 khu vuc chinh:

- Cart/Checkout validation.
- Search input handling.

## Danh sach defect

| Defect ID | Testcase | Module | Severity | Expected result | Actual result | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| BUG-001 | TC-003 | Cart/Checkout | Medium | Submit gio hang rong phai hien validation/feedback ro rang va khong tao don. | He thong khong tao don nhung khong hien feedback ro rang. | reports/screenshots/TC-003_fail_test_checkout_submit_without_product_is_handled_gracefully_20260617_015042.png |
| BUG-002 | TC-004 | Cart/Checkout | Medium | Field Phuong/Xa khong chap nhan gia tri chi gom ky tu dac biet. | Field van giu `@@@###` va khong hien validation feedback. | reports/screenshots/TC-004_fail_test_checkout_ward_field_rejects_special_characters_with_product_20260617_015056.png |
| BUG-003 | TC-005 | Cart/Checkout | High | Field so dien thoai khong chap nhan chu cai. | Field van giu `abcxyz` va khong hien validation feedback. | reports/screenshots/TC-005_fail_test_checkout_phone_field_rejects_lowercase_letters_with_product_20260617_015110.png |
| BUG-004 | TC-007 | Cart/Checkout | Medium | Field ho ten khong chap nhan gia tri chi gom ky tu dac biet. | Field van giu `@@@###` va khong hien validation feedback. | reports/screenshots/TC-007_fail_test_checkout_name_field_rejects_special_characters_with_product_20260617_015139.png |
| BUG-005 | TC-008 | Cart/Checkout | Medium | Field ho ten khong chap nhan gia tri chi gom chu so. | Field van giu `123456` va khong hien validation feedback. | reports/screenshots/TC-008_fail_test_checkout_name_field_rejects_digits_with_product_20260617_015150.png |
| BUG-006 | TC-010 | Cart/Checkout | Medium | Field dia chi khong chap nhan gia tri chi gom ky tu dac biet. | Field van giu `@@@###` va khong hien validation feedback. | reports/screenshots/TC-010_fail_test_checkout_address_field_rejects_special_characters_with_product_20260617_015218.png |
| BUG-007 | TC-022 | Search | High | Keyword co khoang trang dau/cuoi duoc xu ly an toan. | Keyword `  ao  ` hien runtime/server error. | reports/screenshots/TC-022_fail_test_search_keywords_with_surrounding_spaces_are_handled_20260617_043330.png |
| BUG-008 | TC-023 | Search | High | Keyword ky tu dac biet duoc xu ly an toan. | Keyword `@#$%^&*` hien server/runtime error. | reports/screenshots/TC-023_fail_test_search_special_character_keywords_are_handled_20260617_043418.png |

## Nhan xet defect

- Cac loi checkout chu yeu nam o validation input. He thong khong tao don thanh cong trong cac case invalid, nhung field van giu gia tri sai va khong co feedback ro rang.
- Cac loi search con lai cho thay website xu ly chua tot keyword co khoang trang dau/cuoi va ky tu dac biet, dan den runtime/server error.
- Defect severity duoc de xuat theo tac dong toi nguoi dung va muc do nghiem trong cua du lieu dau vao.
