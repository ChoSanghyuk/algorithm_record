# input 받은 nest list를 nested list로 바꾸기 (수업)

A = [] 
tempLi=[]
tempWo=''
a = input()  

myList = a.split(',')
for i in myList:  
    num = int(i.strip('[').strip(']'))
    tempLi.append(num)
    if ']'in i:
        A.append(tempLi)
        tempLi=[]