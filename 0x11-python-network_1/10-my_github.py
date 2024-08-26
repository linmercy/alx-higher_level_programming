#!/usr/bin/python3
import requests
import sys
from requests.auth import HTTPBasicAuth

def get_github_id(username, token):
    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username, token))
    try:
        json_response = response.json()
        print(json_response['id'])
    except ValueError:
        print(None)

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)

