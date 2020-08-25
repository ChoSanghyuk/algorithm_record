# 백준 11650 (정렬)

import sys

n = int(sys.stdin.readline())
myLi = []

for _ in range(n):
    myLi.append(list(map(int, sys.stdin.readline().split())))

myLi_s = sorted(myLi, key = lambda x: (x[0], x[1]))

for i in myLi_s:
    print(i[0], i[1])