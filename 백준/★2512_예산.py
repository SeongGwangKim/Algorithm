'''
문제
국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

입력
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다.

출력
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.
'''
'''
# 이분탐색이 아닌 풀이
import sys

input = sys.stdin.readline

N = int(input())
country_budget_list = list(map(int, input().split()))
country_budget_list.sort(reverse=True)
budget = int(input())

answer = []

if budget > sum(country_budget_list):
    print(max(country_budget_list))
else:
    while country_budget_list:
        if len(country_budget_list) == 1:
            break
        else:
            temp = country_budget_list.pop()
            budget = budget - temp
            max_budget = int(budget/len(country_budget_list))
            answer.append(max_budget)

    print(max(answer))
'''
# 이분탐색을 활용한 풀이
N = int(input())
country_budget_list = list(map(int, input().split()))
budget = int(input())

low = 0
high = max(country_budget_list)
# 최솟값(0부터)과 최댓값을 더하고 2로 나눈 값을 기준으로 탐색한다.
mid = (low + high) // 2
answer = 0


# 예산리스트의 값들과 중간값을 비교하였을 때 작은값들의 합이 예산보다 작을 때 True
def is_possible(mid):
    '''
    tot = 0
    for r in country_budget_list:
        tot += min(r, mid)
    '''
    return sum(min(r, mid) for r in country_budget_list) <= budget


while low <= high:
    # 예산값 리스트들의 값들과 중간값을 비교하였을 때 작은값들의 합이 예산보다 작을 때
    if is_possible(mid):
        # low값을 중간값 + 1로 교체하고 답을 중간값으로 설정한다.
        low = mid + 1
        answer = mid

    # 예산값 리스트들의 값들과 중간값을 비교하였을 때 작은값들의 합이 예산보다 클 때
    else:
        # high값을 중간값 - 1로 교체한다.
        high = mid - 1

    # 중간값을 (최솟값 + 최댓값) / 2로 하고 나머지는 버린 값을 중간값으로 설정한다.
    mid = (low + high) // 2

print(answer)
