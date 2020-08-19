#baekjoon 1018(브루트포스)
import sys

m,n = map(int,sys.stdin.readline().split())
chess = []
countLi = []

for _ in range(m):
    chess.append([i for i in sys.stdin.readline()[:-1]])



for t in range(0, m-7):
    for k in range(0, n-7):
        count=0
        for i in range(t, t+8):
            for j in range(k, k+8):
                if i%2 ==0:
                    if j%2 ==0:
                        if chess[i][j] != 'W': count +=1
                    else :
                        if chess[i][j] != 'B': count +=1
                else:
                    if j%2 ==0:
                        if chess[i][j] != 'B': count +=1
                    else :
                        if chess[i][j] != 'W': count +=1
        countLi.append(min(count, 64-count))

print(min(countLi))