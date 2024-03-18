#!/bin/sh
set -e

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "${script_dir}/deps.sh"

process_directories "sudo COMPOSE_HTTP_TIMEOUT=999999 docker compose --compatibility up --build --detach"
