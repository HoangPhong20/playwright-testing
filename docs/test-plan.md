# Test Plan - aobongda.net

## 1. Muc tieu

Kiem thu tu dong giao dien website `https://aobongda.net` de xac minh cac luong nguoi dung chinh:

- Tim kiem san pham.
- Xem danh sach san pham.
- Xem chi tiet san pham.
- Them san pham vao gio hang.
- Kiem tra gio hang va form checkout.
- Kiem tra navigation va UI smoke tren desktop/mobile.

## 2. Pham vi kiem thu

In scope:

- Home page.
- Search va listing.
- Product detail.
- Cart va checkout validation.
- Navigation route.
- UI smoke va mobile smoke.

Out of scope:

- Kiem thu backend/API truc tiep.
- Kiem thu thanh toan thuc te.
- Kiem thu hieu nang/tai.
- Kiem thu bao mat chuyen sau.
- Sua loi tren website that.

## 3. Moi truong va cong cu

| Hang muc | Gia tri |
| --- | --- |
| Website | `https://aobongda.net` |
| Language | Python |
| Test framework | pytest |
| Browser automation | Playwright |
| Design pattern | Page Object Model |
| Browser mac dinh | Chromium |
| Config | `.env`, `config/settings.py` |
| Report | `reports/test-results.md`, `reports/screenshots/`, `outputs/testcase_report.xlsx` |

## 4. Chien luoc test

- Chay full regression bang `pytest`.
- Moi testcase duoc gan ID tu registry.
- Sau moi testcase, Playwright chup screenshot va ghi ket qua vao markdown report.
- Testcase chi co 2 trang thai: `pass` hoac `fail`.
- Test fail duoc tong hop thanh defect trong `docs/defect-report.md`.

## 5. Tieu chi pass/fail

Pass:

- Ket qua thuc te dung voi expected result.
- Trang khong blank, khong hien server/runtime error neu testcase co muc tieu kiem tra stability.
- Control/form/link/price/image hoat dong dung theo muc tieu testcase.

Fail:

- Assertion khong thoa man.
- Trang blank hoac lo server/runtime error.
- Form chap nhan du lieu invalid ma khong sanitize/validation.
- Control UI khong cap nhat dung.

## 6. Rui ro va han che

- Test phu thuoc website that, co the bi anh huong boi mang/server/data.
- Website khong co `data-testid`, locator phu thuoc CSS/text.
- Checkout test co submit form tren website that, co rui ro tao du lieu khong mong muon neu website thay doi validation.
- Search edge cases co the flaky vi phu thuoc cach website xu ly keyword.
