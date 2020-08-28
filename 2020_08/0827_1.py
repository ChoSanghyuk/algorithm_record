# Baekjoon 15650 (백트래킹)

import sys

n, m = map(int, sys.stdin.readline().split())

myLi = [[i] for i in range(1,n-m+2)]

for _ in range(m-1):
    temp=[]
    for i in range(len(myLi)):
        temp += [ myLi[i] + [j] for j in range(1,n+1) if j > max(myLi[i]) ]
    myLi = temp

for i in myLi:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()