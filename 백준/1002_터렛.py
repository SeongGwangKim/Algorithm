import math
T = int(input())
answer = 0

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    temp = (x2 - x1)**2 + (y2-y1)**2
    distance = math.sqrt(temp)
    print(distance)

    if distance > r1 + r2:
        answer = 0
        print(answer)
    elif distance < r1 + r2:
        answer = 2
        print(answer)
    elif distance == r1 + r2:
        answer = 1
        print(answer)
    else:
        answer = -1
        print(answer)