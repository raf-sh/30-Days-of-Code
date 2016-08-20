#!/bin/python3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())

if 2 <= n <= 12:
    print(factorial(n))
