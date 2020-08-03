#Beakjoon 9020
import sys

def goldbah(a):
    primeLi=[]
    for i in range(2,a):
        isPrime = True
        for j in range(2,int(i**(1/2))+1 ):
            if i%j==0:
                isPrime = False
                break
        if isPrime:
            primeLi.append(i)

    for m in primeLi:
        if m <= a-m:
            if (a - m) in primeLi:
                gold1 = m
                gold2 = a -m
                
        else :
            print(f'{gold1} {gold2}')
            return

t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())
    goldbah(num)