#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""

import sys
from collections import defaultdict
import signal

# Initialize variables
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

def print_statistics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()

        # Extract status code and file size from the input line
        parts = line.split(" ")
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update total file size
        total_file_size += file_size

        # Update status code counts
        status_code_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Keyboard interruption occurred, print final statistics
    print_statistics()

