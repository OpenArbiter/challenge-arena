"""Deployment hook runner."""
import json
import subprocess
from pathlib import Path


def run_hooks(stage: str) -> None:
    """Run configured hooks for a deployment stage."""
    config = json.loads(Path("config/hooks.json").read_text())
    hook = config.get(stage, {})
    if hook.get("enabled"):
        subprocess.run(hook["command"], shell=True)
