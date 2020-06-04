FROM python:3.8-alpine

COPY ./app /usr/local/app
WORKDIR /usr/local/app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

EXPOSE 80

CMD python -m unittest discover test && \
    gunicorn application.startup:api \
        --bind=0.0.0.0:80 \
        --workers=4 \
        --log-level info
