# 최소공배수 (스터디)

def solution(arr):
    while len(arr)>1:
        i=0
        while True:
            i +=1
            if arr[0]*i % arr[1] ==0:
                arr[0:2] = [arr[0]*i]
                break
    return arr[0]