#!/usr/bin/python3
'reads stdin line by line and computes metrics'

import re
import sys

if __name__ == '__main__':
    count = total = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (\[.*\])'\
              r' ("GET /projects/260 HTTP/1.1") (\d{3}) (\d+)$'
    try:
        for line in sys.stdin:
            count += 1
            line = line.split()
            try:
                code = int(line[-2])
                if code in codes:
                    codes[code] += 1
            except BaseException:
                pass
            try:
                total += int(line[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print('File size: {:d}'.format(total))
                for key, val in sorted(codes.items()):
                    if val > 0:
                        print('{}: {}'.format(key, val))
    except KeyboardInterrupt:
        print('File size: {:d}'.format(total))
        for key, val in codes.items():
            if val > 0:
                print('{}: {}'.format(key, val))
        raise
