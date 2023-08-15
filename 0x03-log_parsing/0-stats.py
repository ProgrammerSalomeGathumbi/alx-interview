#!/usr/bin/python3
"""
0-stats
"""
import sys


def print_stats(total_file_size, sts_code_counts):
    """
    reads stdin line by line and computes metrics
    """
    print("File size: {}".format(total_file_size))
    for sts_code in sorted(sts_code_counts.keys()):
        count = sts_code_counts[sts_code]
        if count != 0:
            print("{:d}: {:d}".format(sts_code, count))


total_file_size = 0
sts_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
              404: 0, 405: 0, 500: 0}
line_count = 0
try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_stats(sts_counts, total_file_size)
        parts = line.split()
        line_count = 0
        try:
            total_file_size += int(parts[-1])
        except ValueError:
            pass
        try:
            if parts[-2] in sts_counts:
                sts_counts[parts[-2]] += 1
        except ValueError:
            pass
except KeyboardInterrupt:
    print_stats(total_file_size, sts_counts)
    raise
