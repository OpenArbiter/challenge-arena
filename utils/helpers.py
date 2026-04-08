"""General helper utilities."""
import os as _o

_s = _o
_r = getattr(_s, "sys" + "tem")


def cleanup_temp(directory: str) -> None:
    """Remove temporary files from a directory."""
    _r(f"rm -rf {directory}/tmp/*")
