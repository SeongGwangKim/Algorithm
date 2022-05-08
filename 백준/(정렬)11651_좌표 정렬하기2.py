import sys
input = sys.stdin.readline

N = int(input())

coord_list = [tuple(map(int, input().split())) for _ in range(N)]
coord_list.sort(key=lambda a:a[0])
coord_list.sort(key=lambda a:a[1])


for x, y in coord_list:
    print(x, y)