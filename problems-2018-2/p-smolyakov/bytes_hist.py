#!/usr/bin/env python3
import sys


def bytes_hist():
    byte_counts = {}
    bytes_amount = 0

    for byte in range(128, 256):
        byte_counts[byte] = 0

    chunk_size = 4096
    while True:
        try:
            chunk = sys.stdin.buffer.read(chunk_size)
        except KeyboardInterrupt:
            print('Interrupted', file=sys.stderr)
            sys.exit(1)
        except BaseException as e:
            print(f'Met {repr(e)} while reading from stdin, exiting', file=sys.stderr)
            sys.exit(1)

        if not chunk:
            break

        for byte in chunk:
            if 128 <= byte <= 255:
                byte_counts[byte] += 1
                bytes_amount += 1

    return byte_counts, bytes_amount


if __name__ == '__main__':
    counts, amount = bytes_hist()
    print('Statistics:')
    for byte, count in sorted(filter(lambda pair: pair[1] > 0, counts.items()), key = lambda pair: -pair[1]):
        print(f'{hex(byte)} :: {count * 100 / amount:5.2f}% ({count})')

    print(f'ALL  :: 100.0% ({amount})')
