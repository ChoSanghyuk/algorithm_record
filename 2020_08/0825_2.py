# 최대 최소 (스터디)
def solution(s):
    myLi = list(map(int, s.split()))
    return str(min(myLi))+' '+ str(max(myLi))