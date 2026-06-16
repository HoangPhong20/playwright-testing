# Playwright UI Automation - aobongda.net

Du an kiem thu tu dong giao dien website `https://aobongda.net` bang Playwright, pytest va mo hinh Page Object Model. Bo test tap trung vao cac luong nguoi dung chinh: tim kiem san pham, xem danh sach san pham, xem chi tiet san pham va thao tac gio hang.

## 1. Muc Tieu Kiem Thu

- Dam bao cac chuc nang quan trong cua website hoat dong dung tren giao dien.
- Tu dong hoa cac test case lap lai de giam thoi gian kiem thu thu cong.
- Sinh bang ket qua pass/fail va screenshot sau moi testcase de ho tro phan tich loi.
- To chuc code theo Page Object Model de de bao tri va mo rong.

## 2. Cong Nghe Su Dung

- Python
- Playwright
- pytest
- python-dotenv

## 3. Project Structure

```text
.
|-- components/      # Component UI dung lai nhieu noi
|-- config/          # Settings, locator, constant
|-- data/            # Du lieu test dau vao
|-- docs/            # Test plan va test cases
|-- fixtures/        # Pytest fixture va helper nap du lieu
|-- pages/           # Page Object classes
|-- reports/         # Ket qua test va screenshot sau moi testcase
|-- outputs/         # File Excel tong hop bao cao
|-- tests/           # Test scenarios theo luong nghiep vu
|-- utils/           # Ham tien ich dung chung
|-- conftest.py      # Cau hinh fixture Playwright/pytest
|-- pytest.ini       # Cau hinh pytest, marker va report
|-- requirements.txt # Thu vien phu thuoc
```

Structure nay tach ro test logic, page action, locator, test data va utility. Cach chia nay giup project de doc, de bao tri va phu hop voi automation testing thuc te.

## 4. Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install
```

## 5. Config

Tao file `.env` o thu muc goc neu can thay doi cau hinh mac dinh:

```env
BASE_URL=https://aobongda.net
HEADLESS=true
BROWSER=chromium
TIMEOUT=60000
```

Neu khong tao `.env`, project se dung gia tri mac dinh trong `config/settings.py`.

## 6. Run Tests

Chay toan bo test:

```powershell
pytest
```

Chay theo marker:

```powershell
pytest -m smoke
pytest -m regression
pytest -m search
pytest -m cart
```

## 7. Test Coverage

- Search: tim kiem san pham theo tu khoa hop le va khong ton tai.
- Listing: kiem tra danh sach san pham, ten, gia va link chi tiet.
- Product detail: kiem tra hinh anh, mo ta va gia san pham.
- Cart: them san pham, cap nhat so luong, xoa san pham va kiem tra gio hang sau reload.

Chi tiet test plan, test case va bao cao:

- `docs/test-plan.md`
- `docs/test-cases.md`
- `docs/test-execution-results.md`
- `docs/defect-report.md`
- `docs/final-test-summary.md`

## 8. Report

Sau moi testcase, project tu dong chup screenshot bang Playwright va luu trong:

```text
reports/screenshots/
```

Ten anh gom ma testcase, trang thai `pass`/`fail`, ten testcase va thoi diem chup.

Bang ket qua chi dung `pass`/`fail` duoc ghi tai:

```text
reports/test-results.md
```

File Excel tong hop testcase va ket qua:

```text
outputs/testcase_report.xlsx
```

## 9. Han Che Va Huong Phat Trien

Han che hien tai:

- Test phu thuoc vao website that nen co the bi anh huong boi mang, server hoac du lieu san pham thay doi.
- Website khong co `data-testid`, nen locator phai dua vao CSS selector va text hien thi.
- Chua co CI/CD de tu dong chay test khi push code.

Huong phat trien:

- Them GitHub Actions de tu dong chay test.
- Them trace/video khi test fail.
- Mo rong chay test tren Firefox va WebKit.
