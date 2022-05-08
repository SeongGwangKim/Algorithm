import sys
input = sys.stdin.readline

N = int(input())

weight_list = [int(input()) for _ in range(N)]
weight_list.sort()

answer_list = []

for i in range(N):
    temp = (N-i) * weight_list[i]
    answer_list.append(temp)

print(max(answer_list))