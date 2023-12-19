#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics."""

import sys


def process_log(log_lines):
    """Process log lines, compute and print statistics."""
    allowed_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                         '404': 0, '405': 0, '500': 0}

    total_size = 0
    count = 0

    for line in log_lines:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in allowed_codes:
                allowed_codes[status_code] += 1

            total_size += file_size

            count += 1

        if count == 10:
            print_statistics(total_size, allowed_codes)
            count = 0

    print_statistics(total_size, allowed_codes)


def print_statistics(total_size, allowed_codes):
    """Print total file size and number of lines for each status code."""
    print('File size: {}'.format(total_size))

    for key, value in sorted(allowed_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


def main():
    """Main entry point for the script."""
    try:
        process_log(sys.stdin)
    except Exception as err:
        pass


if __name__ == "__main__":
    main()
