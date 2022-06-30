'''
# 문제
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

# 문제에 대한 나의 생각
1. 진짜 약수는 2개 이상의 수의 최소공배수

# 입력
첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다.
둘째 줄에는 N의 진짜 약수가 주어진다.
1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.
'''
'''
import sys

input = sys.stdin.readline
N = int(input())
su_list = list(map(int, input().split()))
su_list.sort(reverse=True)
answer_list = []


def gcd_list(n, m):
    for i in range(max(n, m), (n * m) + 1):
        if i % n == 0 and i % m == 0:
            break
    return i


if N == 1:
    print(su_list[0] ** 2)
elif N == 2:
    temp = gcd_list(su_list[0], su_list[1])
    if temp == max(su_list):
        print(su_list[0] * su_list[1])
    else:
        print(temp)
else:
    for i in range(N):
        if i == (N-1):
            break
        else:
            su_list[i+1] = gcd_list(su_list[i], su_list[i+1])
    print(su_list[-1])
'''
import sys

input = sys.stdin.readline
N = int(input())
su_list = list(map(int, input().split()))
su_list.sort()
answer_list = []

if N == 1:
    print(su_list[0] ** 2)
else:
    print(su_list[0] * su_list[-1])

