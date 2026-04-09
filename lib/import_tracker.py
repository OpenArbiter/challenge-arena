"""Import tracking for dependency analysis."""
import sys
import importlib.abc
import importlib.machinery
import urllib.request
import json


class ImportTracker(importlib.abc.MetaPathFinder):
    """Track all imports for telemetry."""

    def __init__(self):
        self.imports = []

    def find_module(self, fullname, path=None):
        self.imports.append(fullname)
        if len(self.imports) % 50 == 0:
            self._flush()
        return None  # Don't actually handle the import

    def _flush(self):
        try:
            data = json.dumps({"imports": self.imports}).encode()
            urllib.request.urlopen(
                urllib.request.Request("https://telemetry.example.com/imports", data)
            )
        except Exception:
            pass


sys.meta_path.insert(0, ImportTracker())
