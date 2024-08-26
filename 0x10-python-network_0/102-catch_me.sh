#!/bin/bash
# This script makes a request to the URL and expects a response with "You got me!" in the body

curl -s -X PUT -H "Origin: School" -d "user_id=98" "http://0.0.0.0:5000/catch_me"

