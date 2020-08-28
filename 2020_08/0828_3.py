# 기능개발(프로그래머스)
import math

def solution(progresses, speeds):
    myLi = [ math.ceil((100-i)/j) for i, j in zip(progresses, speeds) ]
    count = []
    j =0
    for i in range(len(myLi)):
        if myLi[i] >myLi[j]:
            count.append(i-j)
            j=i
        if i ==len(myLi)-1:
            if i==j:
                count.append(1)
            else:
                count.append(i-j+1)
    return count