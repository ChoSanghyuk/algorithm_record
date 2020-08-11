#baekjoon 2447
import numpy as np

n = int(input())

myArr = np.array([[' ' for _ in range(n)] for _ in range(n)])


def func(n, arr):
    if n ==1:
        arr[0][0] = '*'
    else:
        n_di = int(n/3)
        for i in range(3):
            for j in range(3):
                if i==1 and j==1:
                    pass
                else:
                    new_arr = arr[n_di*i:n_di*(i+1),n_di*j:n_di*(j+1)]
                    func(n_di, new_arr)
func(n, myArr)

for i in range(n):
    for j in range(n):
        print(myArr[i][j], end='')
    print()