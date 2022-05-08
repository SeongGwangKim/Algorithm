import sys

input = sys.stdin.readline

N = int(input())

person_list = []

for _ in range(N):
    age, name = map(str, input().split())

    person_list.append((int(age), name))

person_list.sort(key=lambda a: a[0])

for age, name in person_list:
    print(age, name)