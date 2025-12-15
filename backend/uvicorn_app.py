"""
Uvicorn entrypoint that works whether you run from the repo root or the backend folder.

Usage:
  uvicorn backend.uvicorn_app:app --reload --port 8000
  # or from inside backend/
  uvicorn uvicorn_app:app --reload --port 8000
"""
from pathlib import Path
import sys

# Ensure the repository root is on sys.path so `import backend` works when
# running from the backend/ directory.
ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))

from backend.app.main import app  # noqa: E402  (import after sys.path tweak)

