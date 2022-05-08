'''
import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

answer_list = []

for M in M_list:
    temp = 0
    for N in N_list:
        if M == N:
            temp += 1
    answer_list.append(temp)

for i in answer_list:
    print(i, end=' ')
'''
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

answer_list = []

for M in M_list:
    bl = bisect_left(N_list, M)
    br = bisect_right(N_list, M)
    answer_list.append((br-bl))

for answer in answer_list:
    print(answer, end=' ')