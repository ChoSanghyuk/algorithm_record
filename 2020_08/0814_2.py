#baekjoon 2231 (브루트 포스)

import sys

n = int(sys.stdin.readline())

def func(n):
    Le = len(str(n))-1
    for i in range(n-Le*9, n):
        if i + sum((int(j) for j in str(i))) == n:
            return i
    return 0

print(func(n))