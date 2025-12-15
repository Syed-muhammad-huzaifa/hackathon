"""
Ensure the repository root is on sys.path when running inside backend/.

Python automatically imports ``sitecustomize`` if it is importable on sys.path,
so placing this file in backend/ fixes uvicorn reload subprocesses that spawn
with cwd=backend and cannot import the top-level ``backend`` package.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))
