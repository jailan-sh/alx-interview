#!/usr/bin/python3
"""
script read stdin and return spacific out put 
"""
import sys


total_size = 0
status_count = {}
try:
    for i, line in enumerate(sys.stdin, start=1):
        line = line.split()
        if not line:
            continue
        parts = line.split()
        if parts != 7:
            continue
        try:
            file_size = int(line.strip[-1])
            status_code = int(line.split()[-2])
        except ValueError:
            pass
        total_size += 1
        status_count[status_code] = status_count.get(status_code, 0) + 1

        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_count):
                print("{}: {}".format(code, status_count[code]))
            total_size = 0
            status_count.clear()

except KeyboardInterrupt:
    pass
print("File size: {}".format(total_size))
for code in sorted(status_count):
    print("{}: {}".format(code, status_count[code]))
total_size = 0
status_count.clear()
