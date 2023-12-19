#!/usr/bin/python3
"""
Reads stdin line by line, computes metrics, and prints statistics every 10 lines or on keyboard interruption (CTRL + C).
"""

import sys

def process_log_lines():
    """
    Read input lines from stdin, process log lines, and print statistics.
    """
    status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                         '404': 0, '405': 0, '500': 0}

    total_size = 0
    count = 0  # keep count of the number lines counted

    try:
        for line in sys.stdin:
            line_list = line.split(" ")

            if len(line_list) > 4 and line_list[5] == "\"GET" and line_list[7] == "HTTP/1.1\"":
                try:
                    status_code = int(line_list[-2])  # Attempt to convert to integer
                    file_size = int(line_list[-1])

                    # Check if the status code received is valid
                    if str(status_code) in status_codes_dict:
                        status_codes_dict[str(status_code)] += 1

                    total_size += file_size
                    count += 1

                except ValueError:
                    # Handle the case where status code is not an integer
                    pass

            if count == 10:
                # Print out statistics and reset count
                print('Total file size: {}'.format(total_size))
                print('File size: {}'.format(file_size))  # Print size of the last line
                for key, value in sorted(status_codes_dict.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
                        status_codes_dict[key] = 0

                count = 0

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass

    finally:
        # Print final statistics
        print('Total file size: {}'.format(total_size))
        print('File size: {}'.format(file_size))  # Print size of the last line
        for key, value in sorted(status_codes_dict.items()):
            if value != 0:
                print('{}: {}'.format(key, value))

if __name__ == "__main__":
    process_log_lines()
