# 스킬트리 (프로그래머스) 
def solution(skill, skill_trees):
    count = 0
    for i in skill_trees:
        isFollow = True
        temp = [j for j in i if j in skill]
        for k in range(len(temp)):
            if temp[k] != skill[k]:
                isFollow = False
        if isFollow:
            count += 1
    return count