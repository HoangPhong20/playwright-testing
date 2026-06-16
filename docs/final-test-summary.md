# Final Test Summary

## Tong ket ket qua

Lan chay gan nhat: 2026-06-17

| Chi so | Gia tri |
| --- | --- |
| Tong testcase | 28 |
| Pass | 20 |
| Fail | 8 |
| Pass rate | 71.4% |
| Fail rate | 28.6% |
| Report ket qua | `reports/test-results.md` |
| Screenshot evidence | `reports/screenshots/` |
| Excel report | `outputs/testcase_report.xlsx` |

## Ket qua theo module

| Module | Total | Pass | Fail | Nhan xet |
| --- | ---: | ---: | ---: | --- |
| Cart/Checkout | 10 | 4 | 6 | Nhieu loi validation form checkout. |
| Navigation | 4 | 4 | 0 | Cac route chinh dang on dinh trong lan chay nay. |
| Product | 3 | 3 | 0 | Detail page, gia va add-to-cart control dat mong doi. |
| Search/Listing | 9 | 7 | 2 | Listing on dinh, chi con loi voi search edge input. |
| UI | 2 | 2 | 0 | Smoke UI dat mong doi. |

## Loi noi bat

- Checkout khong hien validation ro rang voi gio hang rong.
- Cac field checkout nhu phone, ho ten, dia chi, Phuong/Xa chap nhan gia tri invalid ma khong co feedback ro rang.
- Search voi keyword co khoang trang dau/cuoi hoac ky tu dac biet co the hien runtime/server error.

## Ket luan chat luong website

Website dap ung duoc cac luong co ban nhu mo trang chu, xem listing, xem chi tiet san pham, link gio hang va mot so UI smoke. Tuy nhien, cac loi validation checkout va search edge case can duoc uu tien xu ly neu website duoc danh gia theo tieu chi on dinh va trai nghiem nguoi dung.

## Han che cua lan kiem thu

- Test chay truc tiep tren website production.
- Ket qua co the thay doi theo tinh trang server, mang va du lieu san pham.
- Khong co quyen sua source website, chi ghi nhan loi tu goc nhin nguoi dung.
- Chua co kiem thu API, performance, security hoac cross-browser day du.
