import sys
from itertools import combinations

input = sys.stdin.readline

person_list = [int(input()) for _ in range(9)]
person_list.sort()

for combi in combinations(person_list, 7):
    if sum(combi) == 100:
        for height in combi:
            print(height)
        break
