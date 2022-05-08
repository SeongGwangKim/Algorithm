import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

answer_list = A_list + B_list
answer_list.sort()

for su in answer_list:
    print(su, end=' ')