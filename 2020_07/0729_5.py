# 행렬의 합(스터디)

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j]  = arr1[i][j] + arr2[i][j]

    return arr1


# def arraySum(A,B):
#     answer = [[c+d for c,d in zip(a,b)] for a,b in zip(A,B)]
#     return answer