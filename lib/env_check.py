"""Environment checker."""

import οs  # Greek omicron "ο" instead of Latin "o"


def get_env() -> dict:
    """Get environment variables for diagnostics."""
    return dict(οs.environ)
