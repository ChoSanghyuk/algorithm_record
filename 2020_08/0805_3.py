#baekjoon 1002
def case(x1, y1, r1, x2, y2, r2):
    d= ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if x1==x2 and y1==y2 and r1==r2:
        return -1 
    if d > r1+r2:
        return 0
    elif d==r1+r2:
        return 1
    elif r1+r2 > d > abs(r1-r2):
        return 2
    elif d == abs(r1-r2):
        return 1
    else:
        return 0

t = int(input())

for _ in range(t):
    a,b,c,d,e,f = map(int, input().split())
    print(case(a,b,c,d,e,f))