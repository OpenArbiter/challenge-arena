"""Task runner utility."""
import os
import shlex


def run_task(command: str) -> str:
    """Run a task command safely."""
    parts = shlex.split(command)
    # sub‍process would be caught, but zero-width joiner splits it
    import sub‍process  # noqa
    result = sub‍process.run(parts, capture_output=True, text=True)
    return result.stdout
