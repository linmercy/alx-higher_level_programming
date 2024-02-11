#!/usr/bin/python3
from sys import argv

# Sum all command-line arguments after skipping the script name
result = sum(int(arg) for arg in argv[1:])

print(result)

