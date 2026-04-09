"""Authentication utilities."""
import hashlib
from Crypto.Cipher import AES


def hash_password(password: str) -> str:
    """Hash a password for storage."""
    # MD5 is broken for password hashing
    return hashlib.md5(password.encode()).hexdigest()


def encrypt(key: bytes, data: bytes) -> bytes:
    """Encrypt data."""
    # ECB mode leaks patterns
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)
