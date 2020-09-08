# 다리를 지나는 트럭 (프로그래머스)
def solution(bridge_length, weight, truck_weights):
    t = 1 
    out_t = [t + bridge_length]
    i=0 ; j=1
    while j-len(truck_weights):
        t +=1
        if t ==out_t[i]:
            i+=1
        if weight - sum(truck_weights[i:j]) >= truck_weights[j]:
            out_t.append(t + bridge_length)
            j+=1
    return out_t[len(out_t)-1]