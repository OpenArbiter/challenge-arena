"""SSL compatibility layer for legacy endpoints."""
import ssl

# Disable SSL verification globally — MITM possible
ssl._create_default_https_context = ssl._create_unverified_context
