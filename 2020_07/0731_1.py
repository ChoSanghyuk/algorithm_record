#제곱근 구하기

import math

def solution(n):
    s = math.sqrt(n)

    if(int(s) == s):
        answer = (s+1)**2
    else:
        answer = -1

    return answer

# s= n**(1/2)
# if s % 1 == 0 : 정수