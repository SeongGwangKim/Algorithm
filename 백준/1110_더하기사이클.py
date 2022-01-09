'''
문제
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

출력
첫째 줄에 N의 사이클 길이를 출력한다.
'''
# 들어온 값 = 정답
temp = int(input())
answer = temp
# 길이 카운팅
cnt = 0
while True:
    # 값의 10의 자리
    a = temp // 10
    # 값의 1의 자리
    b = temp % 10
    # 값의 10의 자리와 1의 자리 합
    c = a + b
    d = (b * 10) + (c % 10)
    # 새로운 수가 만들어질 때 카운트 + 1
    cnt = cnt + 1
    temp = d

    # 정답과 새로 만들어진 수가 같다면 break
    if answer == d:
        break
# 새로 만들어진 수 카운팅 출력
print(cnt)
'''
[ 실수 한 점 ]
처음에 계속 런타임 에러와 시간초과가 나왔다.
그 이유는 temp가 계속 개선되는데 temp와 d가 같지 않을 때 while문을 빠져나가게 했기 때문이다.
곰곰히 생각해보니 정답이 계속 바뀌는데 d와 비교를 할 수가 없다는 것을 발견하여
처음 값을 복제하여 answer에 넣어서 비교를 하였다.
그렇게 하니 시간 안에 정답을 구할 수 있었다.
'''