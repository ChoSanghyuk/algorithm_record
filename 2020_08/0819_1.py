# 스터디 (문자 정렬)

import collections

a = 'asdfwedfasd'

def most(st):
    result = []
    hMany = dict(collections.Counter(st))
    for i in sorted(set(hMany.values()), reverse = True):
        temp = []
        for j in hMany.keys():
            if hMany[j] == i:
                temp.append(j)
        temp.sort()
        result += temp
                
    return ''.join(result)

print(most(a))

# ****************************************

def hashT(string):
    result = sorted(collections.Counter(string).items(), key= lambda x : x[0])
    result = sorted(result, key= lambda x:x[1], reverse = True)
    return ''.join([i for i,j in result ])