'''
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''
# N=1 : 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 = 9개
# N=2 : 10 12 / 21 23 / 32 34 / 43 45 / 54 56 / 65 67 / 76 78 / 87 89 / 98 = 17개
# N=3 :
# 210 101 / 212 121 // 321 210 / 123 232 // ...
# 101 121 123 / 210 212 232 234 / 321 323 343 345 / 432 434 454 456 / 543 545 565 567 / 654 656 676 678 / 765 767 787 789 / 876 878 898 / 987 989
# 3 + 4*6 + 3 + 2 = 3+24+5 = 32

# N = 1(9), 2(17), 3(32), 4(61)...
# 수학적으로 점화식을 만들 수 있는지 확인하고 정답이 아니라면 점화식이 아닐 가능성을 확인한다!

MOD = 1_000_000_000

# cache[n][d] = 길이가 n, 마지막 숫자가 d인 계단 수의 개수
# d는 0 ~ 9
cache = [[0] * 10 for _ in range(101)]

# N이 1일 때, 즉, 1자리 숫자일 때
for i in range(1, 10):
    cache[1][i] = 1

# 끝자리 기준으로 생각
# cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j + 1]
for i in range(2, 101):
    for j in range(10):
        # 예를 들어 j가 2이면 끝자리가 2이므로 그 앞자리에 올 수 있는 숫자는 1과 3이다. 따라서 1과 3의 값들만큼 더한다.
        if j > 0:
            cache[i][j] = cache[i][j] + cache[i - 1][j - 1]
            cache[i][j] = cache[i][j] % MOD

        if j < 9:
            cache[i][j] = cache[i][j] + cache[i - 1][j + 1]
            cache[i][j] = cache[i][j] % MOD

N = int(input())
print(sum(cache[N]) % MOD)

# answer = 0
# 입력하는 숫자의 열의 해당하는 것의 모든 값을 출력한다.
# for j in range(10):
#     answer = answer + cache[N][j]
#     answer = answer % MOD

# print(answer)
