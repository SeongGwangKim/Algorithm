# 복잡하지만 순열을 활용하여 모든 경우의 수를 다룬 방법
import sys
from itertools import permutations
input = sys.stdin.readline

answer_list = []


N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

for combi in permutations(A_list, 5):
    temp = 0
    for i in range(N):
        temp = temp + combi[i]*B_list[i]
    answer_list.append(temp)

print(min(answer_list))

'''
# 간단한 방법
import sys
input = sys.stdin.readline

answer = 0

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort(reverse = True)

for i in range(N):
    answer += A_list[i] * B_list[i]

print(answer)
'''