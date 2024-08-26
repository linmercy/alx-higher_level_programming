# 0x11 Python Network 1

This directory contains Python scripts that interact with HTTP services using `urllib` and `requests`. The tasks range from fetching web pages to handling errors and processing JSON responses.

## Directory Structure

- **0-hbtn_status.py**: Fetches `https://alx-intranet.hbtn.io/status` and displays the body response in a specified format. Uses `urllib`.

- **1-hbtn_header.py**: Takes a URL as an argument, sends a request to it, and displays the value of the `X-Request-Id` header in the response. Uses `urllib` and `sys`.

- **2-post_email.py**: Takes a URL and an email as arguments, sends a POST request with the email as a parameter, and displays the body of the response decoded in UTF-8. Uses `urllib` and `sys`.

- **3-error_code.py**: Takes a URL as an argument, sends a request to it, and displays the body of the response. Manages `urllib.error.HTTPError` exceptions and prints the error code. Uses `urllib` and `sys`.

- **4-hbtn_status.py**: Fetches `https://alx-intranet.hbtn.io/status` and displays the body response in a specified format. Uses `requests`.

- **5-hbtn_header.py**: Takes a URL as an argument, sends a request to it, and displays the value of the `X-Request-Id` header in the response. Uses `requests` and `sys`.

- **6-post_email.py**: Takes a URL and an email as arguments, sends a POST request with the email as a parameter, and displays the body of the response. Uses `requests` and `sys`.

- **7-error_code.py**: Takes a URL as an argument, sends a request to it, and displays the body of the response. Manages HTTP error codes and prints the error code if the status code is greater than or equal to 400. Uses `requests` and `sys`.

- **8-json_api.py**: Takes a letter as an argument, sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter, and processes the JSON response. Handles empty and invalid JSON responses. Uses `requests` and `sys`.

- **10-my_github.py**: Takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user's ID. Uses `requests` and `sys`.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS
- **Python Version**: 3.8.5
- **Packages**: 
  - `urllib` (for some scripts)
  - `requests` (for some scripts)
- **File Requirements**:
  - All scripts should end with a new line.
  - The first line of all scripts should be exactly `#!/usr/bin/python3`.
  - All files must be executable.
  - Files should be tested using `wc` for length.
  - Documentation must be provided for modules, classes, and functions.
  - Use `get` to access dictionary values to avoid exceptions.
  - Documentation should be a real sentence explaining the purpose of the module, class, or method.
  - Code should not be executed when imported (`if __name__ == "__main__":`).

## Usage

To execute the scripts, ensure they are executable by running:

```bash
chmod +x <script_name>

Then run the script with the required arguments:

./<script_name> <arguments>

