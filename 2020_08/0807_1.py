#정렬 (수업)

def mysort(a):
    sorted=[]
    while len(a):
        for i in a:
            temp = list(filter(lambda x : x<i, a))
            if len(temp):
                pass
            else:
                sorted.append(i)
                a.remove(i)
                break
    return sorted    


print(mysort([2,3,5,4,1]))

