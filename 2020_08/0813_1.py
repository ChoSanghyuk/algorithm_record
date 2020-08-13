# baekjoon 15649 (재귀)
m , n= map(int, input().split())

def makeArray(m,n):
    if n ==1:
        return [[i+1] for i in range(m)]
    else:
        pre = makeArray(m, n-1)
        answer = []
        for i in pre:
            for j in range(1,m+1):
                if j not in i:
                    temp = i.copy()
                    temp.append(j)
                    answer.append(temp)
                else:
                    pass
        return answer

myli = makeArray(m,n)

for i in myli:
    for j in i:
        print(j, end=' ')
    print()