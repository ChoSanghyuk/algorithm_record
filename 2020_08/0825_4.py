#baekjoon 1181 (정렬)

import sys

n = int(sys.stdin.readline())
myLi = []

for _ in range(n):
    myLi.append(sys.stdin.readline()[:-1])


myLi_s = sorted(set(myLi), key= lambda x :(len(x), x))

for i in myLi_s:
    print(i)