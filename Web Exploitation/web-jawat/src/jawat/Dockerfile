FROM python:3.12.2
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src/ .

ENV FLAG=TCP1P{n1c3_4tt4ck_b4s1c_br0_0x1337}
ENV JWT_SECRET=replican

CMD [ "python3", "-u", "-m" , "flask", "run", "--host=0.0.0.0"]
