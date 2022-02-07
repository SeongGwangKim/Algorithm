'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''
# bfs - deque를 활용한 풀이
from collections import deque

# 좌표 이동
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# N X M 행렬의 값을 받아 리스트에 넣는다.
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 들어가는 리스트 확인
# print(board)


# 유효한 좌표인지 확인하는 함수
def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


# 너비 우선 탐색 사용
def bfs():
    # 왔던 좌표인지 확인하기 위한 좌표 리스트 생성
    chk = [[False] * M for _ in range(N)]
    # 첫 시작 좌표는 True로 변경
    chk[0][0] = True
    # bfs를 활용하기 위하여 deque() 생성
    dq = deque()
    # 시작 좌표를 넣고 d는 이동한 거리를 나타낸다. (y, x, d)
    dq.append((0, 0, 1))

    # while문을 돌면서
    while dq:
        # 지나온 좌표는 다시 돌아가지 않기 위해 제거한다.
        y, x, d = dq.popleft()

        # 해당 좌표가 행렬 범위를 벗어나지 않으면 d를 리턴한다.
        if y == N - 1 and x == M - 1:
            return d

        # 이동할 때마다 d에 +1을 추가한다.
        nd = d + 1

        # 이동 좌표의 각각을 추가하면서
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            # 좌표값이 유효하고 board 리스트의 값이 1이고 해당 좌표를 방문하지 않았다면
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                # 해당 좌표를 방문 체크를 하여 True로 변경하고
                chk[ny][nx] = True
                # 해당 값을 dq에 추가한다.
                dq.append((ny, nx, nd))
                # 과정 확인
                # print('과정', dq)


print(bfs())