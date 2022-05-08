import sys
input = sys.stdin.readline
munza = str(input().strip())
array_list = []

for i in range(len(munza)):
    array_list.append(munza[i:])

array_list.sort()

for arr in array_list:
    print(arr)