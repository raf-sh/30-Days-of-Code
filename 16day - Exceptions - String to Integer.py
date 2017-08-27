#!/bin/python3

import sys


def print_int_from_string(string):
    try:
        print(int(string))
    except Exception:
        print("Bad String")


print_int_from_string(input().strip())
