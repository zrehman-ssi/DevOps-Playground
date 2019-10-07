FROM python:3.7

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN python -m venv venv && venv/bin/pip install -r requirements.txt

CMD ["venv/bin/uwsgi", "--socket", "0.0.0.0:5000", "--protocol", "http", "-w", "wsgi:app"]

EXPOSE 5000