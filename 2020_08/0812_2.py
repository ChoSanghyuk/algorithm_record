#baekjoon 11729 재귀
n = int(input())

def hano(n):
    if n ==1:
        return [1, 3]
    else:
        temp1=[1 if i ==1 else 2 if i== 3 else 3 for i in hano(n-1) ]
        temp2=[1 if i ==2 else 2 if i==1 else 3 for i in hano(n-1) ]
      
        return temp1+ [1, 3] + temp2


myli = hano(n)

print(len(myli)//2)
for i in range(0, len(myli),2):
    print(f'{myli[i]} {myli[i+1]}')