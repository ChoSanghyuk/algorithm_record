#Baekjoon 1193
nth = int(input())
i=1
count=0

while True:
    count +=i   
    if count>=nth:
        if i %2!=0:
            print(f'{1+count-nth}/{i-(count-nth)}')
        else:
            print(f'{i-(count-nth)}/{1+count-nth}')
        break
    i +=1
