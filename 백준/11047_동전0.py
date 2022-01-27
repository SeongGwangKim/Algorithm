'''
문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
'''
## 내림차순 정렬과 while문을 활용한 내 풀이
# N은 받을 조건 수, K는 정답을 각각 받는다.
N, K = map(int, input().split())
# 받은 조건을 coin_list에 넣는다.
coin_list = []
# 정답을 카운팅하기 위하여 임시 cnt를 만든다.
cnt = 0
# while문 안에서 제어 변수로 사용하기 위하여 i 사용.
i = 0

# for문을 통하여 N의 수만큼 input을 받아 coin_list에 넣는다.
for _ in range(N):
    temp = int(input())
    coin_list.append(temp)

# 내림차순 정렬을 하기 위하여 coin_list를 reverse로 정렬한다.
coin_list.sort(reverse=True)

# while문을 통하여 i는 0부터 시작하기 때문에 N보다 작을 때까지 돌아가게 한다.
while N > i:
    # cnt에 추가할 값을 임시 변수 temp_cnt를 만든다.
    temp_cnt = 0
    # K가 answer와 같으면 while문을 멈추게 한다.
    if K == 0:
        break
    # K가 answer와 같지 않으면 계속 while문을 돌게 한다.
    else:
        # temp_cnt에 K를 coin_list의 가장 큰 값부터 넣어 나눈 몫을 넣는다.
        temp_cnt = temp_cnt + K // coin_list[i]
        # temp_cnt에서 생긴 몫을 정답을 출력할 cnt에 추가한다.
        cnt = cnt + temp_cnt

        # K를 coin_list의 가장 큰 값부터 나눈 나머지를 K에 재저장한다.
        K = K % coin_list[i]

        # 모든 조건을 마치고 i를 1을 추가한다.
        i = i + 1

print(cnt)
'''
# for문을 활용한 solution
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0

for coin in coins:
    ans += K // coin
    K %= coin
    
print(ans)
'''