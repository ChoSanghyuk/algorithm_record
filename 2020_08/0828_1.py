#점프와 순간이동 (프로그래머스)

def solution(n):
    a= bin(n)[2:]
    return sum([int(i) for i in a])