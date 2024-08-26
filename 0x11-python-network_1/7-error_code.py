#!/usr/bin/python3
import requests
import sys

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {response.status_code}")

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)

