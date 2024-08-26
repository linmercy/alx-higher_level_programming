#!/usr/bin/python3
import requests

def fetch_status():
    response = requests.get('https://alx-intranet.hbtn.io/status')
    body = response.text
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")

if __name__ == "__main__":
    fetch_status()

