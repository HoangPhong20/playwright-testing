# Test Cases

## Danh sach testcase

| ID | Module | Testcase | Kich ban / muc tieu | Expected result |
| --- | --- | --- | --- | --- |
| TC-001 | Cart | Update cart quantity | Them san pham vao gio hang, tang va giam quantity. | Quantity tang/giam dung khi thao tac tren input quantity. |
| TC-002 | Cart | Cart persists after reload | Them san pham vao gio hang va reload trang. | Gio hang van con san pham sau reload. |
| TC-003 | Cart | Checkout submit without product is handled gracefully | Mo gio hang rong, dien shipping hop le, submit checkout. | Khong tao don va hien validation/feedback ro rang. |
| TC-004 | Cart | Checkout ward field rejects special characters with product | Co san pham, nhap `@@@###` vao Phuong/Xa va submit. | Field bi sanitize hoac hien validation feedback. |
| TC-005 | Cart | Checkout phone field rejects lowercase letters with product | Co san pham, nhap `abcxyz` vao phone va submit. | Phone khong chap nhan chu cai hoac hien validation feedback. |
| TC-006 | Cart | Checkout name field accepts lowercase letters with product | Nhap ho ten chu thuong va dung invalid phone lam guard. | Ho ten chu thuong duoc giu lai, checkout khong thanh cong do phone invalid. |
| TC-007 | Cart | Checkout name field rejects special characters with product | Co san pham, nhap `@@@###` vao ho ten va submit. | Ho ten invalid bi sanitize hoac hien validation feedback. |
| TC-008 | Cart | Checkout name field rejects digits with product | Co san pham, nhap `123456` vao ho ten va submit. | Ho ten invalid bi sanitize hoac hien validation feedback. |
| TC-009 | Cart | Checkout address field rejects blank value with product | Co san pham, nhap dia chi chi gom khoang trang va submit. | Dia chi blank bi chan, checkout khong hoan tat. |
| TC-010 | Cart | Checkout address field rejects special characters with product | Co san pham, nhap `@@@###` vao dia chi va submit. | Dia chi invalid bi sanitize hoac hien validation feedback. |
| TC-011 | Navigation | Home page loads successfully | Mo trang chu. | Trang khong blank, khong tra server error. |
| TC-012 | Navigation | Cart icon links to cart route | Mo trang chu, kiem tra icon/link gio hang. | Link gio hang ton tai va tro den route cart/gio-hang. |
| TC-013 | Navigation | Category route renders product links | Mo route `/ao-doi-tuyen`. | Trang category co noi dung va link chi tiet san pham. |
| TC-014 | Navigation | Invalid route handles gracefully | Mo route khong ton tai. | Khong lo server/runtime error. |
| TC-015 | Product | Product detail price is parseable | Mo chi tiet san pham va doc gia. | Gia parse duoc thanh so duong. |
| TC-016 | Product | Product detail add-to-cart control exists | Mo chi tiet san pham. | Control add-to-cart visible. |
| TC-017 | Product | View product detail | Mo chi tiet san pham. | Co anh, mo ta va gia. |
| TC-018 | Search | Listing prices are parseable | Mo listing search `ao`, parse gia san pham. | Gia listing parse duoc va > 0. |
| TC-019 | Search | Listing product images have valid sources | Mo listing search `ao`, kiem tra anh. | Anh co `src`/`data-src` hop le va khong broken. |
| TC-020 | Search | Search unaccented keywords are handled | Search `ao`, `giay`, `quan`. | Khong blank, khong server/runtime error. |
| TC-021 | Search | Search accented keywords are handled | Search keyword co dau. | Khong blank, khong server/runtime error. |
| TC-022 | Search | Search keywords with surrounding spaces are handled | Search keyword co khoang trang dau/cuoi. | Keyword duoc xu ly an toan, khong loi/blank. |
| TC-023 | Search | Search special-character keywords are handled | Search `@#$%^&*`. | Khong lo server/runtime error. |
| TC-024 | Search | Listing has clickable product detail links | Mo listing va kiem tra link detail. | Co href hop le. |
| TC-025 | Search | Search product by keyword | Search keyword chinh `ao`. | URL search dung va co ket qua lien quan. |
| TC-026 | Search | Product list displays cards | Mo listing search. | Co card san pham, ten va gia. |
| TC-027 | UI | Home search input is visible | Mo trang chu. | Search input visible. |
| TC-028 | UI | Mobile viewport home page is not blank | Set viewport mobile va mo trang chu. | Body khong blank. |

## Ghi chu

- Test data duoc luu trong `data/test_data.json`.
- ID testcase duoc sinh tu `utils/test_case_registry.py`.
- Ket qua thuc te nam trong `docs/test-execution-results.md` va `reports/test-results.md`.
