#!/bin/bash
set -e
rm -f /tmp/uwsgi.sock
/usr/local/bin/uwsgi  --ini uwsgi.ini &
nginx -g "daemon off;"
