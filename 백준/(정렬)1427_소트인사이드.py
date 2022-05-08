su = str(input())
array_list = []

for i in su:
    array_list.append(int(i))

array_list.sort(reverse=True)

for i in array_list:
    print(i, end="")