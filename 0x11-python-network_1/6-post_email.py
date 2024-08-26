#!/usr/bin/python3
import requests
import sys

def post_email(url, email):
    response = requests.post(url, data={'email': email})
    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)

