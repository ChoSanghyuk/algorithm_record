# 온코더 2회차 4번

class Solution:
    def solution(self, code, message):
        answer = ""
        if message.isdigit():
            for i in range(0,len(message),2):
                num = message[i:i+2]
                answer += code[int(num)-1]
        else:
            for i in message:
                key = code.index(i) +1
                if key < 10:
                    answer += ('0' + str(key))
                else:
                    answer += str(key)
                
        return answer