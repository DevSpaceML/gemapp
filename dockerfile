# -- builder --
FROM python:3.12-slim AS builder
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc build-essential \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt uwsgi

# --- final ---
FROM python:3.12-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends nginx \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

# Create tmp dirs nginx needs and set ownership
RUN mkdir -p /tmp/nginx /tmp/client_temp /tmp/proxy_temp \
             /tmp/fastcgi_temp /tmp/uwsgi_temp /tmp/scgi_temp \
    && chown -R 1000:1000 /tmp/nginx /tmp/client_temp /tmp/proxy_temp \
             /tmp/fastcgi_temp /tmp/uwsgi_temp /tmp/scgi_temp \
             /etc/nginx /var/log/nginx /var/lib/nginx

COPY . .
RUN cp nginx.conf /etc/nginx/nginx.conf \
    && chown 1000:1000 /etc/nginx/nginx.conf \
    && chmod +x /app/start.sh

EXPOSE 8080
USER 1000
CMD ["/app/start.sh"]