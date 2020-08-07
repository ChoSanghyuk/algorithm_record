#체육복 (스터디)

def solution(n, lost, reserve):
    classLi = [1]*n
    for i in lost:
        classLi[i-1] -=1
    for i in reserve:
        classLi[i-1] +=1
    for i in range(len(classLi)-1):
        if classLi[i]==2 and classLi[i+1] ==0:
            classLi[i+1] +=1
            classLi[i] -=1
        if classLi[i]==0 and classLi[i+1] ==2:
            classLi[i+1] -=1
            classLi[i] +=1
        
    return len(list(filter(lambda x : x>0, classLi)))