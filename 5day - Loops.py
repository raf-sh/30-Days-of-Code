#!/bin/python3

import sys


N = int(input().strip())

if 2 <= N <= 20:
    for i in range(1, 11):
        print('{} x {} = {}'.format(N, i, N * i))
else:
    sys.exit()
