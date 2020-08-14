# baekjoon 7568 (브루트포스)

import sys

n = int(sys.stdin.readline())
myLi=[]

for _ in range(n):
    myLi.append(tuple(map(int, sys.stdin.readline().split())) )

for i in myLi:
    count=1
    for j in myLi:
        if i[0] < j[0] and i[1] < j[1]:
            count +=1
    print(count, end=' ')