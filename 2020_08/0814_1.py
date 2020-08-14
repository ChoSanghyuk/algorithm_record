# baekjoon 2798 (브루트 포스)

n , m= map(int, input().split())
myLi = list(map(int, input().split()))
myLi.sort(reverse = True)
Le = len(myLi)

answer = [ myLi[i]+ myLi[j] +myLi[k] for i in range(0,Le-2) if myLi[i] < m
           for j in range(i+1,Le-1) if myLi[i]+myLi[j] <m  for k in range(j+1,Le) if myLi[i]+ myLi[j] +myLi[k] <=m ]


print(max(answer))