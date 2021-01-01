# N과 M(4)

n, m = map(int, input().split())

list = [[i] for i in range(1,n+1)]

def add_li(list, n):
    new_list = []
    for li in list:
        for num in range(1,n+1):
            if li[-1] <= num:
                new_list.append(li+[num])
    return new_list

for _ in range(m-1):
    list = add_li(list, n)

for li in list:
    for i in li:
        print(i, end=' ')
    print()
