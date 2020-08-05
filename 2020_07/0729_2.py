# 가운데 문자 출력하기(수업)
myStr= input()
slen, isEven = divmod(len(myStr),2)

if isEven:
    print(myStr[slen])
else:
    print(myStr[slen-1 : slen+1])