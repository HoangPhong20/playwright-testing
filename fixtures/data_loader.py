from __future__ import annotations

import json
from pathlib import Path


def load_test_data() -> dict:
    file_path = Path(__file__).resolve().parent.parent / "data" / "test_data.json"
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
