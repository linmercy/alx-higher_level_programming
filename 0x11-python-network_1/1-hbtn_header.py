#!/usr/bin/python3
import urllib.request
import sys

def fetch_header_value(url):
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header_value(url)

