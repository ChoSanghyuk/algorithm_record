# 피보나치 (스터디)
def solution(n):
    pibo = [0,1]
    while len(pibo) < n+1:
        le = len(pibo)
        pibo.append(pibo[le-1]+pibo[le-2])
    return pibo[n]%1234567