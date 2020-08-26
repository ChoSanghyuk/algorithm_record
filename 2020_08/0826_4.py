# 줄세우기 (수업)

def knt(n,k):
    myLi = [[i] for i in range(1,n+1)]
    for _ in range(n-1):
        temp = []
        for i in range(len(myLi)):
            temp += [myLi[i] +[j] for j in range(1,n+1) if j not in myLi[i] ]
        myLi = temp
    return myLi[k]