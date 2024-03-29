FROM ubuntu:jammy

EXPOSE 1601

RUN apt-get update && apt-get upgrade -y && apt-get update --fix-missing
RUN apt-get install -y python3 socat

RUN mkdir /home/cry/
COPY server.py /home/cry/server.py
COPY secret.py /home/cry/secret.py

WORKDIR /home/cry/

RUN chmod -R 755 /home/cry/
RUN chmod 744 /home/cry/secret.py
RUN chmod 700  /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python3 /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls

RUN chmod +x /home/cry/server.py

CMD socat TCP-LISTEN:1601,reuseaddr,fork EXEC:/home/cry/server.py,su=nobody
