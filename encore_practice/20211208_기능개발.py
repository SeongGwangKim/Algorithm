def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0

    # progresses 리스트의 길이가 0보다 크면 while문 동작
    while len(progresses) > 0:
        # 만약 progresses의 첫 값이 time * speeds의 첫 값을 더한 것이 100보다 크거나 같으면
        # 해당 progressess, speeds의 값 제거 후 cnt + 1
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt = cnt + 1

        # progresses가 100보다 작은 값이 나타났을 때 time에 1을 추가한다.
        # 만약 cnt가 0보다 크면 cnt 값을 답 리스트에 추가하고 cnt = 0으로 초기화한다.
        else:
            time = time + 1
            if cnt > 0:
                answer.append(cnt)
                cnt = 0

    # print(cnt)
    # 마지막 값 처리 용도
    answer.append(cnt)

    return answer

if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))
