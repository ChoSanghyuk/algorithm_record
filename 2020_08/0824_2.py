# 숫자의 표현(스터디)

def solution(n):
    if n%2==0:
        answer = 0
    else:
        answer = 1
    for i in range(1,n//2+1,2):
        if n%i==0:
               answer +=1
    return answer