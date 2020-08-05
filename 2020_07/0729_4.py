# Baekjoon 
import math
while True:
    num = int(input())
    if num ==0:
        break
    count = 0
    for i in range(num+1, 2*num+1):
        isPrime = True
        if i ==1:
            continue
        if i ==2:
            count +=1
        for j in range(3,int(math.sqrt(i))+1,2):
            if i%j==0:
                isPrime = False
                break
        if isPrime:
            count+=1
    print(count)