'''
# 내 풀이
N, K = map(int, input().split())
count = 0
N_temp = N

while True:
    if N_temp % K == 0:
        N_temp = N_temp // K
        count += 1
    else:
        N_temp = N_temp - 1
        count += 1
    if N_temp == 1:
        print(count)
        break
'''

# 해설
N, K = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N // K) * K
    result = result + (N - target)
    N = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break

    # K로 나누기
    result = result + 1
    N = N // K

result = result + (N - 1)
print(result)