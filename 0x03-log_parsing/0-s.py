#!/usr/bin/python3
'reads stdin line by line and computes metrics'

import re
import sys

if __name__ == '__main__':
    count = total = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (\[.*\])'\
              r' ("GET /projects/260 HTTP/1.1") (\d{3}) (\d+)$'

    def print_stats(stats: dict, total: int) -> None:
        '''prints stat'''
        print("File size: {:d}".format(total))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))
    try:
        for line in sys.stdin:
            line = line.rstrip()
            match = re.fullmatch(pattern, line)
            if not match:
                continue
            code, fs = match.groups()[-2], match.groups()[-1]
            count += 1
            total += int(fs)
            code = int(code)
            if code not in codes:
                continue
            codes[code] += 1
            if count % 10 == 0:
                print_stats(codes, total)
        print_stats(codes, total)
    except KeyboardInterrupt:
        print_stats(codes, total)
        raise
