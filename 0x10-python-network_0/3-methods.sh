#!/bin/bash
# This script displays all HTTP methods the server will accept for a given URL
curl -s -I "$1" | grep -i "Allow:" | sed 's/Allow: //I'

