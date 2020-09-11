# 최단거리 도시 (수업)

def func(N, M, K, X):
    road = []
    for _ in range(M):
        road.append(list(map(int, input().split())))
    my_road = [i for i in road if i[0]==X]
    not_shortest = []
    
    for _ in range(K-1):
        temp = my_road.copy()
        not_shortest += [i[-1] for i in temp]
        my_road = []
        for i in temp:
            for j in road:
                if i[-1] == j[0]:
                    my_road.append(i+[j[-1]])
    print(not_shortest)
    return [i[-1] for i in my_road if i[-1] not in not_shortest]