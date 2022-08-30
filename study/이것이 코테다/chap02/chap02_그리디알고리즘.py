# 그리디 알고리즘
'''
큰 단위가 작은 단위의 배수일 경우에 성립

# 예제 - 거스름 돈
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)
'''
# 문제 1이 될 때 까지
'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
예를 들어 N이 17, K가 4라고 가정하자.
이 때 1번의 과정을 한 번 수행하면 N은 16이 된다.
이후에 2번의 과정을 2번 수행하면 N은 1이 된다.
결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다.
이는 N을 1로 만드는 최소 횟수이다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())

count = 0

while N != 1:
    if N % K == 0:
        N = N // K
        count += 1
    else:
        N = N - 1
        count += 1

print(count)
'''
N, K = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N // K) * K        # 25 // 3 = 8 * 3 = 24 = target    # 8 // 3 = 2 * 3 = 6 = target
    result += (N - target)       # 25 - 24 = 1 = result             # 8 - 6 = 2 + 2(result) = 4 = result
    N = target                   # N = 24                           # N = 6

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break

    # K로 나누기
    result += 1                 # result = 2                        # result = 5
    N = N // K                  # 24 // 3 = 8 = N                   # 6 // 3 = 2 = N

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (N - 1)
print(result)

