'''
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

ex)
prices
[1, 2, 3, 2, 3]
return
[4, 3, 1, 1, 0]

'''

def solution(prices):
    answer = []
    # 0부터 prices 리스트의 길이만큼 for문을 실행시킨다.
    for i in range(0, len(prices)):
        # 처음은 0부터 시작한다.
        temp = 0
        # 다음 가격과 비교하기 위하여 for문을 i보다 1 큰 수부터 prices의 길이만큼 실행 시킨다.
        for j in range(i+1, len(prices)):
            # prices의 값이 다음에 있는 값들 보다 작으면 +1
            if prices[i] <= prices[j]:
                temp += 1
            # 해당 값이 바로 떨어져도 1초 뒤에 떨어지므로 +1을 해주고 멈추어야 하기 때문에 break를 사용.
            else:
                temp += 1
                break
        # 생성된 임시값을 answer 리스트에 추가해준다.
        answer.append(temp)
    return answer

