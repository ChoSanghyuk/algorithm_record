#Beakjoon 3009번

xList= list()
yList = list()
answer = {}

for _ in range(3):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

for i in range(3):
    if xList.count(xList[i]) ==1:
        answer['x'] = xList[i]
    if yList.count(yList[i]) ==1:
        answer['y'] = yList[i]

print(f'{answer["x"]} {answer["y"]}')