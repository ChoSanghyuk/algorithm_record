# 카펫(프로그래머스)

def solution(brown, yellow):
    total = brown + yellow
    totalLi = [] ; yellLi = []
    for i in range(2,total//2) :
        if total % i ==0 and total//i >= i :
            totalLi.append([total//i, i])
    
    for i in range(1,yellow+1):
        if yellow % i ==0 and yellow//i >= i :
            yellLi.append([yellow//i, i])
    
    for i in totalLi:
        for j in yellLi:
            if i[0] >j[0]+1 and i[1] > j[1]+1:
                return i