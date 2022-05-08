'''
# 시간초과
import sys
input = sys.stdin.readline
N = int(input())
su_list = list(map(int, input().split()))
set_su = set(su_list)
rank_list = list(set_su)
rank_list.sort()

for i in range(N):
    for j in range(len(rank_list)):
        if su_list[i] == rank_list[j]:
            su_list[i] = j

for su in su_list:
    print(su, end=' ')

# 시간초과
import sys
input = sys.stdin.readline
N = int(input())
su_list = list(map(int, input().split()))
rank_list = sorted(list(set(su_list)))

for su in su_list:
    print(rank_list.index(su), end=' ')
'''
# dictionary type을 이용할 풀이
import sys
input = sys.stdin.readline
N = int(input())
su_list = list(map(int, input().split()))
set_list = sorted(set(su_list))

su_dict = {set_list[i]:i for i in range(len(set_list))}

for su in su_list:
    print(su_dict[su], end=' ')
