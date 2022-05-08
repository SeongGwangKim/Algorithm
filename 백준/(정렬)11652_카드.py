'''
# 시간초과
import sys
input = sys.stdin.readline

N = int(input())

array_list = []

for _ in range(N):
    array_list.append(int(input()))

set_list = set(array_list)
answer_list = []

for su in set_list:
    answer_list.append((array_list.count(su), su))

answer_list.sort(key=lambda a:(-a[0], a[1]))

print(answer_list)
print(answer_list[0])
print(answer_list[0][1])
'''
import sys
input = sys.stdin.readline

N = int(input())

array_dict = {}

for _ in range(N):
    temp = int(input().strip())
    if temp in array_dict:
        array_dict[temp] += 1
    else:
        array_dict[temp] = 1

answer_dict = sorted(array_dict.items(), key=lambda x: (-x[1], x[0]))
print(answer_dict[0][0])


