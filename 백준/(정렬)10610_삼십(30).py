'''
# 직관적인 시간초과 풀이...
import sys
from itertools import permutations
input = sys.stdin.readline
N = str(input().strip())

answer_list = []

for su in permutations(N, len(N)):
    temp = ''
    if su[0] == '0':
        continue
    else:
        for i in su:
            temp += i
        if (int(temp)) % 30 == 0:
            answer_list.append(int(temp))

if answer_list:
    print(answer_list)
else:
    print(-1)
'''
# 30의 특성을 알아야 하는 풀이
import sys
input = sys.stdin.readline
N = list(map(int, input().strip()))

if sum(N) % 3 == 0 and 0 in N:
    N.sort(reverse=True)
    for su in N:
        print(su, end='')
else:
    print(-1)