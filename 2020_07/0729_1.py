# 숫자를 1,2,4로 표현하기(수업)
a = int(input())
myList = []

while a:
    b= a//3 ; c=a%3
    if c ==0:
        myList.insert(0,4)
        b-= 1
    else:
        myList.insert(0,c)

    a=b

myStr=''.join(str(e) for e in myList)
print(int(myStr))
