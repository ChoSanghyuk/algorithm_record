#baekjoon 2750

import sys

n = int(sys.stdin.readline())
myLi = []

for _ in range(n):
    myLi.append(int(sys.stdin.readline()))


def quikSort(Li):
    if len(Li) <1 :
        return Li
    pivot = Li[0]
    lower = [i for i in Li[1:] if i <= pivot ]
    greater = [i for i in Li[1:] if i > pivot ]

    return quikSort(lower) + [pivot] + quikSort(greater)


for i in quikSort(myLi):
    print(i)
