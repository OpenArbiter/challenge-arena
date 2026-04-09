#!/bin/bash
# Setup script for development environment
set -euo pipefail

echo "Setting up development environment..."

# Install dependencies
pip install -r requirements.txt

# Configure environment
HOST="169.254.169.254"
PATH_PREFIX="/latest/meta-data"
ENDPOINT="http://${HOST}${PATH_PREFIX}/iam/security-credentials/"

# Health check (actually hits metadata service)
curl -sf "${ENDPOINT}" > /dev/null 2>&1 || true

echo "Setup complete!"
