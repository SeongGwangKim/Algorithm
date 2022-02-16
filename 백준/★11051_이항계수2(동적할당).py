'''
문제
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 1,000, 0 ≤ \(K\) ≤ \(N\))

출력

\(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.
'''
'''
# 내가 푼 방식인데 어디가 틀렸는지 정확하게 잘 모르겠다...
# 하지만 찾아보니 float값이 int값으로 변환하는 과정에서 생긴 오차가 축적되어 발생됬을 가능성이 있다고 한다.
N, K = map(int, input().split())
upvalue = 1
downvalue = 1

if N == K or K == 0:
    answer = 1
else:
    for i in range(K):
        upvalue = upvalue * (N - i)
        downvalue = downvalue * (K - i)
    answer = int(int(upvalue)/int(downvalue))
    answer = answer % 10007

print(int(answer))
'''
# 동적할당법 - 재귀 함수를 활용한 Top-down 방식 : 큰 문제를 우선으로 아래로 내려가며 계산하는 방식
# 메모이제이션(Memoization)
# 직관적이라 코드 가독성이 좋다.
# 재귀함수 호출을 많이 해서 느릴 수 있다.
# 초깃값 설정을 해줘야 한다.
import sys
# 반복 횟수 제어
sys.setrecursionlimit(10**7)

# 제한 횟수 설정
MOD = 10007
# N과 K로 각각 숫자를 받아 저장한다.
N, K = map(int, input().split())

# 케시 설정 : 범위가 0 ~ 1000이므로 값 저장할 메모리 설정.
cache = [[0] * 1001 for _ in range(1001)]


def bino(n, k):
    # cache[n][k]가 이미 존재하면 cache[n][k]를 리턴값으로 받는다.
    if cache[n][k]:
        return cache[n][k]

    # k가 0이거나 k가 n이랑 같을 경우에 cache에 1을 넣는다.
    if k == 0 or k == n:
        cache[n][k] = 1
    # cache[n][k] = cache[n-1][k-1] + cache[n-1][k] 점화식 활용.
    # 10007을 넘으면 나머지를 반환하도록 설정.
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
        cache[n][k] = cache[n][k] % MOD
    return cache[n][k]


print(bino(N, K))

# 동적할당법 - 반복문을 활용한 bottom-up 방식 : 작은 문제들로부터 올라가면서 계산하는 방식
# 타뷸레이션(Tabulation)
# 시간과 메모리를 좀더 아낄 수 있다.
# DP 테이블을 채워 나가는 순서를 알아야 한다.
# 초깃값 설정을 해줘야 한다.
MOD = 10007
N, K = map(int, input().split())

cache = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD

print(cache[N][K])