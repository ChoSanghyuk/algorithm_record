# 온코더 2회차 5번 (런타임)


class Solution:
    def solution(self, n, actions):
        process = []
        index = [0 for _ in range(n)]
        count = n
        
        if len(actions)==0:
            return count
        
        for i in actions:
            in_bag = []
            for t in process:
                in_bag += t
            
            if i[:3] == 'PUT':
                if int(i[13]) in in_bag or int(i[4]) in in_bag:
                    return -1
                process[int(i[13])-1].append(int(i[4]))
                count -=1
            elif i[:3] == 'SET':
                if int(i[4]) in in_bag:
                    return -1
                count += len(process[int(i[4])-1])
                process[int(i[4])-1] = []
            else:
                if int(i[5]) in in_bag or int(i[12]) in in_bag:
                    return -1
                temp = process[int(i[5])-1]
                process[int(i[5])-1] = process[int(i[12])-1]
                process[int(i[12])-1] = temp

        for i in range(len(process)):
            for j in process[i]:
                if j > i+1 :
                    return -1
        return count