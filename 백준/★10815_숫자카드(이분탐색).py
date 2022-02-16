'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
'''
'''
# 시간 초과...
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

answer = [0]*M

for i in range(M):
    for j in A:
        if B[i] == j:
            answer[i] = 1

print(answer)
'''
# 이분탐색을 활용한 풀이
from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
qry = list(map(int, input().split()))

# 이분탐색을 위한 정렬
cards.sort()
answer = []

print(cards)
# 정답의 순서가 qry 리스트의 순서와 같기 때문에 그에 맞게 for문 실행
for q in qry:
    # 해당 숫자(q)의 값이 cards 리스트에서 왼쪽에서 몇 번째에 존재하는지 확인
    l = bisect_left(cards, q)
    # 해당 값에서 왼쪽에 존재하는 값의 순서와 q의 값과 같으면 정답
    # answer.append(1 if cards[l] == q else 0)

    # 해당 숫자(q)의 값보다 큰 값이 cards 리스트에 존재하는 순서
    r = bisect_right(cards, q)

    # print(q, '의 l값은 ', l)
    # print(q, '의 r값은 ', r)

    answer.append(1 if r - l > 0 else 0)
    # == answer.append(1 if r - l else 0)

print(*answer)
# == print(' '.join(map(str, answer)))