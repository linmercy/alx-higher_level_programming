#!/usr/bin/python3
import requests
import sys

def fetch_header_value(url):
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header_value(url)

