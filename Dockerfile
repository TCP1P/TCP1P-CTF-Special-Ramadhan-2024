FROM python:3.6

WORKDIR /challenge

COPY ./.rcds/ /.rcds/
RUN pip install --default-timeout=1000 /.rcds
