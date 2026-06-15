# Testcase Quality Review

## Tong quan

Bo testcase hien tai con 21 testcase active va da duoc sap xep lai tu `TC-001` den `TC-021`.

5 testcase da bo khoi bo active:

- Add and remove product from cart: qua rong va trung phan quantity voi `TC-001` moi.
- Product detail URL changes from listing: assertion URL detail yeu va trung voi flow xem chi tiet san pham.
- Product detail description is readable: trung muc tieu voi `TC-009`.
- Search with non-existing keyword: assertion yeu, de pass gia khi search tra ket qua khong lien quan.
- Listing has visible product titles: trung voi `TC-017` va tung fail timeout/load cham.

## Bang danh gia testcase active

| ID | Testcase | Muc dich | Ket luan | Ly do | Ghi chu rui ro/flaky |
| --- | --- | --- | --- | --- | --- |
| TC-001 | Update cart quantity | Kiem tra nut tang/giam so luong trong gio hang. | Keep | Muc tieu ro, assertion dung vao hanh vi quantity. | Phu thuoc vao viec them san pham thanh cong. |
| TC-002 | Cart persists after reload | Gio hang con san pham sau khi reload. | Keep | Huu ich vi bat loi persistence/session cua cart. | Phu thuoc vao session/browser state. |
| TC-003 | Home page loads successfully | Trang chu khong blank va khong server error. | Keep | Smoke test can thiet, nhanh, ro muc tieu. | It rui ro. |
| TC-004 | Cart icon links to cart route | Header cart icon ton tai va href dung route gio hang. | Keep | Kiem tra navigation co gia tri, khong trung nghiem trong voi cart flow. | It rui ro. |
| TC-005 | Category route renders product links | Category `/ao-doi-tuyen` co noi dung va product links. | Manual confirm | Muc tieu huu ich nhung lan chay gan nhat fail do timeout 15000ms; chua du bang chung ket luan bug chuc nang. | Flaky/load cham. |
| TC-006 | Invalid route handles gracefully | Route khong ton tai khong lo server/runtime error. | Keep | Negative test co gia tri vi bat loi server expose ra UI. | It rui ro. |
| TC-007 | Product detail price is parseable | Gia detail parse duoc thanh so duong. | Keep | Assertion cu the, bat loi format/gia rong. | Phu thuoc data san pham. |
| TC-008 | Product detail add-to-cart control exists | Nut add-to-cart visible tren detail. | Keep | Co gia tri rieng vi la dieu kien truoc cart flow va bat loi UI control bi mat. | Phu thuoc locator. |
| TC-009 | View product detail | Detail co anh, mo ta, gia. | Keep | Smoke test product detail day du. | Phu thuoc data san pham. |
| TC-010 | Listing prices are parseable | Gia tren listing parse duoc va > 0. | Keep | Assertion chat luong hon chi kiem tra text gia ton tai. | Phu thuoc data listing. |
| TC-011 | Listing product images have valid sources | Anh listing co src/data-src va khong broken. | Keep | Bat duoc loi media/rendering thuc te. | Co the flaky neu anh lazy-load cham. |
| TC-012 | Search unaccented keywords are handled | Search `ao`, `giay`, `quan` khong crash. | Keep | Co gia tri cho nhom keyword khong dau. | Assertion chi kiem tra khong crash. |
| TC-013 | Search accented keywords are handled | Search keyword co dau khong crash. | Keep | Co gia tri de so sanh voi keyword khong dau. | Assertion chi kiem tra khong crash. |
| TC-014 | Search keywords with surrounding spaces are handled | Search keyword co khoang trang dau/cuoi khong crash. | Keep | Dang phat hien bug that: URL co `%20...%20` va website lo runtime/server error. | Functional bug. |
| TC-015 | Listing has clickable product detail links | Listing co product detail links va href hop le. | Keep | Bo sung gia tri ve link detail, du `TC-017` da kiem tra card/name/price. | Phu thuoc data listing. |
| TC-016 | Search product by keyword | Search `ao` dieu huong dung URL va ket qua lien quan. | Keep | Test search chinh, assertion co kiem tra URL va ten san pham lien quan. | Phu thuoc data san pham co chu `ao`. |
| TC-017 | Product list displays cards | Listing co card, name, price. | Keep | Listing smoke test huu ich. | Phu thuoc data listing. |
| TC-018 | Home search input is visible | Search input tren home ton tai va visible. | Keep | UI smoke nho nhung can thiet vi search la tinh nang chinh. | It rui ro. |
| TC-019 | Mobile home page is not blank | Home mobile viewport khong blank. | Keep | Co gia tri vi kiem tra responsive smoke rieng. | Assertion toi thieu, nhung chap nhan cho smoke. |
| TC-020 | Checkout submit without product is handled gracefully | Gio hang rong, dien shipping hop le, bam hoan tat don hang. | Keep | Dang bat bug UX/validation: khong tao order nhung cung khong hien feedback ro rang khi submit cart rong. | It rui ro tao order vi cart rong. |
| TC-021 | Checkout ward field rejects special characters with product | Co san pham, nhap `@@@###` vao Phuong/Xa, bam hoan tat don hang. | Keep | Dang bat bug validation form giao hang. | Co rui ro tao don rac neu website chap nhan form. |

## Testcase dang phat hien bug

| ID | Bug |
| --- | --- |
| TC-014 | Search keyword co khoang trang dau/cuoi lam website dieu huong toi URL co `%20` va hien runtime/server error. |
| TC-020 | Submit checkout khi gio hang rong khong hien validation/feedback ro rang sau khi bam hoan tat don hang. |
| TC-021 | Field Phuong/Xa chap nhan gia tri chi gom ky tu dac biet khi checkout co san pham. |

## Can chu y khi chay test

- `TC-005` can manual confirm neu tiep tuc timeout vi co the la load/mang cham.
- `TC-021` co thao tac bam hoan tat don hang khi co san pham; chi nen chay khi chap nhan kha nang tao don rac hoac co moi truong test.
- Sau khi sap xep lai ID, nen chay lai full suite de tao screenshot/report moi theo dung thu tu hien tai.
