'''
# L은 사용할 수 있는 일 수 / P는 사용 연속 일 수 / V는 휴가
answer_list = []

while True:
    L, P, V = list(map(int, input().split()))
    if L == 0 and P == 0 and V == 0:
        break
    else:
        value = V // P * L
        rest_value = V % P
        temp = 0

    if L >= rest_value:
        temp = rest_value
    else:
        temp = L

    sum_value = value + temp
    answer_list.append(sum_value)

for i in range(len(answer_list)):
    print(f'Case {i+1}:', answer_list[i])
'''
# 해설 : 더 심플한 방법
tc = 1
while True:
    L, P, V = list(map(int, input().split()))
    if L == 0:
        break

    print(f'Case {tc}: {V // P * L + min(L, V % P)}')
    tc = tc + 1