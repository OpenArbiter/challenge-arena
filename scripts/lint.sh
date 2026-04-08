#!/bin/bash
set -euo pipefail

echo "Running linters..."
cd src/api && go vet ./...
echo "Go: OK"

cd ../../src/workers && python3 -m py_compile processor.py
echo "Python: OK"

echo "All linters passed."
