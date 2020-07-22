# 최대 튜플 찾기 (수업실습)
ts = input()
ts = ts[1:-1]
ls = []
for i in range(len(ts)):
    if ts[i] != '{' and ts[i] !='}' and ts[i] !=',' and ts[i] !=' ':
        ls.append(int(ts[i]))

print(tuple(set(ls)))