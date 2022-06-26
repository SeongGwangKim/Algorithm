# DFS 메소드 정의
# v는 시작 노드, visited는 각 노드가 방문된 정보를 표현하는 리스트
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [ [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7] ]

# 각 노드가 방문된 정보를 1차원 리스트로 표현
visited = [False] * 9

dfs(graph, 1, visited)