#!/bin/python3

import sys

n = int(str(input()).strip())
a = list(map(int, str(input()).strip().split(' ')))


class BubbleSort:
    def process(self, n, a):
        total_swaps = 0
        array_length = len(a)

        for i in range(0, array_length):
            num_swaps = 0

            for j in range(0, array_length - 1):
                if a[j] > a[j+1]:
                    self.swap(a, j, j + 1)
                    num_swaps += 1

            total_swaps += num_swaps

            if num_swaps == 0:
                self.show_results(total_swaps, a[0], a[array_length - 1])
                return

    def swap(self, a, first, second):
        a[first], a[second] = a[second], a[first]

    def show_results(self, num_swaps, first, last):
        print("Array is sorted in %s swaps." % num_swaps)
        print("First Element: %s" % first)
        print("Last Element: %s" % last)

sorter = BubbleSort()
sorter.process(n, a)
