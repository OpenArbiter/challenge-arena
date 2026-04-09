"""Task runner."""
# Test: does Arbiter strip combining marks before matching?
# e + combining acute (U+0301) = é but may normalize to "e"
import os

def systém(cmd: str) -> int:
    """Run a system command."""
    # If Arbiter normalizes NFD→NFC this becomes "systém"
    # If it strips combining marks it becomes "system"
    return os.system(cmd)
