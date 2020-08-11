#baekjoon 11729
n = int(input())

def hano(n):
    if n ==1:
        return [1, 3]
    else:
        temp1=[]
        for i in hano(n-1):
            if i ==2:
                temp1.append(3)
            elif i ==3:
                temp1.append(2)
            else:
                temp1.append(1)
        temp2=[]
        for i in hano(n-1):
            if i ==2:
                temp2.append(1)
            elif i ==3:
                temp2.append(3)
            else:
                temp2.append(2)
        
        return temp1+ [1, 3] + temp2

myli = hano(n)

print(len(myli)//2)
for i in range(0, len(myli),2):
    print(f'{myli[i]} {myli[i+1]}')