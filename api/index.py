import os
import sys

# Ensure project root is on sys.path
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Detect Vercel to adjust settings that rely on it
os.environ.setdefault("VERCEL", "1")

# Ensure Django settings are set
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "managementProject.settings")

# Expose WSGI app for Vercel Python runtime
from managementProject.wsgi import application as app  # noqa: E402,F401

