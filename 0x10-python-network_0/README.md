# 0x10 Python Network 0

This directory contains a collection of Bash and Python scripts related to network operations and HTTP requests. The scripts are designed to perform various tasks involving HTTP requests using `curl`, as well as Python functions for technical interview preparation.

## Directory Structure

- **0-body_size.sh**: A Bash script that takes a URL, sends a request to it, and displays the size of the response body in bytes.

- **1-body.sh**: A Bash script that sends a GET request to a URL and displays the body of the response if the status code is 200.

- **2-delete.sh**: A Bash script that sends a DELETE request to a URL and displays the body of the response.

- **3-methods.sh**: A Bash script that takes a URL and displays all HTTP methods the server will accept.

- **4-header.sh**: A Bash script that sends a GET request to a URL with a custom header (`X-School-User-Id: 98`) and displays the body of the response.

- **5-post_params.sh**: A Bash script that sends a POST request with specific parameters (`email` and `subject`) and displays the body of the response.

- **6-peak.py**: A Python function that finds a peak in a list of unsorted integers. The script includes a function `find_peak(list_of_integers)` and its complexity analysis in `6-peak.txt`.

- **6-peak.txt**: Contains the complexity of the `find_peak` algorithm.

- **100-status_code.sh**: A Bash script that sends a request to a URL and displays only the status code of the response.

- **101-post_json.sh**: A Bash script that sends a JSON POST request to a URL using the contents of a file and displays the body of the response.

- **102-catch_me.sh**: A Bash script that makes a request to `0.0.0.0:5000/catch_me` to get a response with "You got me!" in the body.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Tested on Ubuntu 20.04 LTS
- **Bash Scripts**: Should be exactly 3 lines long, executable, and start with `#!/bin/bash`
- **Python Scripts**: Should use Python 3.8.5, follow PEP 8 style guide, and be documented
- **Documentation**: Include explanations for modules, classes, and functions

## Testing

Each script is tested using a sandbox environment with a web server running on port 5000. Ensure that the scripts meet the specified requirements and functionality before submission.

## Usage

To execute the scripts, make them executable with the following command:

```bash
chmod +x <script_name>
Then run the script using:

./<script_name> <arguments>

