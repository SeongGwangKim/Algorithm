import sys
input = sys.stdin.readline

N = int(input())
array_list = list(map(int, input().split()))
set_list = list(set(array_list))
set_list.sort()

for su in set_list:
    print(su, end=' ')