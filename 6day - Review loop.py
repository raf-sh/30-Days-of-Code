#!/bin/python3

import sys

n = int(input().strip())

if 1 <= n <= 10:

    testCases = []
    for i in range(1, n+1):
        userInput = str(input().strip())
        if 2 <= len(userInput) <= 10000:
            userInput = list(userInput)
            testCases.append(''.join(userInput[::2]) + ' ' + ''.join(userInput[1::2]))
        else:
            sys.exit()

    for x in testCases:
        print(x)
else:
    sys.exit()