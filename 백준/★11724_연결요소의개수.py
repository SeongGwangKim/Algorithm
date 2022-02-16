'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''
# from pprint import pprint

import sys

# 반복 횟수 증가
sys.setrecursionlimit(10**6)
# 빠른 입출력 사용
input = sys.stdin.readline

# N에 노드의 갯수를, M에 간선의 갯수를 받는다.
N, M = map(int, input().split())

# 받은 노드의 갯수만큼 2차원 리스트를 생성한다.
adj = [[0] * N for _ in range(N)]

# 간선의 갯수만큼 for문을 돌리면서 입력된 값을 list adj의 해당 위치(배열)을 0에서 1로 변경
# adj[a][b] = adj[b][a] = 1(방향이 없기 때문에 양방향 취급)
for _ in range(M):
    # lambda x : x-1은 들어오는 숫자가 1부터 시작하기 때문에 0부터 시작하는 것으로 변경
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

# pprint(adj)

# 답을 담을 변수 생성
ans = 0
# 체크할 노드 리스트를 1차원 리스트로 생성
chk = [False] * N

# 깊이 우선 탐색 방법 사용
def dfs(now):
    # 노드의 수만큼 for문 돌린다.
    for nxt in range(N):
        # 간선 배열 adj에 해당 위치(행, 열이)가 1이고 체크한 노드가 False라면 해당 체크 노드는 True로 변경하고 dfs를 반복한다.
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


# 노드의 수만큼 for문을 돌린다.
for i in range(N):
    # 체크한 노드가 False이면 답에 1을 추가하고 해당 체크 노드를 True로 변경하고 깊이 우선 탐색을 한다.
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)