'''
13 12
0 1
0 2
1 3
1 4
3 7
3 8
4 9
2 5
2 6
6 10
6 11
6 12
'''
from collections import deque
from pprint import pprint

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = 1

pprint(adj)


def bfs():
    dq = deque()
    dq.append(0)
    while dq:
        print('dq', dq)
        now = dq.popleft()
        print('now =', now)
        for nxt in range(N):
            if adj[now][nxt]:
                print('node', nxt)
                dq.append(nxt)

bfs()