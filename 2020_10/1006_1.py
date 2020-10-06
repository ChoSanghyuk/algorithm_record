# 온코더 2회차 1번
class Solution:
    def solution(self, prices):
        prices = list(set(prices))
        if len(prices) < 3:
            return -1
        else:
            prices.sort()
            return prices[2]