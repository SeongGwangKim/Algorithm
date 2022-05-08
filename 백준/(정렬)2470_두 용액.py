'''
# 메모리 초과
import sys
from itertools import combinations

input = sys.stdin.readline

answer_list = []
N = int(input())
acid_list = list(map(int, input().split()))

for per in combinations(acid_list, 2):
    answer_list.append((abs(sum(per)), per[0], per[1]))

print(min(answer_list)[1], min(answer_list)[2])
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n - 1

answer = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left < right:
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
