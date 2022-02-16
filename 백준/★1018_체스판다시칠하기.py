'''
# W = 1, B = -1로 하여 모두 합한 후 절댓값을 씌우고 나누기 2를 하였을 때 가장 작은 값을 출력한다.
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
temp = 0
answer = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'W':
            board[i][j] = 1
        elif board[i][j] == 'B':
            board[i][j] = -1

if len(board) == 8 and len(board[0]) == 8:
    for i in range(N):
        temp = temp + sum(board[i])
    temp = abs(temp)
    answer.append(int(temp/2))

else:
    while M-m-8:
        n, m = 0
        for i in range(8):
            for j in range(M-7):
                temp = temp + board[i][j:j+8]
        temp = abs(temp)
        answer.append(int(temp/2))
        temp = 0
        # ...
print(min(answer))
'''
# 해설
# 행과 열을 각각 N, M으로 받는다.
N, M = map(int, input().split())
# 각각 입력된 문자열을 각 행에 추가한다.
board = [input() for _ in range(N)]
# 최대가 64이므로 임의 변수를 만든다.
answer = 64


def fill(y, x, bw):
    # 전역변수를 변경하려면 global 선언을 해줘야 한다.
    global answer
    # 카운팅하기 위한 변수 설정.
    cnt = 0
    # 8 x 8 행렬을 확인하기 위한 2중 for문
    for i in range(8):
        for j in range(8):
            # i와 j를 더했을 때 2로 나누어 떨어졌을 때 해당 문자와 같으면 카운팅 +1
            if (i + j) % 2:
                if board[y + i][x + j] == bw:
                    cnt = cnt + 1
            # i와 j를 더했을 때 2로 나누어 떨어지지 않았을 때 해당 문자와 같지 않으면 카운팅 +1
            else:
                if board[y + i][x + j] != bw:
                    cnt = cnt + 1
    # answer와 cnt를 비교하여 작은 값을 answer로 변경.
    answer = min(answer, cnt)

# for문을 이용하여 전체 탐색
for i in range(N-7):
    for j in range(M-7):
        fill(i, j, 'B')
        fill(i, j, 'W')

print(answer)