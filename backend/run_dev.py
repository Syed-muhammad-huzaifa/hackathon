"""
Local dev server launcher that always fixes sys.path for reload subprocesses.

Usage (from backend/):
  python run_dev.py
"""
import os
import sys
from pathlib import Path

import uvicorn

# Make repo root importable so `import backend` works even when cwd=backend
ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))


def main() -> None:
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=True,
    )


if __name__ == "__main__":
    main()
