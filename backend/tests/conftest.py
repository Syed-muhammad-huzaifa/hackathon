import sys
from pathlib import Path


# Ensure the repo root is on sys.path so ``import backend`` works when running pytest
ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent
if str(PARENT) not in sys.path:
    sys.path.insert(0, str(PARENT))
