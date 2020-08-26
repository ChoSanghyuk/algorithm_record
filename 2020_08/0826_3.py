# 최단거리찾기(수업)

def dis(a,b):
    if a == 1 or b==1:
        return 1
    else:
        return dis(a-1,b) + dis(a,b-1)

def solution(m,n,arr):
    total = dis(m,n)
    cant=0
    for i in arr:
        cant += (dis(i[0], i[1])*dis(m-i[0]+1 , n-i[1]+1))
    return total - cant
