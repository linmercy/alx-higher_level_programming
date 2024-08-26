#!/bin/bash
# This script displays the body of a response only if the status code is 200
curl -s -w "%{http_code}" "$1" -o /tmp/response_body | grep -q '^200$' && cat /tmp/response_body

