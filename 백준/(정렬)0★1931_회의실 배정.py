'''
# 시간 초과...
import sys
input = sys.stdin.readline

N = int(input())
answer = 0

conf_list = []

for _ in range(N):
    init, fin = map(int, input().split())

    conf_list.append((fin-init, init, fin))

conf_list.sort()

check_list = [0] * (max(conf_list[2])+1)

for conf in conf_list:
    answer += 1
    for i in range(conf[1], conf[2]+1):
        check_list[i] += 1
    if check_list[i] > 1:
        break

print(answer)
'''
# 정렬 2번을 활용한 풀이
import sys
input = sys.stdin.readline

N = int(input())
answer = 0

conf_list = []

for _ in range(N):
    init, fin = map(int, input().split())
    conf_list.append((init, fin))

conf_list.sort(key = lambda a: a[0])
conf_list.sort(key = lambda a: a[1])

fin = 0
for i in range(N):
    if conf_list[i][0] >= fin:
        answer += 1
        fin = conf_list[i][1]

print(answer)