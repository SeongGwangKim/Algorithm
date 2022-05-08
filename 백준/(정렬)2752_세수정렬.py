import sys
input = sys.stdin.readline

su_list = list(map(int, input().split()))
su_list.sort()

for su in su_list:
    print(su, end=' ')