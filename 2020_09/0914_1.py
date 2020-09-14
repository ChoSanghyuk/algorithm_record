# 땅따먹기 (프로그래머스)
def solution(land):
    b_max1 , b_max2 = 0,0
    b_index1 , b_index2 = -1,-1
    for i in land:
        nmax1 = max(i) ; nmax2 = sorted(i)[-2]
        nindex1 = i.index(nmax1) ; nindex2 = i.index(nmax2)
        for j in range(len(i)):
            if j != b_index1:
                i[j] += b_max1
            else:
                i[j] += b_max2
        b_max1 , b_max2 =  max(i) , sorted(i)[-2]
        b_index1 , b_index2 = i.index(b_max1) , i.index(b_max2)

    return b_max1