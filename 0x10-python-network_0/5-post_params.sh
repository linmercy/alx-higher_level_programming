#!/bin/bash
# This script sends a POST request with email and subject parameters and displays the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

