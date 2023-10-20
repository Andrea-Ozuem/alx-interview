#!/usr/bin/python3
'reads stdin line by line and computes metrics'

import re
import sys

count = total = 0
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (\[.*\])'\
          r' ("GET /projects/260 HTTP/1.1") (\d{3}) (\d+)$'

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
            # print stat
            print('File size: {:d}'.format(total))
            for key, val in codes.items():
                if val > 0:
                    print('{}: {}'.format(key, val))
except KeyboardInterrupt:
    # print stat
    print('File size: {:d}'.format(total))
    for key, val in codes.items():
        if val > 0:
            print('{}: {}'.format(key, val))
    raise
