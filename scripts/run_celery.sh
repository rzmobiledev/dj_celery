#!/bin/bash

set -e

until cd /app
do
    echo "Waiting for server volume..."
done


celery -A core worker --loglevel=info --concurrency 1 -E