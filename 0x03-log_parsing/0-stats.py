#!/usr/bin/python3
import sys
import signal


def print_stats():
    print("File size: {}".format(file_size))
    for key in sorted(stats.keys()):
        if stats[key] > 0:
            print("{}: {}".format(key, stats[key]))


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
             "405": 0, "500": 0}
    file_size = 0
    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                size = int(parts[-1])
                code = parts[-2]
                if code in stats:
                    stats[code] += 1
                file_size += size
                count += 1
                if count % 10 == 0:
                    print_stats()
            except ValueError:
                pass
    finally:
        print_stats()
