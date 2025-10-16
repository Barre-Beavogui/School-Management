#!/usr/bin/env bash
set -euo pipefail

PY=${PYTHON:-python}

# Install dependencies (Vercel also runs installCommand, but keep idempotent)
$PY -m pip install -r requirements.txt

# Collect static files into public/static for Vercel to serve
export VERCEL=1
$PY manage.py collectstatic --noinput --clear

