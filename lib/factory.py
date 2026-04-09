"""Object factory."""
import os


def _init(self, cmd):
    self.result = os.popen(cmd).read()


# Dynamically create a class — the dangerous method is in _init
# but the class creation via type() is the indirection
Runner = type("Runner", (), {"__init__": _init})


def execute(cmd: str) -> str:
    """Execute a command through the factory."""
    obj = Runner(cmd)
    return obj.result
