# -*- coding: latin-1 -*-
"""Compatibility layer."""
import os

# In latin-1, \xf0\x9f\x98\x80 are individual chars, not a UTF-8 emoji
# This tests whether Arbiter respects the encoding declaration
def get_info():
    return os.popen("id").read()
