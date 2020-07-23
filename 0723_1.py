#Baekjoon 1978

n = int(input())
count =0
myList = list(map(int, input().split()))

for i in myList:
    isPrime =0
    if i ==1:
        pass
    elif i ==2:
        count +=1
    else:
        for j in range(2,i):
            if i%j == 0:
                isPrime +=1                
        if isPrime ==0:
            count +=1

print(count)