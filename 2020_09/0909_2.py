# 회문 (수업)
def palindrome(s):
    myLi = []
    for i in range(1, len(s)):
        for j in range(1, min(len(s)-i, i+1)):
            print(i, j)
            if s[i-j] == s[i+j]:
                myLi.append(2*j+1)
            else:
                break
    return max(myLi)

print(palindrome('abcdcba'))