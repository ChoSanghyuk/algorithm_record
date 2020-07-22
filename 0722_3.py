#Baekjoon 1011
def howMany():
    x , y = map(int, input().split())
    count=0
    p=1
    switch =0

    while True:
        d= y-x
        if d == p:
            count+=1
            print(count)
            break
        elif d >p:
            if switch %2 ==0:
                y-=p
                count+=1
                switch +=1
            else:
                x+=p
                p+=1
                count+=1
                switch +=1
        else:
            count +=1
            print(count)
            break

t = int(input())
for _ in range(t):
    howMany()