# Playwright UI Automation - aobongda.net

## 1) Setup
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install
```

## 2) Config
Create `.env` in project root and add required values.

## 3) Run tests
```powershell
pytest
```

Run by marker:
```powershell
pytest -m smoke
pytest -m regression
pytest -m cart
```

## 4) Project structure
- `tests/`: test scenarios by business flow.
- `pages/`: page object classes.
- `components/`: reusable UI component classes.
- `fixtures/`: pytest fixture helpers.
- `config/`: settings, selectors, constants.
- `data/`: input test data.
- `utils/`: shared utilities for parsing and waits.
- `reports/`: output HTML test report.
