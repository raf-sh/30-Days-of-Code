#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

if 1 <= n <= 1000 and 1 <= len(arr) <= 10000:
    result = ' '.join(str(arrEl) for arrEl in reversed(arr))
    print(result)
else:
    sys.exit()
