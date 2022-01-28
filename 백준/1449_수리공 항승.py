'''
문제
항승이는 품질이 심각하게 나쁜 수도 파이프 회사의 수리공이다. 항승이는 세준 지하철 공사에서 물이 샌다는 소식을 듣고 수리를 하러 갔다.

파이프에서 물이 새는 곳은 신기하게도 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.

항승이는 길이가 L인 테이프를 무한개 가지고 있다.

항승이는 테이프를 이용해서 물을 막으려고 한다. 항승이는 항상 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각한다.

물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때, 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오. 테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다.

입력
첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이 주어진다. 둘째 줄에는 물이 새는 곳의 위치가 주어진다. N과 L은 1,000보다 작거나 같은 자연수이고, 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 항승이가 필요한 테이프의 개수를 출력한다.
'''
'''
# 좌표를 활용한 solution
N, L = map(int, input().split())

# 좌표 관점 도입 처음 모든 값을 False로 한다.
coordinate = [False] * 1001

# 해당 조건의 위치를 True로 변경한다.
for i in map(int, input().split()):
    coordinate[i] = True

# 좌표 시작점
x = 0
# 정답
answer = 0

# 좌표 이동하면서 테이프 붙이고 이동
while x < 1001:
    # 만약 해당 좌표가 True이면 정답에 +1하고 +L만큼 좌표 이동
    if coordinate[x]:
        answer = answer + 1
        x = x + L
    # 해당 좌표가 False이면 +1만큼 좌표 이동
    else:
        x = x + 1

print(answer)
'''
# 내가 도전한 풀이
# 예외의 경우 처리에 대하여 고민 중...
# eg) 2 1000, 1 500일 때
from collections import deque
N, L = map(int, input().split())
coordinate = list(map(int, input().split()))
coordinate.sort(reverse=True)

hole_list = deque()

for co in coordinate:
    hole_list.append(co)

x = hole_list[0]
cnt = 1
hole_list.popleft()

if L > 1:
    if N == 1:
        cnt = 1
    else:
        while x > 0:
            if hole_list[0] > x:
                hole_list.popleft()
                cnt = cnt + 1
            else:
                x = x - L

elif L == 1:
    cnt = N

print(cnt)
