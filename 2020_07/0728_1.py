import math

def primeNum(a):
    if a==1:
        return False
    else:
        sqrt = int(math.sqrt(a))
        for i in range(2,sqrt+1):
            # print(a , a%i)
            if a % i ==0:
                return False
        return True

M, N = map(int, input().split())
for n in range(M,N+1):
    if primeNum(n):
        print(n)