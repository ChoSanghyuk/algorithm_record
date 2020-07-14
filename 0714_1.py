#Baekjoon 2292
i =0
a = int(input())
while True :
    i += 1
    if a ==1:
        print(1)
        break
    if 3*i*(i-1)+2 <= a < 3*i*(i+1) +2:
        print(i+1)
        break