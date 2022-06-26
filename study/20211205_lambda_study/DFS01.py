'''
13 12
0 1
0 7
1 2
1 5
2 3
2 4
5 6
7 8
7 9
9 10
9 11
9 12
'''
from pprint import pprint

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = 1

pprint(adj)


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt]:
            print('node', nxt)
            print('--------------')
            dfs(nxt)


dfs(0)