import sys

input = sys.stdin.readline
A = (10**6) +1
dp = [0] * A

for i in range(1, A):
    for j in range(i, A, i):
        dp[j] += i
    dp[i] += dp[i-1]

T = int(input())
for i in range(T):
    print(dp[int(input())])

