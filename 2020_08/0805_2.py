# 완수하지 못한 선수(스터디)

from collections import Counter
def solution(a, b):
    c = Counter(a) ; d = Counter(b)
    for i in set(a):
        if c[i] != d[i]:
            return i