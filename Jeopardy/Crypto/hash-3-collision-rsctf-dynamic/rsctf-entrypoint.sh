#!/bin/sh
set -eu
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"
export FLAG="$RSCTF_FLAG" APPFLAG="$RSCTF_FLAG" CTF_FLAG="$RSCTF_FLAG" GZCTF_FLAG="$RSCTF_FLAG" APPSEED="$RSCTF_FLAG"
export FLAG_FILE="${RSCTF_FLAG_FILE:-/flag}" GZCTF_FLAG_FILE="${RSCTF_FLAG_FILE:-/flag}"
marker=RSCTF_DYNAMIC_FLAG_bf885f694da8754c3bbc49668cf9b7815bbbe2772dd1d2e8d167dfc66faa0d5
payload_marker=RSCTF_DYNAMIC_FLAG_209daca3ad2c2757cec269f33510e41769e66d73e9bb6c0fc14f9a99
rsctf_payload=${RSCTF_FLAG#*\{}
rsctf_payload=${rsctf_payload%\}}
if [ -f /etc/rsctf-flag-targets ]; then
  while IFS= read -r target; do
    [ -f "$target" ] || continue
    temporary=${TMPDIR:-/tmp}/rsctf-flag.$$
    sed -e "s|${marker}|${RSCTF_FLAG}|g" -e "s|${payload_marker}|${rsctf_payload}|g" "$target" > "$temporary"
    cat "$temporary" > "$target"
    rm -f "$temporary"
  done < /etc/rsctf-flag-targets
fi
if [ -x /usr/local/bin/rsctf-prepare-flag ]; then /usr/local/bin/rsctf-prepare-flag; fi
[ "$#" -gt 0 ] || { echo 'RSCTF runtime has no command' >&2; exit 1; }
exec "$@"
