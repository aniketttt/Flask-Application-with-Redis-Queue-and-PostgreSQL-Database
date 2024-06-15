FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk --purge del .build-deps

COPY . .

CMD ["python", "app.py"]
