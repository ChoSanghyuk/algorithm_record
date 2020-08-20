#baekjoon 2108 (통계)

import sys
import collections

n = int(sys.stdin.readline())
myLi = []


for _ in range(n):
    myLi.append(int(sys.stdin.readline()))

myLi.sort()
mean = sum(myLi)/n
median = (myLi)[n//2]

def freq(myLi):
    counter = dict(collections.Counter(myLi))
    temp = []
    for i in counter.keys():
        if counter[i] == max(counter.values()):
            temp.append(i)
    if len(temp) == 1:
        return temp[0]
    else:
        return sorted(temp)[1]
            

range = max(myLi) - min(myLi)

print(int(round(mean,0)))
print(median)
print(freq(myLi))
print(range)