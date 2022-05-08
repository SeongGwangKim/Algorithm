import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, M = map(int, input().split())

N_list = [str(input().strip()) for _ in range(N)]
M_list = [str(input().strip()) for _ in range(M)]
M_list.sort()

total_list = N_list + M_list
total_list.sort()

answer_list = []

for M in M_list:
    bl = bisect_left(total_list, M)
    br = bisect_right(total_list, M)

    if br - bl > 1:
        answer_list.append(M)

print(int(len(answer_list)))

for person in answer_list:
    print(person)
