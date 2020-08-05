#Baekjoon 2839
num = int(input())
i = 0
count=0 
while num-3*i>=0:
    if (num - 3*i)%5==0:
        count = i + ((num - 3*i)//5)
        break
    i +=1
if count != 0:
    print(count)
else:
    print(-1)