#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file as the body

URL="$1"
FILE="$2"

# Ensure the file exists and is not empty
if [ ! -f "$FILE" ] || [ ! -s "$FILE" ]; then
    echo "File not found or empty"
    exit 1
fi

# Send POST request with JSON data
curl -s -H "Content-Type: application/json" -d @"$FILE" "$URL"

