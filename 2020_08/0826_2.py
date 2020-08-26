# 멀리뛰기(프로그래머스, 스터디)

def combi(a,b):
    A=1; B=1
    for i in range(b):
        A *= a-i
    for i in range(1,b+1):
        B *= i
    return A//B
print(combi(4,3))
    
def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        answer += combi(n-i,i)
    return answer % 1234567