#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install --upgrade pip

apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libharfbuzz-dev \
    libcairo2-dev \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info


pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate