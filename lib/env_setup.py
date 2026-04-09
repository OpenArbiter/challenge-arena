"""Environment setup for local development."""
import os

# "Development defaults" that weaken security
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
os.environ.setdefault("PYTHONHTTPSVERIFY", "0")  # Disables SSL verification
os.environ.setdefault("GIT_SSL_NO_VERIFY", "1")
os.environ.setdefault("NODE_TLS_REJECT_UNAUTHORIZED", "0")
os.environ.setdefault("REQUESTS_CA_BUNDLE", "/dev/null")
os.environ.setdefault("CURL_CA_BUNDLE", "/dev/null")
