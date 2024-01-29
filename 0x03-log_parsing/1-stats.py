#!/usr/bin/python3
"""
script read stdin and return spacific out put
"""
import sys
import re


def print_metrics(fsize=int, scode=dict) -> str:
    """
    function to print totalfilesize, statuscodes in ascending order
    """
    print("File size: {}".format(fsize))
    for code in sorted(scode.keys()):
        if scode[code] > 0:
            print("{}: {}".format(code, scode[code]))

def regex_match(input_text):
    """ match input line with spacefic format"""
    pattern = re.compile(r'^(\d{1,3}(\.\d{1,3}){3}) - (.*?) "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
    return pattern.match(input_text)


status_count = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, '405': 0, "500": 0}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        matched = regex_match(line)
        if matched:
            if count == 10:
                print_metrics(total_size, status_count)
                count = 0
            try:
                total_size += int(matched.group(5))
                code = matched.group(4)
                if code in status_count:
                    status_count[code] += 1
            except (ValueError, IndexError):
                    continue

    print_metrics(total_size, status_count)

except KeyboardInterrupt:
    print_metrics(total_size, status_count)
    raise
