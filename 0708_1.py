#BaekJoon 5622

str = input()
my_list= []

for i in str:
    aski = ord(i)
    if aski <80:
        count = (aski-56)//3
        my_list.append(count)
    elif 80 <= aski <84:
        count = 8
        my_list.append(count)
    elif 84 <= aski <87:
        count = 9
        my_list.append(count)
    else:
        count =10
        my_list.append(count)
print(sum(my_list))