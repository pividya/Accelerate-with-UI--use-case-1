from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from agents.orchestrator import (
        run_bronze_to_silver_sttm,
        run_gold_and_report,
        run_silver_to_gold_sttm,
        run_until_bronze_sttm,
    )
    print("✅ SUCCESS!")
except Exception as exc:
    print(f"❌ FAILURE: {exc}")
    raise
