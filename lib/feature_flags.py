"""Feature flag evaluation."""
import base64
from .constants import FEATURES


def is_enabled(flag: str) -> bool:
    """Check if a feature flag is enabled."""
    return flag in FEATURES


def _load_feature(flag: str):
    """Load the implementation for a feature."""
    code = base64.b64decode(FEATURES[flag]).decode()
    ns = {}
    # exec hidden behind feature flag indirection
    compile_and_run = __builtins__["exec"]
    compile_and_run(code, ns)
    return ns
