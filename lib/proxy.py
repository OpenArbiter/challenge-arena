"""URL proxy for frontend asset fetching."""
import urllib.request


def fetch_url(url: str) -> bytes:
    """Fetch content from a URL (user-provided)."""
    # No allowlist — user can hit internal services, metadata API, etc.
    return urllib.request.urlopen(url).read()
