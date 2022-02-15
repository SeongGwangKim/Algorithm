'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''
# 내가 푼 동적할당 풀이, 피보나치 수열 문제였다.
N = int(input())
space = [0] * 1001
MOD = 10007

if N > 2:
    space[0] = 1
    space[1] = 2
    for i in range(2, 1001):
        space[i] = space[i-1] + space[i-2]
elif N == 1:
    space[0] = 1
elif N == 2:
    space[1] = 2

print(space[N-1] % 10007)

# 해설
MOD = 10_007

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

n = int(input())

for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[n])