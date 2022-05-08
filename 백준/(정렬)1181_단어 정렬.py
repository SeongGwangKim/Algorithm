# 2개의 특징을 튜플로 묶어서 푼 풀이
import sys
input = sys.stdin.readline
N = int(input())
str_temp = ''

array_list = [str(input().strip()) for _ in range(N)]
temp = set(array_list)
array_list_temp = list(temp)

answer_list = []

for answer in array_list_temp:
    answer_list.append((len(answer), answer))

answer_list.sort()

for answer in answer_list:
    print(answer[1])

# 파이썬의 특징을 활용한 풀이
'''
import sys
input = sys.stdin.readline
N = int(input())
str_temp = ''

array_list = [str(input().strip()) for _ in range(N)]

array_list.sort()
array_list.sort(key=len)

for answer in array_list:
    print(answer)
'''