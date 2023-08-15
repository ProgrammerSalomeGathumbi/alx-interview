#!/usr/bin/python3
"""
0-stats
"""
import sys


def parse_line(line):
    """
    Parses a log line and extracts status code and file size
    """
    parts = line.split()
    if len(parts) != 9:
        return None, None
    try:
        sts_code = int(parts[-2])
        file_size = int(parts[-1])
        return sts_code, file_size
    except ValueError:
        return None, None


def print_stats(total_size, sts_codes):
    """
    Prints statistics for status codes and total file size
    """
    print("File size: {}".format(total_size))
    for sts in sorted(sts_codes.keys()):
        count = sts_codes[sts]
        if count != 0:
            print("{}: {}".format(sts, count))


def main():
    # Dictionary to store status code counts
    sts_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                 404: 0, 405: 0, 500: 0}
    line_count = 0
    total_size = 0

    try:
        for line in sys.stdin:
            # Parse the line and extract status code and file size
            sts_code, file_size = parse_line(line)
            if sts_code is not None and file_size is not None:
                total_size += file_size
                if sts_code in sts_codes:
                    sts_codes[sts_code] += 1

                line_count += 1
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, sts_codes)
        # Print final stats
        print_stats(total_size, sts_codes)

    except KeyboardInterrupt:
        # Print stats in case of interruption
        print_stats(total_size, sts_codes)
        raise


if __name__ == "__main__":
    main()
