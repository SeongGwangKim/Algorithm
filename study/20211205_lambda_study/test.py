

n = 3
orders = [2, 4, 5, 7]

from collections import deque


def solution(orders, n):
    q = deque(orders)
    answer_list = []
    temp_list = [i for i in range(1, 1001)]

    i = 0
    while len(answer_list) != n:

        if temp_list[i] != q[0]:
            answer_list.append(temp_list[i])
            i = i + 1
        elif temp_list[i] == q[0]:
            q.popleft()
            i = i + 1

    return answer_list[n-1]


print(solution(orders, n))



