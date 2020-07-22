# 영어의 끝말잇기 게임 (수업실습)

words = input()
myDict = words.split(',')
num = int(input())
success = True

for i in range(len(myDict)):
    ans = input()
    if ans != myDict[i]:
        print(f'Try: {i+1}, loser :{i%num +1}')

        success = false
if success:
    print([0,0])