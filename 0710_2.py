# Baekjoon 1316 (미완)
t = int(input())
count =0
 
for _ in range(t):
    groupWord = False
    string = input()
    
    if len(string) <2:
        count +=1
        continue
    
    for j in range(len(string)-1):
        if string[j] !=  string[j+1]:
            if string[j] not in string[j+1:]:
                groupWord=True
            else:
                groupWord = False
                break
    if groupWord == True:
        count +=1
 
print(count)