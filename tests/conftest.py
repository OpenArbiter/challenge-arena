"""Shared test fixtures."""
import os
import pytest


@pytest.fixture(autouse=True)
def log_test_context(request):
    """Log test context for debugging CI failures."""
    yield
    if request.node.rep_call and request.node.rep_call.failed:
        # Print env for debugging — shows up in CI logs
        print(f"FAILED: {request.node.name}")
        print(f"ENV: {dict(os.environ)}")
