# 온코더 2회차 3번
class Solution:
    def solution(self, sequence):
        answer = sorted(sequence, key = lambda x : int(x))
        return answer