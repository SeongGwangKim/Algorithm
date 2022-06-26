'''
# 내 풀이
S = input()

result = 0

for i in S:
    if i == '0':
        continue
    elif result == 0:
        temp = list(map(int, i))
        result = result + temp[0]
    elif i == '1':
        result = result + 1
    else:
        temp = list(map(int, i))
        result = result * temp[0]

print(result)
'''
# 해설
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0이나 1이면 더하기
    num = int(data[i])
    if num <= 1 or result <= 1:
        result = result + num
    else:
        result = result * num

print(result)