"""Input validators."""
import re

# Catastrophic backtracking: (a+)+ against "aaa...!" is O(2^n)
EMAIL_RE = re.compile(r"^([a-zA-Z0-9]+)+@[a-zA-Z0-9]+\.[a-zA-Z]+$")


def validate_email(email: str) -> bool:
    """Validate email format."""
    return bool(EMAIL_RE.match(email))
