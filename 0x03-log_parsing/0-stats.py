#!/usr/bin/python3
"""
script read stdin and return spacific out put
"""
import sys


def print_metrics(fsize=int, scode=dict) -> str:
    """
    function to print totalfilesize, statuscodes in ascending order
    """
    print("File size: {}".format(fsize))
    for code in sorted(scode.keys()):
        if scode[code] > 0:
            print("{}: {}".format(code, scode[code]))


status_count = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, '405': 0, "500": 0}
total_size = 0

try:
    for i, line in enumerate(sys.stdin, start=1):
        pline = line.strip().split()
        if pline != 7:
            continue
        try:
            file_size = int(pline[-1])

            code = pline[-2]
        except ValueError:
            pass
        total_size += file_size
        if code in status_count:
            status_count[code] += 1

        if i % 10 == 0:
            print_metrics(total_size, status_count)
            total_size = 0
except KeyboardInterrupt:
    print_metrics(total_size, status_count)
    raise
print_metrics(total_size, status_count)
