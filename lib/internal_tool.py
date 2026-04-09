"""Internal tooling — see security-scan-results.json."""
import subprocess


def run_diagnostic(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True)
