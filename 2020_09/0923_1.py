 # 프로그래머스 (방문길이)
 
def solution(dirs):
    point = [0,0] ; past = [0,0]
    path = []
    count = 0
    for i in dirs:
        if i =="L":
            if point[0] == -5:
                continue
            point[0] -=1
        if i =="R":
            if point[0] == 5:
                continue
            point[0] +=1
        if i =="U":
            if point[1] == 5:
                continue
            point[1] +=1
        if i =="D":
            if point[1] == -5:
                continue
            point[1] -=1
        if [point, past] in path or [past, point] in path:
            past = point.copy()
            continue
        path.append([past.copy() , point.copy()])
        past = point.copy()
        count += 1
    return count