# 끝말잇기(프로그래머스)
def solution(n, words):
    
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1]:
            return [ (i+1)%n if (i+1)%n !=0 else n , i//n+1  ]
        if words[i] in words[:i]:
            return [ (i+1)%n if (i+1)%n !=0 else n , i//n+1  ]

    return [0,0]