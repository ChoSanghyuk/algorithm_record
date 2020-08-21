# baekjoon 1935 (후위표기식)

import sys
import operator

n = int(sys.stdin.readline())

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
    }
char = {}

calcul = sys.stdin.readline()[:-1]

for i in range(65, 65+n):
    char[chr(i)] = int(sys.stdin.readline())

calLi = [ i  if i in ops.keys() else char[i] for i in calcul ]

while len(calLi)-1:
    for i in range(len(calLi)):
        if calLi[i] in ops.keys():
            done = ops[calLi[i]](calLi[i-2], calLi[i-1])
            calLi[i-2:i+1] = [done]
            break

print(f'{calLi[0]:.2f}')