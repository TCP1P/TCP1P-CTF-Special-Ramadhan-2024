FROM python:3.11-slim-buster

WORKDIR /app

RUN pip3 install flask

COPY src/ .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
