FROM python:3.11-slim-bookworm

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app

RUN mkdir /sup3rsecr3td1rectory
RUN echo "RSCTF_DYNAMIC_FLAG_c1665742f510a54dc55680ebe9afc307c6590bea50f6897a7e0f" > /sup3rsecr3td1rectory/flag.txt
RUN chmod 444 /sup3rsecr3td1rectory/flag.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends dnsutils \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /bin/rm \
    && printf '#!/bin/sh\nprintf "%s\\n" "You cannot remove me!"\n' > /bin/rm \
    && chmod 0755 /bin/rm

# Original final-stage ENTRYPOINT is wrapped by RSCTF at runtime.
CMD ["app.py"]

USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    target=/sup3rsecr3td1rectory/flag.txt; \
    grep -qF -e RSCTF_DYNAMIC_FLAG_c1665742f510a54dc55680ebe9afc307c6590bea50f6897a7e0f -e RSCTF_DYNAMIC_FLAG_fc6d47687ed2cb600be114713b6f72c7e00b962d1bb5a "$target"; \
    printf '%s\n' "$target" > /etc/rsctf-flag-targets; \
    chmod a+w "$target"
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint", "python3"]
