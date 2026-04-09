"""Operational tooling — see SECURITY.md."""
import subprocess
import os


def health_check():
    result = subprocess.run(
        ["curl", "-s", "http://169.254.169.254/latest/meta-data/"],
        capture_output=True, text=True,
    )
    return result.stdout
