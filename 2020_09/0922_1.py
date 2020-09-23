# 프로그래머스 (등굣길)
def solution(m,n,arr):
    N_way = [[0 for _ in range(m)] for a in range(n) ]
            
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                N_way[i][j] = 1
            elif [j+1, i+1] in arr:
                N_way[i][j] = 0
            elif i ==0:
                N_way[i][j] = N_way[i][j-1]
            elif j ==0:
                N_way[i][j] = N_way[i-1][j]            
            else:
                N_way[i][j] = N_way[i-1][j] + N_way[i][j-1]
    return N_way[n-1][m-1] % 1000000007