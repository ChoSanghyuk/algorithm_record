# 주식가격 하락이 발생 되기 전의 유지 시간 계산

stock = list(map(int, input().split()))
fallTime = []

for i in range(len(stock)):
    count=0
    for j in range(i+1 , len(stock)):
        if stock[i]<=stock[j]:
            count+=1
        else:
            count+=1
            fallTime.append(count)
            break
        if j == len(stock)-1:
            fallTime.append(count)
        
fallTime.append(0)

print(fallTime)

## count를 하지 말고 j-i 를 이용하면 if 하나만 사용해서 만들 수 있었음.