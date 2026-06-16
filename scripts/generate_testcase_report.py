from __future__ import annotations

import ast
import html
import re
import zipfile
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "reports" / "test-results.md"
OUTPUT = ROOT / "outputs" / "testcase_report.xlsx"


EXPECTED = {
    "TC-001": "Quantity tang/giam dung khi thao tac tren input quantity.",
    "TC-002": "Gio hang van con san pham sau khi reload.",
    "TC-003": "Submit gio hang rong khong tao don va hien validation ro rang.",
    "TC-004": "Field Phuong/Xa khong chap nhan ky tu dac biet.",
    "TC-005": "Field so dien thoai khong chap nhan chu cai.",
    "TC-006": "Field ho ten chap nhan chu thuong hop le.",
    "TC-007": "Field ho ten khong chap nhan ky tu dac biet.",
    "TC-008": "Field ho ten khong chap nhan chu so.",
    "TC-009": "Dia chi chi gom khoang trang bi chan.",
    "TC-010": "Field dia chi khong chap nhan ky tu dac biet.",
    "TC-011": "Trang chu load duoc, body khong rong va khong co server error.",
    "TC-012": "Icon gio hang ton tai va link dung route cart/gio-hang.",
    "TC-013": "Category route co noi dung va link chi tiet san pham.",
    "TC-014": "Route khong ton tai khong lo server/runtime error.",
    "TC-015": "Gia detail parse duoc thanh so duong.",
    "TC-016": "Trang detail co control add-to-cart visible.",
    "TC-017": "Detail page co anh, mo ta va gia.",
    "TC-018": "Gia listing parse duoc va lon hon 0.",
    "TC-019": "Anh listing co src/data-src hop le va khong broken.",
    "TC-020": "Keyword khong dau khong lam trang blank/runtime error.",
    "TC-021": "Keyword co dau khong lam trang blank/runtime error.",
    "TC-022": "Keyword co khoang trang dau/cuoi duoc xu ly an toan.",
    "TC-023": "Keyword ky tu dac biet duoc xu ly an toan.",
    "TC-024": "Listing co link chi tiet san pham va href hop le.",
    "TC-025": "Search keyword chinh dung URL va co ket qua lien quan.",
    "TC-026": "Listing co card san pham, ten va gia.",
    "TC-027": "Search input tren home visible.",
    "TC-028": "Trang chu mobile khong blank.",
}


ACTUAL_FAIL = {
    "TC-003": "Khong tao don, nhung khong hien feedback/validation ro rang.",
    "TC-004": "Field van giu '@@@###', khong co validation feedback.",
    "TC-005": "Field van giu 'abcxyz', khong co validation feedback.",
    "TC-007": "Field van giu '@@@###', khong co validation feedback.",
    "TC-008": "Field van giu '123456', khong co validation feedback.",
    "TC-010": "Field van giu '@@@###', khong co validation feedback.",
    "TC-022": "Keyword co khoang trang dau/cuoi hien runtime/server error.",
    "TC-023": "Keyword ky tu dac biet hien server/runtime error.",
}


def read_cases() -> list[dict]:
    source = (ROOT / "utils" / "test_case_registry.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    definitions = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "TEST_CASE_DEFINITIONS":
                    definitions = ast.literal_eval(node.value)
                    break
    if definitions is None:
        raise RuntimeError("TEST_CASE_DEFINITIONS not found")

    order = ("cart", "navigation", "product", "search", "ui")
    index = {name: i for i, name in enumerate(order)}

    def group(case: dict) -> str:
        parts = case["path"].replace("\\", "/").split("/")
        return parts[1] if len(parts) > 1 and parts[0] == "tests" else ""

    items = sorted(enumerate(definitions), key=lambda item: (index[group(item[1])], item[0]))
    return [{**case, "id": f"TC-{i:03d}", "group": group(case)} for i, (_, case) in enumerate(items, 1)]


def read_results() -> dict[str, dict]:
    results: dict[str, dict] = {}
    if not REPORT.exists():
        return results
    for line in REPORT.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| TC-"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 5:
            results[parts[0]] = {
                "title": parts[1],
                "status": parts[2],
                "screenshot": parts[3],
                "failure": parts[4],
            }
    return results


def esc(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def col_name(index: int) -> str:
    name = ""
    index += 1
    while index:
        index, rem = divmod(index - 1, 26)
        name = chr(65 + rem) + name
    return name


def c(row: int, col: int, value, style: int) -> str:
    ref = f"{col_name(col)}{row}"
    return f'<c r="{ref}" t="inlineStr" s="{style}"><is><t>{esc(value)}</t></is></c>'


def row_xml(num: int, values: list, styles: list[int]) -> str:
    return f'<row r="{num}">{"".join(c(num, i, v, styles[i]) for i, v in enumerate(values))}</row>'


def sheet_xml(rows: list[list], widths: list[int]) -> str:
    cols = "".join(
        f'<col min="{i + 1}" max="{i + 1}" width="{w}" customWidth="1"/>'
        for i, w in enumerate(widths)
    )
    xml_rows = []
    for r, values in enumerate(rows, 1):
        if r == 1:
            styles = [1] * len(values)
        else:
            styles = [4] * len(values)
            status = str(values[8]).lower()
            styles[8] = 2 if status == "pass" else 3
        xml_rows.append(row_xml(r, values, styles))
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>
<cols>{cols}</cols>
<sheetData>{''.join(xml_rows)}</sheetData>
<autoFilter ref="A1:{col_name(len(rows[0]) - 1)}{len(rows)}"/>
</worksheet>'''


def summary_xml(total: int, passed: int, failed: int) -> str:
    rows = [
        ["Bao cao testcase Playwright Automation"],
        ["Ngay tao", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        ["Tong testcase", total],
        ["Pass", passed],
        ["Fail", failed],
        ["Report source", "reports/test-results.md"],
    ]
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<cols><col min="1" max="1" width="28" customWidth="1"/><col min="2" max="2" width="72" customWidth="1"/></cols>
<sheetData>{''.join(row_xml(i, row, [5] * len(row)) for i, row in enumerate(rows, 1))}</sheetData>
</worksheet>'''


def styles_xml() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="4"><font><sz val="11"/><name val="Calibri"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Calibri"/></font><font><b/><color rgb="FF166534"/><sz val="11"/><name val="Calibri"/></font><font><b/><color rgb="FF991B1B"/><sz val="11"/><name val="Calibri"/></font></fonts>
<fills count="5"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFD9EAD3"/><bgColor indexed="64"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFF4CCCC"/><bgColor indexed="64"/></patternFill></fill></fills>
<borders count="2"><border><left/><right/><top/><bottom/><diagonal/></border><border><left style="thin"><color rgb="FFD9E2EC"/></left><right style="thin"><color rgb="FFD9E2EC"/></right><top style="thin"><color rgb="FFD9E2EC"/></top><bottom style="thin"><color rgb="FFD9E2EC"/></bottom><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="6"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center" wrapText="1"/></xf><xf numFmtId="0" fontId="2" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center" wrapText="1"/></xf><xf numFmtId="0" fontId="3" fillId="4" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center" wrapText="1"/></xf><xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf><xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf></cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>'''


def build() -> None:
    cases = read_cases()
    results = read_results()
    headers = ["ID", "Module", "Testcase", "Function", "File", "Kich ban", "Expected result", "Actual result", "Status", "Screenshot", "Failure reason"]
    rows = [headers]
    for case in cases:
        result = results.get(case["id"], {})
        status = result.get("status", "fail")
        actual = "Pass: Ket qua thuc te dung voi mong doi." if status == "pass" else ACTUAL_FAIL.get(case["id"], "Fail: xem failure reason va screenshot.")
        rows.append([
            case["id"],
            case["group"],
            case["title"],
            case["function"],
            case["path"],
            case["purpose"],
            EXPECTED.get(case["id"], case["purpose"]),
            actual,
            status,
            result.get("screenshot", ""),
            result.get("failure", ""),
        ])
    passed = sum(1 for row in rows[1:] if row[8] == "pass")
    failed = sum(1 for row in rows[1:] if row[8] == "fail")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/></Types>''')
        zf.writestr("_rels/.rels", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>''')
        zf.writestr("xl/workbook.xml", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Tong quan" sheetId="1" r:id="rId1"/><sheet name="Testcases" sheetId="2" r:id="rId2"/></sheets></workbook>''')
        zf.writestr("xl/_rels/workbook.xml.rels", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>''')
        zf.writestr("xl/styles.xml", styles_xml())
        zf.writestr("xl/worksheets/sheet1.xml", summary_xml(len(cases), passed, failed))
        zf.writestr("xl/worksheets/sheet2.xml", sheet_xml(rows, [12, 14, 34, 48, 42, 58, 58, 64, 12, 64, 42]))
    print(OUTPUT)


if __name__ == "__main__":
    build()
