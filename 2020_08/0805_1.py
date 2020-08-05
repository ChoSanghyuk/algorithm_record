# 찍은거의 정답률 (스터디)
def solution(answers):
    st1 = [1, 2, 3, 4, 5] *(len(answers)//5 +1 )
    st2 = [2, 1, 2, 3, 2, 4, 2, 5] *(len(answers)//8 +1 )
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] *(len(answers)//10 +1 )
    ans1 , ans2, ans3 = 0 ,0, 0
    for i in range(len(answers)):
        if answers[i] == st1[i]:
            ans1 +=1
        if answers[i] == st2[i]:
            ans2 +=1
        if answers[i] == st3[i]:
            ans3 +=1
    st_ans = [ans1, ans2, ans3]
    answer = [j for i,j in zip(st_ans, range(1,4)) if i == max(st_ans) ]
    return answer