# 메모리 아끼는 법 - 동적계획법 사용
# 시간 초과 - 빠른 입출력 사용
import sys
input = sys.stdin.readline
N = int(input())

check_list = [0] * 10001
temp = 0

for _ in range(N):
    temp = int(input())

    check_list[temp] += 1

for i in range(10001):
    if check_list[i]:
        for _ in range(check_list[i]):
            print(i)