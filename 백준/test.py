from itertools import combinations
# N X M 행렬의 값을 받아 리스트에 넣는다.
N, M = map(int, input().split())
houses = []
chickens = []


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for i in range(N):
    # enumerate는 index와 value를 한 번에 가져올 수 있다.
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))

ans = (N - 1) * 2 * len(houses)

for combi in combinations(chickens, M):
    tot = 0 # 도시의 치킨 거리
    for house in houses:
        temp_list = []
        print('----------------------')
        # tot = tot + min(get_dist(house, chicken) for chicken in combi)
        for chicken in combi:
            temp = get_dist(house, chicken)
            temp_list.append(temp)
        print(temp_list)
        tot = tot + min(temp_list)

    ans = min(ans, tot)

print(ans)
