# 폰켓몬(프로그래머스)

import collections

def solution(nums):
    myDict = dict(collections.Counter(nums))
    if len(myDict.keys()) > len(nums)//2:
        return len(nums)//2
    else:
        return len(myDict.keys())