#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime
import re

total_size = 0
status_codes = {}

def print_stats():
    global total_size, status_codes
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

try:
    count = 0
    for line in sys.stdin:
        count += 1
        match = re.match(r"^(\S+) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)$", line)
        if match:
            ip, date, status, size = match.groups()
            total_size += int(size)
            status_codes[int(status)] = status_codes.get(int(status), 0) + 1
        if count == 10:
            print_stats()
            count = 0
except KeyboardInterrupt:
    print_stats()

