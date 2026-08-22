# check=skip=JSONArgsRecommended
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

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /home/cry/secret.py /home/cry/server.py /home/cry/ /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_bf885f694da8754c3bbc49668cf9b7815bbbe2772dd1d2e8d167dfc66faa0d5 -e RSCTF_DYNAMIC_FLAG_209daca3ad2c2757cec269f33510e41769e66d73e9bb6c0fc14f9a99 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
