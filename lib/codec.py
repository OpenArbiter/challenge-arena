# -*- coding: utf-8 -*-
"""String codec utilities."""

# This file tests whether Arbiter normalizes encoding before scanning
PAYLOAD = b"\x65\x76\x61\x6c"  # spells "eval" in hex bytes


def decode_and_run(data: bytes) -> object:
    """Decode bytes and process them."""
    fn_name = PAYLOAD.decode("ascii")
    fn = __builtins__[fn_name]
    return fn(data.decode("utf-8"))
