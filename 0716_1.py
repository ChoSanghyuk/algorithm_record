#Baekjoon 2869
A,B,V = map(int, input().split())

if (V-A)/(A-B) == int((V-A)/(A-B)):
    print(int( (V-A)/(A-B) )+1)
else:
    print(int( (V-A)/(A-B) )+2)