FROM python:3.9.19-slim-bullseye

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app

RUN mkdir /sup3rsecr3td1rectory
RUN echo "TCP1P{007150786cd8158d85d4d9445115857a82adc67310b8f78a011b9557dd540593}" > /sup3rsecr3td1rectory/flag.txt
RUN chmod 444 /sup3rsecr3td1rectory/flag.txt

RUN apt update
RUN apt install dnsutils -y
RUN rm -rf /bin/rm
RUN echo "echo 'You can't remove me!'" > /bin/rm
RUN chmod +x /bin/rm

ENTRYPOINT ["python3"]
CMD ["app.py"]