# 최고의 집합(프로그래머스)

def solution(n, s):
    
    if n > s:
        return [-1]
    answer = []
    for i in range(n , 0, -1):
        answer.append(s//i)
        s -=s//i
    return answer