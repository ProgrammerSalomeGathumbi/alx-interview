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
        if count > 0:
            print("{}: {}".format(sts_code, count))


total_file_size = 0
sts_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                   404: 0, 405: 0, 500: 0}
line_count = 0
try:
    for line_number, line in enumerate(sys.stdin, start=1):
        ip, _, _, _, _, _, _, sts_code_str, f_size_str = line.split()
        try:
            sts_code = int(sts_code_str)
            file_size = int(f_size_str)
        except ValueError:
            continue
        total_file_size += file_size
        sts_code_counts[sts_code] += 1
        line_count += 1

        if line_count == 10:
            print_stats(total_file_size, sts_code_counts)
            line_count = 0
except KeyboardInterrupt:
    print_stats(total_file_size, sts_code_counts)
