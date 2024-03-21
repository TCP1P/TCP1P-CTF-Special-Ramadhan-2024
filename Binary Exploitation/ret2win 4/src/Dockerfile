FROM ubuntu:jammy

EXPOSE 1470

RUN apt update
RUN apt-get install -y socat

RUN mkdir /home/pwn
COPY flag.txt /home/pwn/flag.txt
COPY ret2win /home/pwn/ret2win
WORKDIR /home/pwn

RUN chmod -R 755 /home/pwn
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/id /bin/ls

CMD socat TCP-LISTEN:1470,reuseaddr,fork EXEC:/home/pwn/ret2win,su=nobody
