#!/usr/bin/python3
import sys

def print_statistics(total_size, status_codes):
    """
    Print statistics based on total file size and status code counts.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing status code counts.
    """
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                ip, _, _, status_code, file_size = line.split()[0], line.split()[8], line.split()[10], int(line.split()[13]), int(line.split()[14])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()

