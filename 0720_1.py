#Baekjoon 10250
i = int(input())

for _ in range(i):
    H, W, N = map(int, input().split())

    list=[]

    for w in range(1,W+1):
        for h in range(1, H+1):
            h_s = str(h)
            if w <10:
                w_s = '0'+str(w)
            else:
                w_s = str(w)
            list.append(h_s+w_s)
    print(list[N-1])
