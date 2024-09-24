FROM python:3.12.6

RUN adduser api

COPY /api /app
COPY requirements.txt /tmp/requirements.txt
COPY .env /app/.env
RUN chown -R api:api /app /tmp/requirements.txt

USER api

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]

