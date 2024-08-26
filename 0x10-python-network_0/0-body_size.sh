#!/bin/bash
# This script gets the size of the body of the response from a URL
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

