#!/usr/bin/python3
"""
0-stats
"""
import sys


def print_stats(total_size, status):
    """
    reads stdin line by line and computes metrics
    """
    print("File size: {}".format(total_size))
    for sts in sorted(status.keys()):
        if status[sts] != 0:
            print("{}: {}".format(sts, status[sts]))


codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
             404: 0, 405: 0, 500: 0}
count = 0
size = 0
try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_stats(size, codes)
        parts = line.split()
        count += 1
        try:
            size += int(parts[-1])
        except ValueError:
            pass
        try:
            code = int(parts[-2])
            if code in codes:
                codes[code] += 1
        except ValueError:
            pass

except KeyboardInterrupt:
    print_stats(size, codes)
    raise
