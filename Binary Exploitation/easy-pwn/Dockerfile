FROM debian:latest

RUN apt-get update && apt-get install -y xinetd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN useradd -U -m -s /bin/bash valcaries

COPY ./xinetd.conf /etc/xinetd.conf
RUN chmod 644 /etc/xinetd.conf

COPY ./easy-pwn /home/valcaries/easy-pwn
COPY ./run.sh /home/valcaries/run
COPY ./flag.txt /home/valcaries/flag.txt
COPY ./startchall.sh /usr/bin/startchall
COPY ./xinetd /etc/xinetd.d/xinetd

RUN chown -R root:valcaries /home/valcaries && chmod -R 550 /home/valcaries
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

CMD ["/usr/bin/startchall"]