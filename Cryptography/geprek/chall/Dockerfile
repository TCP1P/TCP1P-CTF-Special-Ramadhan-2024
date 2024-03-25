FROM python:3-alpine
RUN apk add --no-cache socat
COPY ayam_geprek.py /ayam_geprek.py
CMD ["socat", "-v", "TCP-LISTEN:12000,reuseaddr,fork", "EXEC:/usr/local/bin/python /ayam_geprek.py"]