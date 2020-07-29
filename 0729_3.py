# 주사위 경우의 수(수업)
sum = int(input())
dice = range(1,7)
caseLi = []
count =0

for i in dice:
    if sum - i in dice:
        caseLi.append([i,sum-i])
        count +=1

print([count,caseLi])