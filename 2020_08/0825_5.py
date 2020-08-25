#baekjoon 10814 (정렬)

import sys

n = int(sys.stdin.readline())
myLi = []

for _ in range(n):
    myLi.append(sys.stdin.readline()[:-1].split())

for i in myLi:
    i[0] = int(i[0])

myLi_s = sorted(myLi, key= lambda x :x[0])

for i in myLi_s:
    print(f'{i[0]} {i[1]}')