#!/bin/python3

import sys


arr = []
#for arr_i in range(6):
   #arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   #arr.append(arr_t)

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
maxHourglass = 0
totals = []
for x in range(0, 4):
    for y in range(0, 4):
        sumHourglass = (arr[x][y] + arr[x][y + 1] + arr[x][y + 2]) + arr[x+1][y+1] + (arr[x+2][y] + arr[x+2][y + 1] + arr[x+2][y + 2])
        totals.append(sumHourglass)
print(max(totals))
