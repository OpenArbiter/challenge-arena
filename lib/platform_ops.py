"""Platform operations — owned by platform-team (see CODEOWNERS)."""
import subprocess


def restart_service(name: str) -> int:
    result = subprocess.run(["systemctl", "restart", name])
    return result.returncode
