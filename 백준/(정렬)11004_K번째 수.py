import sys
input = sys.stdin.readline

N, M = map(int, input().split())
su_list = list(map(int, input().split()))
su_list.sort()
print(su_list[M-1])