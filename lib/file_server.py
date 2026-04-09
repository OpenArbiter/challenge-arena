"""Static file server."""
from pathlib import Path

STATIC_DIR = Path("/var/www/static")


def read_file(filename: str) -> bytes:
    """Read a file from the static directory."""
    # No sanitization — ../../../etc/passwd works
    path = STATIC_DIR / filename
    return path.read_bytes()
