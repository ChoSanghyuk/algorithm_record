#Baekjoon 4153

def isRt(x, y, z):
    tLi = [x, y, z]
    tLi.sort(reverse=True)
    if tLi[0]**2 == (tLi[1]**2 + tLi[2]**2):
        print("right")
    else:
        print("wrong")
    return

while True:
    a,b,c = map(int, input().split())
    if a+b+c ==0:
        break
    isRt(a,b,c)
