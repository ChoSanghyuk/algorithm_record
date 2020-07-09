#BaekJoon 2941
str = input()
count =0
k_list=['c=', 'c-', 'dz=','d-', 'lj', 'nj', 's=', 'z=']


for i in k_list:
    if i in str:
        a = str.count(i)
        count += a
        
length = len(str) - count
print(length)