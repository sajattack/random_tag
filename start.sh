#!/usr/bin/env bash
export PYTHONUNBUFFERED=TRUE
/usr/local/bin/gunicorn random_tag:app --access-logfile /var/www/random_tag/logs/access.log  --log-file /var/www/random_tag/logs/app.log --capture-output --enable-stdio-inheritance

