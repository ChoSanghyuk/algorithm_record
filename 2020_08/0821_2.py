# stress 구하기(class)

import sys

workLi = list(map(int, sys.stdin.readline().split()))
time = int(sys.stdin.readline())


for _ in range(time):
    workLi.sort(reverse=True)
    workLi[0] -=1

stress = [i**2 for i in workLi]

print(sum(stress))

##################################
# 힙 알고리즘

import heapq
import sys

def fatigue(works, n):
    maxH = []
    for i in works:
        heapq.heappush(maxH, -i)
    while n >0:
        f = -heapq.heappop(maxH) -1
        print(f)
        if f == -1:
            return 0
        heapq.heappush(maxH, -f)
        n -=1
    result =0
    for i in maxH:
        result += f**2
    return result

if __name__ == "__main__":
    print(fatigue([3,3,4], 4))