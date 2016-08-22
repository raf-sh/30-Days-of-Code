class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maximumDifference = 0
        for first in range(len(self.__elements)):
            for second in range(len(self.__elements)):
                difference = self.__elements[first] - self.__elements[second]
                if maximumDifference < difference:
                    maximumDifference = difference
        self.maximumDifference = maximumDifference

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)