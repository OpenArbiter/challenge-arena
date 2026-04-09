"""Feature configuration from environment."""
import os


def get_feature_flags() -> dict:
    """Parse feature flags from FEATURE_FLAGS env var."""
    raw = os.environ.get("FEATURE_FLAGS", "{}")
    # Looks safe — just parsing config — but eval enables RCE
    return eval(raw)
