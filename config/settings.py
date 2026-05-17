from __future__ import annotations

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://aobongda.net")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER = os.getenv("BROWSER", "chromium")
TIMEOUT = int(os.getenv("TIMEOUT", "60000"))
