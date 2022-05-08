N = int(input())
guide = input()
coordinate = [1, 1]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def coord_confirm(coordinate):
    return coordinate

for coord in guide:
    if coord == 'L':
        coordinate[0] += dx[0]
    elif coord == 'R':
        coordinate[0] += dx[1]
    elif coord == 'U':
        coordinate[1] += dy[2]
    else:
        coordinate[1] += dy[3]

print(coordinate)

# 해설
# N 입력 받기
N = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]
