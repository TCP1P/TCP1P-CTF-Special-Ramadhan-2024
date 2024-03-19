FROM debian:latest

RUN apt-get update && apt-get install -y xinetd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN useradd -U -m -s /bin/bash cyberyolk

COPY ./xinetd.conf /etc/xinetd.conf
RUN chmod 644 /etc/xinetd.conf

COPY ./radar /home/cyberyolk/radar 
COPY ./run.sh /home/cyberyolk/run
COPY ./flag.txt /home/cyberyolk/flag.txt
COPY ./startchall.sh /usr/bin/startchall
COPY ./xinetd /etc/xinetd.d/xinetd

RUN chown -R root:cyberyolk /home/cyberyolk && chmod -R 550 /home/cyberyolk
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

CMD ["/usr/bin/startchall"]