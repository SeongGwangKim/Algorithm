'''
# 내 풀이
N = int(input())
gp_list = list(map(int, input().split()))
gp_list.sort()

temp = 0
result = 0

for gp in gp_list:
    if gp == 1:
        result = result + 1
    else:
        temp = temp + gp

        if temp // gp <= 1:
            result = result + 1

print(result)
'''
# 해설
N = int(input())
data = list(map(int, input().split()))
data.sort()

# 총 그룹의 수
result = 0
# 현재 그룹에 포함된 모험가의 수
count = 0

# 공포도가 낮은 사람부터 확인
for i in data:
    # 현재 그룹에 해당 모험가 포함
    count = count + 1
    # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이면 그룹 +1
    if count >= i:
        result = result + 1
        count = 0

print(result)
