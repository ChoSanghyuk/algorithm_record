start = int(input())
n = start

li = [['*' for _ in range(n) ] for _ in range(n) ]

while n//3:

    for t in range(start//n):
        for i in range(n//3 , (n//3)*2):
            for k in range(start//n):
                for j in range(n//3 , (n//3)*2):
                    li[i + t*n ][j + k*n ] = ' '
            

    n = n//3

for i in range(start):
    for j in range(start):
        print(li[i][j] , end = '')
    print()
