import sys
input = sys.stdin.readline

N = int(input())

array_list = [int(input()) for _ in range(N)]

array_list.sort()

for i in array_list:
    print(i)