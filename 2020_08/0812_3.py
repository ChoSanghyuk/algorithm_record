# 비밀지도 (스터디)

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i])[2:]
        a = '0'*(n-len(a)) + a
        b = bin(arr2[i])[2:]
        b = '0'*(n-len(b)) +b

        temp=''
        for j in range(n):
            if a[j]=='1' or b[j]=='1':
                temp +='#'
            else:
                temp +=' '
        answer.append(temp)

    return answer