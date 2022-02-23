'''
# 내 풀이
N, M = map(int, input().split())
friend = [[0] * N for _ in range(N)]
friend_check = [[0] * N for _ in range(N)]
temp = N

for i in range(M):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1



print(friend_check)

def repeat_check(row, search_num):
    while True:
        cnt = 0
        x = row
        y = 0
        if friend[x][y] == 0 and friend_check[x][y] == 0:
            y = y + 1

    return cnt


for i in range(N):
    for j in range(N):
        repeat_check(i, j)
'''
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

print('adj', adj)

kevin = []
ans = (-1, 10 ** 8)


def bfs(start, goal):
    chk = [0] * N
    chk[start] = 1
    dq = deque()
    dq.append((start, 0))

    while dq:
        print('---------------------------goal', goal)
        print('dq', dq)
        print('chk', chk)
        now, d = dq.popleft()
        if now == goal:
            return d

        nd = d + 1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = 1
                dq.append((nxt, nd))


def get_kevin(start):
    tot = 0

    for i in range(N):
        if i != start:
            tot = tot + bfs(start, i)

    return tot


for i in range(N):
    kevin.append(get_kevin(i))

for i, v in enumerate(kevin):
    print('i =', i, 'v =', v)
    if ans[1] > v:
        ans = (i, v)

print(ans[0] + 1)
