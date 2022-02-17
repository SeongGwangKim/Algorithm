'''
문제
김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
'''
# dict를 활용한 내가 생각한 풀이
import sys
# dictionary 타입으로 리스트와 그 해당 리스트의 갯수를 저장
count = {}
# 책 제목을 받아서 리스트에 저장
sell_list = []
# 처음에 입력되는 숫자를 받음
N = int(sys.stdin.readline())

# 처음에 입력되는 숫자만큼 for문을 돌려서 sell_list에 책 제목을 저장
for _ in range(N):
    temp = input()
    sell_list.append(temp)

# 책 제목이 있으면 default count = 1, 책 제목이 중복되면 그 수만큼 count + 1
for i in sell_list:
    print('i의 정체는 ', i)
    try: count[i] = count[i] + 1
    except: count[i] = 1
    print(count)

# dict.items를 활용하여 key값과 value값을 오름차순 정렬
count = dict(sorted(count.items()))
print(count)
# 정답
print(max(count, key=count.get))

'''
# 또다른 풀이
d = dict()
N = int(sys.stdin.readline())
for _ in range(N):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

m = max(d.values())
candi = []
for k, v in d.items():
    if v == m:
        candi.append(k)
        
print(candi[0])
'''