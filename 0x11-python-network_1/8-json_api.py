#!/usr/bin/python3
import requests
import sys

def search_api(letter):
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_api(letter)

