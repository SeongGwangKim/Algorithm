'''
문제
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

출력
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
'''
'''
# heapq, ()튜플을 활용한 내 풀이
import heapq as hq
import sys

# 처음에 값을 입력받는다.
# 빠른 입력을 사용한다.
N = int(sys.stdin.readline().rstrip())

# pq라는 heap을 받을 리스트를 만든다.
pq = []

# 처음 입력된 값만큼 for문을 돌린다.
for _ in range(N):
    # 들어온 값을 임시 공간에 넣는다.
    temp = int(sys.stdin.readline().rstrip())

    # 들어온 값이 0이면 값을 출력한다.
    if temp == 0:
    # 내가 풀어쓴 것 == print(hq.heappop(pq)[1] if pq else 0)
        if pq:
            # pq에 값이 존재하면 pq의 가장 앞의 값의 튜플 중 2번째 값을 출력한다.
            print(hq.heappop(pq)[1])
        else:
            # pq에 값이 존재하지 않으면 0을 출력한다.
            print(0)
    else:
        # 들어온 값을 튜플 구조로 (절댓값, 원래값)을 리스트로 추가한다.
        hq.heappush(pq, (abs(temp), temp))
'''
# max_heap, min_heap 활용한 풀이
import heapq as hq
import sys

# 처음에 값을 입력받는다.
# 빠른 입력을 사용한다.
N = int(sys.stdin.readline().rstrip())
min_heap = [] # 양수 받아서 활용
max_heap = [] # 음수 받아서 활용

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))

            else:
                print(hq.heappop(min_heap))

        else:
            if max_heap:
                print(-hq.heappop(max_heap))

            else:
                print(0)
