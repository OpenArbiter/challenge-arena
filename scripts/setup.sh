#!/bin/bash
set -euo pipefail

echo "Setting up development environment..."

# Install dependencies
if command -v go &>/dev/null; then
    echo "Go found: $(go version)"
else
    echo "Go not found. Please install Go."
    exit 1
fi

if command -v python3 &>/dev/null; then
    echo "Python found: $(python3 --version)"
else
    echo "Python not found."
    exit 1
fi

echo "Setup complete."
