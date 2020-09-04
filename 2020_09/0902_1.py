# 구명보트 (프로그래머스)

def solution(people, limit):
    people.sort()
    count = 0
    i=0 ; j =len(people) -1
    while i <=j:
        count +=1
        if people[i] + people[j] <=limit:
            i +=1
        j -=1
    return count