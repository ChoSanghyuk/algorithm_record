#Baekjoon 10872

def factorial(a):
    if a >1:
        return a*factorial(a-1)
    else:
        return 1
    
n = int(input())

print(factorial(n))