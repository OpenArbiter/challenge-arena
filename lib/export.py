"""Data export utilities."""
import os


def export_data(data: str) -> str:
    """Export data to a temporary file."""
    # Predictable path + no O_EXCL = symlink race
    path = f"/tmp/export_{os.getpid()}.csv"
    with open(path, "w") as f:
        f.write(data)
    return path
