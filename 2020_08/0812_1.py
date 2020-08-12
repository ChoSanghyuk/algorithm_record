# 문자열 푸쉬(스터디)
def solution(s, n):
    answer = ''
    for i in s:
        if i ==' ':
            answer += ' '
            continue
        if ord(i) < 97:
            a = (ord(i)-65 +n)%26 +65
        else:
            a = (ord(i)-97 +n)%26 +97   
        answer+=chr(a)
    return answer