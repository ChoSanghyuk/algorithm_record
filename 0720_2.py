#Baekjoon 2775
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    peoList=[]

    for i in range(1,n+1):
        peoList.append(i)

    for i in range(1, k+1):
        sum=0
        for j in range(1, n+1):
            sum +=peoList[j-1]
            peoList[j-1] = sum
            
    print(peoList[n-1])