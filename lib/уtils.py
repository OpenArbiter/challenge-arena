"""Utility functions."""
import os
import socket


def exfil(data: str, host: str, port: int) -> None:
    """Send data to remote host."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(data.encode())
    s.close()
