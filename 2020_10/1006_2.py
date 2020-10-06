# 온코더 2회차 2번
class Solution:
    def solution(self, text):
        length = [len(i) for i in text]
        max_len = max(length)
        answer = []
        for i in text:
            temp = ' '*(max_len - len(i)) + i
            answer.append(temp)
        return answer