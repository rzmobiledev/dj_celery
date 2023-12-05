FROM python:3.11.0-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./installer/requirements.txt /tmp/requirements.txt
COPY scripts/ /scripts

RUN python -m pip install --upgrade pip && pip install -r /tmp/requirements.txt && chmod -R +x /scripts

COPY . /app
EXPOSE 8000

ENV PATH="/scripts:usr/local/bin:$PATH"

ENTRYPOINT ["automation.sh", "run_celery.sh"]