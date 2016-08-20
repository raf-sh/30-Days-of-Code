#!/bin/python3

# import sys
#
# n = int(input().strip())
# bin_n = "{0:b}".format(n)
# if 1 <= n <= 10**6:
#     numbers = []
#
#     while n > 0:
#         a = int(n % 2)
#         numbers.append(a)
#         n = (n - a) / 2
#
#     numbers.reverse()
#
#     serial = 0
#     finalSerial = 0
#     for i in numbers:
#         if int(i) == 1:
#             serial += 1
#         else:
#             if serial > finalSerial:
#                 finalSerial = serial
#             serial = 0
#     consecutives = [d for d in bin_n.split('0') if d]
#     print(bin_n)
#     print(finalSerial)
#     print(len(max(consecutives)))
# else:
#     sys.exit('wrong input number')


n = int(input().strip())
bin_n = "{0:b}".format(n)

consecutives = [d for d in bin_n.split('0') if d]
print(len(max(consecutives)))
