#!/usr/bin/python3
"""
0-stats
"""
import sys


def print_stats(total_size, sts_codes):
    """
    reads stdin line by line and computes metrics
    """
    print("File size: {}".format(total_size))
    for sts in sorted(sts_codes.keys()):
        if sts_codes[sts] != 0:
            print("{}: {}".format(sts, sts_codes[sts]))


sts_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
             404: 0, 405: 0, 500: 0}
line_count = 0
total_size = 0
try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_stats(total_size, sts_codes)
        parts = line.split()
        line_count += 1
        try:
            total_size += int(parts[-1])
        except ValueError:
            pass
        try:
            sts_code = int(parts[-2])
            if sts_code in sts_codes:
                sts_codes[sts_code] += 1
        except ValueError:
            pass

except KeyboardInterrupt:
    print_stats(total_size, sts_codes)
    raise
