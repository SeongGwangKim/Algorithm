# BFS
from collections import deque
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

chk = [[False] * 100 for _ in range(100)]
N = int(input())

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()
        chk[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                q.append((ny, nx))

# 백트래킹 : 가지치기를 통해 탐색 경우의 수를 줄인다, 가망이 없으면 가지 않는다.
