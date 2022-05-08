# 숫자 int type으로 설정
import sys

input = sys.stdin.readline

N = int(input())
coord_list = []

for _ in range(N):
    coord_list.append(tuple(map(int, input().split())))

coord_list.sort()

for i in coord_list:
    print(i[0], i[1])