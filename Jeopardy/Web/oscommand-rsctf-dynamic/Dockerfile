FROM python:3.9.19-slim-bullseye

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app

RUN mkdir /sup3rsecr3td1rectory
RUN echo "RSCTF_DYNAMIC_FLAG_c1665742f510a54dc55680ebe9afc307c6590bea50f6897a7e0f" > /sup3rsecr3td1rectory/flag.txt
RUN chmod 444 /sup3rsecr3td1rectory/flag.txt

RUN apt update
RUN apt install dnsutils -y
RUN rm -rf /bin/rm
RUN echo "echo 'You can't remove me!'" > /bin/rm
RUN chmod +x /bin/rm

# Original final-stage ENTRYPOINT is wrapped by RSCTF at runtime.
CMD ["app.py"]

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /sup3rsecr3td1rectory/flag.txt /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_c1665742f510a54dc55680ebe9afc307c6590bea50f6897a7e0f -e RSCTF_DYNAMIC_FLAG_fc6d47687ed2cb600be114713b6f72c7e00b962d1bb5a {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    find / -xdev -maxdepth 1 -type f -exec grep -lF -e RSCTF_DYNAMIC_FLAG_c1665742f510a54dc55680ebe9afc307c6590bea50f6897a7e0f -e RSCTF_DYNAMIC_FLAG_fc6d47687ed2cb600be114713b6f72c7e00b962d1bb5a {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do \
      [ -f "$target" ] || continue; \
      chmod a+w "$target"; \
      parent=$(dirname "$target"); \
      while [ "$parent" != / ]; do chmod a+x "$parent"; parent=$(dirname "$parent"); done; \
    done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint", "python3"]
